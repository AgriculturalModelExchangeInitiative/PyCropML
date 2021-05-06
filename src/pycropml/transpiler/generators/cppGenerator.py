# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.rules.cppRules import CppRules
from pycropml.transpiler.generators.docGenerator import DocGenerator
from pycropml.transpiler.pseudo_tree import Node
import os
from pycropml.transpiler.interface import middleware
from path import Path
from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree
from pycropml import code2nbk
from pycropml.render_cyml import my_input

class CppGenerator(CodeGenerator,CppRules):
    """ This class contains the specific properties of
    C++ language and use the NodeVisitor to generate a cpp
    code source from a well formed syntax tree.
    """
    
    def __init__(self, tree, model=None, name=None):
        CodeGenerator.__init__(self)
        CppRules.__init__(self)
        self.tree = tree
        self.model=model
        self.indent_with=' '*4
        self.initialValue=[] 
        self.z = middleware(self.tree)
        self.z.transform(self.tree)
        self.name= name
        if self.model: 
            self.doc= DocGenerator(model, '//')
            self.generator = CppTrans([model])
            self.generator.model2Node()
            self.states = [st.name for st in self.model.states]  
            self.rates = [rt.name for rt in self.generator.rates ]
            self.auxiliary = [au.name for au in self.generator.auxiliary] 
            self.node_param = self.generator.node_param
            self.modparam=[param.name for param in self.node_param]
        self.funcname = ""

    def visit_notAnumber(self, node):
        self.visit(Node(type="local", name="NAN"))
           
    def visit_comparison(self, node):
        #self.write('(')
        self.visit_binary_op(node)
        #self.write(')')
        
    def visit_binary_op(self, node):
        op = node.op
        prec = self.binop_precedence.get(op, 0)
        self.operator_enter(prec)
        self.visit(node.left)
        self.write(u" %s " % self.binary_op[op].replace('_', ' '))
        if "type" in dir(node.right):
            if node.right.type=="binary_op" and node.right.op not in ("+","-") :
                self.write("(")
                self.visit(node.right)
                self.write(")")
            else:
                self.visit(node.right)
        else:
            self.visit(node.right)
        self.operator_exit()


    def visit_constant(self, node):
        self.write(self.constant[node.library][node.name])
        
    def visit_unary_op(self, node):
        op = node.operator
        prec = self.unop_precedence[op]
        self.operator_enter(prec)
        self.write(u"%s" % self.unary_op[op])
        self.visit(node.value)
        self.operator_exit()         
        
    def visit_breakstatnode(self, node):
        self.newline(node)
        self.write('break;')    

         
    def visit_import(self, node):
        pass

    def visit_cond_expr_node(self, node):
        self.visit(node.test)
        self.write(u" ? ")
        self.visit(node.true_val)     
        self.write(u" : ")
        self.visit(node.false_val) 
        
    def visit_if_statement(self, node):
        self.newline(node)
        self.write('if (')
        self.visit(node.test)
        self.write(')')
        self.newline(node)
        self.write('{')
        self.newline(node)
        self.body(node.block)
        self.newline(node)
        self.write('}')
        while True:
            else_ = node.otherwise
            if len(else_) == 0:
                break
            elif len(else_) == 1 and else_[0].type=='elseif_statement':
                self.visit(else_[0])
            else:
                self.visit(else_)
                break
            break

    def visit_elseif_statement(self, node):
        self.newline()
        self.write('else if ( ')
        self.visit(node.test)
        self.write(')')
        self.newline(node)
        self.write('{')
        self.body(node.block)
        self.newline(node)
        self.write('}')        

    def visit_else_statement(self, node):
        self.newline()
        self.write('else')
        self.newline(node)
        self.write('{')        
        self.body(node.block)
        self.newline(node)
        self.write('}') 

    def visit_print(self, node):
        pass
        
    
    def visit_float(self, node):
        self.write("%sd"%node.value)

    def visit_double(self, node):
        self.write("%sd"%node.value)

    def visit_array(self, node):
        self.write("new []")        
        self.write(u'{')
        self.comma_separated_list(node.elements)
        self.write(u'}')
                
    def visit_dict(self, node):
        self.write("new ")
        self.visit_decl(node.pseudo_type)
        self.write(u'{')
        self.comma_separated_list(node.pairs)
        self.write(u'}')
    
    def visit_bool(self, node):
        self.write("true") if node.value==True else self.write("false")
   
    def visit_standard_method_call(self, node):
        l = node.receiver.pseudo_type
        if isinstance(l, list):
            l = l[0]
        z = self.methods[l][node.message]        
        if callable(z):
            self.visit(z(node))
        else:
            if not node.args:
                self.write(z)
                self.write('(')
                self.visit(node.receiver)
                self.write(')')
            else:
                "%s.%s"%(self.visit(node.receiver),self.write(z))
                self.write("(")
                self.comma_separated_list(node.args)
                self.write(")")

            
    
    def visit_method_call(self, node):
        "%s.%s"%(self.visit(node.receiver),self.write(node.message))
        
                                
    def visit_index(self, node):
        self.visit(node.sequence)
        self.write(u"[")
        if isinstance(node.index.type, tuple):
            self.emit_sequence(node.index)
        else:
            self.visit(node.index)
        self.write(u"]")

    def visit_sliceindex(self, node):
        self.visit(node.receiver)
        self.write(u"[")
        if node.message=="sliceindex_from":
            self.visit(node.args)
            self.write(u":")
        if node.message=="sliceindex_to":
            self.write(u":")
            self.visit(node.args)
        if node.message=="sliceindex":
            self.visit(node.args[0])
            self.write(u":")
            self.visit(node.args[1])
        self.write(u"]")
    
    def visit_assignment(self, node):
        if "function" in dir(node.value) and node.value.function.split('_')[0]=="model":
            name  = node.value.function.split('model_')[1]
            self.write("_%s.Calculate_%s(s, s1, r, a);"%(name.capitalize(), name))
            self.newline(node)
        elif node.value.type =="standard_call" and node.value.function=="copy":
            self.newline(node)
            self.write("%s = %s;"%(node.target.name,node.value.args.name))
        elif node.value.type == "standard_call" and node.value.function=="integr":
            self.newline(node)
            self.write("%s = %s;"%(node.target.name,node.value.args[0].name))
            self.newline(node)
            if isinstance(node.value.args[1].pseudo_type, list):
                self.write("%s.reserve(%s.size() + distance(%s.begin(),%s.end()));"%(node.target.name, node.target.name, node.value.args[1].name, node.value.args[1].name))
                self.newline(node)
                self.write("%s.insert(%s.end(),%s.begin(),%s.end());"%(node.target.name, node.target.name, node.value.args[1].name, node.value.args[1].name))
            else: 
                self.write("%s.push_back("%node.target.name)
                self.visit( node.value.args[1])
                self.write(");")        
        elif node.value.type =="standard_method_call" and node.value.message in ["keys", "values"]:
                self.write("%s.reserve(%s.size());"%(node.target.name, node.value.receiver.name))
                self.newline(node)
                self.write("for(auto const&i : %s)"%node.value.receiver.name)
                self.newline(node)
                self.write("{")
                self.newline(node)
                self.write("    %s.push_back(i.first);"%node.target.name) if node.value.message=="keys" else self.write("    %s.push_back(i.second);"%node.target.name)
                self.newline(node)
                self.write("}")
                self.newline(node)
        else:
            self.newline(node)
            self.visit(node.target)
            self.write(' = ')
            self.visit(node.value) 
            self.write(";")
            self.newline(node)

    def visit_continuestatnode(self, node):
        self.newline(node)
        self.write('continue;')

    def transform_return(self, node):
        if self.funcname.startswith("model") or self.funcname.startswith("init"):
            returnvalues=node.block[-1].value
            if returnvalues.type=="tuple":
                output = [elt.name for elt in returnvalues.elements]
                node_output = [elt for elt in returnvalues.elements]
            else:
                output = [returnvalues.name]
                node_output = [returnvalues]
        else:
            if len(self.z.returns)==1:
                returnvalues=self.z.returns[0].value
                if returnvalues.type=="tuple":
                    output = [elt.name for elt in returnvalues.elements]
                    node_output = [elt for elt in returnvalues.elements]
                else:
                    if "name" in dir(returnvalues): 
                        output = [returnvalues.name]
                        node_output = [returnvalues]
                    else:                  
                        output = []
                        node_output = []  
            else: 
                output = []
                node_output = []
        return output, node_output

    def retrieve_params(self, node):
        parameters=[]
        node_params=[]
        for pa in node.params:
            parameters.append(pa.name)
            node_params.append(pa)
        return node.params
    
    def array_parameter(self, params):
        dict_arrParamSize ={}
        i=0
        tplte=False
        for pa in params:
            if isinstance(pa.pseudo_type, list) and pa.pseudo_type[0]=="array":
                if len(pa.elts)==0:
                    tplte=True
                    elt ="SIZE_%s"%i
                    i=i+1
                    dict_arrParamSize[pa.name] =elt
                elif "name" in dir(pa.elts[0]):
                    tplte=True
                    elt=pa.elts[0].name
                    dict_arrParamSize[pa.name] =elt
        return dict_arrParamSize, tplte
    
    def templateArr(self, node):
        def myfunc(n):
            return "size_t %s"%n
        narr=self.array_parameter(node)
        uniq_val=[]
        for k, v in narr[0].items():
            if v not in uniq_val: uniq_val.append(v)
        if narr[1]==True: self.write("template<%s>"%", ".join(map(myfunc,uniq_val)) )    
        self.newline(node)

    def internal_declaration(self, node):
        statements  = node.block
        if isinstance(statements, list):
            intern_decl=statements[0].decl if statements[0].type=="declaration" else None
            for stmt in statements[1:]:
                if stmt.type=="declaration":
                    intern_decl=intern_decl+stmt.decl
        else: intern_decl=statements.decl if statements.type=="declaration" else None
        return intern_decl
    
    def add_features(self, node):
        self.internal = self.internal_declaration(node)
        internal_name=[]
        if self.internal is not None:
            self.internal = self.internal if isinstance(self.internal,list) else [self.internal]
            for inter in self.internal:
                if 'elements' in dir(inter):
                    self.initialValue.append(Node(type="initial",name = inter.name, pseudo_type=inter.pseudo_type, value = inter.elements))
            internal_name= [e.name  for e in self.internal]
        self.params = self.retrieve_params(node)
        params_name = [e.name  for e in self.params]
        outputs = self.transform_return(node)[1]
        if not isinstance(outputs, list):
            outputs=[outputs]
        outputs_name = [e.name  for e in outputs]
        
        variables = self.params+self.internal if self.internal else self.params
        newNode=[]
        for var in variables:
            if var not in newNode:
                if var.name in params_name and var.name not in outputs_name:
                    var.feat = "IN"
                    newNode.append(var)
                if var.name in params_name and var.name in outputs_name:
                    var.feat = "INOUT"
                    newNode.append(var)
                if var.name in internal_name and var.name in outputs_name:
                    var.feat = "OUT"
                    newNode.append(var)
                if var.name in internal_name and var.name not in outputs_name:
                    newNode.append(var)
        return newNode    

    def visit_module(self, node):
        self.write(u'#define _USE_MATH_DEFINES\n#include <cmath>\n#include <iostream>\n# include<vector>\n# include<string>\n# include<numeric>\n# include<algorithm>\n# include<array>\n#include <map>\n# include <tuple>\n')
        if self.model:
            self.write('#include "%s.h"\nusing namespace std;\n'%self.model.name.capitalize())
        else : self.write("using namespace std;\n")
        self.visit(node.body)
        self.newline(node)          

    def visit_function_definition(self, node):      
        self.newline(node)
        self.funcname = node.name
        self.add_features(node)
        if (not node.name.startswith("model_") and not node.name.startswith("init_")) :
            self.templateArr(node.params)
            self.visit_decl(node.return_type) if node.return_type else self.write("void")
            if self.model: self.write(" %s::"%self.model.name.capitalize())
            self.write(" %s("%node.name)
            for i, pa in enumerate(node.params):
                if pa.name in self.array_parameter(node.params)[0].values(): continue
                if pa.feat=="IN" and pa.type in ["list","array"]: self.write("const ")
                self.visit_decl(pa.pseudo_type, pa)
                if i!= (len(node.params)-1):
                    self.write(', ')
            self.write(')')
            self.newline(node)
            self.write('{') 
            self.newline(node)
        else:
            self.write("%s::%s() { }"%(self.model.name.capitalize(),self.model.name.capitalize())) if not node.name.startswith("init_") else ""
            self.newline(node) 
            if self.node_param and not node.name.startswith("init_") :
                self.getter(self.model.name.capitalize(),self.node_param)
                self.newline(1)
                self.setter(self.model.name.capitalize(),self.node_param)
                self.newline(1)    
            self.write("void %s::Calculate_Model("%self.model.name.capitalize()) if not node.name.startswith("init_") else self.write("void %s::Init("%self.model.name.capitalize())
            self.write('%sState& s, %sState& s1, %sRate& r, %sAuxiliary& a)'%(self.name.capitalize(),self.name.capitalize(), self.name.capitalize(), self.name.capitalize()))
            self.newline(node)
            self.write('{') 
            self.newline(node)
            if not node.name.startswith("init_"):
                self.write(self.doc.header)
                self.newline(node)
                self.write(self.doc.desc)
                self.newline(node)
                self.write(self.doc.inputs_doc)
                self.newline(node)
                self.write(self.doc.outputs_doc)
                self.newline(node)
            self.indentation += 1 
            for arg in self.add_features(node) :
                if "feat" in dir(arg):
                    if arg.feat in ("IN","INOUT") :
                        self.newline(node) 
                        if self.model and arg.name not in self.modparam:
                            self.visit_decl(arg.pseudo_type)
                            self.write(" ")
                            self.write(arg.name)
                            if not node.name.startswith("init_"):
                                if arg.name in self.states and not arg.name.endswith("_t1") :
                                    self.write(" = s.get%s()"%arg.name)
                                if arg.name.endswith("_t1") and arg.name in self.states:
                                    self.write(" = s1.get%s()"%arg.name[:-3])
                                if arg.name in self.rates:
                                    self.write(" = r.get%s()"%arg.name)
                                if arg.name in self.auxiliary:
                                    self.write(" = a.get%s()"%arg.name) 
                            else:
                                if arg.pseudo_type[0] =="list":
                                    self.write(" = vector<%s>()"%(self.types[arg.pseudo_type[1]]))
                                elif arg.pseudo_type[0] =="array":
                                    self.write(" = array<%s,%s>"%(self.types[arg.pseudo_type[1]], arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name))
                            self.write(";")                   
            self.indentation -= 1 
        self.body(node.block)
        self.newline(node)
        self.visit_return(node)
        self.newline(node)
        self.indentation -= 1 
        self.write('}') 
        self.newline(node)

    def getter(self,m, node):
        for arg in node:
            self.newline(node)
            self.visit_decl(arg.pseudo_type)
            self.write(" %s::get%s()"%(m,arg.name)) if not isinstance(arg.pseudo_type, list) else self.write("& %s::get%s()"%(m,arg.name) )         
            self.write (" {return this-> %s; }"%arg.name)

    def setter(self,m, node):
        for arg in node:
            self.newline(node)
            self.write("void %s::set%s("%(m,arg.name))
            self.visit_decl(arg.pseudo_type)
            if not isinstance(arg.pseudo_type, list):
                self.write(" _%s) { this->%s = _%s; }"%(arg.name, arg.name, arg.name)) 
            else:
                self.write("& _%s){"%arg.name)
                self.newline(1)
                self.indentation +=1
                self.write("this->%s = _%s;"%(arg.name, arg.name))
                self.newline(1)
                self.indentation -=1
                self.write("}")



    def visit_custom_call(self, node):
        "TODO"
        self.visit_call(node)
        #self.write(".result")

    def visit_implicit_return(self, node):
        self.newline(node)
        if (not self.funcname.startswith("model_") and not self.funcname.startswith("init_")) :
            self.newline(node)
            if node.value is None:
                self.write('return')
            else:
                self.write('return ')
                self.visit(node.value)
            self.write(";")  
    
    def visit_return(self, node):
        if self.model:
            self.newline(node)
            self.indentation += 1
            for arg in self.add_features(node):
                if "feat" in dir(arg):
                    if arg.feat in ("OUT", "INOUT"):
                        self.newline(node) 
                        if arg.name in self.states:
                            self.write("s.set%s(%s);"%(arg.name,arg.name))
                        if arg.name in self.rates:
                            self.write("r.set%s(%s);"%(arg.name,arg.name))
                        if arg.name in self.auxiliary:
                            self.write("a.set%s(%s);"%(arg.name,arg.name))
        else:
            self.newline(node)
            self.indentation += 1
    
    def visit_list(self, node): 
        self.visit_decl(node.pseudo_type)
        self.write(u'{')
        self.comma_separated_list(node.elements)
        self.write(u'}')
    
    def visit_tuple(self,node):
        self.write("make_tuple(")
        self.comma_separated_list(node.elements)
        self.write(")")
    

    def visit_datetime(self, node):
        self.write("new DateTime(")
        self.comma_separated_list(node.elements)
        self.write(")")
    
    def visit_str(self, node):
        self.safe_double(node)


    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl:
            self.newline(node)
            if 'value' not in dir(n) and not isinstance(n.pseudo_type, list) and n.pseudo_type!="datetime":
                self.write(self.types[n.pseudo_type])
                self.write(' %s;'%n.name) 
            if 'elements' not in dir(n) and n.type in ("list","array"):
                if n.type=="list":
                    self.write("vector<%s> %s;"%(self.types[n.pseudo_type[1]],n.name))
                if n.type=="array":
                    self.write(self.types["array"]%(self.types[n.pseudo_type[1]], n.elts.name if "name" in dir(n.elts) else n.elts.value))
                    self.write("%s;"%n.name)
            if 'value' in dir(n) and n.type in ("int", "float", "str", "bool"):
                self.write("%s %s"%(self.types[n.type], n.name))
                self.write(" = ")
                if n.type=="local":
                    self.write(n.value)
                else: self.visit(n)
                self.write(";")           
            elif  n.type=='datetime':
                self.newline(node)
                self.write("DateTime ")
                self.write(n.name)
                if "elts" in dir(n):
                    self.write(" = ")
                    self.visit(n.elts)
                self.write(";")            
            elif 'elements' in dir(n) and n.type in ("list", "tuple"):
                if n.type=="list":
                    self.visit_decl(n.pseudo_type)
                    self.write(n.name)
                    self.write(" = ") 
                    self.write(u'{')
                    self.comma_separated_list(n.elements)
                    self.write(u'};')
                if n.type=='tuple':
                    pass
            elif 'pairs' in dir(n) and n.type=="dict":
                self.visit_decl(n.pseudo_type)
                self.write(n.name)             
                self.write(u' = {')
                self.comma_separated_list(n.pairs)
                self.write(u'};')
            
                
        self.newline(node)
    
    def visit_list_decl(self, node, pa=None):        
        if not isinstance(node[1], list):
            self.write(self.types[node[1]])
            self.write('>')
        else:
            node = node[1]
            self.visit_decl(node, pa)
            self.write('>')
        if pa: self.write(" %s"%pa.name)
    
    def visit_dict_decl(self, node):  
        self.write(self.types[node[1]])
        self.write(",")        
        if not isinstance(node[2], list):
            self.write(self.types[node[2]])
            self.write('>')
        else:
            node = node[2]
            self.visit_decl(node)
            self.write('>')
    
    def visit_tuple_decl(self, node):
        self.visit_decl(node[0])
        for n in node[1:-1]:
            self.visit_decl(n)
            self.write(",")
        self.visit_decl(node[-1])
        self.write('>')
    
    def visit_float_decl(self, node, pa=None):
        self.write(self.types[node])
        self.write(" %s"%pa.name) if (pa and "name" in dir(pa)) else ''

    def visit_datetime_decl(self, node):
        self.write(self.types[node]) 

    def visit_int_decl(self, node, pa=None):
        self.write(self.types[node])
        self.write(" %s"%pa.name) if (pa and "name" in dir(pa)) else ''

    def visit_str_decl(self, node, pa=None):
        self.write(self.types[node])
        self.write(" %s"%pa.name) if (pa and "name" in dir(pa)) else ''
        
    def visit_bool_decl(self, node, pa=None):
        self.write(self.types[node])
        self.write(" %s"%pa.name) if (pa and "name" in dir(pa)) else ''        

    def visit_array_decl(self, node, pa=None):
        v =self.array_parameter([pa])[0]
        if pa.name in v: size = v[pa.name]
        else: size = pa.elts[0].value
        if not isinstance(node[1], list):
            self.write("%s, %s"%(self.types[node[1]],size))
            self.write('>& ')
        else:
            node = node[1]
            self.visit_decl(node)
            self.write('>& ')
        self.write(pa.name)
        
        
    def visit_decl(self, node, pa=None):
        if isinstance(node, list):
            if node[0]=="list":
                self.write('vector<')
                self.visit_list_decl(node, pa)
            if node[0] == "dict":
                self.write("map<")
                self.visit_dict_decl(node)
            if node[0]=="tuple":
                self.write('tuple<')
                self.visit_tuple_decl(node)
            if node[0]=="array":
                self.write('array<')
                self.visit_array_decl(node, pa)
        else:
            if node=="float":
                self.visit_float_decl(node, pa)
            if node =="int":
                self.visit_int_decl(node, pa)
            if node =="str":
                self.visit_str_decl(node, pa)
            if node =="bool":
                self.visit_bool_decl(node, pa) 
            if node in ("DateTime", "datetime"):
                self.visit_datetime_decl(node)                              
            
            
    def visit_pair(self, node):
        self.write(u'{')
        self.visit(node.key)
        self.write(u", ")
        self.visit(node.value)
        self.write(u'}')
            
    def visit_call(self, node):
        want_comma = []
        def write_comma():
            if want_comma:
                self.write(', ')
            else:
                want_comma.append(True)
        if "attrib" in dir(node):
             self.write(u"%s.%s"%(node.namespace,self.visit(node.function)))
        else:
            if callable(node.function):
                self.visit(node.function(node))
            else: 
                self.write(node.function)
                self.write('(')
                if isinstance(node.args, list):
                    for arg in node.args:
                        write_comma()
                        self.visit(arg)
                else:self.visit(node.args)
                self.write(')')
    
    def visit_standard_call(self, node):     
        node.function = self.functions[node.namespace][node.function]
        self.visit_call(node) 

        
    def visit_importfrom(self, node):
        pass
    
    def visit_for_statement(self, node):
        self.newline(node)
        self.write("for(")
        if "iterators" in dir(node):
            self.visit(node.iterators) 
        if "sequences" in dir(node):
            self.visit(node.sequences)
            self.write(')')
        self.newline(node)
        self.write('{')   
        if "iterators" in dir(node):
            self.newline(node)
            self.indentation += 1 
            self.write("%s = %s_cyml;"%(node.iterators.iterator.name, node.iterators.iterator.name))
            self.indentation -= 1
        self.body(node.block)
        self.newline(node)
        self.write('}')   
          
    def visit_for_iterator_with_index(self, node):
        self.visit(node.index)
        self.write(' , ')
        self.visit(node.iterator)        

    def visit_for_sequence_with_index(self, node):     
        "TODO"
        pass

    
    def visit_for_iterator(self, node):
        #self.write("%s "%node.iterator.pseudo_type)
        self.write("const auto& ")
        self.visit(node.iterator)
        self.write("_cyml")
        self.write(" : ")
           
    
    def visit_for_range_statement(self, node):
        self.newline(node)
        self.write("for (")
        self.visit(node.index)
        self.write("=")
        self.visit(node.start)
        self.write(' ; ')
        self.visit(node.index)
        self.write("!=")        
        self.visit(node.end)
        self.write(' ; ')
        self.visit(node.index)
        self.write("+=")
        if "value" in dir(node.step) and node.step.value==1: 
            self.write("1")
        else:      
            self.visit(node.step)
        self.write(')')
        self.newline(node)
        self.write('{')        
        self.body(node.block)
        self.newline(node)
        self.write('}')        
        
    def visit_while_statement(self, node):
        self.newline(node)
        self.write('while ( ')
        self.visit(node.test)
        self.write(')')
        self.newline(node)
        self.write('{')
        self.body_or_else(node)
        self.newline(node)
        self.write('}')        





class CppTrans(CppGenerator):
    """ This class used to generates states, rates and auxiliary classes
    for C++ languages.
    """
    
    def __init__(self, models, tree=None):
        CppGenerator.__init__(self, tree)
        #CppRules.__init__(self)
        self.models=models
        self.states=[]
        self.rates=[]
        self.auxiliary=[]
        self.extern =[] 
        self.modparam=[] 
    DATATYPE={
        "INT": "int",
        "DOUBLE": "float",
        "STRING":"str",
        "DATEARRAY":["array","str"],
        "INTARRAY":["array","int"],
        "DOUBLEARRAY":["array","float"],
        "STRINGARRAY":["array","str"],
        "STRINGLIST":["list","str"],
        "DOUBLELIST":["list","float"],
        "INTLIST":["list","int"],
        "DATELIST":["list","str"],
        "BOOLEAN":'bool',
        "DATE":"str"
    }
    def model2Node(self):
        variables=[]
        varnames=[]   
        for m in self.models:
            if "function" in dir(m):
                for f in m.function:
                    self.extern.append(f.name)
            for inp in m.inputs:
                if inp.name not in varnames:
                    variables.append(inp)
                    varnames.append(inp.name)
            for out in m.outputs:
                if out.name not in varnames:
                    variables.append(out)
                    varnames.append(out.name)
            if "ext" in dir(m):
                for ex in m.ext:
                    if ex.name not in varnames:
                        variables.append(ex)
                        varnames.append(ex.name) 

        #print(len(variables))
        for var in variables:
            if "variablecategory" in dir(var):
                if var.variablecategory=="state" and not var.name.endswith("_t1"):
                    self.states.append(var)
                if var.variablecategory=="rate" :
                    self.rates.append(var)
                if var.variablecategory=="auxiliary":
                    self.auxiliary.append(var)
            if "parametercategory" in dir(var):
                self.modparam.append(var)
        #print(self.auxiliary)

        def create(typevar):
            node_typevar=[]
            def catvar(var):
                if "variablecategory" in dir(var) and var.variablecategory=="state": return "s"
                if "variablecategory" in dir(var) and var.variablecategory=="rate": return "r"
                if "variablecategory" in dir(var) and var.variablecategory=="auxiliary": return "a"
            for st in typevar:
                if st.datatype in ("INT","DOUBLE","BOOLEAN","STRING","INTLIST","DOUBLELIST","STRINGLIST", "DATE", "DATELIST"):
                    node=Node(type="local", name=st.name, pseudo_type=self.DATATYPE[st.datatype], cat=catvar(st), desc = st.description, unit = st.unit)
                    node_typevar.append(node)
                if st.datatype in ("INTARRAY","DOUBLEARRAY","STRINGARRAY", "DATEARRAY", ):
                    if st.len.isdigit():
                        elts = Node(type='int', value= st.len, pseudo_type= 'int', desc = st.description, unit = st.unit)
                    else:
                        elts = Node(type='name', name= st.len, pseudo_type= 'int', desc = st.description, unit = st.unit)
                    node=Node(type="local", name=st.name, elts=[elts], pseudo_type=self.DATATYPE[st.datatype], cat=catvar(st), desc = st.description, unit = st.unit)
                    node_typevar.append(node)
            return node_typevar
        self.node_states = create(self.states)
        self.node_rates= create(self.rates)
        self.node_auxiliary= create(self.auxiliary) 
        self.node_param=create(self.modparam)       

    def private_hpp(self, node):
        self.write("private:")
        self.indentation += 1
        for arg in node:
            self.newline(node)
            self.visit_decl(arg.pseudo_type)
            self.write(" %s;"%arg.name)
    
    def public_hpp(self, node, typ, mc=None, h=None, init=False, iscompo=False):
        self.write("public:")
        self.indentation += 1
        self.newline(1)
        self.write("%s();"%typ)
        self.newline(1)
        if iscompo: self.write("%s(const %s& copy);"%(typ, typ))  # copy constructor
        self.newline(1)
        if mc: # except domain classes
            mc = mc.capitalize()
            self.write("void  Calculate_Model(%sState& s, %sState& s1, %sRate& r, %sAuxiliary& a);"%(mc, mc,mc, mc))
        
        if init: # initialization
            self.newline(1)
            mc = mc.capitalize()
            self.write("void  Init(%sState& s,%sState& s1, %sRate& r, %sAuxiliary& a);"%(mc, mc, mc, mc))        
        
        if h:  # function externes
            for i in h:
                self.newline(1)
                self.visit_decl(list(i.values())[0][0])
                self.write(" %s("%list(i.keys())[0])
                x=list(i.values())[0][1]
                for pa in x:
                    self.visit_decl(pa.pseudo_type)
                    self.write(" %s"%pa.name)
                    if pa!=x[len(x)-1]:
                        self.write(",")
                self.write(");")
        for arg in node:
            self.newline(node)
            self.visit_decl(arg.pseudo_type)
            self.write(" get%s();"%arg.name) if not isinstance(arg.pseudo_type, list) else self.write("& get%s();"%arg.name) 
            self.newline(node)
            self.write("void set%s("%arg.name)
            self.visit_decl(arg.pseudo_type)
            self.write(" _%s);"%arg.name) if not isinstance(arg.pseudo_type, list) else self.write("& _%s);"%arg.name)



    def private(self,node):
        for arg in node:
            self.newline(node) 
            self.write ('private ') 
            self.visit_decl(arg.pseudo_type)
            self.write(" _")
            self.write(arg.name) 
            if arg.pseudo_type[0] =="list":
                self.write("()")
            elif arg.pseudo_type[0] =="array":
                self.write(" = new %s[%s]"%(self.types[arg.pseudo_type[1]], arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name))
            self.write(";") 

    def getset(self,node, wrap=False):
        for arg in node:         
            self.newline(node)
            self.write("public ")
            if isinstance(arg.pseudo_type, list):
                if arg.pseudo_type[0] in ("list", "array"):
                    self.visit_decl(arg.pseudo_type)
                    self.write(' ' + arg.name)                                                            
            else:
                self.visit_decl(arg.pseudo_type)
                self.write(' ' +arg.name)
            self.write(self.public_properties%(arg.name,arg.name)) if wrap==False else self.write(self.public_properties_wrap%(arg.cat,arg.name))


    def copyconstructor(self,node):
        for arg in node:
            self.newline(node)
            if isinstance(arg.pseudo_type, list):
                if arg.pseudo_type[0] =="list":
                    self.write("vector<%s> %s;"%(arg.name, self.types[arg.pseudo_type[1]]))
                    self.write(self.copy_constrList%(arg.name,arg.name,arg.name))
                if arg.pseudo_type[0] =="array":
                    self.write("%s = new %s[%s];"%(arg.name, self.types[arg.pseudo_type[1]], arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name))
                    self.write(self.copy_constrArray%(arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name,arg.name,arg.name))
            else:
                self.write("_%s = toCopy._%s;"%(arg.name, arg.name))

    def generate(self, nodes, typ): 
        self.newline(1)
        self.write("%s::%s() { }"%(typ,typ))
        self.newline(extra=1)
        self.getter(typ, nodes)
        self.newline(extra = 1)
        self.setter(typ, nodes)
    
    def generate_hpp(self, node, typ, dc=False, mc=None, h=None, init=False, iscompo=False):
        self.write("class %s"%typ)
        self.newline(1)
        self.write("{")
        self.newline(node)
        self.indentation += 1        
        self.newline(1)
        self.private_hpp(node)
        self.newline(node)
        self.indentation -= 1
        self.public_hpp(node, typ,mc,h, init, iscompo)
        self.newline(extra = 1)
        if iscompo: self.instanceModels()   
        self.newline(extra=1)
        self.indentation -= 2
        self.write("};")
        self.newline(1)
        if dc: self.write("#endif")
    
    def instanceModels(self):
        self.newline(extra = 1)
        for m in self.models[0].model:
            name = m.name.capitalize()
            self.write("%s _%s;"%(name, name))
            self.newline(1)





def to_struct_cpp(models, rep, name):
    header_cpp(models, rep, name)
    header_mu_cpp(models, rep, name)
    headerCompo(models, rep, name)
    generator = CppTrans(models)
    generator.result=['#include "%sState.h"'%name.capitalize()]
    generator.model2Node()
    states = generator.node_states
    generator.generate(states, "%sState"%name.capitalize())
    z= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sState.cpp"%name.capitalize()))
    with open(filename, "wb") as tg_file:
        tg_file.write(z.encode('utf-8'))
    rates = generator.node_rates
    generator.result=['#include "%sRate.h"'%name.capitalize()]
    generator.generate(rates, "%sRate"%name.capitalize())
    z1= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sRate.cpp"%name.capitalize()))
    with open(filename, "wb") as tg1_file:
        tg1_file.write(z1.encode('utf-8'))       
    auxiliary = generator.node_auxiliary
    generator.result=['#include "%sAuxiliary.h"'%name.capitalize()]
    generator.generate(auxiliary, "%sAuxiliary"%name.capitalize())
    z2= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sAuxiliary.cpp"%name.capitalize()))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z2.encode('utf-8'))
    return 0
def header_cpp(models, rep, name):
    generator = CppTrans(models)
    generator.result=[u"#ifndef _%sState_\n#define _%sState_\n#define _USE_MATH_DEFINES\n#include <cmath>\n#include <iostream>\n# include<vector>\n# include<string>\nusing namespace std;\n"%(name.capitalize(),name.capitalize())]
    generator.model2Node()
    states = generator.node_states
    generator.generate_hpp(states, "%sState"%name.capitalize(), dc=True)
    z= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sState.h"%name.capitalize()))
    with open(filename, "wb") as tg_file:
        tg_file.write(z.encode('utf-8'))
    rates = generator.node_rates
    generator.result=[u"#ifndef _%sRate_\n#define _%sRate_\n#define _USE_MATH_DEFINES\n#include <cmath>\n#include <iostream>\n# include<vector>\n# include<string>\nusing namespace std;\n"%(name.capitalize(),name.capitalize())]
    generator.generate_hpp(rates, "%sRate"%name.capitalize(), dc=True)
    z1= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sRate.h"%name.capitalize()))
    with open(filename, "wb") as tg1_file:
        tg1_file.write(z1.encode('utf-8'))       
    auxiliary = generator.node_auxiliary
    generator.result=[u"#ifndef _%sAuxiliary_\n#define _%sAuxiliary_\n#define _USE_MATH_DEFINES\n#include <cmath>\n#include <iostream>\n# include<vector>\n# include<string>\nusing namespace std;\n"%(name.capitalize(),name.capitalize())]
    generator.generate_hpp(auxiliary, "%sAuxiliary"%name.capitalize(), dc=True)
    z2= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sAuxiliary.h"%name.capitalize()))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z2.encode('utf-8'))
    return 0


def header_mu_cpp(models, rep, name):
    mc = models[0].name 
    h = [] 
    init=False
    for m in models[0].model:
        if m.function:
            for mf in m.function:
                file_func = mf.filename
                path_func = Path(os.path.join(m.path,"crop2ml", file_func))
                func_tree=parser(Path(path_func))  
                newtree = AstTransformer(func_tree,path_func)
                dictAst = newtree.transformer()
                nodeAst= transform_to_syntax_tree(dictAst)
                z ={nodeAst.body[0].name: [nodeAst.body[0].return_type,nodeAst.body[0].params]}
                h.append(z) 
        if m.initialization:
                init = True
        generator = CppTrans([m])
        generator.result=[u'#define _USE_MATH_DEFINES\n#include <cmath>\n#include <iostream>\n# include<vector>\n# include<string>\n#include "%sState.h"\n#include "%sRate.h"\n#include "%sAuxiliary.h"\nusing namespace std;\n'%(name.capitalize(),name.capitalize(), name.capitalize())]
        generator.model2Node()
        param = generator.node_param
        generator.generate_hpp(param, "%s"%m.name.capitalize(), mc=mc, h=h, init=init)
        z= ''.join(generator.result)
        filename = Path(os.path.join(rep, "%s.h"%m.name.capitalize()))
        with open(filename, "wb") as tg_file:
            tg_file.write(z.encode('utf-8'))
        h=[]

def headerCompo(models, rep, name):
    ''' Header file of model composite'''
    mc = models[0].name 
    h = [] 
    models_incl = ['#include "%s.h"'%m.name.capitalize() for m in models[0].model]
    #domclass_inc = ['#include "%sState.h"'%name.capitalize(),'#include "%sRate.h"'%name.capitalize(),'#include "%sAuxiliary.h"'%name.capitalize()]   
    includes = '\n'.join(models_incl)
    generator = CppTrans(models)
    generator.result=["%s"%includes + "\n" + "using namespace std;\n\n"]
    generator.model2Node()
    param = generator.node_param
    generator.generate_hpp(param, "%sComponent"%mc.capitalize(), mc=mc, h=h, init=True, iscompo=True)
    z= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sComponent.h"%mc.capitalize()))
    with open(filename, "wb") as tg_file:
            tg_file.write(z.encode('utf-8'))


class CppCompo(CppTrans):
    """ This class generate the C++ composite class.
    """
    def __init__(self, tree=None, modelt=None, name=None):
        CppTrans.__init__(self,[modelt]) 
        self.modelt=modelt
        self.tree = tree
        self.name = modelt.name
        self.init=False
        self.write('#include "%sComponent.h"\n'%self.name.capitalize()) 
        self.params = [pa for pa in self.modelt.inputs if "parametercategory" in dir(pa)]
        self.model2Node()
        self.statesName = [st.name for st in self.states]
        self.ratesName = [rt.name for rt in self.rates]
        self.auxiliaryName = [au.name for au in self.auxiliary]
        self.aux = [link["source"].split(".")[1] for link in self.modelt.internallink]
        self.realinp=[]  # determine the real inputs of the composite      
        for node in self.node_auxiliary:
            if node.name not in self.realinp and node.name not in self.aux:
                self.realinp.append(node)

    def visit_module(self, node):        
        self.visit(node.body)
        self.newline(node)
        if "function" in dir(self.modelt) and self.modelt.function:
            func_name = os.path.split(self.modelt.function[0].filename)[1]
            func_path = os.path.join(self.modelt.path,"src","pyx", func_name)
            func_tree=parser(Path(func_path))  
            newtree = AstTransformer(func_tree, func_path)
            dictAst = newtree.transformer()
            nodeAst= transform_to_syntax_tree(dictAst)
            self.modelt=None
            self.visit(nodeAst.body)
        self.indentation -= 1        
        self.newline(node)              

    def visit_function_definition(self, node):      
        self.add_features(node)
        self.funcname = node.name
        self.write(self.constructor%("%sComponent"%self.modelt.name.capitalize(),"%sComponent"%self.modelt.name.capitalize())) if not node.name.startswith("init_") else self.write("")
        self.newline(extra=1)          

        if self.node_param and not node.name.startswith("init_"):
            self.getter( "%sComponent"%self.name.capitalize(),self.node_param)
            self.newline(extra=1)
            self.setter( "%sComponent"%self.name.capitalize(),self.node_param)
            self.newline(node)      

        if not node.name.startswith("init_"):
            self.write("void %sComponent::Calculate_Model("%self.name.capitalize())
        else:
            self.write("void %sComponent::Init("%self.name.capitalize())
            self.init=True
        self.write('%sState& s, %sState& s1, %sRate& r, %sAuxiliary& a)'%(self.name.capitalize(),self.name.capitalize(), self.name.capitalize(), self.name.capitalize()))
        self.newline(node)
        self.write('{') 
        self.newline(node)
        self.body(node.block)
        self.newline(node)
        self.visit_return(node)
        self.newline(node)
        #self.indentation -= 1 
        self.write('}') 
        self.newline(node)
        typ = self.modelt.name.capitalize()+"Component"
        if not node.name.startswith("init_"):
            self.write("%s::%s(const %s& toCopy)"%(typ, typ, typ))
            self.newline(1)
            self.write("{")
            self.copyconstructor(self.node_param)
            self.newline(node)
            self.write('}')  
        else: self.write("")###### copy constructor     
        self.newline(1)

    def visit_assignment(self, node):
        if "function" in dir(node.value) and node.value.function.split('_')[0]=="model":
            name  = node.value.function.split('model_')[1]
            self.write("_%s.Calculate_Model(s, s1, r, a);"%(name.capitalize()))
            self.newline(node)
        else:
            self.newline(node)
            self.visit(node.target)
            self.write(' = ')
            self.visit(node.value) 
            self.write(";")
            self.newline(node)

    def visit_declaration(self, node):
        if self.init is True:
            return CppGenerator(self.tree).visit_declaration(node)
        else: 
            pass

    def assignParam(self):
        h = 'from datetime import datetime\n'
        for m in self.model.inputs:
            if "parametercategory" in dir(m):
                h +="cdef " + my_input(m) + "\n"
        return h
    
    def tranAssignParam(self):
        from pycropml.transpiler.main import Main
        snip =Main(self.assignParam(),"cpp")
        a=snip.parse()    
        g=snip.to_ast(self.assignParam())  
        snip.dictAst
        return snip.to_source()
    
    def format(self):
        code = self.tranAssignParam()
        lines = code.split("\n")
        print(lines)
        lines = lines[5:-1]
        code = "\n".join(lines)
        return code

    def visit_local(self, node):
        if node.name in self.statesName:
            self.write("s.%s"%node.name)
        elif node.name in self.ratesName:
            self.write("r.%s"%node.name)
        elif node.name in self.auxiliaryName:
            self.write("a.%s"%node.name)
        else: self.write(node.name)


    """def visit_declaration(self, node):
        pass"""
    
    def visit_return(self, node):
        self.newline(node)
    
    def setter(self,m, node):
        for arg in node:
            self.newline(node)
            self.write("void %s::set%s("%(m,arg.name))
            self.visit_decl(arg.pseudo_type)
            if not isinstance(arg.pseudo_type, list):
                self.write(" _%s)"%arg.name)
            else:
                self.write("& _%s)"%arg.name)
            self.newline(1)
            self.write("{")
            self.newline(1)
            self.indentation += 1
            mo = self.get_mo(arg.name)
            for mi in mo:
                self.write("_%s.set%s(_%s);"%(mi.capitalize(),arg.name, arg.name))            
                self.newline(1)    
            self.newline(1)
            self.indentation -=1
            self.write("}")

        
        

 
    def get_mo(self,varname):
        listmo=[]
        for inp in self.modelt.inputlink:
            var = inp["source"]
            mod = inp["target"].split(".")[0]
            if var==varname:
                listmo.append(mod)
        return listmo
    

      
    def copyconstructor(self,node):
        for arg in node:
            self.newline(node)
            if isinstance(arg.pseudo_type, list):
                if arg.pseudo_type[0] =="list":
                    self.write("    %s"%self.copy_constrList%(arg.name,arg.name,arg.name))
                if arg.pseudo_type[0] =="array":
                    self.write("    %s"%self.copy_constrArray%(arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name,arg.name,arg.name))
            else:
                self.write("    %s = toCopy.%s;"%(arg.name, arg.name)) 

    def initCompo(self):            
        pass
    
    def wrapper(self):           
        self.write("class %sWrapper"%self.modelt.name.capitalize())
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1
        self.privateWrap()
        self.constrWrap()
        self.newline(extra=1)
        self.write(self.format())
        self.newline(extra=1)
        self.outputWrap()
        self.newline(extra=1)
        self.copyconstrWrap()
        self.newline(extra=1)
        self.initWrap()
        self.newline(extra=1)
        self.loadParamWrap()
        self.newline(extra=1)
        self.estimateWrap()
        self.newline(extra=1)
        self.indentation -= 1
        self.write("}")
        self.newline(extra=1)


    def privateWrap(self) :
        name = self.modelt.name
        self.write("private %sState s;"%(name.capitalize()))
        self.newline(1)
        self.write("private %sRate r;"%(name.capitalize()))
        self.newline(1)
        self.write("private %sAuxiliary a;"%(name.capitalize()))
        self.newline(1)
        self.write("private %sComponent %sComponent;"%(name.capitalize(),name.lower()))
        self.newline(extra=1)
    
    def constrWrap(self):
        name = self.modelt.name
        self.write("public %sWrapper()"%(name.capitalize()))
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1
        self.write("s = new %sState();"%(name.capitalize()))
        self.newline(1)
        self.write("r = new %sRate();"%(name.capitalize()))
        self.newline(1)
        self.write("a = new %sAuxiliary();"%(name.capitalize()))
        self.newline(1)
        self.write("%sComponent = new %sComponent();"%(name.lower(), name.capitalize()))
        self.newline(1)
        self.write("loadParameters();")
        self.newline(1)
        self.indentation -= 1
        self.write("}")
    
    def outputWrap(self):
        out = [out.name for out in self.modelt.outputs]
        tabout=[]
        nodes =self.node_states+self.node_rates+self.node_auxiliary
        for node in nodes :
            if node.name in out and node.name not in tabout:
                self.getset([node], True)
                tabout.append(node.name)

    def copyconstrWrap(self):
        self.write("public %sWrapper(%sWrapper toCopy, bool copyAll) : this()"%(self.modelt.name.capitalize(),self.modelt.name.capitalize()))
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.write("s = (toCopy.s != null) ? new %sState(toCopy.s, copyAll) : null;"%(self.model.name.capitalize()))
        self.newline(1)
        self.newline(1)
        self.write("r = (toCopy.r != null) ? new %sRate(toCopy.r, copyAll) : null;"%(self.model.name.capitalize()))
        self.newline(1)
        self.write("a = (toCopy.a != null) ? new %sAuxiliary(toCopy.a, copyAll) : null;"%(self.model.name.capitalize()))
        self.newline(1)
        self.write("if (copyAll)")
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.write("%sComponent = (toCopy.%sComponent != null) ? new %sComponent(toCopy.%sComponent) : null;"%(self.model.name.lower(),self.model.name.lower(),self.model.name.capitalize(),self.model.name.lower()))
        self.newline(1)
        self.indentation -= 1        
        self.write("}")
        self.newline(1)
        self.indentation -= 1        
        self.write("}")

    def initWrap(self):
        self.write("public void Init()")
        self.write("{")
        self.newline(1)
        self.indentation += 1 
        self.write("%sComponent.Init(s, r, a);"%(self.modelt.name.lower()))
        self.newline(1)
        self.write("loadParameters();")
        self.newline(1)
        self.indentation -= 1
        self.write("}")
    
    def loadParamWrap(self):
        self.write("private void loadParameters()")  
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        tab=[]         
        for node in self.modparam :
            if node.name not in tab:
                self.write("%sComponent.%s = %s;"%(self.model.name.lower(), node.name, node.name))
                tab.append(node.name)
                self.newline(1)
        self.indentation -= 1 
        self.write("}")
    
    def estimateWrap(self):
        self.write("public void Estimate%s("%(self.modelt.name.capitalize()))       
        for node in self.realinp:
                self.visit_decl(node.pseudo_type)
                self.write(" ")
                self.write(node.name)
                self.write(", ") if node!=self.realinp[len(self.realinp)-1] else ''
        self.write(")")
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1 
        for node in self.realinp:
            self.write("a.%s = %s;"%(node.name, node.name))
            self.newline(1)
        self.write("%sComponent.Calculate_%s(s, s1, r, a);"%(self.modelt.name.lower(),self.modelt.name.lower()))
        self.newline(1)
        self.indentation -= 1 
        self.write("}")


def to_wrapper_cpp(models, rep, name):
    generator = CppCompo(modelt =models)
    generator.result=["#define _USE_MATH_DEFINES\n#include <cmath>\n#include <iostream>\n# include<vector>\n# include<string>\nusing namespace std;\n"]
    generator.model2Node()
    generator.wrapper()
    z= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sWrapper.cpp"%name.capitalize()))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z.encode('utf-8'))
    return 0
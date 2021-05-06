# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.rules.pythonRules import PythonRules
from pycropml.transpiler.generators.docGenerator import DocGenerator
import os
from pycropml.render_cyml import signature
from path import Path
from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree

class PythonGenerator(CodeGenerator, PythonRules):
    """This class contains the specific properties of 
    python language and use the NodeVisitor to generate a python
    code source from a well formed syntax tree.
    """
    def __init__(self, tree, model=None, name = None):
        CodeGenerator.__init__(self)
        PythonRules.__init__(self)
        self.tree=tree
        self.model=model
        self.name = name
        self.indent_with=' '*4 
        self.imp=True
        if self.model: 
            self.doc=DocGenerator(self.model, " ")

    def comment(self,doc):
        list_com = [self.indent_with + '#'+x for x in doc.split('\n')]
        com = '\n'.join(list_com)
        return com
    
    def visit_import(self, node):
        if self.imp:
            self.write(u"import %s" % node.module)

    def visit_notAnumber(self, node):
        self.write("float('nan')")

    def visit_local(self, node):
        if "units" in dir(node):
            self.write("%s%s"%(node.name,node.units)) if node.units[0]=='/' else self.write("%s*%s"%(node.name,node.units))
        else: self.write(node.name)

    def visit_int(self, node):
        if "units" in dir(node):
            self.write("%s%s"%(node.value,node.units)) if node.units[0]=='/' else self.write("%s*%s"%(node.value,node.units))
        else:self.write(node.value)


    def visit_assignment(self, node):
        self.newline(node)
        if node.value.type == "standard_call" and node.value.function=="integr":
            self.write("%s = copy(%s)"%(node.target.name, node.value.args[0].name))
            self.newline(node)
            if isinstance(node.value.args[1].pseudo_type, list):
                self.write("%s.extend("%node.target.name)
            else: self.write("%s.append("%node.target.name)
            self.visit( node.value.args[1])
            self.write(")")
        
        else:
            self.visit(node.target)
            self.write(' = ')
            self.visit(node.value)

    def visit_cond_expr_node(self, node):
        self.visit(node.true_val)
        self.write(u" if ")
        self.visit(node.test)
        self.write(u" else ")
        self.visit(node.false_val)  
        
    def visit_constant(self, node):
        self.write(self.constant[node.library][node.name])

    def visit_if_statement(self, node):
        self.newline(node)
        self.write('if ')
        self.visit(node.test)
        self.write(':')
        self.body(node.block)
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
        self.write('elif ')
        self.visit(node.test)
        self.write(':')
        self.body(node.block)

    def visit_else_statement(self, node):
        self.newline()
        self.write('else:')
        self.body(node.block)
    
    def visit_float(self, node):
        if "units" in dir(node):
            self.write("%s%s"%(node.value,node.units)) if node.units[0]=='/' else self.write("%s*%s"%(node.value,node.units))
        else: self.write(node.value)
        
    def visit_bool(self, node):
        self.write(str(node.value))

    def visit_str(self, node):
        self.safe_double(node)
    
    def visit_tuple(self, node):
        self.emit_sequence(node.elements, u"()")
        
    def visit_dict(self, node):
        self.emit_sequence(node.pairs, u"{}")
        
    def visit_pair(self, node):
        self.visit(node.key)
        self.write(u": ")
        self.visit(node.value)         

    def visit_ExprStatNode(self, node):
        self.newline(node)
        self.visit(node.expr)
    
    def visit_list(self, node):
        self.emit_sequence(node.elements, u"[]")

    def visit_datetime(self, node):
        self.write("datetime")
        self.emit_sequence(node.value, u"()")

    def visit_standard_method_call(self, node):
        l = node.receiver.pseudo_type
        if isinstance(l, list):
            l = l[0]
        z = self.methods[l][node.message]
        if callable(z):
            self.visit(z(node))
        
        else:
            if not node.args:
                self.write(node.message)
                self.write('(')
                self.visit(node.receiver)
                self.write(')')
            else:
                "%s.%s"%(self.visit(node.receiver),self.write(z))
                self.write("(")
                self.comma_separated_list(node.args)
                self.write(")")

    def visit_custom_call(self, node):
        self.visit_call(node)


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


    def visit_module(self, node):
        self.newline(extra=1)
        self.newline(node)
        self.write("# coding: utf8")
        self.newline(node)
        self.write("from pycropml.units import u")
        self.newline(node)
        self.write("from copy import copy\nfrom array import array\nfrom math import *\n")
        self.newline(node)
        self.visit(node.body)

        
    def visit_comparison(self, node):
        #self.write('(')
        self.visit_binary_op(node)
        #self.write(')')

    def visit_method_call(self, node):
        "%s.%s"%(self.visit(node.receiver),self.write(node.message))  
              
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
    
    def visit_unary_op(self, node):
        op = node.operator
        prec = self.unop_precedence[op]
        self.operator_enter(prec)
        self.write(u"%s" % self.unary_op[op])
        self.visit(node.value)
        self.operator_exit()

    def visit_function_definition(self, node):
        self.newline(extra=1)
        self.newline(node)
        self.write('def %s(' % node.name)
        for i, pa in enumerate(node.params):
            #if pa.type == "local": 
            self.write(pa.name)
            if "value" in dir(pa) or "elements" in dir(pa) or "pairs" in dir(pa) :
                #self.write(pa.name)
                self.write(" = ")
                self.visit(pa)  
            if i!= (len(node.params)-1):
                self.write(',\n         ')
        self.write('):')
        self.newline(node)
        if self.model and node.name.split("model_")[1]==signature(self.model):
            self.write('    """\n')
            self.write(self.doc.header)
            self.newline(node)
            self.write(self.doc.desc)
            self.newline(node)
            self.write(self.doc.inputs_doc)
            self.newline(node)
            self.write(self.doc.outputs_doc)
            self.newline(node)
            self.write('    """\n')
            self.newline(node)
            self.model = None
        self.body(node.block)
        
    def visit_implicit_return(self, node):
        self.newline(node)
        if node.value is None:
            self.write('return')
        else:
            self.write('return ')
        self.visit(node.value)

    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl  :           
            if 'value' in dir(n) and n.type in ("int", "float"):
                self.newline(node)
                self.write(n.name)
                self.write(" = ")                 
                self.write(n.value)
            elif 'value' in dir(n) and n.type=="bool":
                self.newline(node)
                self.write(n.name)
                self.write(" = ") 
                self.write(str(n.value))        
            elif 'value' in dir(n) and n.type=="str":
                self.newline(node)
                self.write(n.name)
                self.write(" = ") 
                self.emit_string(n)                
            elif 'elements' in dir(n) and n.type in ("list", "tuple"):
                self.newline(node)
                self.write(n.name)
                self.write(" = ") 
                if n.type=="list":                
                    self.visit_list(n)
                else: self.visit_tuple(n)
            elif 'args' in dir(n) and n.type=='datetime':
                self.newline(node)
                self.write(n.name)
                self.write(" = datetime") 
                self.visit_datetime               
            elif 'pairs' in dir(n) and n.type=="dict":
                self.newline(node)
                self.write(n.name)
                self.write(" = ")                 
                self.visit_dict(n)
            elif n.type=="array" and 'elements' in dir(n):
                if n.dim == 1:
                    self.write(n.name)
                    self.write(" = array('%s',"%n.pseudo_type[1][0])
                    self.write("[")
                    self.comma_separated_list(n.elements)
                    self.write("] )")                    
            elif n.type in ("list"):
                self.newline(node)
                self.write(n.name)
                self.write(" = []")                  


    def visit_array(self,node): 
        #self.write(node.name)
        self.write("[")
        self.comma_separated_list(node.elements)
        self.write("]")

    def visit_continuestatnode(self, node):
        self.newline(node)
        self.write('continue')
        
    def visit_breakstatnode(self, node):
        self.newline(node)
        self.write('break')              
        
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
            self.write(self.visit(node.function))
        self.write('(')
        for arg in node.args:
            write_comma()
            self.visit(arg)
        self.write(')')
    
    def visit_standard_call(self, node):
        node.function = self.functions[node.namespace][node.function]
        if callable(node.function):
               self.visit(node.function(node)) 
        else: self.visit_call(node)  
        
    def visit_importfrom(self, node):
        if self.imp:
            self.newline(node)
            if node.namespace=="math":
                self.write("from math import *")  
            else:
                self.write('from %s import ' % (node.namespace))
                for idx, item in enumerate(node.name):
                    if idx:
                        self.write(', ')
                    self.write(item)
    
    def visit_for_statement(self, node):
        self.newline(node)
        self.write("for ")
        if "iterators" in dir(node):
            self.visit(node.iterators) 
        if "sequences" in dir(node):
            self.visit(node.sequences)
        self.body(node.block)

    
    def visit_for_iterator_with_index(self, node):
        self.visit(node.index)
        self.write(' , ')
        self.visit(node.iterator)        

    def visit_for_sequence_with_index(self, node):
        
        self.write(" in enumerate(")
        self.visit(node.sequence)
        self.write('):')
    
    def visit_for_iterator(self, node):
        self.visit(node.iterator)
        self.write(" in ")
        
    def visit_for_sequence(self, node):
        self.visit(node.sequence)
        self.write(":")
        
        
    
    def visit_for_range_statement(self, node):
        self.newline(node)
        self.write("for ")
        self.visit(node.index)
        self.write(" in range(")
        self.visit(node.start)
        self.write(' , ')
        self.visit(node.end)
        self.write(' , ')
        self.visit(node.step)
        self.write('):')
        self.body(node.block)
        
    def visit_while_statement(self, node):
        self.newline(node)
        self.write('while ')
        self.visit(node.test)
        self.write(':')
        self.body_or_else(node)


class PythonCompo(PythonGenerator):
    """ This class generate the composite module in Python
    """
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        PythonGenerator.__init__(self,tree, model, self.name)
            
        

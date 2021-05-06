# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:05:11 2020

@author: midingoy
"""

from pycropml.transpiler.antlr_py.csharp import csharpRules
from pycropml.transpiler.env import Env

namespace = {
    'Math':'math'}

functions = {
        'math': {

        },
        'io': {
            'Console.ReadLine':       'read',
        },
        'system': {
            'min': 'Math.Min',
            'max': 'Math.Max',
            'abs': 'Math.Abs'},

        'datetime':{
            'DateTime': 'datetime'
        }
    }


def cyml_ru(cs_op, ru):  
    for k, v in ru.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if v == cs_op:
            return k
    
lib = csharpRules.Cs_CymlRules()
                
from pycropml.transpiler.pseudo_tree import Node
class Cs_Cyml_ast():
    
    op = lib.binary_op
    
    def __init__(self, tree, model=None, name=None, var= []):
        self.tree = tree
        self.model = model
        self.name = name
        self.recursive = False
        self.type_env = Env()
        self.var =  var


    def visit(self, node):
        '''
        Parameters
        ----------
        node : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        if isinstance(node, list):
            results = []
            for n in node:
                x = self.visit(n)
                if isinstance(x, list):
                    results.extend(x)
                else:
                    results.append(x)
            return results
        elif isinstance(node, Node):
            return getattr(self, 'visit_%s'%(node.type))(node)
        else: 
            return node
    
    def visit_namespace(self, node):
        return self.visit(node.body)
            
    def transform(self):
        self.type_env['functions'] = {}
        self.function_name = 'top level'
        self.decl = []
        body = self.visit(self.tree.body) if "body" in dir(self.tree) else self.visit(self.tree)
        
        return  {'type': 'module', 'body': body if isinstance(body, list) else [body]}
    
    def visit_classDef(self, node):
        return self.visit(node.block)
    
    def visit_methodDef(self, node):
        self.function_name = node.name
        pa = self.visit(node.params)
        block = self.visit(node.block)
        
        z = {
            'type':   "function_definition",
            'name':   node.name,
            'params': pa,
            'return_type':  node.return_type,
            'pseudo_type': node.pseudo_type,
            'block': block,
            'recursive':self.recursive

        }
        for j in self.decl: z['block'].insert(0,j)
        self.decl=[]
        return  z
    
    def translate_decl(self, type_):
        if isinstance(type_, Node):
            s = None
        elif type_ is None:
            s = None
        elif not isinstance(type_, list):
            s = lib.types[type_]
        else: s = [self.translate_decl(i) for i in type_]
        return s
    
    def visit_local(self, node):
        #ps = self.translate_decl(node.pseudo_type)
        #if str(node.name) not in self.type_env: self.type_env[str(node.name)]= ps
        return {"type":"local", "name":str(node.name), "pseudo_type": self.translate_decl(node.pseudo_type)}
    
    def visit_declaration(self, node):
        res = []
        for de in node.decl:
            if de.name not in self.var:
                z = self.visit(de)
                self.type_env[z["name"]] = z["pseudo_type"]
                res.append(z)            
        if res:
            return {"type":"declaration", "decl": res} 
        else:
            pass
    
    def visit_int(self, node):
        if "value" in dir(node) and "name" in dir(node): 
            val = self.visit(node.value)
            return  {'type': 'int', 'name': str(node.name), 'value': val["value"], 'pseudo_type': 'int'}
        elif "value" in dir(node): 
            val = self.visit(node.value)
            return {'type': 'int', 'value': val, 'pseudo_type': 'int'}
        elif "name" in dir(node): 
            return {'type': 'int', 'name':str(node.name), 'pseudo_type': 'int'}

    def visit_double(self, node):
        if "value" in dir(node) and "name" in dir(node): 
            val = self.visit(node.value)
            return  {'type': 'float', 'name': str(node.name), 'value': val, 'pseudo_type': 'float'}
        elif "value" in dir(node): 
            val = self.visit(node.value)
            return {'type': 'float', 'value': val, 'pseudo_type': 'float'}
        elif "name" in dir(node): return {'type': 'float', 'name':str(node.name), 'pseudo_type': 'float'}
        else: print ("todo doble")
 
    def visit_string(self, node):
        if "value" in dir(node) and "name" in dir(node): 
            val = self.visit(node.value)
            return  {'type': 'str', 'name': node.name, 'value': val["value"], 'pseudo_type': 'str'}
        elif "value" in dir(node): 
            val = self.visit(node.value)
            return {'type': 'str', 'value': val, 'pseudo_type': 'str'}
        elif "name" in dir(node): return {'type': 'str', 'name':node.name, 'pseudo_type': 'str'}
 
    def visit_fielddecl(self, node):
        return
 
    def visit_float(self, node):
        if "value" in dir(node) and "name" in dir(node): 
            val = self.visit(node.value)
            return  {'type': 'float', 'name': str(node.name), 'value': val["value"], 'pseudo_type': 'float'}
        elif "value" in dir(node): 
            val = self.visit(node.value)
            return {'type': 'float', 'value': val, 'pseudo_type': 'float'}
        elif "name" in dir(node): return {'type': 'float', 'name':str(node.name), 'pseudo_type': 'float'}

    def visit_array(self, node):
        if "init" not in dir(node):
            res = {"type":"array",
                   "name": str(node.name),
                   "pseudo_type": self.translate_decl(node.pseudo_type),
                   "dim":0} 
            self.type_env[res["name"]] = res["pseudo_type"]
        else: 
            z = self.visit(node.init.value) 
            res = {'type': 'array',
              'elements': z,           
              'pseudo_type': ['array', z[0]["type"]],
              'dim':1}
            
        return res
    
    def visit_List(self, node):
        if "value" not in dir(node):
            z = []
        elif "name" not in dir(node):
            z = self.visit(node.init.value)
        else:
            z = self.visit(node.value.init.value)
        res =   {'type': 'list',
          'elements': z,           
          'pseudo_type': self.translate_decl(node.pseudo_type)}  
        if "name" in dir(node):
            res["name"] = str(node.name) 
            return res
        if "args" in dir(node):
            return {"type": "standard_call",
                    "function":"copy",
                    "namespace":"system",
                    "pseudo_type": self.translate_decl(node.pseudo_type),
                    "args": node.args[0]
                }
            
        #self.type_env[res["name"]] = res["pseudo_type"]
        
        
    def visit_assignment(self, node):
        target = self.visit(node.target)
        value = self.visit(node.value)
        if "name" in value and target["name"]== value["name"]:
            return
        else:
            return {'type': 'assignment',
           'target': target,
           'op': '=',
           'value': value,
           'pseudo_type': 'Void'}
    
    def visit_cond_expr_node(self, node):
        return {
                'type': 'cond_expr_node',
                'test': self.visit(node.test),
                'true_val': self.visit(node.true_val),
                'pseudo_type': 'Void',
                'false_val': self.visit(node.false_val)
            }

    
    def visit_implicit_return(self, node):
        z = self.visit(node.value)
        
        return {'type': 'implicit_return',
         'value': z, 'pseudo_type': z['pseudo_type']}
    
    def visit_binary_op(self, node):
        return {'type': 'binary_op',
          'op': str(node.op),
          'left': self.visit(node.left),
          'right': self.visit(node.right),
          'pseudo_type': self.translate_decl(node.pseudo_type)}
    
    def visit_if_statement(self, node):
        return {'type': 'if_statement',
         'test': self.visit(node.test),
         'block': self.visit(node.block),
         'pseudo_type': 'Void',
         'otherwise': self.visit(node.otherwise)}
 
    def visit_else_statement(self, node):
        return {'type': 'else_statement',
             'block': self.visit(node.block),
             'pseudo_type': 'Void'}
    
    def visit_elseif_statement(self, node):
        return {'type': 'elseif_statement',
           'test': self.visit(node.test),
           'block': self.visit(node.block),
           'pseudo_type': 'Void'}
    
    def visit_comparison(self, node):
        return {'type': 'comparison',
            'op': cyml_ru(node.op, self.op),
            'left':self.visit(node.left),
            'right': self.visit(node.right),
            'pseudo_type': 'Void'}
    
    def visit_standard_call(self, node):
        return {'type': 'standard_call',
              'namespace': node.namespace,
              'function': node.function,
              'args': self.visit(node.args),
              'pseudo_type': self.translate_decl(node.pseudo_type)}
    
    def visit_standard_method_call(self, node):
        return {'type': 'standard_method_call',
                  'receiver': self.visit(node.receiver),
                  'args': self.visit(node.args) if "args" in dir(node) else [],
                  'message': node.message,
                  'pseudo_type': self.translate_decl(node.pseudo_type)}
    
    def visit_ExprStatNode(self, node):
        return {
            "type": "ExprStatNode",
            "expr": self.visit(node.expr)
        }
    
    def visit_custom_call(self, node):
        return {"type": "custom_call",
                "args": self.visit(node.args),
                "function": node.function,
                "pseudo_type": self.translate_decl(node.pseudo_type)}
    
    def visit_for_range_statement(self, node):
        
        z =  {'type': 'for_range_statement',
         'start': self.visit(node.start),
         'end': self.visit(node.end),
         'step': self.visit(node.step),
         'index': self.visit(node.index),
         'block': self.visit(node.block)}
        
        self.decl.append({'type': 'declaration',
                          'decl': [{'type': z["index"]["pseudo_type"],
                                    'name': z["index"]["name"],
                                    'pseudo_type': z["index"]["pseudo_type"]}]})
        return z
    
    def visit_for_statement(self, node):
        z =  {'type': 'for_statement',
                'sequences': {'type': 'for_sequence',
                    'sequence': self.visit(node.sequences.sequence)},
                'iterators': {'type': 'for_iterator',
                    'iterator': self.visit(node.iterators.iterator)},
                'block': self.visit(node.block)} 
        
        self.decl.append({'type': 'declaration',
                          'decl': [{'type': z["iterators"]["iterator"]["pseudo_type"],
                                    'name': z["iterators"]["iterator"]["name"],
                                    'pseudo_type': z["iterators"]["iterator"]["pseudo_type"]}]})
        
        return z
    
    def visit_unary_op(self, node):
        return {
            'type': 'unary_op',
                    'operator': str(node.operator),
                    'value': self.visit(node.value),
                    'pseudo_type': self.translate_decl(node.pseudo_type)
        } 
    
    def visit_while_statement(self, node):
        
        return {'type': 'while_statement',
            'test': self.visit(node.test),
            'block': self.visit(node.block),
            'pseudo_type': 'Void'
        }
        
    def visit_index(self, node):
        z = self.visit(node.sequence)
        index = self.visit(node.index)
        return {'type': 'index',
            'sequence': z,
            'index': index[0],
            'pseudo_type': z["pseudo_type"]}
    
    def visit_member_access(self, node):
        return {"type":"local", "name":node.member, "pseudo_type":None}


from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node

def translateCeil(node,*z): return {"type":"standard_method_call","receiver": {"type": "standard_call", 
'namespace': "math", "function":"ceil",'pseudo_type': "int", 'args':z[0]}, 'args': [],'message': 'float',"pseudo_type": 'float'}

class Cs_CymlRules(GeneralRule):
    def __init__(self):
        GeneralRule.__init__(self)
    binary_op = {"and": "&&",
                 "or": "||",
                 "not": "!",
                 "<": "<",
                 ">": ">",
                 "==": "==",
                 "+": "+",
                 "-": "-",
                 "*": "*",
                 "/": "/",
                 ">=": ">=",
                 "<=": "<=",
                 "!=": "!="
                 }

    unary_op = {
        'not': '!',
        '+': '+',
        '-': '-',
        '~': '~'
    }

    types = {
        "int": "int",
        "float": "float",
        "double": "float",
        "bool": "bool",
        "array": "array",
        "List": "list",
        "tuple": "tuple",
        "string": "str",
        "Dictionary": "dict",
        "DateTime":"datetime",
        "unknown":"unknown"
    }

    functions = {
        'Math': {
            'Log':         'math.log',
            'Tan':         'math.tan',
            'Sin':         'math.sin',
            'Cos':         'math.cos',
            'Asin':        'math.asin',
            'Acos':        'math.acos',
            'Atan':         'math.atan',
            'Sqrt':         'math.sqrt',
            'Ceiling':         translateCeil,
            'Round':        'math.round',
            'Exp':         'math.exp',
            'Pow':         'math.pow',
            'Min' :        'system.min',
            'Max' :        'system.max',
            'Abs':         'system.abs'

        },
        'io': {
            'Console.WriteLine':  'print',
            'Console.ReadLine':   'read',
            'File.ReadAllText':  'read_file',
            'File.WriteAllText': 'write_file'
        },
        'system': {
            'copy': 'copy'},

        'datetime':{
            'new DateTime': 'datetime '
        }
    }
    constant = {
            
        'math':{
                
            'Math.PI': 'pi'
                
                }            
    }        

    methods = {

        'int': {
            'float': 'float'
        },
        'float': {
            'int': 'int'
        },
        'str': {
            'int': 'int',
            '.IndexOf': 'find'
        },
        'List': {
            'length': "len",
            '.Add': 'append',
            'Sum': 'sum',
            '.RemoveAt': 'pop',
            '.Insert': "insert_at",
            '.Contains': 'contains?',
            '!Contains': "not contains?",
            '.IndexOf': 'index',
            'linq':'map'
        },
        'dict': {
            'len': "len",
            'keys': "keys",
            'values':"value",
            "get": "get"
        },
        'array':{
                'len': "len",
                '.Add': 'append'
                
                }
    }
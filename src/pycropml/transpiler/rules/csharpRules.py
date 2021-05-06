

from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node

def translateLenList(node): return Node("method_call", receiver=node.receiver, message=".Count", args=[], pseudo_type=node.pseudo_type)
def translateSum(node): return Node("method_call", receiver=node.receiver, message=".Sum()", args=[], pseudo_type=node.pseudo_type)
def translateNotContains(node): return Node("unary_op", operator="not", value=Node("standard_method_call", receiver=node.receiver, message="contains?", args=node.args, pseudo_type=node.pseudo_type))
def translateLenDict(node): return Node("method_call", receiver=node.receiver, message=".Count", args=[], pseudo_type=node.pseudo_type)
def translateLenArray(node): return Node("method_call", receiver=node.receiver, message=".Length", args=[], pseudo_type=node.pseudo_type)
def translatekeyDict(node): return Node("method_call", receiver=node.receiver, message=".Keys.ToList()", args=[], pseudo_type=node.pseudo_type)
def translatevalueDict(node): return Node("method_call", receiver=node.receiver, message=".Values.ToList()", args=[], pseudo_type=node.pseudo_type)
def translateget(node): 
    if "value" in dir(node.args[0]):
        return Node('index',sequence = Node('local',name= node.receiver.name, pseudo_type = node.receiver.pseudo_type), index= Node(node.args[0].type, value = node.args[0].value, pseudo_type= node.args[0].pseudo_type), pseudo_type = "Void")
    elif "name" in dir(node.args[0]):
        return Node('index',sequence = Node('local',name= node.receiver.name, pseudo_type = node.receiver.pseudo_type), index= Node(node.args[0].type, name = node.args[0].name, pseudo_type= node.args[0].pseudo_type), pseudo_type = "Void")

def translatePrint(node):
    if node.args[0].type=="tuple":
        x=[]
        for n in node.args[0].elements:
            if "value" in dir(n) and n.value in [b'\r', b'\t', b'\n']: continue
            x.append(Node(type="ExprStatNode", expr=Node(type="custom_call", function="Console.WriteLine", args=[n])))
        return x
    else:
        return Node(type="ExprStatNode", expr=Node(type="custom_call", function="Console.WriteLine", args=node.args))
def translatePow(node): 
    if node.pseudo_type=="int":
        return Node(type="custom_call", function="(int) Math.Pow", args=node.args)
    return Node(type="custom_call", function="Math.Pow", args=node.args)
def linq(name, z=True, swap=False):
    def x(l, f, *args):
        pseudo_type, args = args[-1], list(args[:-1])
        if args and swap:
            f, args[0] = args[0], f
        cs = Node(type="method_call",receiver=l, message=name, args=[f] + args,pseudo_type= pseudo_type)
        if z:
            cs.pseudo_type = 'CSharpEnumerable'
            return Node(type="method_call",receiver=cs, message='ToList', args=[], pseudo_type=pseudo_type)
        else:
            return cs
    return x
def translateCopy(node):
    types = {
        "int": "int",
        "float": "double",
        "bool": "bool",
        "array": "%s[] %s= new %s",
        "list": "List",
        "tuple": "Tuple",
        "str": "string",
        "dict": "Dictionary",
        "datetime":"DateTime",
        "DateTime":"DateTime"
    }
    return Node(type="call", function = "new List<%s>"%(types[node.pseudo_type[1]]), args=[Node("local", name=node.args.name)])

class CsharpRules(GeneralRule):
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
        "float": "double",
        "bool": "bool",
        "array": "%s[] %s;",
        "list": "List",
        "tuple": "Tuple",
        "str": "string",
        "dict": "Dictionary",
        "datetime":"DateTime",
        "DateTime":"DateTime"
    }

    functions = {
        'math': {
            'ln':          'Math.Log',
            'log':         'Math.Log',
            'tan':         'Math.Tan',
            'sin':         'Math.Sin',
            'cos':         'Math.Cos',
            'asin':        'Math.Asin',
            'acos':        'Math.Acos',
            'atan':         'Math.Atan',
            'sqrt':         'Math.Sqrt',
            'ceil':         '(int) Math.Ceiling',
            'round':        'Math.Round',
            'exp':         'Math.Exp',
            'pow':          'Math.Pow'

        },
        'io': {
            'print':    translatePrint,
            'read':       'Console.ReadLine',
            'read_file':  'File.ReadAllText',
            'write_file': 'File.WriteAllText'
        },
        'system': {
            'min': 'Math.Min',
            'max': 'Math.Max',
            'abs': 'Math.Abs',
            'pow': translatePow,
            'copy': translateCopy},

        'datetime':{
            'datetime': ' new DateTime'
        }
    }
    constant = {
            
        'math':{
                
            'pi': 'Math.PI'
                
                }            
    }        

    methods = {

        'int': {
            'float': '(double)'
        },
        'float': {
            'int': '(int)'
        },
        'str': {
            'int': '(int)',
            'find': '.IndexOf',
            'contains?': '.Contains'
        },
        'list': {
            'len': translateLenList,
            'append': '.Add',
            'sum': translateSum,
            'pop': '.RemoveAt',
            'insert_at': ".Insert",
            'contains?': '.Contains',
            'not contains?': translateNotContains,
            'index': '.IndexOf',
            'map':lambda node:linq('Select')(node.receiver, node.message, node.args)
        },
        'dict': {
            'len': translateLenDict,
            'keys': translatekeyDict,
            'values':translatevalueDict,
            "get": translateget
        },
        'array':{
                'len': translateLenArray,
                'append': '.Add'

                
                }
    }
    public_properties = '''
        {
            get { return this._%s; }
            set { this._%s= value; } 
        }'''

    public_properties_wrap = '''{ get { return %s.%s;}} 
     '''  
    constructor = '''
    public %s() { }
    '''

    copy_constr = '''
    public %s(%s toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    '''
    copy_constrList = '''
            for (int i = 0; i < toCopy.%s.Count; i++)
            { %s.Add(toCopy.%s[i]); }
    '''
    copy_constrArray = '''
            for (int i = 0; i < %s; i++)
            { _%s[i] = toCopy._%s[i]; }
    '''
    public_properties_compo = '''
    {
        get
        { return _%s.%s; }
        set
        { %s } 
    }
    '''
    copy_constr_compo = '''
    public %s(%s toCopy): this() // copy constructor 
    {
'''


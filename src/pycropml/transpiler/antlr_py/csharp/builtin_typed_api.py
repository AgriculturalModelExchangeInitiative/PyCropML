# coding: utf8
from __future__ import absolute_import
from pycropml.transpiler.errors import PseudoCythonTypeCheckError
from pycropml.transpiler.helpers import serialize_type
from Cython.Compiler import ExprNodes
from six.moves import zip


# based on pseudo
V = '_' # we don't really typecheck or care for a lot of the arg types, so just use this
_ = ()


'''Methods used to:
    -check data types compatibility
    
    - inference type compared with type declared
    
    - methods on builtin functions to check consistency
        
'''
def builtin_type_check(namespace, function, receiver, args):
    fs = TYPED_API[namespace]
    if fs == 'library':
        fs = TYPED_API['_%s' % namespace]
    # print(namespace, function, receiver, args, TYPED_API[namespace])
    # input(0)
    if function not in fs:        
        raise  PseudoCythonTypeCheckError('wrong usage of %s' % str(function))
    x = fs[function]
    a = namespace + '#' + function if receiver else namespace + ':' + function
    if namespace == 'List' or namespace == 'array':
        if not isinstance(receiver['pseudo_type'], list):
            generics = {'@t': args[0]['pseudo_type']}
            if receiver['pseudo_type']=="List": receiver["pseudo_type"]=["List",args[0]['pseudo_type']]
        else:
            generics = {'@t': receiver['pseudo_type'][1]}
    elif namespace == 'dict':
        generics = {'@k': receiver['pseudo_type'][1], '@v': receiver['pseudo_type'][2]}
    else:
        generics = {}

    
    s = []
    if x[0][0] == '*':
        e = x[0][1:]
        for arg in args:
            s.append(simplify(e, generics))
            arg_check(s[-1], arg, a)
    else:
        if len(x) - 1 != len(args):   
            raise PseudoCythonTypeCheckError("%s expects %d args not %d" % (a, len(x) - 1, len(args)))
        for e, arg in zip(x[:-1], args):
            s.append(simplify(e, generics))
            #arg_check(s[-1], arg, a)  to do
    s.append(simplify(x[-1], generics))
    return s

def arg_check(expected_type, args, a):
    if expected_type != args['pseudo_type'] and expected_type != 'Any' and not(expected_type == 'Number' and (args['pseudo_type'] == 'int' or args['pseudo_type'] == 'float' or args['pseudo_type'] == 'double')):
        raise PseudoCythonTypeCheckError('%s expected %s not %s' % (a, serialize_type(expected_type), serialize_type(args['pseudo_type'])))

def simplify(kind, generics):
    if not generics:
        return kind
    elif isinstance(kind, str):
        if kind[0] == '@' and kind in generics:
            return generics[kind]
        else:
            return kind
    else:
        return [simplify(child, generics) for child in kind]

# refactoring here in future

def add(l, r):
    if l == 'float' and r in ['float', 'int']  or r == 'float' and l in ['float', 'int'] :
        return [l, r, 'float']
    elif l == 'double' and r in ['float', 'int','double']  or r == 'double' and l in ['float', 'int',"double"] :
        return [l, r, 'double']
    elif l == 'int' and r == 'int':
        return [l, r, 'int']
    elif l == 'str' and r == 'str':
        return [l, r, 'str']
    elif isinstance(l, list) and l[0] == "List" and l == r:
        return [l, r, l]
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]
    else:
        return [l, r, "unknown"] #### to change
        #raise PseudoCythonTypeCheckError("wrong types for +: %s and %s" % (serialize_type(l), serialize_type(r)))

def sub(l, r):
    if l == 'float' and r in ['float', 'int']  or r == 'float' and l in ['float', 'int'] :
        return [l, r, 'float']
    elif l == 'double' and r in ['float', 'int','double']  or r == 'double' and l in ['float', 'int',"double"] :
        return [l, r, 'double']
    elif l == 'int' and r == 'int':
        return [l, r, 'int']
    elif l == 'str' and r == 'str':
        return [l, r, 'str']
    elif isinstance(l, list) and l[0] == "List" and l == r:
        return [l, r, l]
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]
    else:
        return [l, r, "unknown"] #### to change
        #raise PseudoCythonTypeCheckError("wrong types for +: %s and %s" % (serialize_type(l), serialize_type(r)))

def mul(l, r):
    if l in ['float', 'double'] and r in ['float', 'int', 'double'] :
        return [l, r, 'float']
    elif r in ['float', 'double'] and l in ['float', 'int', 'double'] :
        return [l, r, 'float']
    elif l == 'int' and r == 'int':
        return [l, r, 'int']
    elif l == 'int' and (isinstance(r, list) and r[0] == "List" or r == 'str'): 
        return [l, r, r]
    elif r == 'int' and (isinstance(l, list) and l[0] == "List" or l == 'str'):
        return [l, r, l]
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]    
    else:
        return [l, r, "unknown"] #### to change
        #raise PseudoCythonTypeCheckError("wrong types for *: %s and %s" % (serialize_type(l), serialize_type(r)))

def div(l, r, lo=None):
    if l in ['float', 'double'] and r in ['float', 'int', 'double'] :
        return [l, r, 'float']
    elif r in ['float', 'double'] and l in ['float', 'int', 'double'] :
        return [l, r, 'float']
    elif l == 'int' and r == 'int':
        return [l, r, 'int']
        #raise PseudoCythonTypeCheckError("cast one variable at line %s position %s between /: %s and %s" % (lo[0], lo[1], serialize_type(l), serialize_type(r)))
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]    
    else:
        return [l, r, "unknown"] #### to change
        #raise PseudoCythonTypeCheckError("wrong types for /: %s and %s" % (serialize_type(l), serialize_type(r)))

def pow_(l, r):
    if l == 'float' and r in ['float', 'int'] or r == 'float' and l in ['float', 'int']:
        return [l, r, 'float']
    elif l == 'int' and r == 'int':
        return [l, r, 'int']
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]    
    else:
        raise PseudoCythonTypeCheckError("wrong types for **: %s and %s" % (serialize_type(l), serialize_type(r)))

def mod(l, r):
    if l == 'int' and r == 'int':
        return [l, r, 'int']
    elif l == 'str' and (r == 'str' or r == ['array', 'str']):
        return [l, ['array', 'str'], 'str']   
    else:
        raise PseudoCythonTypeCheckError("wrong types for modulo : %s and %s" % (serialize_type(l), serialize_type(r)))

def and_(l, r):
    if l == 'bool' and r == 'bool':
        return 'bool'
    else:
        raise PseudoCythonTypeCheckError("wrong types for and: %s and %s" % (serialize_type(l), serialize_type(r)))

def or_(l, r):
    if l == 'bool' and r == 'bool':
        return 'bool'
    else:
        raise PseudoCythonTypeCheckError("wrong types for or: %s and %s" % (serialize_type(l), serialize_type(r)))        

def binary_and(l, r):
    if l == r == 'int':
        return l
    else:
        raise PseudoCythonTypeCheckError("wrong types for &: %s and %s" % (serialize_type(l), serialize_type(r)))

def binary_or(l, r):
    if l == r == 'int' or l == r == 'Set':
        return l
    else:
        raise PseudoCythonTypeCheckError("wrong types for |: %s and %s" % (serialize_type(l), serialize_type(r)))



TYPED_API = {
    'system':{
        "max":['Number','Number']
    },
        
    'math': {
        'abs':         ["Number", "Number"],
        'tan':          ['Number', 'double'],
        'atan':          ['Number', 'double'],
        'sin':          ['Number', 'double'],
        'asin':          ['Number', 'double'],
        'cos':          ['double', 'double'],
        'acos':          ['double', 'double'],
        'log':          ['double', 'double', 'double'],
        'sqrt':         ['Number', 'double'],
        'ceil':      ['double', 'int'],
        'exp':          ['double','double'],
        'PI': 'PI',
        'Floor':          ['double','double'],
        'Max':          ['Number','Number'],
        'Min':          ['Number','Number'],
        'Round':          ['double','double']
    },

    'operators': {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
        '**': pow_,
        '%': mod,
        '&':   binary_and,
        '|':   binary_or,
    },
    
    'List': {
        'append':       ['@t', ['List', '@t']],
        'sum':       [['List', '@t'], '@t'],
        'extend':       [["List",'@t'], ['List', '@t']],
        'contains?':       ["@t", "bool"],
        'Remove':        ['@t','bool'],
        'Insert':     ['int','@t', ["List", '@t']],
        'len':     ['int'],
        'index':      ['@t','int'],
    },
}
    
ORIGINAL_METHODS = {
    'List': {
        'Add':       'Add(element)',
        'pop':        'pop',
        'insert':     'insert(element)',
        'insert_at':  'insert(element, index)',
        'index':       'index(element)',
        'concat':     '+',
        'repeat':     '*',
        'extend':  'extend(other)',
        'remove':     'remove',
        'length':     'len',
        'copy':'copy',
        'map':        'list comprehension / map',
        'filter':     'list comprehension / filter'
    },

    'dict': {
        'keys':       'keys',
        'values':     'values',
        'length':     'len',
        'copy':'copy',
        'get': 'get(element)'
    },

    'int': {
        'int':     'int',
        'float':   'float'
    },
    'float': {
        'int':     'int',
        'float':   'float'
    },
    'str': {
        'find':       'index(substr)',
        'join':       'join(elements)',
        'split':      'split(delimiter)',
        'c_format':   '%',
        'format':     'format(*elements)',
        'upper':      'upper',
        'lower':      'lower',
        'title':      'title',
        'center':     'center',
        'find_from':  'index(substr, index)',
        'int':     'int'
    },


    'array': {
        'length':      'len',
        'find':        'find(element)',
        'count':       'count(element)',
        'append':       'append(element)'
    },

    'tuple': {
        'length':       'len'
    }
}
    

BUILTIN_TYPES = {
    'int':      'int',
    'float':    'float',
    'object':   'Object',
    'str':      'str',
    'List':     'List',
    'dict':     'dict',
    'tuple':    'tuple',
    'bool':     'bool',
    'array':    'array',
    "datetime": 'datetime'
}

PSEUDON_BUILTIN_TYPES = {v: k for k, v in BUILTIN_TYPES.items()}

BUILTIN_SIMPLE_TYPES = {
    'int':      'int',
    'float':    'float',
    'str':      'str',
    'boolean':     'bool',
    'double':'double'
}

KEY_TYPES = {'str', 'int', 'float', 'bool','double'}

PSEUDO_KEY_TYPES = {'str', 'int', 'float', 'bool','double'}

BUILTIN_FUNCTIONS = {'print', 'input', 'str', 'set', 'int','float', 'len', 'any', 'all', 'sum', 'min', 'max', 'abs','pow', "mean", "count", "copy", "integr"}

FORBIDDEN_TOP_LEVEL_FUNCTIONS = {'map', 'filter'}

ITERABLE_TYPES = {'str', "List", 'dict', 'array'}

TESTABLE_TYPE = 'bool'

INDEXABLE_TYPES = {'str', "List", 'dict', 'array', 'tuple'}

COMPARABLE_TYPES = {'int', 'float', 'str'}

TYPES_WITH_LENGTH = {'str', "List", 'dict', 'array', 'tuple', 'Set'}

NUMBER_TYPES = {'int', 'float','double'}






##############################################

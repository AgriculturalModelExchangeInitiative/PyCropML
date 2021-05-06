"""Add License, Header.
Use pkglts
Problems:
- name of a model unit?
"""
from __future__ import print_function
from __future__ import absolute_import
from path import Path
import numpy 
from datetime import datetime
import os.path
import six
import shutil
from . import error
import sys

DATATYPE = {}
DATATYPE['INT'] = "int"
DATATYPE['STRING'] = "str"
DATATYPE['DOUBLE'] = "float"
DATATYPE['DOUBLELIST'] = "list"
DATATYPE['INTLIST'] = "list"
DATATYPE['STRINGLIST'] = "list"
DATATYPE['CHARLIST'] = "list"
DATATYPE['DATELIST'] = "datelist"
DATATYPE['DOUBLEARRAY'] = "float"
DATATYPE['INTARRAY'] = "int"
DATATYPE['BOOLEAN'] = "bool"
DATATYPE['DATE'] = "datetime"
class Model2Package(object):
    """ TODO
    """

    num = 0

    def __init__(self, models, dir=None, pkg_name=None):
        """TODO."""
        self.models = models
        self.dir = dir

        self.with_import = True
        if pkg_name is None:
            self.pkg_name = "CropModel"
        else: self.pkg_name = pkg_name
        self.cwd = Path(self.dir)
        print(self.cwd)
        self.rep = os.path.abspath(os.path.dirname(self.cwd))

    def run(self):
        """TODO."""
        self.generate_package()
        #self.write_tests()


    def generate_package(self):
        """Generate a Cyml package equivalent to the xml definition.
        Args:
        - models : a list of model
        - dir: the directory where the code is generated.
        Returns:
        - None or status
        """

        # Create a directory (mymodel)
        
        directory=Path(os.path.join(self.cwd,'pyx'))
        if (directory).isdir() :
            self.dir = directory
        else:
            self.dir = directory.mkdir()

        files = []
        count = 0
        for model in self.models:          
            self.generate_component(model) 
            filename = Path(os.path.join(self.dir,"%s.pyx"%signature(model) ))                   
            with open(filename, "wb") as cyml_file:
#                cyml_file.write(self.code.encode('utf-8','ignore'))
                cyml_file.write(self.code.encode('utf-8'))
                files.append(filename)          
                model.module_name = str(Path(filename).name)
            count += 1
        return files
        
    def generate_component(self, model_unit):
        """ Todo
        """      
        if model_unit.modelid.split(".")[0]!="function":
            func_name = "model_%s"%signature(model_unit)
        else : func_name = signature(model_unit)
        types = [inp.datatype for inp in model_unit.inputs] +[out.datatype for out in model_unit.outputs]  
        self.code= "import numpy \n" + "from math import *\n"
        if "DATE" in types or "DATELIST" in types: self.code += "from datetime import datetime\n\n" 
   
        self.code += self.generate_function_signature(func_name, model_unit.inputs)
        self.code += self.generate_function_doc(model_unit)
        if  sys.version_info[0]>=3:
            self.code += self.generate_algorithm(model_unit) 
        else : self.code += self.generate_algorithm(model_unit).decode("utf-8") 

            
        if model_unit.function:
            for function in model_unit.function:
                if function.language in ("Cyml", "cyml"):
                    filefunc = Path(os.path.join(model_unit.path,"crop2ml",function.filename))
                    with open(filefunc.encode('utf-8'), 'r') as f:
                        source = f.read()
                        self.code += source 
        if model_unit.initialization is not None: self.code += self.initialization(model_unit)      
        return self.code

    def generate_algorithm(self, model_unit):
        print(model_unit.name)
        outputs = model_unit.outputs
        inputs = model_unit.inputs
        tab = ' '*4
        list_inputs=[]
        algo=""        
        
        """ we  declare all outputs which are not in inputs"""
        output_declaration=""
        for inp in inputs:
            list_inputs.append(inp.name)
        for out in outputs:
            if out.name not in list_inputs:
                output_declaration += tab+"cdef "+my_input(out)+"\n"

        for algorithm in model_unit.algorithms:                                  
            if (algorithm.language=="Cyml") or (algorithm.language=="cyml"):
                algo = algorithm
                break
        
        if algo :
            development = algo.development           
            lines = [tab+l for l in development.split('\n') if l.split()]
            code = output_declaration
            code += '\n'.join(lines)
            code += '\n'+tab + 'return  ' + ', '.join([o.name  for o in outputs]) + '\n'
            self.code = code
        else:
            raise error.Error("algorithm is not defined in model unit")
        return self.code

    def initialization(self, model_unit):
        outputs = model_unit.outputs
        inputs = model_unit.inputs
        tab = ' '*4
        list_inputs=[]        
        
        """ we  declare all outputs which are not in inputs"""
        output_declaration=""
        z=[]
        for inp in inputs:
            if "parametercategory" not in dir(inp):
                list_inputs.append(inp.name)
                output_declaration += tab+"cdef "+my_input(inp, defa=False)+"\n"
        for out in outputs:
            if out.name not in list_inputs:
                output_declaration += tab+"cdef "+my_input(out, defa = False)+"\n"
        code =""
        if model_unit.initialization:
            file_init = model_unit.initialization[0].filename
            path_init = Path(os.path.join(model_unit.path,"crop2ml", file_init))
            par = []
            for inp in inputs:
                if "parametercategory" in dir(inp):
                    par.append(inp)        
            with open(path_init, 'r') as f:
                code_init = f.read() 
            if code_init is not None :         
                lines = [tab+l for l in code_init.split('\n') if l.split()]
                code += self.generate_function_signature("init_%s"%signature(model_unit),par) +'\n'
                code += output_declaration
                code += '\n'.join(lines)
                code += '\n'+tab + 'return  ' + ', '.join([o.name  for o in outputs]) + '\n'            
        return code

            



    # documentation
    def generate_function_doc(self, model_unit):
        doc='''
    """%s
    """
'''%generate_doc(model_unit)
        return doc

    def generate_function_signature(self, func_name,inputs):
        #inputs = model_unit.inputs
        # Compute name from title.
        # We need an explicit name rather than infering it from Title
        #name = desc.Title
        code = 'def %s('%(func_name,)
        code_size = len(code)
        #_input_names = [inp.name.lower() for inp in inputs]
        ins = [ my_input(inp) for inp in inputs]
        separator = ',\n'+ code_size*' '
        code += separator.join(ins)
        code+= '):'
        return code


    def generate_test(self, model_unit):

        tab = ' '*4
        m = model_unit

        model_name = signature(m)

        psets = m.parametersets
        self.codetest = ""
        for v_tests in m.testsets:

            test_runs = v_tests.test  # different run in the thest
            test_paramsets = v_tests.parameterset  # name of paramsets

        # map the paramsets
            params = {}

            if   test_paramsets not in list(psets.keys()):
                print('Unknown parameter %s'%test_paramsets)
            else:
                params.update(psets[test_paramsets].params)

                for each_run in test_runs :
                    test_codes = []

                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')


                    (run, inouts) = list(each_run.items())[0]

                    ins = inouts['inputs']
                    outs = inouts['outputs']

                    code = '\n'
                    test_codes.append(code)

                    code = "def test_%s():"%(tname)
                    test_codes.append(code)
                    code = "    params= %s("%model_name
                    test_codes.append(code)

                    run_param = params.copy()
                    run_param.update(ins)

                    for k, v in six.iteritems(run_param):
                        code = "    %s = %s,"%(k,v)
                        test_codes.append(code)
                    code = "     )"
                    test_codes.append(code)

                    for j, k in enumerate(m.outputs):
                        if  k.datatype.strip() in ("STRINGLIST", "DATELIST", "STRINGARRAY", "DATEARRAY") :
                        
                            code = tab + "%s_estimated = params[%s]"%(k.name,j) if len(m.outputs)>1 else tab + "%s_estimated = params"%(k.name)
                            
                            test_codes.append(code)
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                        
                            test_codes.append(code)
                            code = tab+ "assert np.all(%s_estimated == %s_computed)"%(k.name,k.name)
                        
                            test_codes.append(code)
                                                   
                        if k.datatype.strip() in ("STRING", "BOOL", "INT", "DATE"):
                            code = tab + "%s_estimated = params[%s]"%(k.name,j) if len(m.outputs)>1 else tab + "%s_estimated = params"%(k.name)
                            test_codes.append(code)
                       
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
                       
                            code = tab+ "assert (%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)
                       
                           
                        if k.datatype.strip() in ("DOUBLELIST", "DOUBLEARRAY"):
                            code = tab + "%s_estimated = np.around(params[%s], %s)"%(k.name,j,outs[k.name][1]) if len(m.outputs)>1 else tab + "%s_estimated = np.around(params, %s)"%(k.name,outs[k.name][1])
                            test_codes.append(code)
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
                       
                            code = tab+ "assert np.all(%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)
                           
                           
                        if k.datatype.strip() in ("INTLIST", "INTARRAY"):
                            code = tab + "%s_estimated = params[%s]"%(k.name,j) if len(m.outputs)>1 else tab + "%s_estimated = params"%(k.name)
                            test_codes.append(code)
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
                            code = tab+ "assert np.all(%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)

                        if k.datatype.strip() == "DOUBLE":
                            code = tab + "%s_estimated = round(params[%s], %s)"%(k.name,j,outs[k.name][1]) if len(m.outputs)>1 else tab + "%s_estimated = round(params, %s)"%(k.name,outs[k.name][1])
                            test_codes.append(code)
                           
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
                           
                            code = tab+ "assert (%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)

                    code = '\n'.join(test_codes)

                    self.codetest += code

        return self.codetest
    
    def generate_func_test(self, model_unit):
        pass

    def write_tests(self):
        """ TODO: Manage several models rather than just one.
        """
        self.rep = Path(os.path.join(self.rep,'test', 'pyx'))
        if not self.rep.isdir():
            self.rep.mkdir()
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            filename = Path(os.path.join(self.rep,"test_%s.pyx"%signature(model)))
            codetest = "#'Test generation'\n\n"+"from %s"%signature(model) + " import *\n"+ "from math import *\n"+"import numpy \n\n" + codetest
            with open(filename, "wb") as cyml_file:
                cyml_file.write(codetest.encode('utf-8'))
                files.append(filename)
            count +=1
        return files


def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_')

    return name


def generate_doc(model):
    desc = model.description
        
    _doc = """
    %s
    Author: %s
    Reference: %s
    Institution: %s
    Abstract: %s
""" %(desc.Title, desc.Authors, desc.Reference, desc.Institution, desc.Abstract)

    code = '\n'
    code += _doc

    return code

def transfDate(type, elem):
    ser = elem.split("/")
    if len(ser)==3:
        year, month, day = ser[0], ser[1], ser[2]
        return "datetime(%s, %s, %s) "%( year, month, day)
    if len(ser)==4:
        year, month, day, hour= ser[0], ser[1], ser[2], ser[3]
        return "datetime(%s, %s, %s,%s ) "%( year, month, day, hour)
    if len(ser)==5:
        year, month, day, hour, min = ser[0], ser[1], ser[2],ser[3], ser[4]
        return "datetime(%s, %s, %s, %s, %s) "%( year, month, day, hour, min) 
    if len(ser)==6:
        year, month, day, hour, min, sec = ser[0], ser[1], ser[2],ser[3], ser[4], ser[5]
        return "datetime(%s, %s, %s,%s,%s,%s) "%( year, month, day, hour, min, sec)   

def transfDateList(type, elem):
    res=""
    for dat in eval(elem):
        t = transfDate("DateTime",dat)
        res+=t+","
    return "[%s]"%(res)

def transBool(type, elem):
    return elem.lower().capitalize()

def transf(type_, elem):
    if type_=="DATE":
        return transfDate(type_, elem)
    elif type_=="DATELIST":
        return transfDateList(type_, elem)
    elif type_ =="BOOLEAN":
        return transBool(type_, elem)
    else: return elem


def my_input(_input, defa=True):
    name = _input.name
    _type = _input.datatype
        
    if 'default' in dir(_input) and defa==True:
        if _input.default :
            default = _input.default              
            if DATATYPE[_type]  == "bool":
                val = default.capitalize()
                return "bool %s=%s"%(name, val.lower().capitalize())                    
            elif DATATYPE[_type] == "list":
                val = eval(default)
                return 'list %s=%s'%(name, val) 
            elif DATATYPE[_type] == "datelist":
                return 'list %s=%s'%(name, transfDateList(type, default))                  
            elif DATATYPE[_type] == "str":                
                return "str %s='%s'"%(name, default)
            elif DATATYPE[_type] == "datetime":                   
                return "datetime %s=%s"%(name, transfDate(_type,default))                               
            elif _type in DATATYPE:                  
                default = float(default) if DATATYPE[_type]=="float" else int(default)                                    
                return '%s %s=%s'%(DATATYPE[_type], name, default)
        else:
            if _type=="DOUBLEARRAY" or _type=="INTARRAY": 
                length = _input.len
                    #print("%s %s[%s]"%(DATATYPE[_type], name,len))
                return ("%s %s[%s]"%(DATATYPE[_type], name, length))
            else:
                return ("%s %s"%(DATATYPE[_type], name))
    else:
            if _type=="DOUBLEARRAY" or _type=="INTARRAY": 
                length = _input.len
                    #print("%s %s[%s]"%(DATATYPE[_type], name,len))
                return ("%s %s[%s]"%(DATATYPE[_type], name, length))
            else:
                return ("%s %s"%(DATATYPE2[_type], name))            

DATATYPE2 = {}
DATATYPE2['INT'] = "int"
DATATYPE2['STRING'] = "str"
DATATYPE2['DOUBLE'] = "float"
DATATYPE2['DOUBLELIST'] = "floatlist"
DATATYPE2['INTLIST'] = "intlist"
DATATYPE2['STRINGLIST'] = "stringlist"
DATATYPE2['CHARLIST'] = "stringlist"
DATATYPE2['DATELIST'] = "datelist"
DATATYPE2['DOUBLEARRAY'] = "floatarray"
DATATYPE2['INTARRAY'] = "intarray"
DATATYPE2['BOOLEAN'] = "bool"
DATATYPE2['DATE'] = "datetime"
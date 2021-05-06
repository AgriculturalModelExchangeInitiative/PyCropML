"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""
from __future__ import print_function
from __future__ import absolute_import
from path import Path
import numpy 
import os.path
import six

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

    def run(self):
        """TODO."""
        self.write_tests()

    # documentation
    def generate_function_doc(self, model_unit):
        doc='''
    %s  
'''%comment(generate_doc(model_unit))
        return doc

    def generate_test(self, model_unit):
        tab = ' '*4
        m = model_unit
        inputs = m.inputs
        outputs = m.outputs
        model_name  = signature(m)
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
                    test_codes = ["library(assertthat)"]
                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')
                    (run, inouts) = list(each_run.items())[0]
                    ins = inouts['inputs']
                    outs = inouts['outputs']
                    code = '\n'
                    test_codes.append(code)
                    code = "test_%s<-function(){"%(tname)
                    test_codes.append(code)
                    code = "    params= model_%s("%model_name
                    test_codes.append(code)
                    run_param = params.copy()
                    run_param.update(ins)
                    n=0
                    for k, v in six.iteritems(run_param):
                        type_v = [inp.datatype for inp in inputs if inp.name==k][0]
                        code = tab*2 + "%s = %s"%(k,transf(type_v, v))
                        if n!=len(run_param)-1:
                            code +=","
                            n=n+1
                        test_codes.append(code)
                    code =tab*2 +  ")"
                    test_codes.append(code)
                    for k, v in six.iteritems(outs):
                        type_v = [out.datatype for out in outputs if out.name==k][0]     
                        code = tab + "%s_estimated = params$%s"%(k,k) 
                        test_codes.append(code)
                        code = tab + "%s_computed = %s"%(k,transf(type_v,outs[k][0]))
                        test_codes.append(code)
                        if  type_v.strip() in ("STRINGLIST", "DATELIST", "STRINGARRAY", "DATEARRAY", "BOOL","STRING", "DATE","INT", "INTLIST","INTARRAY") : # without precision
                            code = tab+ "assert_that(all.equal(%s_estimated, %s_computed)==TRUE)"%(k,k)   
                            test_codes.append(code)                                    
                        if type_v.strip() in ( "DOUBLE", "DOUBLELIST", "DOUBLEARRAY"): # with precision
                            code = tab+ "assert_that(all.equal(%s_estimated, %s_computed, scale=1, tol=0.%s)==TRUE)"%(k,k, outs[k][1])
                            test_codes.append(code)
                    code = '\n'.join(test_codes)
                    self.codetest += code +'\n}\n'
                    self.codetest += "test_%s()"%tname
        return self.codetest
    

    def generate_func_test(self, model_unit):
        pass

    def write_tests(self):
        """ TODO: Manage several models rather than just one.
        """
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            filename = self.dir/"test_%s.r"%signature(model)
            codetest = "#Test generation'\n\n"+'source("%s/%s.r")'%(self.dir.replace('\\','/'),signature(model)) + codetest
            with open(filename, "w") as r_file:
                r_file.write(codetest.encode('utf-8'))
                files.append(filename)
            count +=1
        return files

def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_').lower()
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

def comment(line):
    list_com = ['#'+x for x in line.split('\n')]
    com = '\n'.join(list_com)
    return com

DATATYPE = {}
DATATYPE['INT'] = "int"
DATATYPE['STRING'] = "string"
DATATYPE['DOUBLE'] = "double"
DATATYPE['BOOLEAN'] = "bool"
DATATYPE['DATE'] = "string"
DATATYPE['STRINGLIST'] = "c(%s)"
DATATYPE['DOUBLELIST'] = "c(%s)"
DATATYPE['INTLIST'] = "c(%s)"
DATATYPE['DATELIST']="c(%s)"

def transf(type_v, elem):
    if type_v == "BOOLEAN":
        return elem.upper()
    if type_v in ["STRING", "DATE"]:
        return ('"%s"'%elem).replace('""', '"')
    if type_v in ["DOUBLE", "INT"]:
        return str(elem)
    elif "LIST" in type_v:
        return DATATYPE[type_v.strip()]%",".join(list(map(transf,[type_v.split("LIST")[0]]*len(elem),eval(elem))))
        

from pycropml import composition
from pycropml.pparse import model_parser
from path import Path
import networkx as nx
from collections import defaultdict
from IPython.display import Image, display
from networkx.drawing.nx_pydot import to_pydot
from pycropml.render_cyml import signature
import os
import sys
from pycropml.transpiler.main import Main
from copy import copy
from pycropml.render_cyml import my_input, DATATYPE

 
class Package():
    def __init__(self, name, metainfo, path=None):
        self.name=name
        self.metainfo = metainfo
        
        if (not path):
            # package directory
            import inspect
            # get the path of the file which call this function
            call_path = os.path.abspath(inspect.stack()[1][1])
            self.path = os.path.dirname(call_path)
            self.wralea_path = call_path        

        # package directory

        if (not path):
            # package directory
            import inspect
            # get the path of the file which call this function
            call_path = os.path.abspath(inspect.stack()[1][1])
            self.path = os.path.dirname(call_path)
            self.wralea_path = call_path

        # wralea.py path is specified
        else:
            if (not os.path.exists(path)):
                os.mkdir(path)
            if (not os.path.isdir(path)):
                self.path = os.path.dirname(path)
                self.wralea_path = path

            else:
                self.path = path
                self.wralea_path = os.path.join(self.path, "model.py")
                self.crop2ml_path = os.path.join(self.path, "crop2ml")


 
class PackageManager():
    def __init__(self, proj):
        self.syspath = sys.path[:]
        self.pkg={}
        self.user_crop2ml_path = set()
        self.sys_crop2ml_path = set()  
        self.proj = proj
        

    def check_exist(self):
        pass
      
    def contain_pkg(self):
        pk={}
        for root, dirs, files in os.walk(self.proj):
            if "crop2ml" in dirs:
                pk[root.split('/')[-1]]=root              
        return pk
    
    def get_path(self,pkg):
        di = self.contain_pkg()
        wf_path={}
        for k, v in di.items():
            wf_name = k.split('\\')[-1]
            wf_path[wf_name]=v
        if pkg in wf_path.keys():
            return wf_path[pkg]
        else:
            print("pkge doesn't exist")

import importlib
class Topology():
    pkgs={}
    def __init__(self, name, pkg=None):
        self.name=name
        if pkg is None:
            if self.isPackage(self.name):
                self.pkg = self.load_pkge(self.name).crop2mlpath
            else: 
                self.pkg=input("Give the path of package %s"%self.name)
        else:
            self.pkg=pkg
        self.data = Path(self.pkg)/"crop2ml"
        
        composite_file = self.data.glob("composition*.xml")[0]
        self.mu =  model_parser(self.pkg)
        self.model, = composition.model_parser(composite_file)
        self.pkgs[self.name]=[self.pkg, self.model]
        self.model.inputs = self.meta_inp(self.name)
        self.model.outputs = self.meta_out(self.name)
        self.model.ext = self.meta_ext(self.name)
        self.model.states = self.findstates(self.model.inputs,self.model.outputs )
        self.model.path = Path(self.pkg)
        self.minout()
        self.path_pkg = None
         
    def isPackage(self, name):
        if sys.version_info[0]>=3:
            pkg=importlib.util.find_spec(name)   #### Python>=3
        else: 
            if name not in sys.modules: pkg=None
        if pkg is None:
            return False
        else:
            if "crop2mlpath" in dir(self.load_pkge(name)):
                return True
            else: return False

    def findstates(self, inputs, outputs):
        st=[]
        stname = []
        for n in inputs:
            if "variablecategory" in dir(n) and n.variablecategory=="state":
                stname.append(n.name)
                st.append(n)
        for m in outputs:
            if "variablecategory" in dir(m) and m.variablecategory=="state" and m.name not in stname:
                st.append(m)
                stname.append(m.name)
        return st




    def load_pkge(self, name):
        module=None
        try:
            module = importlib.import_module(name)
        except Exception as e:
            print(e)
        return module

    def createGraph(self):
        d= defaultdict(list)        
        for mod in self.model.model:
            for inter in self.model.internallink:    
                source = inter["source"].split(".")[0]
                target = inter["target"].split(".")[0]
                if mod.name==source:
                    d[mod.name].append(target)
        return nx.DiGraph(d, name = self.model.name)
    
    def create_edgeInOut(self):
        edge_inout=defaultdict(list)
        for inter in self.model.internallink:
            out = inter["source"].split(".")[1]
            out_name = inter["source"].split(".")[0]
            inp = inter["target"].split(".")[1]
            if out!=inp:
                edge_inout[out_name].append([out,inp])
        return edge_inout
    
    def topologicalSort(self):
        ordV = list(nx.topological_sort(self.createGraph()))
        return ordV

    def info_minout(self):
        inout={}
        for m in self.model.model:
            if m.file.split(".")[0]=="unit" and m.package_name is None:
                for mo in self.mu:
                    if mo.name==m.name:
                        inout[mo.name] = (mo.inputs, mo.outputs)
            else:
                pkgname = m.package_name
                inout[m.name] = (self.meta_inp(pkgname), self.meta_out(pkgname))
        return inout
 

    def minout(self):
        inout={}
        i=0
        for m in self.model.model:        
            if m.file.split(".")[0]=="unit" and m.package_name is None:
                for mo in self.mu:
                    if mo.name==m.name:
                        inp = [m.name for m in mo.inputs]
                        out = [m.name for m in mo.outputs]
                        inout[mo.name] = (inp, out)
                        self.model.model[i].inputs = mo.inputs
                        self.model.model[i].outputs = mo.outputs
                        self.model.model[i].description = mo.description
                        self.model.model[i].parametersets = mo.parametersets
                        self.model.model[i].testsets = mo.testsets
                        self.model.model[i].path = mo.path
                        self.model.model[i].function = mo.function
                        self.model.model[i].initialization = mo.initialization
                        self.model.model[i].algorithms = mo.algorithms

            else:
                pkgname = m.package_name
                inp = [p.name for p in self.meta_inp(pkgname)]
                out = [p.name for p in self.meta_out(pkgname)]
                inout[m.name] = (inp, out)
                self.model.model[i].inputs = self.meta_inp(pkgname)
                self.model.model[i].outputs = self.meta_out(pkgname)
                data = Path(os.path.join(self.path_pkg,"crop2ml"))
                composite_file = data.glob("composition*.xml")[0]
                mc, = composition.model_parser(composite_file)
                self.model.model[i].description = mc.description
                self.model.model[i].inputlink = mc.inputlink
                self.model.model[i].outputlink = mc.outputlink
                self.model.model[i].internallink = mc.internallink
                self.model.model[i].path = self.path_pkg
                self.model.model[i].model, = composition.model_parser(composite_file)
                #self.model.model[i].parametersets = mc.parametersets
                #self.model.model[i].testsets = mc.testsets                
            i = i+1
        return inout

    def algorithm(self):
        code=""
        W= self.topologicalSort()
        edge = self.create_edgeInOut()
        for v in W:
            if not self.check_compo(self.model,v):
                code += "%s = model_%s( %s)\n"%(', '.join(self.minout()[v][1]),v.strip().replace(' ','_'),','.join(self.minout()[v][0]))
            else:
                code += "%s = model_%s( %s)\n"%(', '.join(self.minout()[v][1]),v.strip().replace(' ','_'),','.join(self.minout()[v][0]))
                
            if len(edge)!=0:
                if v in list(edge.keys()):
                    for val in list(edge[v]):
                        code += "%s = %s\n"%(val[1],val[0])
        return code
              
    def write_xml(self):
        G = self.createGraph()
        filename = "%s.xml"%(self.model.name)
        nx.write_graphml_xml(G,filename)
    
    def write_png(self):
        a=to_pydot(self.createGraph())
        print('%s/%s.png' % (self.model.path,self.model.name))
        a.write_png('%s/%s.png' % (self.model.path,self.model.name))
        #from networkx.drawing.nx_pydot import graphviz_layout
        #print(graphviz_layout(self.createGraph()))
    
    def display_wf(self):
        a=to_pydot(self.createGraph())
        d=a.create_png()
        display(Image(d))
     
    def algo2cyml(self):
        code='from datetime import datetime\nfrom math import *\n'
        tab=' '*4
        #print(self.meta_inp(self.name))
        for mod in self.model.model:
            code+= 'from %s import model_%s\n'%(signature(mod), signature(mod)) if mod.package_name is None else 'from %s import model_%s\n'%(signature(mod), signature(mod))
        name =self.model.name.strip().replace(' ','_')
        signature_mod= "def model_" +  name + "(%s):"%(",\n      ".join(map(my_input,self.meta_inp(self.name))))
        code += signature_mod+"\n"
        code += self.decl(defa=False)
        lines = [tab+l for l in self.algorithm().split('\n') if l.split()]
        code += '\n'.join(lines)
        code += "\n" + tab + "return " + ", ".join([out.name for out in self.model.outputs])
        out_states=[out for out in self.model.outputs if out.variablecategory=="state"]
        if self.model.initialization:
            file_init = self.model.initialization[0].filename
            path_init = Path(os.path.join(self.pkg,"crop2ml", file_init))
            with open(path_init, 'r') as f:
                code_init = f.read()
            if code_init is not None :         
                lines = [tab+l for l in code_init.split('\n') if l.split()]
                code += self.generate_function_signature(self.model) +'\n'
                code += self.val_init(self.model)
                code += '\n'.join(lines)
                code += '\n'+tab + 'return  ' + ', '.join([o.name  for o in self.model.outputs]) + '\n'                
        return code

    def generate_function_signature(self,model):
        input = model.inputs
        output = model.outputs
        inout = input + output
        outname = [o.name for o in output]
        tab=[]
        # initialization inputs
        for inp in inout:
            if inp.name not in outname and not inp.name.endswith("_t1"):
                if inp.name not in tab :
                    tab.append(inp)
        if  sys.version_info[0]>=3: init_inp = tab.copy()
        else: init_inp = tab   
        # Compute name from title.
        # We need an explicit name rather than infering it from Title
        #name = desc.Title
        code = '\n\ndef init_%s('%(signature(model))
        code_size = len(code)
        #_input_names = [inp.name.lower() for inp in inputs]
        ins = [ my_input(inp) for inp in init_inp]        
        separator = ',\n'+ code_size*' '
        code += separator.join(ins)
        code+= '):\n'
        return code
    
    def val_init(self, model):
        inputs = model.inputs
        outputs = model.outputs
        #inout = inputs + outputs
        tab=""
        listab=[]
        for inp in outputs:
            if inp.name not in listab:
                name = inp.name
                listab.append(name)
                if inp.datatype=="INT":
                    tab +="    cdef int %s = 0\n"%(name)
                if inp.datatype=="DOUBLE":
                    tab +="    cdef float %s = 0.0\n"%(name)
                if inp.datatype=="STRING":
                    tab +="    cdef str %s ='' \n"%(name)
                if inp.datatype=="BOOLEAN":
                    tab +="    cdef bool %s = FALSE\n"%(name)
                if inp.datatype=="INTLIST":
                    tab +="    cdef intlist %s\n"%(name)
                if inp.datatype=="DOUBLELIST":
                    tab +="    cdef floatlist %s\n" %(name)
                if inp.datatype=="STRINGLIST":
                    tab +="    cdef stringlist %s\n" %(name)
                if inp.datatype=="DATELIST":
                    tab +="    cdef datelist %s \n"%(name)
                if inp.datatype=="DATE":
                    tab +="    cdef datetime %s\n"%(name)
                if inp.datatype=="INTARRAY":
                    tab +="    cdef intarray %s\n"%(name)           
                if inp.datatype=="DOUBLEARRAY":
                    tab +="    cdef doublarray %s\n" %(name) 
                if inp.datatype=="STRINGARRAY":
                    tab +="    cdef stringarray %s\n" %(name) 
        return tab       



    def retrive(self, pkgname):
        if pkgname in self.pkgs:
            pkg = self.pkgs[pkgname][0]
            mc = self.pkgs[pkgname][1]
        else:     
            model = Topology(name=pkgname)
            pkg = model.pkg
            mc = model.model
            self.pkgs[pkgname]=[pkg, mc]
        
        return pkg, mc

    def meta_inp(self, pkgname):
        pkg, mc = self.retrive(pkgname)        
        list_var=[]
        mod_inputs=[]
        for inter in mc.inputlink: 
            var = inter["source"]
            mod = inter["target"].split(".")[0]
            if var not in list_var:
                if self.check_compo(mc, mod)!=True:
                    inp = self.info_inputs_mu(pkg,mod,var)
                    list_var.append(var)
                    mod_inputs.append(inp)
                else:
                    name=self.pkg_m(mc, mod)
                    pos = [j for j,k in enumerate(mc.model) if k.name == mod][0]
                    if mc.model[pos].file.split(".")[0]=="unit":
                        mc_path = self.retrive(name)[1].path
                        inps = [m.inputs for m in model_parser(mc_path) if m.name == mod][0]
                        inp = [k for k in inps if k.name == var][0]
                    else:
                        inp = self.get_mu_inp(name, var)
                    mod_inputs.append(inp)
                    list_var.append(var) 
        self.path_pkg = pkg                         
        return mod_inputs

    def meta_ext(self, pkgname):
        pkg, mc = self.retrive(pkgname)        
        list_var=[]
        mod_ext=[]
        for inter in mc.internallink: 
            vars = inter["source"].split(".")[1]
            mods = inter["source"].split(".")[0]
            vart = inter["target"].split(".")[1]
            modt = inter["target"].split(".")[0]

            if vars not in list_var:
                if self.check_compo(mc, mods)!=True:
                    ext = self.info_outputs_mu(pkg,mods,vars)
                    list_var.append(vars)
                    mod_ext.append(ext)
                else:
                    name=self.pkg_m(mc, mods)
                    ext = self.get_mu_out(name, vars)
                    mod_ext.append(ext)
                    list_var.append(vars)

            if vart not in list_var:
                if self.check_compo(mc, modt)!=True:
                    ext = self.info_inputs_mu(pkg,modt,vart)
                    list_var.append(vart)
                    mod_ext.append(ext)
                else:
                    name=self.pkg_m(mc, modt)
                    ext = self.get_mu_inp(name, vart)
                    mod_ext.append(ext)
                    list_var.append(vart)                           
        return mod_ext



    def meta_out(self, pkgname):
        pkg, mc = self.retrive(pkgname)
        list_var=[]
        mod_outputs=[]
        for inter in mc.outputlink:    
            var = inter["target"]
            mod = inter["source"].split(".")[0]
            
            if var not in list_var:
                if self.check_compo(mc, mod)!=True:
                    out = self.info_outputs_mu(pkg,mod,var)
                    list_var.append(var)
                    mod_outputs.append(out)
                else:
                    #pa, mc = self.retrive(self.pkg_m(mc, mod))
                    name=self.pkg_m(mc, mod)
                    #out = self.get_mu_out(pa, mod, var)
                    out = self.get_mu_out(name, var)
                    mod_outputs.append(out)
                    list_var.append(var)                           
        return mod_outputs


    # check if a model m is a composite model including in mc   
    def check_compo(self,mc, m):
        test=False
        for mod in mc.model:
            if mod.name == m:
                if mod.file.split(".")[0] == "composition" or mod.package_name:
                    test = True
                    break
        return test

    # get the name of composite model package    
    def pkg_m(self,mc, m):
        pkg_name=None
        for mod in mc.model:
            if mod.name == m:
                pkg_name = mod.package_name
        return pkg_name
    """
    #get the path of the package    
    def path_pkg(self, mc,m):
        name = self.pkg_m(mc,m)
        ppkg = PackageManager(self.path).get_path(name)
        return ppkg
    """
    # get the info of an input of a model unit from its name and the name of the input
    def info_inputs_mu(self,ppkg,mu,varname):
        mod =  model_parser(ppkg)
        for m in mod:
            if m.name==mu:
                for inp in m.inputs:
                    if inp.name == varname:
                        return inp
 
    # get the info of an output of a model unit from its name and the name of the output
    def info_outputs_mu(self,ppkg,mu,varname):
        mod =  model_parser(ppkg)
        for m in mod:
            if m.name==mu:
                for out in m.outputs:
                    if out.name == varname:
                        return out   
    
    # get the model unit from an input of a composite model                
    def get_mu_inp(self,pkgname,varname):
        listvar=[]
        ppkg,mc=self.retrive(pkgname)
        for inp in mc.inputlink:
            var = inp["source"]
            mod = inp["target"].split(".")[0]
            if var==varname and var not in listvar:
                if self.check_compo(mc,mod)==True:
                    ppkg, mc = self.retrive(self.pkg_m(mc, mod))
                    self.get_mu_inp(ppkg, var)      
                inp = self.info_inputs_mu(ppkg,mod,var)
                listvar.append(var)
                return inp

    def get_mu_out(self,pkgname,varname):
        listvar=[]
        ppkg,mc=self.retrive(pkgname)
        for out in mc.outputlink:
            var = out["target"]
            mod = out["source"].split(".")[0]
            if var==varname and var not in listvar:
                if self.check_compo(mc,mod)==True:
                    ppkg, mc = self.retrive(self.pkg_m(mc, mod))
                    self.get_mu_out(ppkg, var)      
                out = self.info_outputs_mu(ppkg,mod,var)
                listvar.append(var)
                return out

    """def get_mu_out(self,ppkg, mc, varname):
        listvar=[]
        data = Path(ppkg)/"crop2ml"
        composite_file = data.glob("composition.%s*.xml"%mc)[0]
        mc, = composition.model_parser(composite_file)
        for out in mc.outputlink:
            var = out["target"]
            mod = out["source"].split(".")[0]
            if var==varname and var not in listvar:
                if self.check_compo(mc,mod)==True:
                    ppkg, mc = self.retrive(self.pkg_m(mc, mod))
                    self.get_mu_out(ppkg, mod, var)      
                inp = self.info_outputs_mu(ppkg,mod,var)
                listvar.append(var)
                return inp   """  

    def decl(self, defa=True):
        info_var = self.info_minout()
        inp = [m.name for m in self.meta_inp(self.name)]
        declaration=""
        tab = ' '*4
        for k, v in info_var.items():
            for j in v[0]:
                #print(j)
                if j.name not in inp:
                    declaration += tab+"cdef "+my_input(j, defa=False)+"\n"
                    inp.append(j.name)
            for w in v[1]:
                if w.name not in inp:
                    #print(w, w.name)
                    declaration += tab+"cdef "+my_input(w, defa)+"\n"
                    inp.append(w.name)
     
        return declaration
                     
    def compotranslate(self, language):
        d= self.algo2cyml()
        test=Main(d, language, self.model,self.model.name)
        test.parse()
        test.to_ast(d)
        code=test.translate()  
        return code
                
    def translate_all(self, model):
        for mod in model.model:
            if mod.package_name is not None:
                T= Topology(mod.package_name)
                model = self.retrive(mod.package_name)[1]
                self.translate_all(model)
                
    def translate(self):
        #print(self.algo2cyml())
        self.translate_all(self.model)
        
                


#from pycropml.topology import Topology
'''
from pycropml.topology import Topology
from pycropml.transpiler.generators.openaleaGenerator import OpenaleaCompo
pkg1 = "C:/Users/midingoy/Documents/THESE/pycropml_pheno/test/Models/energybalance_pkg"
T = Topology(name='energybalance', pkg=pkg1)
a =OpenCompo(tree =None, model = T.model)
"C:/Users/midingoy/Documents/THESE/pycropml_pheno/test/Tutorial/testA"
print(T.compotranslate('cs'))
T.translate()
algo = T.algo2cyml
aCsharpCompo(tree =None, model = T.model)


T.translate()

print(T.algo2cyml())
print(T.compotranslate('cs'))
T.translate_all()
T.write_png()
T.decl()


T.model.model[0].package_name
print(T.algo2cyml())

from pycropml.cyml import transpile_package
transpile_package(pkg, "py")
'''



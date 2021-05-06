# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.rules.csharpRules import CsharpRules
from pycropml.transpiler.generators.docGenerator import DocGenerator
from pycropml.transpiler.pseudo_tree import Node
import os
from path import Path
from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree
from pycropml import code2nbk
from pycropml.transpiler.generators.csharpGenerator import CsharpGenerator, CsharpTrans,CsharpCompo



category = {"state":"s", "rate":"r", "auxiliary":"a", "exogenous":"ex"}
param_datatype ={"STRING":"String", 
                "INT":"Integer", 
                "DOUBLE":"Double", 
                "BOOLEAN":"Boolean",
                "DATE":"Date",
                "DATELIST":"ListDate",
                "STRINGLIST": "ListString",
                "DOUBLELIST": "ListDouble",
                "INTLIST": "ListInteger",
                "BOOLEANLIST": "ListBoolean"}

def getdefault(x):
    if "default" in dir(x):
        if x.datatype == "STRING": return '"%s"'%x.default if x.default is not None  else "-1D"
        elif x.datatype == "BOOLEAN": return x.default.lower() if x.default is not None  else "-1D"
        elif x.datatype in ("DATE", "DATELIST"): return "-1D"
        elif x.datatype.endswith("LIST"): return x.default if x.default is not None else "-1D"
        else: return x.default if x.default is not None else "-1D"
    else: return "-1D"

class SiriusGenerator(CsharpGenerator):
    """ This class contains the specific properties of
    SQ components and use the NodeVisitor to generate a csharp
    code source from a well formed syntax tree based on BioMa structure.
    """
    
    def __init__(self, tree=None, model=None, name=None):
        self.tree = tree
        self.model=model
        self.name = name
        self.indent_with=' '*4
        CsharpGenerator.__init__(self, tree, model, name)  
        self.usingBioma()  
                

    def usingBioma(self):
        self.write("""
using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml;
using CRA.ModelLayer.MetadataTypes;
using CRA.ModelLayer.Core;
using CRA.ModelLayer.Strategy;
using System.Reflection;
using VarInfo=CRA.ModelLayer.Core.VarInfo;
using Preconditions=CRA.ModelLayer.Core.Preconditions;
using CRA.AgroManagement;       
""")

    def desc(self,node, n, inp, vartype) :
        self.write("PropertyDescription pd%s = new PropertyDescription();"%n)              
        self.newline(node)
        self.write("pd%s.DomainClassType = typeof(SiriusQuality%s.DomainClass.%s%s);"%(n, self.name,self.name,inp.variablecategory.capitalize()))
        self.newline(node)
        self.write('pd%s.PropertyName = "%s";'%(n,inp.name if not inp.name.endswith("_t1") else inp.name[:-3]))
        self.newline(node)
        self.write('pd%s.PropertyType = (SiriusQuality%s.DomainClass.%s%sVarInfo.%s).ValueType.TypeForCurrentValue;'%(n, self.name,self.name, inp.variablecategory.capitalize(),inp.name if not inp.name.endswith("_t1") else inp.name[:-3]))
        self.newline(node)
        self.write('pd%s.PropertyVarInfo =(SiriusQuality%s.DomainClass.%s%sVarInfo.%s);'%(n,self.name,self.name, inp.variablecategory.capitalize(),inp.name if not inp.name.endswith("_t1") else inp.name[:-3]))
        self.newline(node)
        self.write('%s.Add(pd%s);'%(vartype, n)) 

    def inOutputDesc(self, node):
        self.newline(node)        
        self.write("ModellingOptions mo0_0 = new ModellingOptions();")
        self.newline(node)
        self.write("//Parameters")
        self.newline(node)
        self.write("List<VarInfo> _parameters0_0 = new List<VarInfo>();")
        self.newline(node)
        n = 1
        for p in self.model.parameters:
            self.write("VarInfo v%s = new VarInfo();"%n)
            self.newline(node)
            self.write("v%s.DefaultValue = %s;"%(n, getdefault(p)))
            self.newline(node)
            self.write('v%s.Description = "%s";'%(n,p.description))
            self.newline(node)
            self.write("v%s.Id = 0;"%n)
            self.newline(node)
            self.write("v%s.MaxValue = %s;"%(n, p.max if p.max is not None else getdefault(p)))
            self.newline(node)
            self.write("v%s.MinValue = %s;"%(n, p.min if p.min is not None else getdefault(p)))
            self.newline(node)
            self.write('v%s.Name = "%s";'%(n, p.name))
            self.newline(node)
            self.write("v%s.Size = 1;"%n)
            self.newline(node)
            self.write('v%s.Units = "%s";'%(n, p.unit if ("unit" in dir(p) and p.unit is not None) else "dimensionless"))
            self.newline(node)
            self.write('v%s.URL = "%s";'%(n, p.url if ("url" in dir(p) and p.url is not None) else ""))
            self.newline(node)
            self.write("v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;"%n)
            self.newline(node)
            self.write('v%s.ValueType = VarInfoValueTypes.GetInstanceForName("%s");'%(n, param_datatype[p.datatype]))
            self.newline(node)
            self.write("_parameters0_0.Add(v%s);"%n)
            self.newline(node)
            n = n+1
        self.write("mo0_0.Parameters=_parameters0_0;")

        n = 1
        self.newline(extra=1)
        self.write("//Inputs")
        self.newline(node)
        self.write("List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();"%())
        self.newline(node)
        for inp in self.model.inputs:
            if inp.name not in self.modparam :
                self.desc(node,n,inp, "_inputs0_0")
                self.write("")
                self.newline(node)
                n = n+1
        self.write("mo0_0.Inputs=_inputs0_0;")
    
        self.newline(extra=1)
        self.write("//Outputs")
        self.newline(node)
        self.write("List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();")
        self.newline(node)

        for out in self.model.outputs:
            if out.name not in self.modparam :
                self.desc(node,n,out,"_outputs0_0")
                self.newline(node)
                n = n+1
            self.write("mo0_0.Outputs=_outputs0_0;")
        self.newline(node)
        self.otherDesc(node)
        self.newline(extra=1)
    
    def otherDesc(self,node):
        self.write("//Associated strategies")
        self.newline(node)
        self.write('List<string> lAssStrat0_0 = new List<string>();')
        self.newline(node)
        self.write("mo0_0.AssociatedStrategies = lAssStrat0_0;")
        self.newline(node)
        self.write("//Adding the modeling options to the modeling options manager")
        self.newline(node)
        self.write("_modellingOptionsManager = new ModellingOptionsManager(mo0_0);")
        self.newline(node)
        self.write("SetStaticParametersVarInfoDefinitions();")
        self.newline(node)
        self.write("SetPublisherData();")
        self.newline(extra=1) 

    def description(self, node):
        self.write("public string Description") 
        self.open(node)
        self.write('get { return "%s" ;}'%self.model.description.Abstract.replace("\n", ""))
        self.close(node)
        self.newline(extra=1) 

    def url(self, node):
        self.write("public string URL") 
        self.open(node)
        self.write('get { return "%s" ;}'%(self.model.description.url if "url" in dir(self.model.description) else ""))
        self.close(node)
        self.newline(extra=1) 

    def domain(self, node):
        self.write("public string Domain") 
        self.open(node)
        self.write('get { return "";}')
        self.close(node)
        self.newline(extra=1) 

    def modelType(self, node):
        self.write("public string ModelType") 
        self.open(node)
        self.write('get { return "";}')
        self.close(node)
        self.newline(extra=1)

    def isContext(self, node):
        self.write("public bool IsContext") 
        self.open(node)
        self.write('get { return false;}')
        self.close(node)
        self.newline(extra=1) 

    def isTimeStep(self, node):
        self.write("public IList<int> TimeStep")
        self.open(node)
        self.write("get")
        self.open(node)
        self.write("IList<int> ts = new List<int>();")
        self.newline(node)
        self.write("return ts;")
        self.close(node)
        self.close(node)
        self.newline(extra=1) 

    def publisherdata(self, node):
        self.write("private  PublisherData _pd;")
        self.newline(node)	
        self.write("public PublisherData PublisherData")
        self.open(node)
        self.write("get { return _pd;} ")
        self.close(node)
        self.newline(extra=1) 
    
    def SetPublisherData(self, node):
        self.write("private  void SetPublisherData()")
        self.open(node)	
        self.write("_pd = new CRA.ModelLayer.MetadataTypes.PublisherData();")
        self.newline(node)
        self.write('_pd.Add("Creator", "%s");'%self.model.description.Authors)
        self.newline(node)
        self.write('_pd.Add("Date", "");')
        self.newline(node)
        self.write('_pd.Add("Publisher", "%s");'%self.model.description.Institution)
        self.close(node)
        self.newline(extra=1) 

    def getStrategyDomainClassesTypes(self, node):	
        self.write("public IEnumerable<Type> GetStrategyDomainClassesTypes()")
        self.open(node)
        self.write("return new List<Type>() {  typeof(SiriusQuality%s.DomainClass.%sState),  typeof(SiriusQuality%s.DomainClass.%sState), typeof(SiriusQuality%s.DomainClass.%sRate), typeof(SiriusQuality%s.DomainClass.%sAuxiliary), typeof(SiriusQuality%s.DomainClass.%sExogenous)};"%(self.name, self.name,self.name, self.name,self.name, self.name,self.name, self.name,self.name, self.name))
        self.close(node)
        self.newline(extra=1)
    
    def setParametersDefaultValue(self, node):
        self.write("public void SetParametersDefaultValue()")
        self.open(node)
        self.write("_modellingOptionsManager.SetParametersDefaultValue();")
        self.close(node)
        self.newline(extra=1)

    def varinfodef(self, node, pa):
        self.write('%sVarInfo.Name = "%s";'%(pa.name, pa.name)); self.newline(node)
        self.write('%sVarInfo.Description = "%s";'%(pa.name, pa.description)); self.newline(node)
        self.write('%sVarInfo.MaxValue = %s;'%(pa.name,pa.max if pa.max is not None else getdefault(pa))); self.newline(node)
        self.write('%sVarInfo.MinValue = %s;'%(pa.name, pa.min if pa.min is not None else getdefault(pa))); self.newline(node)
        self.write('%sVarInfo.DefaultValue = %s;'%(pa.name, getdefault(pa))); self.newline(node)
        self.write('%sVarInfo.Units = "%s";'%(pa.name, pa.unit if ("unit" in dir(pa) and pa.unit is not None) else "dimensionless")); self.newline(node)
        self.write('%sVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("%s");'%(pa.name, param_datatype[pa.datatype])); self.newline(node)

    def SetStaticParametersVarInfoDefinitions(self, node):
        self.write("private static void SetStaticParametersVarInfoDefinitions()")
        self.open(node)
        for pa in self.model.parameters: 
            self.newline(extra=1)  
            self.varinfodef(node, pa)
        self.close(node)
        self.newline(extra=1)
    
    def staticVarInfo(self, node):
        for pa in self.model.parameters:
            self.write("private static VarInfo _%sVarInfo = new VarInfo();"%pa.name)
            self.newline(node)	
            self.write("public static VarInfo %sVarInfo"%pa.name)
            self.open(node)
            self.write("get { return _%sVarInfo;} "%pa.name)
            self.close(node) 
            self.newline(extra=1)  

    def TestPostConditions(self, node):
        self.write("public string TestPostConditions(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex,string callID)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        self.open(node)
        self.write("try")
        self.open(node)
        self.write("//Set current values of the outputs to the static VarInfo representing the output properties of the domain classes")	
        for out in self.model.outputs:
            self.newline(node)
            self.write('SiriusQuality%s.DomainClass.%s%sVarInfo.%s.CurrentValue=%s.%s;'%(self.name, self.name, out.variablecategory.capitalize(),out.name,category[out.variablecategory], out.name))
        self.newline(node)
        self.write('ConditionsCollection prc = new ConditionsCollection();'); self.newline(node)
        self.write('Preconditions pre = new Preconditions(); ' ); self.newline(node)
        n = len(self.model.inputs) + 1
        for out in self.model.outputs:
            self.newline(node)
            self.write("RangeBasedCondition r%s = new RangeBasedCondition(SiriusQuality%s.DomainClass.%s%sVarInfo.%s);"%(n,self.name, self.name, out.variablecategory.capitalize(),out.name)); self.newline(node)
            self.write("if(r%s.ApplicableVarInfoValueTypes.Contains( SiriusQuality%s.DomainClass.%s%sVarInfo.%s.ValueType)){prc.AddCondition(r%s);}"%(n, self.name, self.name, out.variablecategory.capitalize(), out.name, n)); self.newline(node)
            n = n+1
        self.write('string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;')
        self.close(node)
        self.newline(node)
        self.write("catch (Exception exception)"); 
        self.open(node)
        self.write('string msg = "SiriusQuality.%s, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";'%self.name); self.newline(node)
        self.write('throw new Exception(msg, exception);'); self.newline(node)
        self.close(node)
        self.close(node)
        self.newline(extra=1)

    def TestPreConditions(self, node):
        self.write("public string TestPreConditions(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex,string callID)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        self.open(node)
        self.write("try")
        self.open(node)
        self.write("//Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes")	
        for inp in self.model.inputs:
            if "variablecategory" in dir(inp):
                self.newline(node)
                self.write('SiriusQuality%s.DomainClass.%s%sVarInfo.%s.CurrentValue=%s.%s;'%(self.name, self.name, inp.variablecategory.capitalize(),inp.name if not inp.name.endswith("_t1") else inp.name[:-3],category[inp.variablecategory], inp.name if not inp.name.endswith("_t1") else inp.name[:-3]))
            self.newline(node)
        self.write('ConditionsCollection prc = new ConditionsCollection();'); self.newline(node)
        self.write('Preconditions pre = new Preconditions(); ' ); self.newline(node)
        n =  1
        for inp in self.model.inputs:
            if "variablecategory" in dir(inp):
                self.newline(node)
                self.write("RangeBasedCondition r%s = new RangeBasedCondition(SiriusQuality%s.DomainClass.%s%sVarInfo.%s);"%(n,self.name, self.name,inp.variablecategory.capitalize(), inp.name if not inp.name.endswith("_t1") else inp.name[:-3])); self.newline(node)
                self.write("if(r%s.ApplicableVarInfoValueTypes.Contains( SiriusQuality%s.DomainClass.%s%sVarInfo.%s.ValueType)){prc.AddCondition(r%s);}"%(n, self.name, self.name, inp.variablecategory.capitalize(), inp.name if not inp.name.endswith("_t1") else inp.name[:-3], n)); self.newline(node)
                n = n+1
        self.newline(node)
        for p in self.model.parameters:
            self.write('prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("%s")));'%p.name)
            self.newline(node)
        self.write('string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in strategy " + this.GetType().Name); } return preConditionsResult;')
        self.close(node)
        self.newline(node)
        self.write("catch (Exception exception)"); 
        self.open(node)
        self.write('string msg = "SiriusQuality.%s, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";'%self.name); self.newline(node)
        self.write('throw new Exception(msg, exception);'); self.newline(node)
        self.close(node)
        self.close(node)
        self.newline(extra=1)



    def estimate(self, node):
        self.write("public void Estimate(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        self.open(node)
        self.write("try")
        self.open(node)
        self.write("CalculateModel(s, s1, r, a, ex);")
        self.close(node)
        self.newline(node)
        self.write("catch (Exception exception)")
        self.open(node)
        self.write('string msg = "Error in component SiriusQuality%s, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;'%self.name)				
        self.newline(node)
        self.write('throw new Exception(msg, exception);')
        self.close(node)
        self.close(node)
        self.newline(extra=1)


    def get_set_param(self, node):
        self.write("// Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.\n")
        for arg in self.node_param : 
            self.newline(node)
            self.write("public ")
            self.visit_decl(arg.pseudo_type)
            self.write(' ' +arg.name)
            self.open(node)
            self.write("get { ")
            self.newline(node)
            self.indentation += 1  
            self.write('VarInfo vi= _modellingOptionsManager.GetParameterByName("%s");'%arg.name)
            self.newline(node)
            self.write("if (vi != null && vi.CurrentValue!=null) return (")
            self.visit_decl(arg.pseudo_type)
            self.write(")vi.CurrentValue ;")
            self.newline(node)
            self.write('else throw new Exception("Parameter')
            self.write(" '%s' not found (or found null) in strategy '%s'"%(arg.name,self.model.name))
            self.write('");')
            self.newline(node)
            self.indentation -= 1 
            self.write('} set {')
            self.newline(node)
            self.indentation += 1
            self.write('VarInfo vi = _modellingOptionsManager.GetParameterByName("%s");'%arg.name)
            self.newline(node)
            self.write('if (vi != null)  vi.CurrentValue=value;')
            self.newline(node)
            self.write('else throw new Exception("Parameter')
            self.write(" '%s' not found in strategy '%s'"%(arg.name,self.model.name))
            self.write('");')
            self.close(node)
            self.close(node)
        self.newline(extra=1)

    def visit_function_definition(self, node):      
        self.newline(node)
        self.funcname = node.name  
        if (not node.name.startswith("model_") and not node.name.startswith("init_")) :
            self.write("public static ")
            self.visit_decl(node.return_type) if node.return_type else self.write("void")
            self.write(" Main(") if node.name=="main" else self.write(" %s("%node.name)
            for i, pa in enumerate(node.params):
                self.visit_decl(pa.pseudo_type)
                self.write(" %s"%pa.name)
                if i!= (len(node.params)-1):
                    self.write(', ')
            self.write(')')
            self.open(node)
        else: 
            self.write("private void CalculateModel(") if not node.name.startswith("init_") else self.write("public void Init(")
            self.write('SiriusQuality%s.DomainClass.%sState s, SiriusQuality%s.DomainClass.%sState s1, SiriusQuality%s.DomainClass.%sRate r, SiriusQuality%s.DomainClass.%sAuxiliary a, SiriusQuality%s.DomainClass.%sExogenous ex)'%(self.name, self.name,self.name,self.name,self.name, self.name,self.name,self.name, self.name,self.name))
            self.open(node)
            for arg in self.add_features(node) :
                if "feat" in dir(arg):
                    if arg.feat in ["IN","INOUT"] :
                        self.newline(node) 
                        if self.model and arg.name not in self.modparam:
                            self.visit_decl(arg.pseudo_type)
                            self.write(" ")
                            self.write(arg.name)
                            if not node.name.startswith("init_"):
                                if arg.name in self.states and not arg.name.endswith("_t1") :
                                    self.write(" = s.%s"%arg.name)
                                if arg.name in self.states and arg.name.endswith("_t1") :
                                    self.write(" = s1.%s"%arg.name[:-3])
                                if arg.name in self.rates:
                                    self.write(" = r.%s"%arg.name)
                                if arg.name in self.auxiliary:
                                    self.write(" = a.%s"%arg.name) 
                            else:
                                if arg.pseudo_type[0] =="list":
                                    self.write(" = new List<%s>()"%(self.types[arg.pseudo_type[1]]))
                                elif arg.pseudo_type[0] =="array":
                                    self.write(" = new %s[%s]"%(self.types[arg.pseudo_type[1]], arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name))
                            self.write(";")                   
        self.indentation -= 1 
        self.body(node.block)
        self.newline(node)
        self.visit_return(node)
        self.close(node)
        self.newline(extra=1)

    def open(self, node):
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation += 1 
    
    def close(self, node):
        self.newline(node)
        self.indentation -= 1 
        self.write("}")


    def visit_module(self, node):
        self.write("using SiriusQuality%s.DomainClass;"%self.name)
        self.newline(node)
        self.write("namespace SiriusQuality%s.Strategies"%self.name)
        self.open(node)
        self.write("public class %s : IStrategySiriusQuality%s"%(self.model.name, self.name))
        self.open(node)
        self.write("public %s()"%self.model.name)  
        self.open(node)      
        self.inOutputDesc(node)
        self.close(node)
        self.newline(extra=1) 
        self.description(node)
        self.url(node)  
        self.domain(node)
        self.modelType(node)   
        self.isContext(node)
        self.isTimeStep(node)
        self.publisherdata(node)
        self.SetPublisherData(node)
        self.write("private ModellingOptionsManager _modellingOptionsManager;")
        self.newline(node)	
        self.write("public ModellingOptionsManager ModellingOptionsManager")
        self.open(node)
        self.write("get { return _modellingOptionsManager; } ")
        self.close(node)
        self.newline(extra=1)
        self.getStrategyDomainClassesTypes(node) ###
        self.get_set_param(node) ####
        self.setParametersDefaultValue(node) ###
        self.SetStaticParametersVarInfoDefinitions(node) ####
        self.staticVarInfo(node) ###
        self.TestPostConditions(node) ###
        self.TestPreConditions(node) ###
        self.estimate(node)  ###
        self.visit(node.body)
        self.close(node)  #class
        self.close(node)  #namespace            


class SiriusTrans(CsharpTrans):
    """ This class used to generates states, rates, and auxiliary classes
    for Sirius.
    """
    
    def __init__(self, models):
        self.models = models
        CsharpTrans.__init__(self, self.models)


    def using(self):
        self.write("""
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

""")

    def open(self, node):
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation += 1 
    
    def close(self, node):
        self.newline(node)
        self.indentation -= 1 
        self.write("}")

    def constr(self, node, typ):
        self.write('private ParametersIO _parametersIO;')
        self.newline(extra=1)
        self.write('public %s()'%typ)
        self.open(node)
        self.write('_parametersIO = new ParametersIO(this);')
        self.close(node)
    
    def copyConstr(self, nodes, typ):
        self.write('public %s(%s toCopy, bool copyAll) // copy constructor '%(typ, typ))
        self.open(nodes)
        self.write('if (copyAll)')
        self.open(nodes)
        self.copyconstructor(nodes)
        self.close(nodes)
        self.close(nodes)
        self.newline(extra = 1)
    
    def description(self, node, typ):
        self.write("public string Description") 
        self.open(node)
        self.write('get { return "%s of the component";}'%typ)
        self.close(node)
        self.newline(extra=1) 

    def url(self, node):
        self.write("public string URL") 
        self.open(node)
        self.write('get { return "http://" ;}')
        self.close(node)
        self.newline(extra=1) 

    def propertiesDescription(self, node):
        self.write('public virtual IDictionary<string, PropertyInfo> PropertiesDescription')
        self.open(node)
        self.write('get { return _parametersIO.GetCachedProperties(typeof(IDomainClass));}')
        self.close(node)
        self.newline(extra=1) 

    def clone(self, node):
        self.write("public virtual Object Clone()")
        self.open(node)
        self.write('IDomainClass myclass = (IDomainClass) this.MemberwiseClone();')
        self.newline(node)
        self.write('_parametersIO.PopulateClonedCopy(myclass);')
        self.newline(node)
        self.write('return myclass;')
        self.close(node)

    def clearValue(self, node):
        self.write("public virtual Boolean ClearValues()")
        self.open(node)
        for arg in node:
            self.newline(node) 
            self.write(" _")
            self.write(arg.name)
            if arg.pseudo_type[0] =="list":
                self.write(" = new List<%s>()"%(self.types[arg.pseudo_type[1]]))
            elif arg.pseudo_type=="DateTime":
                self.write(" = new DateTime()")
            elif arg.pseudo_type[0] =="array":
                self.write(" = new %s[%s]"%(self.types[arg.pseudo_type[1]], arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name))
            elif arg.pseudo_type == "str":
                self.write(" = null")
            else: self.write(" = default(%s)"%(self.types[arg.pseudo_type]))
            self.write(";") 
        self.newline(node);
        self.write("return true;")
        self.close(node)
        self.newline(extra=1)



    def generate(self, nodes, typ, name): 
        self.using()
        self.write("namespace SiriusQuality%s.DomainClass"%name)
        self.open(nodes)
        self.write("public class %s : ICloneable, IDomainClass"%typ)
        self.newline()
        self.write("{")
        self.indentation += 1        
        self.newline()
        self.private(nodes)
        self.newline()
        self.constr(nodes, typ)    ########### constructor
        self.newline(extra = 1)
        self.copyConstr(nodes, typ)###### copy constructor     
        self.getset(nodes)
        self.newline(extra=1)
        self.description(nodes, typ)
        self.url(nodes)
        self.propertiesDescription(nodes)
        self.clearValue(nodes)
        self.clone(nodes)
        self.indentation -= 1
        self.newline()
        self.write('}')
        self.close(nodes)
    
    def staticVarInfoDef(self, node):
        for n in node:
            self.write('static VarInfo _%s = new VarInfo();'%n.name)
            self.newline(1)
        self.newline(extra = 1)

    def varInfoConstrctor(self, node, typ):
        self.write("static %sVarInfo()"%typ)
        self.open(node)
        self.write("%sVarInfo.DescribeVariables();"%typ)
        self.close(node)
        self.newline(extra = 1)
    
    def infoDescription(self, node, typ):
        self.write('public virtual string Description')
        self.open(node)
        self.write('get { return "%s Domain class of the component";}'%typ)
        self.close(node)
        self.newline(extra = 1)

    def domainClassOfReference(self, node, typ):
        self.write('public string DomainClassOfReference')
        self.open(node)
        self.write('get { return "%s";}'%typ)
        self.close(node)
        self.newline(extra = 1)

    def getVarInfo(self, node):
        for n in node:
            self.write('public static  VarInfo %s'%n.name)
            self.open(node)
            self.write('get { return _%s;}'%n.name)
            self.close(node)
            self.newline(extra = 1)
        self.newline(extra = 1)

    def describeVariables(self, node):
        self.write('static void DescribeVariables()')
        self.open(node)
        for pa in node :
            self.write('_%s.Name = "%s";'%(pa.name, pa.name)); self.newline(node)
            self.write('_%s.Description = "%s";'%(pa.name, pa.description)); self.newline(node)
            self.write('_%s.MaxValue = %s;'%(pa.name,pa.max if ("max" in dir(pa) and pa.max is not None) or pa.max=="" else getdefault(pa))); self.newline(node)
            self.write('_%s.MinValue = %s;'%(pa.name, pa.min if ("min" in dir(pa) and pa.min is not None) or pa.min=="" else getdefault(pa))); self.newline(node)
            self.write('_%s.DefaultValue = %s;'%(pa.name, getdefault(pa))); self.newline(node)
            self.write('_%s.Units = "%s";'%(pa.name, pa.unit if ("unit" in dir(pa) and pa.unit is not None) else "dimensionless")); self.newline(node)
            self.write('_%s.ValueType = VarInfoValueTypes.GetInstanceForName("%s");'%(pa.name, param_datatype[pa.datatype])); self.newline(node)
            self.newline(extra=1)
        self.close(node)  
        self.newline(extra = 1)  
    
    def generateVarInfo(self, nodes, typ, name):
        self.using()
        self.write("namespace SiriusQuality%s.DomainClass"%name)
        self.open(nodes)
        self.write('public class %sVarInfo : IVarInfoClass'%typ)
        self.open(nodes)
        self.staticVarInfoDef(nodes)
        self.varInfoConstrctor(nodes, typ)
        self.infoDescription(nodes, typ)
        self.url(nodes)
        self.domainClassOfReference(nodes, typ)
        self.getVarInfo(nodes)
        self.describeVariables(nodes)
        self.close(nodes)
        self.close(nodes)


def to_struct_sirius(models, rep, name):
    generator = SiriusTrans(models)
    generator.model2Node()

    def createdc(states, catvar):
        generator.result = []
        generator.generate(states, "%s%s"%(name,catvar), name)
        z= ''.join(generator.result)
        filename = Path(os.path.join(rep, "%s%s.cs"%(name, catvar)))
        with open(filename, "wb") as tg_file:
            tg_file.write(z.encode('utf-8'))

    states = generator.node_states
    createdc(states,"State")
    rates = generator.node_rates
    createdc(rates,"Rate")      
    auxiliary = generator.node_auxiliary
    createdc(auxiliary,"Auxiliary") 
    

    def varinfo(states, catvar):
        generator.result = []
        generator.generateVarInfo(states, "%s%s"%(name,catvar), name)
        z= ''.join(generator.result)
        filename = Path(os.path.join(rep, "%s%sVarInfo.cs"%(name, catvar)))
        with open(filename, "wb") as tg_file:
            tg_file.write(z.encode('utf-8'))

    states = generator.states
    varinfo(states,"State")
    rates = generator.rates
    varinfo(rates,"Rate")      
    auxiliary = generator.auxiliary
    varinfo(auxiliary,"Auxiliary")
    auxiliary = generator.exogenous
    varinfo(auxiliary,"Exogenous")



''' Csharp composite'''


class SiriusCompo(CsharpCompo):
    """ This class used to generates states, rates and auxiliary classes
        for C# languages.
    """
    def __init__(self, tree=None, model=None, name=None):
        self.model=model
        self.tree = tree
        self.name = name
        CsharpCompo.__init__(self, tree, model, name)

    def usingBioma(self):
        self.write("""
using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml;
using CRA.ModelLayer.MetadataTypes;
using CRA.ModelLayer.Core;
using CRA.ModelLayer.Strategy;
using System.Reflection;
using VarInfo=CRA.ModelLayer.Core.VarInfo;
using Preconditions=CRA.ModelLayer.Core.Preconditions;
using CRA.AgroManagement;       
""")


    def desc(self,node, n, inp, vartype) :
        self.write("PropertyDescription pd%s = new PropertyDescription();"%n)              
        self.newline(node)
        self.write("pd%s.DomainClassType = typeof(SiriusQuality%s.DomainClass.%s%s);"%(n, self.name,self.name,inp.variablecategory.capitalize()))
        self.newline(node)
        self.write('pd%s.PropertyName = "%s";'%(n,inp.name if not inp.name.endswith("_t1") else inp.name[:-3]))
        self.newline(node)
        self.write('pd%s.PropertyType = (SiriusQuality%s.DomainClass.%s%sVarInfo.%s).ValueType.TypeForCurrentValue;'%(n, self.name,self.name, inp.variablecategory.capitalize(),inp.name if not inp.name.endswith("_t1") else inp.name[:-3]))
        self.newline(node)
        self.write('pd%s.PropertyVarInfo =(SiriusQuality%s.DomainClass.%s%sVarInfo.%s);'%(n,self.name,self.name, inp.variablecategory.capitalize(),inp.name if not inp.name.endswith("_t1") else inp.name[:-3]))
        self.newline(node)
        self.write('%s.Add(pd%s);'%(vartype, n)) 

    def constructor(self, node):
        self.write("public %sComponent()"%self.model.name)  
        self.open(node)       
        self.write("ModellingOptions mo0_0 = new ModellingOptions();")
        self.newline(node)
        self.write("//Parameters")
        self.newline(node)
        self.write("List<VarInfo> _parameters0_0 = new List<VarInfo>();")
        n = 1
        for p in self.node_param:
            for j in self.get_mo(p.name):
                self.newline(node)
                self.write('VarInfo v%s = new CompositeStrategyVarInfo(_%s, "%s");'%(n,j,p.name))
                self.newline(node)
                self.write("_parameters0_0.Add(v%s);"%n)
                n = n+1
        self.newline(node)
        self.write("List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();")
        self.newline(node)
        n=1
        for inp in self.model.inputs:
            if "variablecategory" in dir(inp) :
                self.desc(node,n,inp, "_inputs0_0")
                self.write("")
                self.newline(node)
                n = n+1      
        self.newline(node)
        self.write('mo0_0.Inputs=_inputs0_0;')
        self.newline(node)
        self.write("List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();")
        self.newline(node)
        for out in self.model.outputs:
            if "variablecategory" in dir(out):
                self.desc(node,n,out, "_outputs0_0")
                self.write("")
                self.newline(node)
                n = n+1
        self.newline(node)
        self.write('mo0_0.Outputs=_outputs0_0;')
        self.newline(node)
        self.write("List<string> lAssStrat0_0 = new List<string>();")
        self.newline(node)
        for m in self.model.model:
            name = m.name
            self.write("lAssStrat0_0.Add(typeof(SiriusQuality%s.Strategies.%s).FullName);"%(self.model.name, name))
            self.newline(1)
        self.write("mo0_0.AssociatedStrategies = lAssStrat0_0;")
        self.newline(1)
        self.write("_modellingOptionsManager = new ModellingOptionsManager(mo0_0);")
        self.newline(1)
        self.write("SetStaticParametersVarInfoDefinitions();")
        self.newline(1)
        self.write("SetPublisherData();")
        self.close(node)
        self.newline(extra=1)


    def description(self, node):
        self.write("public string Description") 
        self.open(node)
        self.write('get { return "%s" ;}'%self.model.description.Abstract.replace("\n", ""))
        self.close(node)
        self.newline(extra=1) 

    def url(self, node):
        self.write("public string URL") 
        self.open(node)
        self.write('get { return "%s" ;}'%(self.model.description.url if "url" in dir(self.model.description) else ""))
        self.close(node)
        self.newline(extra=1) 

    def domain(self, node):
        self.write("public string Domain") 
        self.open(node)
        self.write('get { return "";}')
        self.close(node)
        self.newline(extra=1) 

    def modelType(self, node):
        self.write("public string ModelType") 
        self.open(node)
        self.write('get { return "";}')
        self.close(node)
        self.newline(extra=1)

    def isContext(self, node):
        self.write("public bool IsContext") 
        self.open(node)
        self.write('get { return false;}')
        self.close(node)
        self.newline(extra=1) 

    def isTimeStep(self, node):
        self.write("public IList<int> TimeStep")
        self.open(node)
        self.write("get")
        self.open(node)
        self.write("IList<int> ts = new List<int>();")
        self.newline(node)
        self.write("return ts;")
        self.close(node)
        self.close(node)
        self.newline(extra=1) 

    def publisherdata(self, node):
        self.write("private  PublisherData _pd;")
        self.newline(node)	
        self.write("public PublisherData PublisherData")
        self.open(node)
        self.write("get { return _pd;} ")
        self.close(node)
        self.newline(extra=1) 

    def modelingOptions(self, node):
        self.write("private ModellingOptionsManager _modellingOptionsManager;")
        self.newline(node)	
        self.write("public ModellingOptionsManager ModellingOptionsManager")
        self.open(node)
        self.write("get { return _modellingOptionsManager; } ")
        self.close(node)
        self.newline(extra=1) 
    
    def SetPublisherData(self, node):
        self.write("private  void SetPublisherData()")
        self.open(node)	
        self.write("_pd = new CRA.ModelLayer.MetadataTypes.PublisherData();")
        self.newline(node)
        self.write('_pd.Add("Creator", "%s");'%self.model.description.Authors)
        self.newline(node)
        self.write('_pd.Add("Date", "");')
        self.newline(node)
        self.write('_pd.Add("Publisher", "%s");'%self.model.description.Institution)
        self.close(node)
        self.newline(extra=1) 

    def getStrategyDomainClassesTypes(self, node):	
        self.write("public IEnumerable<Type> GetStrategyDomainClassesTypes()")
        self.open(node)
        self.write("return new List<Type>() {  typeof(SiriusQuality%s.DomainClass.%sState), typeof(SiriusQuality%s.DomainClass.%sState), typeof(SiriusQuality%s.DomainClass.%sRate), typeof(SiriusQuality%s.DomainClass.%sAuxiliary), typeof(SiriusQuality%s.DomainClass.%sExogenous)};"%(self.name, self.name,self.name, self.name,self.name, self.name,self.name, self.name, self.name, self.name))
        self.close(node)
        self.newline(extra=1)

    def SetParametersDefaultValue(self, node):
        self.write("public void SetParametersDefaultValue()")
        self.open(node)
        self.write("_modellingOptionsManager.SetParametersDefaultValue();")
        for m in self.model.model:
            self.newline(node)
            self.write("_%s.SetParametersDefaultValue();"%m.name)
        self.close(node)
        self.newline(extra=1)

    def varinfodef(self, node, pa):
        self.write('%sVarInfo.Name = "%s";'%(pa.name, pa.name)); self.newline(node)
        self.write('%sVarInfo.Description = "%s";'%(pa.name, pa.description)); self.newline(node)
        self.write('%sVarInfo.MaxValue = %s;'%(pa.name,pa.max if pa.max is not None else getdefault(pa))); self.newline(node)
        self.write('%sVarInfo.MinValue = %s;'%(pa.name, pa.min if pa.min is not None else getdefault(pa))); self.newline(node)
        self.write('%sVarInfo.DefaultValue = %s;'%(pa.name, getdefault(pa))); self.newline(node)
        self.write('%sVarInfo.Units = "%s";'%(pa.name, pa.unit if ("unit" in dir(pa) and pa.unit is not None) else "dimensionless")); self.newline(node)
        self.write('%sVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("%s");'%(pa.name, param_datatype[pa.datatype])); self.newline(node)

    def SetStaticParametersVarInfoDefinitions(self, node):
        self.write("private static void SetStaticParametersVarInfoDefinitions()")
        self.open(node)
        for pa in self.params: 
            self.newline(extra=1)  
            self.varinfodef(node, pa)
        self.close(node)
        self.newline(extra=1)

    def staticVarInfo(self, node):
        for pa in self.node_param: 	
            self.write("public static VarInfo %sVarInfo"%pa.name)
            self.open(node)
            self.write("get { return SiriusQuality%s.Strategies.%s.%sVarInfo;} "%(self.model.name,self.get_mo(pa.name)[0],pa.name))
            self.close(node) 
            self.newline(extra=1) 

    def TestPostConditions(self, node):
        self.write("public string TestPostConditions(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex,string callID)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        self.open(node)
        self.write("try")
        self.open(node)
        self.write("//Set current values of the outputs to the static VarInfo representing the output properties of the domain classes")	
        for out in self.model.outputs:
            self.newline(node)
            self.write('SiriusQuality%s.DomainClass.%s%sVarInfo.%s.CurrentValue=%s.%s;'%(self.name, self.name, out.variablecategory.capitalize(),out.name,category[out.variablecategory], out.name))
        self.newline(extra=1)
        self.write('ConditionsCollection prc = new ConditionsCollection();'); self.newline(node)
        self.write('Preconditions pre = new Preconditions(); ' ); self.newline(node)
        self.newline(extra=1)
        n = len(self.model.inputs) + 1
        for out in self.model.outputs:
            self.newline(node)
            self.write("RangeBasedCondition r%s = new RangeBasedCondition(SiriusQuality%s.DomainClass.%s%sVarInfo.%s);"%(n,self.name, self.name, out.variablecategory.capitalize(), out.name)); self.newline(node)
            self.write("if(r%s.ApplicableVarInfoValueTypes.Contains( SiriusQuality%s.DomainClass.%s%sVarInfo.%s.ValueType)){prc.AddCondition(r%s);}"%(n, self.name, self.name, out.variablecategory.capitalize(), out.name, n)); self.newline(node)
            n = n+1
        self.newline(extra=1)
        self.write('string ret = "";')
        self.newline(node)
        for m in self.model.model:
            self.write('ret += _%s.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQuality%s.Strategies.%s");'%(m.name, self.model.name, self.name ))
            self.newline(node)
        self.write('if (ret != "") { pre.TestsOut(ret, true, "   postconditions tests of associated classes"); }')
        self.newline(extra=1)
        self.write('string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;')
        self.close(node)
        self.newline(node)
        self.write("catch (Exception exception)"); 
        self.open(node)
        self.write('string msg = "Component SiriusQuality.%s, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";'%self.name); self.newline(node)
        self.write('throw new Exception(msg, exception);'); self.newline(node)
        self.close(node)
        self.close(node)
        self.newline(extra=1)


    def TestPreConditions(self, node):
        self.write("public string TestPreConditions(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex,string callID)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        self.open(node)
        self.write("try")
        self.open(node)
        self.write("//Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes")	
        for inp in self.model.inputs:
            if "variablecategory" in dir(inp):
                self.newline(node)
                self.write('SiriusQuality%s.DomainClass.%s%sVarInfo.%s.CurrentValue=%s.%s;'%(self.name, self.name, inp.variablecategory.capitalize(),inp.name if not inp.name.endswith("_t1") else inp.name[:-3],category[inp.variablecategory], inp.name if not inp.name.endswith("_t1") else inp.name[:-3]))
            self.newline(node)
        self.write('ConditionsCollection prc = new ConditionsCollection();'); self.newline(node)
        self.write('Preconditions pre = new Preconditions(); ' ); self.newline(node)
        n =  1
        for inp in self.model.inputs:
            if "variablecategory" in dir(inp):
                self.newline(node)
                self.write("RangeBasedCondition r%s = new RangeBasedCondition(SiriusQuality%s.DomainClass.%s%sVarInfo.%s);"%(n,self.name, self.name, inp.variablecategory.capitalize(), inp.name if not inp.name.endswith("_t1") else inp.name[:-3])); self.newline(node)
                self.write("if(r%s.ApplicableVarInfoValueTypes.Contains( SiriusQuality%s.DomainClass.%s%sVarInfo.%s.ValueType)){prc.AddCondition(r%s);}"%(n, self.name, self.name, inp.variablecategory.capitalize(), inp.name if not inp.name.endswith("_t1") else inp.name[:-3], n)); self.newline(node)
                n = n+1
        self.newline(extra=1)
        for p in self.params:
            self.write('prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("%s")));'%p.name)
            self.newline(node)

        self.write('string ret = "";')
        self.newline(node)
        for m in self.model.model:
            self.write('ret += _%s.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQuality%s.Strategies.%s");'%(m.name, self.model.name, self.name ))
            self.newline(node)
        self.write('if (ret != "") { pre.TestsOut(ret, true, "   preconditions tests of associated classes"); }')
        self.newline(extra=1)
        self.write('string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in component " + this.GetType().Name); } return preConditionsResult;')
        self.close(node)
        self.newline(node)
        self.write("catch (Exception exception)"); 
        self.open(node)
        self.write('string msg = "Component SiriusQuality.%s, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";'%self.name); self.newline(node)
        self.write('throw new Exception(msg, exception);'); self.newline(node)
        self.close(node)
        self.close(node)
        self.newline(extra=1)


    def estimate(self, node):
        self.write("public void Estimate(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        self.open(node)
        self.write("try")
        self.open(node)
        self.write("CalculateModel(s, s1, r, a, ex);")
        self.close(node)
        self.newline(node)
        self.write("catch (Exception exception)")
        self.open(node)
        self.write('string msg = "Error in component SiriusQuality%s, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;'%self.name)				
        self.newline(node)
        self.write('throw new Exception(msg, exception);')
        self.close(node)
        self.close(node)
        self.newline(extra=1)
    
    def calculateModel(self, node):
        self.write("private void CalculateModel(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        self.open(node)
        self.write("EstimateOfAssociatedClasses(s, s1, r, a, ex);")
        self.close(node)
        self.newline(extra=1)
    
    def copy_Constructor(self, node):
        self.write('public %sComponent(%sComponent toCopy): this() // copy constructor '%(self.model.name, self.model.name))
        self.open(node)
        self.copyconstructor(self.node_param)
        self.close(node)
        



    def visit_module(self, node): 
        self.usingBioma()
        self.newline(node)
        self.write("using SiriusQuality%s.DomainClass;"%self.model.name)
        self.newline(node)
        self.write("namespace SiriusQuality%s.Strategies"%self.model.name)
        self.open(node)
        self.write("public class %sComponent : IStrategySiriusQuality%s"%(self.model.name, self.model.name))
        self.open(node)
        self.constructor(node)
        self.description(node)
        self.url(node)  
        self.domain(node)
        self.modelType(node)   
        self.isContext(node)
        self.isTimeStep(node)
        self.publisherdata(node) 
        self.SetPublisherData(node) 
        self.modelingOptions(node) 
        self.getStrategyDomainClassesTypes(node)              
        self.getsetParam(node,self.node_param)
        self.SetParametersDefaultValue(node)
        self.SetStaticParametersVarInfoDefinitions(node)
        self.staticVarInfo(node)
        self.TestPostConditions(node)
        self.TestPreConditions(node)
        self.estimate(node)
        self.calculateModel(node)
        self.createModelInstances()
        self.newline(extra=1)
        self.visit(node.body)
        self.newline(extra=1)
        self.copy_Constructor(self.node_param)
        self.newline(node)
        self.close(node)
        self.close(node)
    
    def visit_function_definition(self, node):
        if node.name.startswith("model"):
            self.write("private void EstimateOfAssociatedClasses(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        else:
            self.write("public void Init(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
            self.init=True
        self.open(node)
        self.visit(node.block)
        self.close(node)
        self.newline(extra=1)

    def visit_implicit_return(self, node):
        self.newline(node)

    def visit_assignment(self, node):
        if "function" in dir(node.value) and node.value.function.split('_')[0]=="model":
            name  = node.value.function.split('model_')[1]
            self.write("_%s.Estimate(s,s1, r, a, ex);"%(name))
            self.newline(node)
        else:
            self.newline(node)
            self.visit(node.target)
            self.write(' = ')
            self.visit(node.value) 
            self.write(";")
            self.newline(node)
    
    def interfaceStrategy(self, node):
        self.write('using System;'); self.newline(1)
        self.write('using CRA.AgroManagement;'); self.newline(1)
        self.write('using CRA.ModelLayer.Strategy;'); self.newline(1)
        self.write('namespace SiriusQuality%s.DomainClass'%(self.model.name))
        self.open(node)
        self.write('public interface IStrategySiriusQuality%s : IStrategy'%self.model.name)
        self.open(node)
        self.write('void Estimate( %sState s, %sState s1, %sRate r, %sAuxiliary a, %sExogenous ex);'%(self.model.name, self.model.name, self.model.name, self.model.name, self.model.name))
        self.newline(extra=1)
        self.write('string TestPreConditions( %sState s, %sState s1, %sRate r, %sAuxiliary a, %sExogenous ex, string callID);'%(self.model.name, self.model.name, self.model.name, self.model.name, self.model.name))
        self.newline(extra=1)
        self.write('string TestPostConditions( %sState s, %sState s1, %sRate r, %sAuxiliary a, %sExogenous ex, string callID);'%(self.model.name, self.model.name, self.model.name, self.model.name, self.model.name))
        self.newline(extra=1)
        self.write('void SetParametersDefaultValue();')
        self.close(node)
        self.close(node)



    def wrapper(self):
        self.write("using SQCrop2ML_%s.DomainClass;"%self.model.name)
        self.newline(1)
        self.write("using SQCrop2ML_%s.Strategies;"%self.model.name)
        self.newline(extra=1)
        self.write("namespace SiriusModel.Model.%s"%self.model.name)
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1         
        self.write("class %sWrapper :  UniverseLink"%self.model.name)
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1
        self.privateWrap()
        self.constrWrap()
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
        self.indentation -= 1
        self.write("}")
    
    def constrWrap(self):
        name = self.model.name
        self.write("public %sWrapper(Universe universe) : base(universe)"%(name))
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1
        self.write("s = new %sState();"%(name))
        self.newline(1)
        self.write("r = new %sRate();"%(name))
        self.newline(1)
        self.write("a = new %sAuxiliary();"%(name))
        self.newline(1)
        self.write("%sComponent = new %s();"%(name.lower(), name))
        self.newline(1)
        self.write("loadParameters();")
        self.newline(1)
        self.indentation -= 1
        self.write("}")


    def copyconstrWrap(self):
        self.write("public %sWrapper(Universe universe, %sWrapper toCopy, bool copyAll) : base(universe)"%(self.model.name,self.model.name))
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.write("s = (toCopy.s != null) ? new %sState(toCopy.s, copyAll) : null;"%(self.model.name))
        self.newline(1)
        self.newline(1)
        self.write("r = (toCopy.r != null) ? new %sRate(toCopy.r, copyAll) : null;"%(self.model.name))
        self.newline(1)
        self.write("a = (toCopy.a != null) ? new %sAuxiliary(toCopy.a, copyAll) : null;"%(self.model.name))
        self.newline(1)
        self.write("if (copyAll)")
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.write("%sComponent = (toCopy.%sComponent != null) ? new %s(toCopy.%sComponent) : null;"%(self.model.name.lower(),self.model.name.lower(),self.model.name,self.model.name.lower()))
        self.newline(1)
        self.indentation -= 1        
        self.write("}")
        self.newline(1)
        self.indentation -= 1        
        self.write("}")

def to_wrapper_sirius(models, rep, name):
    generator = SiriusCompo(model = models)
    generator.result=[u"using System;\nusing System.Collections.Generic;\nusing System.Linq;\n"]
    generator.model2Node()
    generator.wrapper()
    z= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sWrapper.cs"%name))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z.encode('utf-8'))
    filename = Path(os.path.join(rep, "IStrategySiriusQuality%s.cs"%name))
    generator2 = SiriusCompo(model = models)
    generator2.interfaceStrategy(1)
    z= ''.join(generator2.result)
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z.encode('utf-8'))

    return 0
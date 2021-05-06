
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
using SiriusQualityPhenology.DomainClass;
namespace SiriusQualityPhenology.Strategies
{
    public class UpdatePhase : IStrategySiriusQualityPhenology
    {
        public UpdatePhase()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 1;
            v1.Description = "true if the plant is vernalizable";
            v1.Id = 0;
            v1.MaxValue = 1;
            v1.MinValue = 0;
            v1.Name = "isVernalizable";
            v1.Size = 1;
            v1.Units = "";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 105;
            v2.Description = "Thermal time from sowing to emergence";
            v2.Id = 0;
            v2.MaxValue = 1000;
            v2.MinValue = 0;
            v2.Name = "dse";
            v2.Size = 1;
            v2.Units = "°C d";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = 2.22;
            v3.Description = "Phyllochronic duration of the period between flag leaf ligule appearance and anthesis";
            v3.Id = 0;
            v3.MaxValue = 1000;
            v3.MinValue = 0;
            v3.Name = "pFLLAnth";
            v3.Size = 1;
            v3.Units = "";
            v3.URL = "";
            v3.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v3);
            VarInfo v4 = new VarInfo();
            v4.DefaultValue = 100;
            v4.Description = "Duration of the endosperm cell division phase";
            v4.Id = 0;
            v4.MaxValue = 10000;
            v4.MinValue = 0;
            v4.Name = "dcd";
            v4.Size = 1;
            v4.Units = "°C d";
            v4.URL = "";
            v4.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v4.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v4);
            VarInfo v5 = new VarInfo();
            v5.DefaultValue = 450;
            v5.Description = "Grain filling duration (from anthesis to physiological maturity)";
            v5.Id = 0;
            v5.MaxValue = 10000;
            v5.MinValue = 0;
            v5.Name = "dgf";
            v5.Size = 1;
            v5.Units = "°C d";
            v5.URL = "";
            v5.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v5.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v5);
            VarInfo v6 = new VarInfo();
            v6.DefaultValue = 0;
            v6.Description = "Grain maturation duration (from physiological maturity to harvest ripeness)";
            v6.Id = 0;
            v6.MaxValue = 50;
            v6.MinValue = 0;
            v6.Name = "degfm";
            v6.Size = 1;
            v6.Units = "°C d";
            v6.URL = "";
            v6.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v6.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v6);
            VarInfo v7 = new VarInfo();
            v7.DefaultValue = 15;
            v7.Description = "Saturating photoperiod above which final leaf number is not influenced by daylength";
            v7.Id = 0;
            v7.MaxValue = 24;
            v7.MinValue = 0;
            v7.Name = "maxDL";
            v7.Size = 1;
            v7.Units = "h";
            v7.URL = "";
            v7.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v7.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v7);
            VarInfo v8 = new VarInfo();
            v8.DefaultValue = 0.85;
            v8.Description = "Daylength response of leaf production";
            v8.Id = 0;
            v8.MaxValue = 1;
            v8.MinValue = 0;
            v8.Name = "sLDL";
            v8.Size = 1;
            v8.Units = "leaf h-1";
            v8.URL = "";
            v8.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v8.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v8);
            VarInfo v9 = new VarInfo();
            v9.DefaultValue = false;
            v9.Description = "true to ignore grain maturation";
            v9.Id = 0;
            v9.MaxValue = false;
            v9.MinValue = false;
            v9.Name = "ignoreGrainMaturation";
            v9.Size = 1;
            v9.Units = "";
            v9.URL = "";
            v9.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v9.ValueType = VarInfoValueTypes.GetInstanceForName("Boolean");
            _parameters0_0.Add(v9);
            VarInfo v10 = new VarInfo();
            v10.DefaultValue = 1;
            v10.Description = "Number of phyllochron between heading and anthesiss";
            v10.Id = 0;
            v10.MaxValue = 1000;
            v10.MinValue = 0;
            v10.Name = "pHEADANTH";
            v10.Size = 1;
            v10.Units = "";
            v10.URL = "";
            v10.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v10.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v10);
            VarInfo v11 = new VarInfo();
            v11.DefaultValue = "Default";
            v11.Description = "Switch to choose the type of phyllochron calculation to be used";
            v11.Id = 0;
            v11.MaxValue = "Default";
            v11.MinValue = "Default";
            v11.Name = "choosePhyllUse";
            v11.Size = 1;
            v11.Units = "";
            v11.URL = "";
            v11.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v11.ValueType = VarInfoValueTypes.GetInstanceForName("String");
            _parameters0_0.Add(v11);
            VarInfo v12 = new VarInfo();
            v12.DefaultValue = 120;
            v12.Description = "Phyllochron (Varietal parameter)";
            v12.Id = 0;
            v12.MaxValue = 1000;
            v12.MinValue = 0;
            v12.Name = "p";
            v12.Size = 1;
            v12.Units = "°C d leaf-1";
            v12.URL = "";
            v12.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v12.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v12);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd1.PropertyName = "cumulTT";
            pd1.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd2.PropertyName = "leafNumber";
            pd2.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd3.PropertyName = "cumulTTFromZC_39";
            pd3.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_39).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_39);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd4.PropertyName = "isMomentRegistredZC_39";
            pd4.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.isMomentRegistredZC_39).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.isMomentRegistredZC_39);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd5.PropertyName = "gAI";
            pd5.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI);
            _inputs0_0.Add(pd5);
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd6.PropertyName = "grainCumulTT";
            pd6.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.grainCumulTT).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.grainCumulTT);
            _inputs0_0.Add(pd6);
            PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd7.PropertyName = "dayLength";
            pd7.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength);
            _inputs0_0.Add(pd7);
            PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd8.PropertyName = "vernaprog";
            pd8.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog);
            _inputs0_0.Add(pd8);
            PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd9.PropertyName = "minFinalNumber";
            pd9.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber);
            _inputs0_0.Add(pd9);
            PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd10.PropertyName = "fixPhyll";
            pd10.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll);
            _inputs0_0.Add(pd10);
            PropertyDescription pd11 = new PropertyDescription();
            pd11.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd11.PropertyName = "phase";
            pd11.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase).ValueType.TypeForCurrentValue;
            pd11.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase);
            _inputs0_0.Add(pd11);
            PropertyDescription pd12 = new PropertyDescription();
            pd12.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd12.PropertyName = "cumulTTFromZC_91";
            pd12.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_91).ValueType.TypeForCurrentValue;
            pd12.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_91);
            _inputs0_0.Add(pd12);
            PropertyDescription pd13 = new PropertyDescription();
            pd13.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd13.PropertyName = "phyllochron";
            pd13.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron).ValueType.TypeForCurrentValue;
            pd13.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron);
            _inputs0_0.Add(pd13);
            PropertyDescription pd14 = new PropertyDescription();
            pd14.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd14.PropertyName = "hasLastPrimordiumAppeared";
            pd14.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared).ValueType.TypeForCurrentValue;
            pd14.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared);
            _inputs0_0.Add(pd14);
            PropertyDescription pd15 = new PropertyDescription();
            pd15.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd15.PropertyName = "finalLeafNumber";
            pd15.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber).ValueType.TypeForCurrentValue;
            pd15.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber);
            _inputs0_0.Add(pd15);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd16 = new PropertyDescription();
            pd16.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd16.PropertyName = "finalLeafNumber";
            pd16.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber).ValueType.TypeForCurrentValue;
            pd16.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber);
            _outputs0_0.Add(pd16);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd17 = new PropertyDescription();
            pd17.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd17.PropertyName = "phase";
            pd17.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase).ValueType.TypeForCurrentValue;
            pd17.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase);
            _outputs0_0.Add(pd17);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd18 = new PropertyDescription();
            pd18.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd18.PropertyName = "hasLastPrimordiumAppeared";
            pd18.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared).ValueType.TypeForCurrentValue;
            pd18.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared);
            _outputs0_0.Add(pd18);
            mo0_0.Outputs=_outputs0_0;
            //Associated strategies
            List<string> lAssStrat0_0 = new List<string>();
            mo0_0.AssociatedStrategies = lAssStrat0_0;
            //Adding the modeling options to the modeling options manager
            _modellingOptionsManager = new ModellingOptionsManager(mo0_0);
            SetStaticParametersVarInfoDefinitions();
            SetPublisherData();

        }

        public string Description
        {
            get { return "This strategy advances the phase and calculate the final leaf number    	" ;}
        }

        public string URL
        {
            get { return "" ;}
        }

        public string Domain
        {
            get { return "";}
        }

        public string ModelType
        {
            get { return "";}
        }

        public bool IsContext
        {
            get { return false;}
        }

        public IList<int> TimeStep
        {
            get
            {
                IList<int> ts = new List<int>();
                return ts;
            }
        }

        private  PublisherData _pd;
        public PublisherData PublisherData
        {
            get { return _pd;} 
        }

        private  void SetPublisherData()
        {
            _pd = new CRA.ModelLayer.MetadataTypes.PublisherData();
            _pd.Add("Creator", "Pierre MARTRE");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "INRA Montpellier");
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        public IEnumerable<Type> GetStrategyDomainClassesTypes()
        {
            return new List<Type>() {  typeof(SiriusQualityPhenology.DomainClass.PhenologyState),  typeof(SiriusQualityPhenology.DomainClass.PhenologyState), typeof(SiriusQualityPhenology.DomainClass.PhenologyRate), typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary), typeof(SiriusQualityPhenology.DomainClass.PhenologyExogenous)};
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public int isVernalizable
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("isVernalizable");
                if (vi != null && vi.CurrentValue!=null) return (int)vi.CurrentValue ;
                else throw new Exception("Parameter 'isVernalizable' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("isVernalizable");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'isVernalizable' not found in strategy 'UpdatePhase'");
            }
        }
        public double dse
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("dse");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'dse' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("dse");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'dse' not found in strategy 'UpdatePhase'");
            }
        }
        public double pFLLAnth
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("pFLLAnth");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'pFLLAnth' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("pFLLAnth");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'pFLLAnth' not found in strategy 'UpdatePhase'");
            }
        }
        public double dcd
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("dcd");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'dcd' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("dcd");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'dcd' not found in strategy 'UpdatePhase'");
            }
        }
        public double dgf
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("dgf");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'dgf' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("dgf");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'dgf' not found in strategy 'UpdatePhase'");
            }
        }
        public double degfm
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("degfm");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'degfm' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("degfm");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'degfm' not found in strategy 'UpdatePhase'");
            }
        }
        public double maxDL
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("maxDL");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'maxDL' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("maxDL");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'maxDL' not found in strategy 'UpdatePhase'");
            }
        }
        public double sLDL
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("sLDL");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'sLDL' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("sLDL");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'sLDL' not found in strategy 'UpdatePhase'");
            }
        }
        public bool ignoreGrainMaturation
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("ignoreGrainMaturation");
                if (vi != null && vi.CurrentValue!=null) return (bool)vi.CurrentValue ;
                else throw new Exception("Parameter 'ignoreGrainMaturation' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("ignoreGrainMaturation");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'ignoreGrainMaturation' not found in strategy 'UpdatePhase'");
            }
        }
        public double pHEADANTH
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("pHEADANTH");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'pHEADANTH' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("pHEADANTH");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'pHEADANTH' not found in strategy 'UpdatePhase'");
            }
        }
        public string choosePhyllUse
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("choosePhyllUse");
                if (vi != null && vi.CurrentValue!=null) return (string)vi.CurrentValue ;
                else throw new Exception("Parameter 'choosePhyllUse' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("choosePhyllUse");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'choosePhyllUse' not found in strategy 'UpdatePhase'");
            }
        }
        public double p
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("p");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'p' not found (or found null) in strategy 'UpdatePhase'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("p");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'p' not found in strategy 'UpdatePhase'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            isVernalizableVarInfo.Name = "isVernalizable";
            isVernalizableVarInfo.Description = "true if the plant is vernalizable";
            isVernalizableVarInfo.MaxValue = 1;
            isVernalizableVarInfo.MinValue = 0;
            isVernalizableVarInfo.DefaultValue = 1;
            isVernalizableVarInfo.Units = "";
            isVernalizableVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            dseVarInfo.Name = "dse";
            dseVarInfo.Description = "Thermal time from sowing to emergence";
            dseVarInfo.MaxValue = 1000;
            dseVarInfo.MinValue = 0;
            dseVarInfo.DefaultValue = 105;
            dseVarInfo.Units = "°C d";
            dseVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pFLLAnthVarInfo.Name = "pFLLAnth";
            pFLLAnthVarInfo.Description = "Phyllochronic duration of the period between flag leaf ligule appearance and anthesis";
            pFLLAnthVarInfo.MaxValue = 1000;
            pFLLAnthVarInfo.MinValue = 0;
            pFLLAnthVarInfo.DefaultValue = 2.22;
            pFLLAnthVarInfo.Units = "";
            pFLLAnthVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            dcdVarInfo.Name = "dcd";
            dcdVarInfo.Description = "Duration of the endosperm cell division phase";
            dcdVarInfo.MaxValue = 10000;
            dcdVarInfo.MinValue = 0;
            dcdVarInfo.DefaultValue = 100;
            dcdVarInfo.Units = "°C d";
            dcdVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            dgfVarInfo.Name = "dgf";
            dgfVarInfo.Description = "Grain filling duration (from anthesis to physiological maturity)";
            dgfVarInfo.MaxValue = 10000;
            dgfVarInfo.MinValue = 0;
            dgfVarInfo.DefaultValue = 450;
            dgfVarInfo.Units = "°C d";
            dgfVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            degfmVarInfo.Name = "degfm";
            degfmVarInfo.Description = "Grain maturation duration (from physiological maturity to harvest ripeness)";
            degfmVarInfo.MaxValue = 50;
            degfmVarInfo.MinValue = 0;
            degfmVarInfo.DefaultValue = 0;
            degfmVarInfo.Units = "°C d";
            degfmVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            maxDLVarInfo.Name = "maxDL";
            maxDLVarInfo.Description = "Saturating photoperiod above which final leaf number is not influenced by daylength";
            maxDLVarInfo.MaxValue = 24;
            maxDLVarInfo.MinValue = 0;
            maxDLVarInfo.DefaultValue = 15;
            maxDLVarInfo.Units = "h";
            maxDLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            sLDLVarInfo.Name = "sLDL";
            sLDLVarInfo.Description = "Daylength response of leaf production";
            sLDLVarInfo.MaxValue = 1;
            sLDLVarInfo.MinValue = 0;
            sLDLVarInfo.DefaultValue = 0.85;
            sLDLVarInfo.Units = "leaf h-1";
            sLDLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            ignoreGrainMaturationVarInfo.Name = "ignoreGrainMaturation";
            ignoreGrainMaturationVarInfo.Description = "true to ignore grain maturation";
            ignoreGrainMaturationVarInfo.MaxValue = false;
            ignoreGrainMaturationVarInfo.MinValue = false;
            ignoreGrainMaturationVarInfo.DefaultValue = false;
            ignoreGrainMaturationVarInfo.Units = "";
            ignoreGrainMaturationVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Boolean");

            pHEADANTHVarInfo.Name = "pHEADANTH";
            pHEADANTHVarInfo.Description = "Number of phyllochron between heading and anthesiss";
            pHEADANTHVarInfo.MaxValue = 1000;
            pHEADANTHVarInfo.MinValue = 0;
            pHEADANTHVarInfo.DefaultValue = 1;
            pHEADANTHVarInfo.Units = "";
            pHEADANTHVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            choosePhyllUseVarInfo.Name = "choosePhyllUse";
            choosePhyllUseVarInfo.Description = "Switch to choose the type of phyllochron calculation to be used";
            choosePhyllUseVarInfo.MaxValue = "Default";
            choosePhyllUseVarInfo.MinValue = "Default";
            choosePhyllUseVarInfo.DefaultValue = "Default";
            choosePhyllUseVarInfo.Units = "";
            choosePhyllUseVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("String");

            pVarInfo.Name = "p";
            pVarInfo.Description = "Phyllochron (Varietal parameter)";
            pVarInfo.MaxValue = 1000;
            pVarInfo.MinValue = 0;
            pVarInfo.DefaultValue = 120;
            pVarInfo.Units = "°C d leaf-1";
            pVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        private static VarInfo _isVernalizableVarInfo = new VarInfo();
        public static VarInfo isVernalizableVarInfo
        {
            get { return _isVernalizableVarInfo;} 
        }

        private static VarInfo _dseVarInfo = new VarInfo();
        public static VarInfo dseVarInfo
        {
            get { return _dseVarInfo;} 
        }

        private static VarInfo _pFLLAnthVarInfo = new VarInfo();
        public static VarInfo pFLLAnthVarInfo
        {
            get { return _pFLLAnthVarInfo;} 
        }

        private static VarInfo _dcdVarInfo = new VarInfo();
        public static VarInfo dcdVarInfo
        {
            get { return _dcdVarInfo;} 
        }

        private static VarInfo _dgfVarInfo = new VarInfo();
        public static VarInfo dgfVarInfo
        {
            get { return _dgfVarInfo;} 
        }

        private static VarInfo _degfmVarInfo = new VarInfo();
        public static VarInfo degfmVarInfo
        {
            get { return _degfmVarInfo;} 
        }

        private static VarInfo _maxDLVarInfo = new VarInfo();
        public static VarInfo maxDLVarInfo
        {
            get { return _maxDLVarInfo;} 
        }

        private static VarInfo _sLDLVarInfo = new VarInfo();
        public static VarInfo sLDLVarInfo
        {
            get { return _sLDLVarInfo;} 
        }

        private static VarInfo _ignoreGrainMaturationVarInfo = new VarInfo();
        public static VarInfo ignoreGrainMaturationVarInfo
        {
            get { return _ignoreGrainMaturationVarInfo;} 
        }

        private static VarInfo _pHEADANTHVarInfo = new VarInfo();
        public static VarInfo pHEADANTHVarInfo
        {
            get { return _pHEADANTHVarInfo;} 
        }

        private static VarInfo _choosePhyllUseVarInfo = new VarInfo();
        public static VarInfo choosePhyllUseVarInfo
        {
            get { return _choosePhyllUseVarInfo;} 
        }

        private static VarInfo _pVarInfo = new VarInfo();
        public static VarInfo pVarInfo
        {
            get { return _pVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber.CurrentValue=s.finalLeafNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase.CurrentValue=s.phase;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared.CurrentValue=s.hasLastPrimordiumAppeared;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r28 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber);
                if(r28.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber.ValueType)){prc.AddCondition(r28);}
                RangeBasedCondition r29 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase);
                if(r29.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase.ValueType)){prc.AddCondition(r29);}
                RangeBasedCondition r30 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared);
                if(r30.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared.ValueType)){prc.AddCondition(r30);}
                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.Phenology, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT.CurrentValue=a.cumulTT;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.CurrentValue=s.leafNumber;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_39.CurrentValue=a.cumulTTFromZC_39;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.isMomentRegistredZC_39.CurrentValue=s.isMomentRegistredZC_39;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI.CurrentValue=a.gAI;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.grainCumulTT.CurrentValue=a.grainCumulTT;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength.CurrentValue=a.dayLength;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog.CurrentValue=s.vernaprog;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber.CurrentValue=s.minFinalNumber;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll.CurrentValue=a.fixPhyll;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase.CurrentValue=s.phase;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_91.CurrentValue=a.cumulTTFromZC_91;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron.CurrentValue=s.phyllochron;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared.CurrentValue=s.hasLastPrimordiumAppeared;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber.CurrentValue=s.finalLeafNumber;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_39);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_39.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.isMomentRegistredZC_39);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.isMomentRegistredZC_39.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI.ValueType)){prc.AddCondition(r5);}
                RangeBasedCondition r6 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.grainCumulTT);
                if(r6.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.grainCumulTT.ValueType)){prc.AddCondition(r6);}
                RangeBasedCondition r7 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength);
                if(r7.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll.ValueType)){prc.AddCondition(r10);}
                RangeBasedCondition r11 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase);
                if(r11.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase.ValueType)){prc.AddCondition(r11);}
                RangeBasedCondition r12 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_91);
                if(r12.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_91.ValueType)){prc.AddCondition(r12);}
                RangeBasedCondition r13 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron);
                if(r13.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron.ValueType)){prc.AddCondition(r13);}
                RangeBasedCondition r14 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared);
                if(r14.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared.ValueType)){prc.AddCondition(r14);}
                RangeBasedCondition r15 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber);
                if(r15.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber.ValueType)){prc.AddCondition(r15);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("isVernalizable")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("dse")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pFLLAnth")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("dcd")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("dgf")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("degfm")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("maxDL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sLDL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("ignoreGrainMaturation")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pHEADANTH")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("choosePhyllUse")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("p")));
                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in strategy " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.Phenology, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SiriusQualityPhenology, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        private void CalculateModel(SiriusQualityPhenology.DomainClass.PhenologyState s, SiriusQualityPhenology.DomainClass.PhenologyState s1, SiriusQualityPhenology.DomainClass.PhenologyRate r, SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a, SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            double cumulTT = a.cumulTT;
            double leafNumber_t1 = s1.leafNumber;
            double cumulTTFromZC_39 = a.cumulTTFromZC_39;
            int isMomentRegistredZC_39 = s.isMomentRegistredZC_39;
            double gAI = a.gAI;
            double grainCumulTT = a.grainCumulTT;
            double dayLength = a.dayLength;
            double vernaprog = s.vernaprog;
            double minFinalNumber = s.minFinalNumber;
            double fixPhyll = a.fixPhyll;
            double phase_t1 = s1.phase;
            double cumulTTFromZC_91 = a.cumulTTFromZC_91;
            double phyllochron = s.phyllochron;
            int hasLastPrimordiumAppeared_t1 = s1.hasLastPrimordiumAppeared;
            double finalLeafNumber_t1 = s1.finalLeafNumber;
            double finalLeafNumber;
            double phase;
            int hasLastPrimordiumAppeared;
            double ttFromLastLeafToHeading;
            double appFLN;
            double localDegfm;
            double ttFromLastLeafToAnthesis;
            hasLastPrimordiumAppeared = hasLastPrimordiumAppeared_t1;
            finalLeafNumber = finalLeafNumber_t1;
            phase = phase_t1;
            if (phase_t1 >= 0.0d && phase_t1 < 1.0d)
            {
                if (cumulTT >= dse)
                {
                    phase = 1.0d;
                }
                else
                {
                    phase = phase_t1;
                }
            }
            else if ( phase_t1 >= 1.0d && phase_t1 < 2.0d)
            {
                if (isVernalizable == 1 && vernaprog >= 1.0d || isVernalizable == 0)
                {
                    if (dayLength > maxDL)
                    {
                        finalLeafNumber = minFinalNumber;
                        hasLastPrimordiumAppeared = 1;
                    }
                    else
                    {
                        appFLN = minFinalNumber + (sLDL * (maxDL - dayLength));
                        if (appFLN / 2.0d <= leafNumber_t1)
                        {
                            finalLeafNumber = appFLN;
                            hasLastPrimordiumAppeared = 1;
                        }
                        else
                        {
                            phase = phase_t1;
                        }
                    }
                    if (hasLastPrimordiumAppeared == 1)
                    {
                        phase = 2.0d;
                    }
                }
                else
                {
                    phase = phase_t1;
                }
            }
            else if ( phase_t1 >= 2.0d && phase_t1 < 4.0d)
            {
                if (isMomentRegistredZC_39 == 1)
                {
                    if (phase_t1 < 3.0d)
                    {
                        ttFromLastLeafToHeading = 0.0d;
                        if (choosePhyllUse == "Default")
                        {
                            ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * fixPhyll;
                        }
                        else if ( choosePhyllUse == "PTQ")
                        {
                            ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron;
                        }
                        else if ( choosePhyllUse == "Test")
                        {
                            ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p;
                        }
                        if (cumulTTFromZC_39 >= ttFromLastLeafToHeading)
                        {
                            phase = 3.0d;
                        }
                        else
                        {
                            phase = phase_t1;
                        }
                    }
                    else
                    {
                        phase = phase_t1;
                    }
                    ttFromLastLeafToAnthesis = 0.0d;
                    if (choosePhyllUse == "Default")
                    {
                        ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll;
                    }
                    else if ( choosePhyllUse == "PTQ")
                    {
                        ttFromLastLeafToAnthesis = pFLLAnth * phyllochron;
                    }
                    else if ( choosePhyllUse == "Test")
                    {
                        ttFromLastLeafToAnthesis = pFLLAnth * p;
                    }
                    if (cumulTTFromZC_39 >= ttFromLastLeafToAnthesis)
                    {
                        phase = 4.0d;
                    }
                }
                else
                {
                    phase = phase_t1;
                }
            }
            else if ( phase_t1 == 4.0d)
            {
                if (grainCumulTT >= dcd)
                {
                    phase = 4.5d;
                }
                else
                {
                    phase = phase_t1;
                }
            }
            else if ( phase_t1 == 4.5d)
            {
                if (grainCumulTT >= dgf || gAI <= 0.0d)
                {
                    phase = 5.0d;
                }
                else
                {
                    phase = phase_t1;
                }
            }
            else if ( phase_t1 >= 5.0d && phase_t1 < 6.0d)
            {
                localDegfm = degfm;
                if (ignoreGrainMaturation)
                {
                    localDegfm = -1.0d;
                }
                if (cumulTTFromZC_91 >= localDegfm)
                {
                    phase = 6.0d;
                }
                else
                {
                    phase = phase_t1;
                }
            }
            else if ( phase_t1 >= 6.0d && phase_t1 < 7.0d)
            {
                phase = phase_t1;
            }
            s.finalLeafNumber= finalLeafNumber;
            s.phase= phase;
            s.hasLastPrimordiumAppeared= hasLastPrimordiumAppeared;
        }

    }
}
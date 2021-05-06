
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
    public class VernalizationProgress : IStrategySiriusQualityPhenology
    {
        public VernalizationProgress()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 0.0;
            v1.Description = "Minimum temperature for vernalization to occur";
            v1.Id = 0;
            v1.MaxValue = 60;
            v1.MinValue = -20;
            v1.Name = "minTvern";
            v1.Size = 1;
            v1.Units = "°C";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue =  11.0;
            v2.Description = "Intermediate temperature for vernalization to occur";
            v2.Id = 0;
            v2.MaxValue = 60;
            v2.MinValue = -20;
            v2.Name = "intTvern";
            v2.Size = 1;
            v2.Units = "°C";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue =  0.015;
            v3.Description = "Response of vernalization rate to temperature";
            v3.Id = 0;
            v3.MaxValue = 1;
            v3.MinValue = 0;
            v3.Name = "vAI";
            v3.Size = 1;
            v3.Units = "d-1 °C-1";
            v3.URL = "";
            v3.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v3);
            VarInfo v4 = new VarInfo();
            v4.DefaultValue = 0.01;
            v4.Description = "Vernalization rate at 0°C";
            v4.Id = 0;
            v4.MaxValue = 1;
            v4.MinValue = 0;
            v4.Name = "vBEE";
            v4.Size = 1;
            v4.Units = "d-1";
            v4.URL = "";
            v4.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v4.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v4);
            VarInfo v5 = new VarInfo();
            v5.DefaultValue = 8.0;
            v5.Description = "Threshold daylength below which it does influence vernalization rate";
            v5.Id = 0;
            v5.MaxValue = 24;
            v5.MinValue = 12;
            v5.Name = "minDL";
            v5.Size = 1;
            v5.Units = "h";
            v5.URL = "";
            v5.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v5.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v5);
            VarInfo v6 = new VarInfo();
            v6.DefaultValue = 15.0;
            v6.Description = "Saturating photoperiod above which final leaf number is not influenced by daylength";
            v6.Id = 0;
            v6.MaxValue = 24;
            v6.MinValue = 0;
            v6.Name = "maxDL";
            v6.Size = 1;
            v6.Units = "h";
            v6.URL = "";
            v6.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v6.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v6);
            VarInfo v7 = new VarInfo();
            v7.DefaultValue =  23.0;
            v7.Description = "Maximum temperature for vernalization to occur";
            v7.Id = 0;
            v7.MaxValue = 60;
            v7.MinValue = -20;
            v7.Name = "maxTvern";
            v7.Size = 1;
            v7.Units = "°C";
            v7.URL = "";
            v7.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v7.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v7);
            VarInfo v8 = new VarInfo();
            v8.DefaultValue = 4.0;
            v8.Description = "Number of primorida in the apex at emergence";
            v8.Id = 0;
            v8.MaxValue = 24;
            v8.MinValue = 0;
            v8.Name = "pNini";
            v8.Size = 1;
            v8.Units = "primordia";
            v8.URL = "";
            v8.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v8.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v8);
            VarInfo v9 = new VarInfo();
            v9.DefaultValue = 24.0;
            v9.Description = "Absolute maximum leaf number";
            v9.Id = 0;
            v9.MaxValue = 25;
            v9.MinValue = 0;
            v9.Name = "aMXLFNO";
            v9.Size = 1;
            v9.Units = "leaf";
            v9.URL = "";
            v9.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v9.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v9);
            VarInfo v10 = new VarInfo();
            v10.DefaultValue = 1;
            v10.Description = "true if the plant is vernalizable";
            v10.Id = 0;
            v10.MaxValue = 1;
            v10.MinValue = 0;
            v10.Name = "isVernalizable";
            v10.Size = 1;
            v10.Units = "";
            v10.URL = "";
            v10.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v10.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
            _parameters0_0.Add(v10);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd1.PropertyName = "dayLength";
            pd1.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd2.PropertyName = "deltaTT";
            pd2.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd3.PropertyName = "cumulTT";
            pd3.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd4.PropertyName = "leafNumber";
            pd4.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd5.PropertyName = "calendarMoments";
            pd5.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
            _inputs0_0.Add(pd5);
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd6.PropertyName = "calendarDates";
            pd6.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
            _inputs0_0.Add(pd6);
            PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd7.PropertyName = "calendarCumuls";
            pd7.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
            _inputs0_0.Add(pd7);
            PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd8.PropertyName = "vernaprog";
            pd8.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog);
            _inputs0_0.Add(pd8);
            PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd9.PropertyName = "currentdate";
            pd9.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate);
            _inputs0_0.Add(pd9);
            PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd10.PropertyName = "minFinalNumber";
            pd10.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber);
            _inputs0_0.Add(pd10);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd11 = new PropertyDescription();
            pd11.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd11.PropertyName = "vernaprog";
            pd11.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog).ValueType.TypeForCurrentValue;
            pd11.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog);
            _outputs0_0.Add(pd11);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd12 = new PropertyDescription();
            pd12.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd12.PropertyName = "minFinalNumber";
            pd12.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber).ValueType.TypeForCurrentValue;
            pd12.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber);
            _outputs0_0.Add(pd12);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd13 = new PropertyDescription();
            pd13.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd13.PropertyName = "calendarMoments";
            pd13.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments).ValueType.TypeForCurrentValue;
            pd13.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
            _outputs0_0.Add(pd13);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd14 = new PropertyDescription();
            pd14.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd14.PropertyName = "calendarDates";
            pd14.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates).ValueType.TypeForCurrentValue;
            pd14.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
            _outputs0_0.Add(pd14);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd15 = new PropertyDescription();
            pd15.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd15.PropertyName = "calendarCumuls";
            pd15.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls).ValueType.TypeForCurrentValue;
            pd15.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
            _outputs0_0.Add(pd15);
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
            get { return "Calculate progress (VernaProg) towards vernalization, but there         			is no vernalization below minTvern         			and above maxTvern . The maximum value of VernaProg is 1.        			Progress towards full vernalization is a linear function of shoot         			temperature (soil temperature until leaf # reach MaxLeafSoil and then        			 canopy temperature)    	" ;}
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

        public double minTvern
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("minTvern");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'minTvern' not found (or found null) in strategy 'VernalizationProgress'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("minTvern");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'minTvern' not found in strategy 'VernalizationProgress'");
            }
        }
        public double intTvern
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("intTvern");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'intTvern' not found (or found null) in strategy 'VernalizationProgress'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("intTvern");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'intTvern' not found in strategy 'VernalizationProgress'");
            }
        }
        public double vAI
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("vAI");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'vAI' not found (or found null) in strategy 'VernalizationProgress'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("vAI");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'vAI' not found in strategy 'VernalizationProgress'");
            }
        }
        public double vBEE
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("vBEE");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'vBEE' not found (or found null) in strategy 'VernalizationProgress'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("vBEE");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'vBEE' not found in strategy 'VernalizationProgress'");
            }
        }
        public double minDL
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("minDL");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'minDL' not found (or found null) in strategy 'VernalizationProgress'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("minDL");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'minDL' not found in strategy 'VernalizationProgress'");
            }
        }
        public double maxDL
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("maxDL");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'maxDL' not found (or found null) in strategy 'VernalizationProgress'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("maxDL");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'maxDL' not found in strategy 'VernalizationProgress'");
            }
        }
        public double maxTvern
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("maxTvern");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'maxTvern' not found (or found null) in strategy 'VernalizationProgress'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("maxTvern");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'maxTvern' not found in strategy 'VernalizationProgress'");
            }
        }
        public double pNini
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("pNini");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'pNini' not found (or found null) in strategy 'VernalizationProgress'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("pNini");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'pNini' not found in strategy 'VernalizationProgress'");
            }
        }
        public double aMXLFNO
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("aMXLFNO");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'aMXLFNO' not found (or found null) in strategy 'VernalizationProgress'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("aMXLFNO");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'aMXLFNO' not found in strategy 'VernalizationProgress'");
            }
        }
        public int isVernalizable
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("isVernalizable");
                if (vi != null && vi.CurrentValue!=null) return (int)vi.CurrentValue ;
                else throw new Exception("Parameter 'isVernalizable' not found (or found null) in strategy 'VernalizationProgress'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("isVernalizable");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'isVernalizable' not found in strategy 'VernalizationProgress'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            minTvernVarInfo.Name = "minTvern";
            minTvernVarInfo.Description = "Minimum temperature for vernalization to occur";
            minTvernVarInfo.MaxValue = 60;
            minTvernVarInfo.MinValue = -20;
            minTvernVarInfo.DefaultValue = 0.0;
            minTvernVarInfo.Units = "°C";
            minTvernVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            intTvernVarInfo.Name = "intTvern";
            intTvernVarInfo.Description = "Intermediate temperature for vernalization to occur";
            intTvernVarInfo.MaxValue = 60;
            intTvernVarInfo.MinValue = -20;
            intTvernVarInfo.DefaultValue =  11.0;
            intTvernVarInfo.Units = "°C";
            intTvernVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            vAIVarInfo.Name = "vAI";
            vAIVarInfo.Description = "Response of vernalization rate to temperature";
            vAIVarInfo.MaxValue = 1;
            vAIVarInfo.MinValue = 0;
            vAIVarInfo.DefaultValue =  0.015;
            vAIVarInfo.Units = "d-1 °C-1";
            vAIVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            vBEEVarInfo.Name = "vBEE";
            vBEEVarInfo.Description = "Vernalization rate at 0°C";
            vBEEVarInfo.MaxValue = 1;
            vBEEVarInfo.MinValue = 0;
            vBEEVarInfo.DefaultValue = 0.01;
            vBEEVarInfo.Units = "d-1";
            vBEEVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            minDLVarInfo.Name = "minDL";
            minDLVarInfo.Description = "Threshold daylength below which it does influence vernalization rate";
            minDLVarInfo.MaxValue = 24;
            minDLVarInfo.MinValue = 12;
            minDLVarInfo.DefaultValue = 8.0;
            minDLVarInfo.Units = "h";
            minDLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            maxDLVarInfo.Name = "maxDL";
            maxDLVarInfo.Description = "Saturating photoperiod above which final leaf number is not influenced by daylength";
            maxDLVarInfo.MaxValue = 24;
            maxDLVarInfo.MinValue = 0;
            maxDLVarInfo.DefaultValue = 15.0;
            maxDLVarInfo.Units = "h";
            maxDLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            maxTvernVarInfo.Name = "maxTvern";
            maxTvernVarInfo.Description = "Maximum temperature for vernalization to occur";
            maxTvernVarInfo.MaxValue = 60;
            maxTvernVarInfo.MinValue = -20;
            maxTvernVarInfo.DefaultValue =  23.0;
            maxTvernVarInfo.Units = "°C";
            maxTvernVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pNiniVarInfo.Name = "pNini";
            pNiniVarInfo.Description = "Number of primorida in the apex at emergence";
            pNiniVarInfo.MaxValue = 24;
            pNiniVarInfo.MinValue = 0;
            pNiniVarInfo.DefaultValue = 4.0;
            pNiniVarInfo.Units = "primordia";
            pNiniVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            aMXLFNOVarInfo.Name = "aMXLFNO";
            aMXLFNOVarInfo.Description = "Absolute maximum leaf number";
            aMXLFNOVarInfo.MaxValue = 25;
            aMXLFNOVarInfo.MinValue = 0;
            aMXLFNOVarInfo.DefaultValue = 24.0;
            aMXLFNOVarInfo.Units = "leaf";
            aMXLFNOVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            isVernalizableVarInfo.Name = "isVernalizable";
            isVernalizableVarInfo.Description = "true if the plant is vernalizable";
            isVernalizableVarInfo.MaxValue = 1;
            isVernalizableVarInfo.MinValue = 0;
            isVernalizableVarInfo.DefaultValue = 1;
            isVernalizableVarInfo.Units = "";
            isVernalizableVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
        }

        private static VarInfo _minTvernVarInfo = new VarInfo();
        public static VarInfo minTvernVarInfo
        {
            get { return _minTvernVarInfo;} 
        }

        private static VarInfo _intTvernVarInfo = new VarInfo();
        public static VarInfo intTvernVarInfo
        {
            get { return _intTvernVarInfo;} 
        }

        private static VarInfo _vAIVarInfo = new VarInfo();
        public static VarInfo vAIVarInfo
        {
            get { return _vAIVarInfo;} 
        }

        private static VarInfo _vBEEVarInfo = new VarInfo();
        public static VarInfo vBEEVarInfo
        {
            get { return _vBEEVarInfo;} 
        }

        private static VarInfo _minDLVarInfo = new VarInfo();
        public static VarInfo minDLVarInfo
        {
            get { return _minDLVarInfo;} 
        }

        private static VarInfo _maxDLVarInfo = new VarInfo();
        public static VarInfo maxDLVarInfo
        {
            get { return _maxDLVarInfo;} 
        }

        private static VarInfo _maxTvernVarInfo = new VarInfo();
        public static VarInfo maxTvernVarInfo
        {
            get { return _maxTvernVarInfo;} 
        }

        private static VarInfo _pNiniVarInfo = new VarInfo();
        public static VarInfo pNiniVarInfo
        {
            get { return _pNiniVarInfo;} 
        }

        private static VarInfo _aMXLFNOVarInfo = new VarInfo();
        public static VarInfo aMXLFNOVarInfo
        {
            get { return _aMXLFNOVarInfo;} 
        }

        private static VarInfo _isVernalizableVarInfo = new VarInfo();
        public static VarInfo isVernalizableVarInfo
        {
            get { return _isVernalizableVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog.CurrentValue=s.vernaprog;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber.CurrentValue=s.minFinalNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.CurrentValue=s.calendarMoments;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.CurrentValue=s.calendarDates;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.CurrentValue=s.calendarCumuls;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r21 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog);
                if(r21.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog.ValueType)){prc.AddCondition(r21);}
                RangeBasedCondition r22 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber);
                if(r22.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber.ValueType)){prc.AddCondition(r22);}
                RangeBasedCondition r23 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
                if(r23.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.ValueType)){prc.AddCondition(r23);}
                RangeBasedCondition r24 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
                if(r24.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.ValueType)){prc.AddCondition(r24);}
                RangeBasedCondition r25 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
                if(r25.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.ValueType)){prc.AddCondition(r25);}
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
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength.CurrentValue=a.dayLength;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT.CurrentValue=a.deltaTT;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT.CurrentValue=a.cumulTT;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.CurrentValue=s.leafNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.CurrentValue=s.calendarMoments;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.CurrentValue=s.calendarDates;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.CurrentValue=s.calendarCumuls;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog.CurrentValue=s.vernaprog;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate.CurrentValue=a.currentdate;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber.CurrentValue=s.minFinalNumber;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.ValueType)){prc.AddCondition(r5);}
                RangeBasedCondition r6 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
                if(r6.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.ValueType)){prc.AddCondition(r6);}
                RangeBasedCondition r7 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
                if(r7.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber.ValueType)){prc.AddCondition(r10);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("minTvern")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("intTvern")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("vAI")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("vBEE")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("minDL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("maxDL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("maxTvern")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pNini")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("aMXLFNO")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("isVernalizable")));
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
            double dayLength = a.dayLength;
            double deltaTT = a.deltaTT;
            double cumulTT = a.cumulTT;
            double leafNumber_t1 = s1.leafNumber;
            List<string> calendarMoments_t1 = s1.calendarMoments;
            List<DateTime> calendarDates_t1 = s1.calendarDates;
            List<double> calendarCumuls_t1 = s1.calendarCumuls;
            double vernaprog_t1 = s1.vernaprog;
            DateTime currentdate = a.currentdate;
            double minFinalNumber_t1 = s1.minFinalNumber;
            double vernaprog;
            double minFinalNumber;
            List<string> calendarMoments = new List<string>();
            List<DateTime> calendarDates = new List<DateTime>();
            List<double> calendarCumuls = new List<double>();
            double maxVernaProg;
            double dLverna;
            double primordno;
            double minLeafNumber;
            double potlfno;
            double tt;
            calendarMoments = new List<string>(calendarMoments_t1);
            calendarCumuls = new List<double>(calendarCumuls_t1);
            calendarDates = new List<DateTime>(calendarDates_t1);
            minFinalNumber = minFinalNumber_t1;
            vernaprog = vernaprog_t1;
            if (isVernalizable == 1 && vernaprog_t1 < 1.0d)
            {
                tt = deltaTT;
                if (tt >= minTvern && tt <= intTvern)
                {
                    vernaprog = vernaprog_t1 + (vAI * tt) + vBEE;
                }
                else
                {
                    vernaprog = vernaprog_t1;
                }
                if (tt > intTvern)
                {
                    maxVernaProg = vAI * intTvern + vBEE;
                    dLverna = Math.Max(minDL, Math.Min(maxDL, dayLength));
                    vernaprog = vernaprog + Math.Max(0.0d, maxVernaProg * (1.0d + ((intTvern - tt) / (maxTvern - intTvern) * ((dLverna - minDL) / (maxDL - minDL)))));
                }
                primordno = 2.0d * leafNumber_t1 + pNini;
                minLeafNumber = minFinalNumber_t1;
                if (vernaprog >= 1.0d || primordno >= aMXLFNO)
                {
                    minFinalNumber = Math.Max(primordno, minFinalNumber_t1);
                    calendarMoments.Add("EndVernalisation");
                    calendarCumuls.Add(cumulTT);
                    calendarDates.Add(currentdate);
                    vernaprog = Math.Max(1.0d, vernaprog);
                }
                else
                {
                    potlfno = aMXLFNO - ((aMXLFNO - minLeafNumber) * vernaprog);
                    if (primordno >= potlfno)
                    {
                        minFinalNumber = Math.Max((potlfno + primordno) / 2.0d, minFinalNumber_t1);
                        vernaprog = Math.Max(1.0d, vernaprog);
                        calendarMoments.Add("EndVernalisation");
                        calendarCumuls.Add(cumulTT);
                        calendarDates.Add(currentdate);
                    }
                }
            }
            s.vernaprog= vernaprog;
            s.minFinalNumber= minFinalNumber;
            s.calendarMoments= calendarMoments;
            s.calendarDates= calendarDates;
            s.calendarCumuls= calendarCumuls;
        }

    }
}
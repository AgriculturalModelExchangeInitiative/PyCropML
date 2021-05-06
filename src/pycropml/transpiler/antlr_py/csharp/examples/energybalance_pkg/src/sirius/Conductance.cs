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
using SiriusQualityEnergybalance.DomainClass;
namespace SiriusQualityEnergybalance.Strategies
{
    public class Conductance : IStrategySiriusQualityEnergybalance
    {
        public Conductance()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 0.42;
            v1.Description = "von Karman constant";
            v1.Id = 0;
            v1.MaxValue = 1;
            v1.MinValue = 0;
            v1.Name = "vonKarman";
            v1.Size = 1;
            v1.Units = "dimensionless";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 2;
            v2.Description = "reference height of wind and humidity measurements";
            v2.Id = 0;
            v2.MaxValue = 10;
            v2.MinValue = 0;
            v2.Name = "heightWeatherMeasurements";
            v2.Size = 1;
            v2.Units = "m";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = 0.13;
            v3.Description = "roughness length governing momentum transfer, FAO";
            v3.Id = 0;
            v3.MaxValue = 1;
            v3.MinValue = 0;
            v3.Name = "zm";
            v3.Size = 1;
            v3.Units = "m";
            v3.URL = "";
            v3.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v3);
            VarInfo v4 = new VarInfo();
            v4.DefaultValue = 0.013;
            v4.Description = "roughness length governing transfer of heat and vapour, FAO";
            v4.Id = 0;
            v4.MaxValue = 1;
            v4.MinValue = 0;
            v4.Name = "zh";
            v4.Size = 1;
            v4.Units = "m";
            v4.URL = "";
            v4.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v4.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v4);
            VarInfo v5 = new VarInfo();
            v5.DefaultValue = 0.67;
            v5.Description = "corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO";
            v5.Id = 0;
            v5.MaxValue = 1;
            v5.MinValue = 0;
            v5.Name = "d";
            v5.Size = 1;
            v5.Units = "dimensionless";
            v5.URL = "";
            v5.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v5.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v5);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliary);
            pd1.PropertyName = "plantHeight";
            pd1.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.plantHeight).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.plantHeight);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliary);
            pd2.PropertyName = "wind";
            pd2.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.wind).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.wind);
            _inputs0_0.Add(pd2);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceState);
            pd3.PropertyName = "conductance";
            pd3.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.conductance).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.conductance);
            _outputs0_0.Add(pd3);
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
            get { return  "The boundary layer conductance is expressed as the wind speed profile above the
            canopy and the canopy structure. The approach does not take into account buoyancy
            effects. 
        " ;}
        }

        public string URL
        {
            get { return  "" ;}
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
            _pd.Add("Creator", "Pierre Martre");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "INRA/LEPSE Montpellier");
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        public IEnumerable<Type> GetStrategyDomainClassesTypes()
        {
            return new List<Type>() {  typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceState), typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceRate), typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliary), typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceExogenous)};
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public double vonKarman
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("vonKarman");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'vonKarman' not found (or found null) in strategy 'Conductance'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'vonKarman' not found in strategy 'Conductance'");
            }
        }
        public double heightWeatherMeasurements
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("heightWeatherMeasurements");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'heightWeatherMeasurements' not found (or found null) in strategy 'Conductance'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'heightWeatherMeasurements' not found in strategy 'Conductance'");
            }
        }
        public double zm
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("zm");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'zm' not found (or found null) in strategy 'Conductance'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'zm' not found in strategy 'Conductance'");
            }
        }
        public double zh
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("zh");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'zh' not found (or found null) in strategy 'Conductance'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'zh' not found in strategy 'Conductance'");
            }
        }
        public double d
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("d");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'd' not found (or found null) in strategy 'Conductance'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'd' not found in strategy 'Conductance'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            vonKarmanVarInfo.Name = "vonKarman";
            vonKarmanVarInfo.Description = "von Karman constant";
            vonKarmanVarInfo.MaxValue = 1;
            vonKarmanVarInfo.MinValue = 0;
            vonKarmanVarInfo.DefaultValue = 0.42;
            vonKarmanVarInfo.Units = "dimensionless";
            vonKarmanVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            heightWeatherMeasurementsVarInfo.Name = "heightWeatherMeasurements";
            heightWeatherMeasurementsVarInfo.Description = "reference height of wind and humidity measurements";
            heightWeatherMeasurementsVarInfo.MaxValue = 10;
            heightWeatherMeasurementsVarInfo.MinValue = 0;
            heightWeatherMeasurementsVarInfo.DefaultValue = 2;
            heightWeatherMeasurementsVarInfo.Units = "m";
            heightWeatherMeasurementsVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            zmVarInfo.Name = "zm";
            zmVarInfo.Description = "roughness length governing momentum transfer, FAO";
            zmVarInfo.MaxValue = 1;
            zmVarInfo.MinValue = 0;
            zmVarInfo.DefaultValue = 0.13;
            zmVarInfo.Units = "m";
            zmVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            zhVarInfo.Name = "zh";
            zhVarInfo.Description = "roughness length governing transfer of heat and vapour, FAO";
            zhVarInfo.MaxValue = 1;
            zhVarInfo.MinValue = 0;
            zhVarInfo.DefaultValue = 0.013;
            zhVarInfo.Units = "m";
            zhVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            dVarInfo.Name = "d";
            dVarInfo.Description = "corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO";
            dVarInfo.MaxValue = 1;
            dVarInfo.MinValue = 0;
            dVarInfo.DefaultValue = 0.67;
            dVarInfo.Units = "dimensionless";
            dVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        private static VarInfo _vonKarmanVarInfo = new VarInfo();
        public static VarInfo vonKarmanVarInfo
        {
            get { return _vonKarmanVarInfo;} 
        }

        private static VarInfo _heightWeatherMeasurementsVarInfo = new VarInfo();
        public static VarInfo heightWeatherMeasurementsVarInfo
        {
            get { return _heightWeatherMeasurementsVarInfo;} 
        }

        private static VarInfo _zmVarInfo = new VarInfo();
        public static VarInfo zmVarInfo
        {
            get { return _zmVarInfo;} 
        }

        private static VarInfo _zhVarInfo = new VarInfo();
        public static VarInfo zhVarInfo
        {
            get { return _zhVarInfo;} 
        }

        private static VarInfo _dVarInfo = new VarInfo();
        public static VarInfo dVarInfo
        {
            get { return _dVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityEnergybalance.DomainClass.EnergybalanceState s,SiriusQualityEnergybalance.DomainClass.EnergybalanceState s1,SiriusQualityEnergybalance.DomainClass.EnergybalanceRate r,SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliary a,SiriusQualityEnergybalance.DomainClass.EnergybalanceExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.conductance.CurrentValue=s.conductance;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.conductance);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.conductance.ValueType)){prc.AddCondition(r8);}
                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.Energybalance, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualityEnergybalance.DomainClass.EnergybalanceState s,SiriusQualityEnergybalance.DomainClass.EnergybalanceState s1,SiriusQualityEnergybalance.DomainClass.EnergybalanceRate r,SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliary a,SiriusQualityEnergybalance.DomainClass.EnergybalanceExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.plantHeight.CurrentValue=a.plantHeight;
                SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.wind.CurrentValue=a.wind;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.plantHeight);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.plantHeight.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.wind);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.wind.ValueType)){prc.AddCondition(r2);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("vonKarman")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("heightWeatherMeasurements")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("zm")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("zh")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("d")));
                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in strategy " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.Energybalance, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SiriusQualityEnergybalance.DomainClass.EnergybalanceState s,SiriusQualityEnergybalance.DomainClass.EnergybalanceState s1,SiriusQualityEnergybalance.DomainClass.EnergybalanceRate r,SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliary a,SiriusQualityEnergybalance.DomainClass.EnergybalanceExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SiriusQualityEnergybalance, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        private void  CalculateModel(SiriusQualityEnergybalance.DomainClass.EnergybalanceState s, SiriusQualityEnergybalance.DomainClass.EnergybalanceState s1, SiriusQualityEnergybalance.DomainClass.EnergybalanceRate r, SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliary a, SiriusQualityEnergybalance.DomainClass.EnergybalanceExogenous ex)
        {
            double plantHeight = a.plantHeight;
            double wind = a.wind;
            double conductance;
            double h;
            h = Math.Max(10.0d, plantHeight) / 100.0d;
            conductance = wind * Math.Pow(vonKarman, 2) / (Math.Log((heightWeatherMeasurements - (d * h)) / (zm * h)) * Math.Log((heightWeatherMeasurements - (d * h)) / (zh * h)));
            s.conductance= conductance;
        }

    }
}
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
    public class Evapotranspiration : IStrategySiriusQualityEnergybalance
    {
        public Evapotranspiration()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 1;
            v1.Description = "if wind and vapour pressure are defined";
            v1.Id = 0;
            v1.MaxValue = 1;
            v1.MinValue = 0;
            v1.Name = "isWindVpDefined";
            v1.Size = 1;
            v1.Units = "";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Int");
            _parameters0_0.Add(v1);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceRate);
            pd1.PropertyName = "evapoTranspirationPriestlyTaylor";
            pd1.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspirationPriestlyTaylor).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspirationPriestlyTaylor);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceRate);
            pd2.PropertyName = "evapoTranspirationPenman";
            pd2.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspirationPenman).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspirationPenman);
            _inputs0_0.Add(pd2);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceRate);
            pd3.PropertyName = "evapoTranspiration";
            pd3.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspiration).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspiration);
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
            get { return  "According to the availability of wind and/or vapor pressure daily data, the
            SiriusQuality2 model calculates the evapotranspiration rate using the Penman (if wind
            and vapor pressure data are available) (Penman 1948) or the Priestly-Taylor
            (Priestley and Taylor 1972) method " ;}
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
            _pd.Add("Publisher", "INRA Montpellier");
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

        public int isWindVpDefined
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("isWindVpDefined");
                if (vi != null && vi.CurrentValue!=null) return (int)vi.CurrentValue ;
                else throw new Exception("Parameter 'isWindVpDefined' not found (or found null) in strategy 'Evapotranspiration'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'isWindVpDefined' not found in strategy 'Evapotranspiration'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            isWindVpDefinedVarInfo.Name = "isWindVpDefined";
            isWindVpDefinedVarInfo.Description = "if wind and vapour pressure are defined";
            isWindVpDefinedVarInfo.MaxValue = 1;
            isWindVpDefinedVarInfo.MinValue = 0;
            isWindVpDefinedVarInfo.DefaultValue = 1;
            isWindVpDefinedVarInfo.Units = "";
            isWindVpDefinedVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Int");
        }

        private static VarInfo _isWindVpDefinedVarInfo = new VarInfo();
        public static VarInfo isWindVpDefinedVarInfo
        {
            get { return _isWindVpDefinedVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityEnergybalance.DomainClass.EnergybalanceState s,SiriusQualityEnergybalance.DomainClass.EnergybalanceState s1,SiriusQualityEnergybalance.DomainClass.EnergybalanceRate r,SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliary a,SiriusQualityEnergybalance.DomainClass.EnergybalanceExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspiration.CurrentValue=r.evapoTranspiration;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.evapoTranspiration);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspiration.ValueType)){prc.AddCondition(r4);}
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
                SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspirationPriestlyTaylor.CurrentValue=r.evapoTranspirationPriestlyTaylor;
                SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspirationPenman.CurrentValue=r.evapoTranspirationPenman;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.evapoTranspirationPriestlyTaylor);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspirationPriestlyTaylor.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.evapoTranspirationPenman);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspirationPenman.ValueType)){prc.AddCondition(r2);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("isWindVpDefined")));
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
            double evapoTranspirationPriestlyTaylor = r.evapoTranspirationPriestlyTaylor;
            double evapoTranspirationPenman = r.evapoTranspirationPenman;
            double evapoTranspiration;
            if (isWindVpDefined == 1)
            {
                evapoTranspiration = evapoTranspirationPenman;
            }
            else
            {
                evapoTranspiration = evapoTranspirationPriestlyTaylor;
            }
            r.evapoTranspiration = evapoTranspiration;
        }

    }
}
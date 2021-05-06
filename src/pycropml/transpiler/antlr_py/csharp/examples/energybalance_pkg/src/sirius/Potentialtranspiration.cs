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
    public class Potentialtranspiration : IStrategySiriusQualityEnergybalance
    {
        public Potentialtranspiration()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 0.9983;
            v1.Description = "plant cover factor";
            v1.Id = 0;
            v1.MaxValue = 1;
            v1.MinValue = 0;
            v1.Name = "tau";
            v1.Size = 1;
            v1.Units = "";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v1);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceRate);
            pd1.PropertyName = "evapoTranspiration";
            pd1.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspiration).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspiration);
            _inputs0_0.Add(pd1);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceRate);
            pd2.PropertyName = "potentialTranspiration";
            pd2.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.potentialTranspiration).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.potentialTranspiration);
            _outputs0_0.Add(pd2);
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
            get { return  "SiriusQuality2 uses availability of water from the soil reservoir as a method to restrict
                    transpiration as soil moisture is depleted " ;}
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

        public double tau
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("tau");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'tau' not found (or found null) in strategy 'Potentialtranspiration'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'tau' not found in strategy 'Potentialtranspiration'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            tauVarInfo.Name = "tau";
            tauVarInfo.Description = "plant cover factor";
            tauVarInfo.MaxValue = 1;
            tauVarInfo.MinValue = 0;
            tauVarInfo.DefaultValue = 0.9983;
            tauVarInfo.Units = "";
            tauVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        private static VarInfo _tauVarInfo = new VarInfo();
        public static VarInfo tauVarInfo
        {
            get { return _tauVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityEnergybalance.DomainClass.EnergybalanceState s,SiriusQualityEnergybalance.DomainClass.EnergybalanceState s1,SiriusQualityEnergybalance.DomainClass.EnergybalanceRate r,SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliary a,SiriusQualityEnergybalance.DomainClass.EnergybalanceExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.potentialTranspiration.CurrentValue=r.potentialTranspiration;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.potentialTranspiration);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.potentialTranspiration.ValueType)){prc.AddCondition(r3);}
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
                SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspiration.CurrentValue=r.evapoTranspiration;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.evapoTranspiration);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.evapoTranspiration.ValueType)){prc.AddCondition(r1);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("tau")));
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
            double evapoTranspiration = r.evapoTranspiration;
            double potentialTranspiration;
            potentialTranspiration = evapoTranspiration * (1.0d - tau);
            r.potentialTranspiration = potentialTranspiration;
        }

    }
}
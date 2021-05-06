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
    public class Cropheatflux : IStrategySiriusQualityEnergybalance
    {
        public Cropheatflux()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliary);
            pd1.PropertyName = "netRadiationEquivalentEvaporation";
            pd1.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.netRadiationEquivalentEvaporation).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.netRadiationEquivalentEvaporation);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceRate);
            pd2.PropertyName = "soilHeatFlux";
            pd2.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.soilHeatFlux).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.soilHeatFlux);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceRate);
            pd3.PropertyName = "potentialTranspiration";
            pd3.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.potentialTranspiration).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.potentialTranspiration);
            _inputs0_0.Add(pd3);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityEnergybalance.DomainClass.EnergybalanceRate);
            pd4.PropertyName = "cropHeatFlux";
            pd4.PropertyType = (SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.cropHeatFlux).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.cropHeatFlux);
            _outputs0_0.Add(pd4);
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
            get { return  "It is calculated from net Radiation, soil heat flux and potential transpiration " ;}
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


        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {
        }

        public string TestPostConditions(SiriusQualityEnergybalance.DomainClass.EnergybalanceState s,SiriusQualityEnergybalance.DomainClass.EnergybalanceState s1,SiriusQualityEnergybalance.DomainClass.EnergybalanceRate r,SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliary a,SiriusQualityEnergybalance.DomainClass.EnergybalanceExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.cropHeatFlux.CurrentValue=r.cropHeatFlux;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.cropHeatFlux);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.cropHeatFlux.ValueType)){prc.AddCondition(r4);}
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
                SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.netRadiationEquivalentEvaporation.CurrentValue=a.netRadiationEquivalentEvaporation;
                SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.soilHeatFlux.CurrentValue=r.soilHeatFlux;
                SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.potentialTranspiration.CurrentValue=r.potentialTranspiration;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.netRadiationEquivalentEvaporation);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceAuxiliaryVarInfo.netRadiationEquivalentEvaporation.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.soilHeatFlux);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.soilHeatFlux.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityEnergybalance.DomainClass.EnergybalanceStateVarInfo.potentialTranspiration);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergybalance.DomainClass.EnergybalanceRateVarInfo.potentialTranspiration.ValueType)){prc.AddCondition(r3);}
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
            double netRadiationEquivalentEvaporation = a.netRadiationEquivalentEvaporation;
            double soilHeatFlux = r.soilHeatFlux;
            double potentialTranspiration = r.potentialTranspiration;
            double cropHeatFlux;
            cropHeatFlux = netRadiationEquivalentEvaporation - soilHeatFlux - potentialTranspiration;
            r.cropHeatFlux = cropHeatFlux;
        }

    }
}
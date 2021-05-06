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
namespace SiriusQualityEnergybalance
{
    public class Soilevaporation : IStrategySiriusQualityEnergybalance
    {
    #region Constructor
        public Soilevaporation()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceState);
            pd1.PropertyName = "diffusionLimitedEvaporation";
            pd1.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceStateVarInfo.diffusionLimitedEvaporation)).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceStateVarInfo.diffusionLimitedEvaporation);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceState);
            pd2.PropertyName = "energyLimitedEvaporation";
            pd2.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceStateVarInfo.energyLimitedEvaporation)).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceStateVarInfo.energyLimitedEvaporation);
            _inputs0_0.Add(pd2);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd3.PropertyName = "soilEvaporation";
            pd3.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.soilEvaporation)).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.soilEvaporation);
            _outputs0_0.Add(pd3);
            mo0_0.Outputs=_outputs0_0;
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.


        public void Estimate(SiriusQualityEnergybalance.EnergybalanceState s,SiriusQualityEnergybalance.Energybalance s1,SiriusQualityEnergybalance.EnergybalanceRAte r,SiriusQualityEnergybalance.EnergybalanceAuxiliary a,SiriusQualityEnergybalance.EnergybalanceExogenous ex,CRA.AgroManagement.ActEvents actevents)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex)
            }
            catch (Exception exception)
            {
                string msg = "Error in component SiriusQualityEnergybalance, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }
        private void  CalculateModel(SiriusQualityEnergybalance.EnergybalanceState s, SiriusQualityEnergybalance.EnergybalanceState s1, SiriusQualityEnergybalance.EnergybalanceRate r, SiriusQualityEnergybalance.EnergybalanceAuxiliary a, SiriusQualityEnergybalance.EnergybalanceExogenous ex)
        {
            double diffusionLimitedEvaporation = s.diffusionLimitedEvaporation;
            double energyLimitedEvaporation = s.energyLimitedEvaporation;
            double soilEvaporation;
            soilEvaporation = Math.Min(diffusionLimitedEvaporation, energyLimitedEvaporation);
            a.soilEvaporation= soilEvaporation;
        }
    }
}
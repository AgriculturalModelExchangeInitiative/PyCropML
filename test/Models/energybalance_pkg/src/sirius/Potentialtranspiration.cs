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
    public class Potentialtranspiration : IStrategySiriusQualityEnergybalance
    {
    #region Constructor
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
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v1);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceRate);
            pd1.PropertyName = "evapoTranspiration";
            pd1.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceRateVarInfo.evapoTranspiration)).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceRateVarInfo.evapoTranspiration);
            _inputs0_0.Add(pd1);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceRate);
            pd2.PropertyName = "potentialTranspiration";
            pd2.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceRateVarInfo.potentialTranspiration)).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceRateVarInfo.potentialTranspiration);
            _outputs0_0.Add(pd2);
            mo0_0.Outputs=_outputs0_0;
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
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
            double evapoTranspiration = r.evapoTranspiration;
            double potentialTranspiration;
            potentialTranspiration = evapoTranspiration * (1.0d - tau);
            r.potentialTranspiration = potentialTranspiration;
        }
    }
}
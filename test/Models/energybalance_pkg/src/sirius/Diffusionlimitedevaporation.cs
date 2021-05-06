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
    public class Diffusionlimitedevaporation : IStrategySiriusQualityEnergybalance
    {
    #region Constructor
        public Diffusionlimitedevaporation()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 4.2;
            v1.Description = "soil Diffusion Constant";
            v1.Id = 0;
            v1.MaxValue = 10;
            v1.MinValue = 0;
            v1.Name = "soilDiffusionConstant";
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
            pd1.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd1.PropertyName = "deficitOnTopLayers";
            pd1.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.deficitOnTopLayers)).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.deficitOnTopLayers);
            _inputs0_0.Add(pd1);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceState);
            pd2.PropertyName = "diffusionLimitedEvaporation";
            pd2.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceStateVarInfo.diffusionLimitedEvaporation)).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceStateVarInfo.diffusionLimitedEvaporation);
            _outputs0_0.Add(pd2);
            mo0_0.Outputs=_outputs0_0;
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public double soilDiffusionConstant
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("soilDiffusionConstant");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'soilDiffusionConstant' not found (or found null) in strategy 'Diffusionlimitedevaporation'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'soilDiffusionConstant' not found in strategy 'Diffusionlimitedevaporation'");
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
            double deficitOnTopLayers = a.deficitOnTopLayers;
            double diffusionLimitedEvaporation;
            if (deficitOnTopLayers / 1000.0d <= 0.0d)
            {
                diffusionLimitedEvaporation = 8.3d * 1000.0d;
            }
            else
            {
                if (deficitOnTopLayers / 1000.0d < 25.0d)
                {
                    diffusionLimitedEvaporation = 2.0d * soilDiffusionConstant * soilDiffusionConstant / (deficitOnTopLayers / 1000.0d) * 1000.0d;
                }
                else
                {
                    diffusionLimitedEvaporation = 0.0d;
                }
            }
            s.diffusionLimitedEvaporation= diffusionLimitedEvaporation;
        }
    }
}
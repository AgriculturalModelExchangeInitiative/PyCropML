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
    public class Canopytemperature : IStrategySiriusQualityEnergybalance
    {
    #region Constructor
        public Canopytemperature()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 2.454;
            v1.Description = "latent heat of vaporization of water";
            v1.Id = 0;
            v1.MaxValue = 10;
            v1.MinValue = 0;
            v1.Name = "lambdaV";
            v1.Size = 1;
            v1.Units = "MJ/kg";
            v1.URL = "";
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 1.225;
            v2.Description = "Density of air";
            v2.Id = 0;
            v2.MaxValue = None;
            v2.MinValue = None;
            v2.Name = "rhoDensityAir";
            v2.Size = 1;
            v2.Units = "kg/m**3";
            v2.URL = "";
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = 0.00101;
            v3.Description = "Specific heat capacity of dry air";
            v3.Id = 0;
            v3.MaxValue = None;
            v3.MinValue = None;
            v3.Name = "specificHeatCapacityAir";
            v3.Size = 1;
            v3.Units = "MJ/kg/degC";
            v3.URL = "";
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v3);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd1.PropertyName = "minTair";
            pd1.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.minTair)).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.minTair);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd2.PropertyName = "maxTair";
            pd2.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.maxTair)).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.maxTair);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceRate);
            pd3.PropertyName = "cropHeatFlux";
            pd3.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceRateVarInfo.cropHeatFlux)).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceRateVarInfo.cropHeatFlux);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceState);
            pd4.PropertyName = "conductance";
            pd4.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceStateVarInfo.conductance)).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceStateVarInfo.conductance);
            _inputs0_0.Add(pd4);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceState);
            pd5.PropertyName = "minCanopyTemperature";
            pd5.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceStateVarInfo.minCanopyTemperature)).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceStateVarInfo.minCanopyTemperature);
            _outputs0_0.Add(pd5);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceState);
            pd6.PropertyName = "maxCanopyTemperature";
            pd6.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceStateVarInfo.maxCanopyTemperature)).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceStateVarInfo.maxCanopyTemperature);
            _outputs0_0.Add(pd6);
            mo0_0.Outputs=_outputs0_0;
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public double lambdaV
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("lambdaV");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'lambdaV' not found (or found null) in strategy 'Canopytemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'lambdaV' not found in strategy 'Canopytemperature'");
            }
        }
        public double rhoDensityAir
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("rhoDensityAir");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'rhoDensityAir' not found (or found null) in strategy 'Canopytemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'rhoDensityAir' not found in strategy 'Canopytemperature'");
            }
        }
        public double specificHeatCapacityAir
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("specificHeatCapacityAir");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'specificHeatCapacityAir' not found (or found null) in strategy 'Canopytemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'specificHeatCapacityAir' not found in strategy 'Canopytemperature'");
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
            double minTair = a.minTair;
            double maxTair = a.maxTair;
            double cropHeatFlux = r.cropHeatFlux;
            double conductance = s.conductance;
            double minCanopyTemperature;
            double maxCanopyTemperature;
            minCanopyTemperature = minTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0d));
            maxCanopyTemperature = maxTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0d));
            s.minCanopyTemperature= minCanopyTemperature;
            s.maxCanopyTemperature= maxCanopyTemperature;
        }
    }
}
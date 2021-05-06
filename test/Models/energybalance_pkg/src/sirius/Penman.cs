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
    public class Penman : IStrategySiriusQualityEnergybalance
    {
    #region Constructor
        public Penman()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 0.66;
            v1.Description = "psychrometric constant";
            v1.Id = 0;
            v1.MaxValue = 1;
            v1.MinValue = 0;
            v1.Name = "psychrometricConstant";
            v1.Size = 1;
            v1.Units = "hPa/degC";
            v1.URL = "";
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 1.5;
            v2.Description = "Priestley-Taylor evapotranspiration proportionality constant";
            v2.Id = 0;
            v2.MaxValue = 100;
            v2.MinValue = 0;
            v2.Name = "Alpha";
            v2.Size = 1;
            v2.Units = "";
            v2.URL = "";
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = 2.454;
            v3.Description = "latent heat of vaporization of water";
            v3.Id = 0;
            v3.MaxValue = 10;
            v3.MinValue = 0;
            v3.Name = "lambdaV";
            v3.Size = 1;
            v3.Units = "MJ/kg";
            v3.URL = "";
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v3);
            VarInfo v4 = new VarInfo();
            v4.DefaultValue = 1.225;
            v4.Description = "Density of air";
            v4.Id = 0;
            v4.MaxValue = 1000;
            v4.MinValue = None;
            v4.Name = "rhoDensityAir";
            v4.Size = 1;
            v4.Units = "kg/m**3";
            v4.URL = "";
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v4.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v4);
            VarInfo v5 = new VarInfo();
            v5.DefaultValue = 0.00101;
            v5.Description = "Specific heat capacity of dry air";
            v5.Id = 0;
            v5.MaxValue = 1;
            v5.MinValue = 0;
            v5.Name = "specificHeatCapacityAir";
            v5.Size = 1;
            v5.Units = "(MJ/kg)/degC";
            v5.URL = "";
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v5.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v5);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceRate);
            pd1.PropertyName = "evapoTranspirationPriestlyTaylor";
            pd1.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceRateVarInfo.evapoTranspirationPriestlyTaylor)).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceRateVarInfo.evapoTranspirationPriestlyTaylor);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd2.PropertyName = "hslope";
            pd2.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.hslope)).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.hslope);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd3.PropertyName = "VPDair";
            pd3.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.VPDair)).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.VPDair);
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
            pd5.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceRate);
            pd5.PropertyName = "evapoTranspirationPenman";
            pd5.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceRateVarInfo.evapoTranspirationPenman)).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceRateVarInfo.evapoTranspirationPenman);
            _outputs0_0.Add(pd5);
            mo0_0.Outputs=_outputs0_0;
        }
    #endregion
        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public double psychrometricConstant
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'psychrometricConstant' not found (or found null) in strategy 'Penman'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'psychrometricConstant' not found in strategy 'Penman'");
            }
        }
        public double Alpha
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("Alpha");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'Alpha' not found (or found null) in strategy 'Penman'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'Alpha' not found in strategy 'Penman'");
            }
        }
        public double lambdaV
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("lambdaV");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'lambdaV' not found (or found null) in strategy 'Penman'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'lambdaV' not found in strategy 'Penman'");
            }
        }
        public double rhoDensityAir
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("rhoDensityAir");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'rhoDensityAir' not found (or found null) in strategy 'Penman'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'rhoDensityAir' not found in strategy 'Penman'");
            }
        }
        public double specificHeatCapacityAir
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("specificHeatCapacityAir");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'specificHeatCapacityAir' not found (or found null) in strategy 'Penman'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'specificHeatCapacityAir' not found in strategy 'Penman'");
            }
        }

        public void Estimate(SiriusQualityEnergybalance.EnergybalanceState s,SiriusQualityEnergybalance.Energybalance s1,SiriusQualityEnergybalance.EnergybalanceRAte r,SiriusQualityEnergybalance.EnergybalanceAuxiliary a,SiriusQualityEnergybalance.EnergybalanceExogenous ex,CRA.AgroManagement.ActEvents actevents)
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
        private void  CalculateModel(SiriusQualityEnergybalance.EnergybalanceState s, SiriusQualityEnergybalance.EnergybalanceState s1, SiriusQualityEnergybalance.EnergybalanceRate r, SiriusQualityEnergybalance.EnergybalanceAuxiliary a, SiriusQualityEnergybalance.EnergybalanceExogenous ex)
        {
            double evapoTranspirationPriestlyTaylor = r.evapoTranspirationPriestlyTaylor;
            double hslope = a.hslope;
            double VPDair = a.VPDair;
            double conductance = s.conductance;
            double evapoTranspirationPenman;
            evapoTranspirationPenman = evapoTranspirationPriestlyTaylor / Alpha + (1000.0d * (rhoDensityAir * specificHeatCapacityAir * VPDair * conductance / (lambdaV * (hslope + psychrometricConstant))));
            r.evapoTranspirationPenman = evapoTranspirationPenman;
        }
    }
}
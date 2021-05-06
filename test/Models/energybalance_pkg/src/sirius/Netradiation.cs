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
    public class Netradiation : IStrategySiriusQualityEnergybalance
    {
    #region Constructor
        public Netradiation()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 0.23;
            v1.Description = "albedo Coefficient";
            v1.Id = 0;
            v1.MaxValue = 1;
            v1.MinValue = 0;
            v1.Name = "albedoCoefficient";
            v1.Size = 1;
            v1.Units = "";
            v1.URL = "";
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 4.903E-09;
            v2.Description = "stefan Boltzman constant";
            v2.Id = 0;
            v2.MaxValue = 1;
            v2.MinValue = 0;
            v2.Name = "stefanBoltzman";
            v2.Size = 1;
            v2.Units = "";
            v2.URL = "";
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = 0;
            v3.Description = "elevation";
            v3.Id = 0;
            v3.MaxValue = 10000;
            v3.MinValue = -500;
            v3.Name = "elevation";
            v3.Size = 1;
            v3.Units = "m";
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
            pd3.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd3.PropertyName = "solarRadiation";
            pd3.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.solarRadiation)).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.solarRadiation);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd4.PropertyName = "vaporPressure";
            pd4.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.vaporPressure)).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.vaporPressure);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd5.PropertyName = "extraSolarRadiation";
            pd5.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.extraSolarRadiation)).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.extraSolarRadiation);
            _inputs0_0.Add(pd5);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd6.PropertyName = "netRadiation";
            pd6.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.netRadiation)).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.netRadiation);
            _outputs0_0.Add(pd6);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd7.PropertyName = "netOutGoingLongWaveRadiation";
            pd7.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.netOutGoingLongWaveRadiation)).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.netOutGoingLongWaveRadiation);
            _outputs0_0.Add(pd7);
            mo0_0.Outputs=_outputs0_0;
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public double albedoCoefficient
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("albedoCoefficient");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'albedoCoefficient' not found (or found null) in strategy 'Netradiation'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'albedoCoefficient' not found in strategy 'Netradiation'");
            }
        }
        public double stefanBoltzman
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("stefanBoltzman");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'stefanBoltzman' not found (or found null) in strategy 'Netradiation'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'stefanBoltzman' not found in strategy 'Netradiation'");
            }
        }
        public double elevation
        { 
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("elevation");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'elevation' not found (or found null) in strategy 'Netradiation'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'elevation' not found in strategy 'Netradiation'");
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
            double solarRadiation = a.solarRadiation;
            double vaporPressure = a.vaporPressure;
            double extraSolarRadiation = a.extraSolarRadiation;
            double netRadiation;
            double netOutGoingLongWaveRadiation;
            double Nsr;
            double clearSkySolarRadiation;
            double averageT;
            double surfaceEmissivity;
            double cloudCoverFactor;
            double Nolr;
            Nsr = (1.0d - albedoCoefficient) * solarRadiation;
            clearSkySolarRadiation = (0.75d + (2 * Math.Pow(10.0d, -5) * elevation)) * extraSolarRadiation;
            averageT = (Math.Pow(maxTair + 273.16d, 4) + Math.Pow(minTair + 273.16d, 4)) / 2.0d;
            surfaceEmissivity = 0.34d - (0.14d * Math.Sqrt(vaporPressure / 10.0d));
            cloudCoverFactor = 1.35d * (solarRadiation / clearSkySolarRadiation) - 0.35d;
            Nolr = stefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor;
            netRadiation = Nsr - Nolr;
            netOutGoingLongWaveRadiation = Nolr;
            a.netRadiation= netRadiation;
            a.netOutGoingLongWaveRadiation= netOutGoingLongWaveRadiation;
        }
    }
}
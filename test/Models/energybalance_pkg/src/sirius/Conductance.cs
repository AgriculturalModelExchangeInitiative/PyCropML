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
    public class Conductance : IStrategySiriusQualityEnergybalance
    {
    #region Constructor
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
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
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
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
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
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
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
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v4.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
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
            v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v5.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLE");
            _parameters0_0.Add(v5);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd1.PropertyName = "plantHeight";
            pd1.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.plantHeight)).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.plantHeight);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceAuxiliary);
            pd2.PropertyName = "wind";
            pd2.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.wind)).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceAuxiliaryVarInfo.wind);
            _inputs0_0.Add(pd2);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityEnergybalance.EnergybalanceState);
            pd3.PropertyName = "conductance";
            pd3.PropertyType = ((SiriusQualityEnergybalance.EnergybalanceStateVarInfo.conductance)).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityEnergybalance.EnergybalanceStateVarInfo.conductance);
            _outputs0_0.Add(pd3);
            mo0_0.Outputs=_outputs0_0;
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
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
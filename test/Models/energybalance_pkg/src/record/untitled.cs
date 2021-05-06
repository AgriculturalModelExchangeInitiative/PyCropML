using System;
using System.Collections.Generic;
using System.Linq;

using System.Xml;
using CRA.ModelLayer.MetadataTypes;
using CRA.ModelLayer.Core;
using CRA.ModelLayer.Strategy;
using System.Reflection;
using VarInfo=CRA.ModelLayer.Core.VarInfo;

using CRA.AgroManagement;       

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
            v4.MaxValue = 10000;
            v4.MinValue = 0;
            v4.Name = "rhoDensityAir";
            v4.Size = 1;
            v4.Units = "kg/m**3";
            v4.URL = "";
            v4.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
            v4.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v4);
            


        private void  CalculateModel(SiriusQualityEnergybalance.EnergybalanceState s, 
                                     SiriusQualityEnergybalance.EnergybalanceState s1, 
                                     SiriusQualityEnergybalance.EnergybalanceRate r,           
                                     SiriusQualityEnergybalance.EnergybalanceAuxiliary a,   
                                     SiriusQualityEnergybalance.EnergybalanceExogenous ex)
        {
            double evapoTranspirationPriestlyTaylor = r.evapoTranspirationPriestlyTaylor;
            double hslope = a.hslope;
            double VPDair = a.VPDair;
            double conductance = s.conductance;
            double evapoTranspirationPenman;
            evapoTranspirationPenman = evapoTranspirationPriestlyTaylor / Alpha + 
                                       (1000.0d * (rhoDensityAir * specificHeatCapacityAir * VPDair 
                                       * conductance / (lambdaV * (hslope + psychrometricConstant))));
            r.evapoTranspirationPenman = evapoTranspirationPenman;
        }
            
            
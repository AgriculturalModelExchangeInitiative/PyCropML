using System;
using System.Collections.Generic;
using System.Linq;
using SQCrop2ML_Energybalance.DomainClass;
using SQCrop2ML_Energybalance.Strategies;

namespace SiriusModel.Model.Energybalance
{
    class EnergybalanceWrapper 
    {
        private EnergybalanceState s;
        private EnergybalanceRate r;
        private EnergybalanceAuxiliary a;
        private EnergybalanceComponent energybalanceComponent;

        public EnergybalanceWrapper() 
        {
            s = new EnergybalanceState();
            r = new EnergybalanceRate();
            a = new EnergybalanceAuxiliary();
			s1 = new EnergybalanceState();
			
            energybalanceComponent = new Energybalance();
            loadParameters();
        }
		
		// output of the component
        public double diffusionLimitedEvaporation{ get { return s.diffusionLimitedEvaporation;}} 
     
        public double conductance{ get { return s.conductance;}} 
     
        public double minCanopyTemperature{ get { return s.minCanopyTemperature;}} 
     
        public double maxCanopyTemperature{ get { return s.maxCanopyTemperature;}} 
     
        public double evapoTranspirationPriestlyTaylor{ get { return r.evapoTranspirationPriestlyTaylor;}} 
     
        public double evapoTranspirationPenman{ get { return r.evapoTranspirationPenman;}} 
     
        public double evapoTranspiration{ get { return r.evapoTranspiration;}} 
     
        public double potentialTranspiration{ get { return r.potentialTranspiration;}} 
     
        public double soilHeatFlux{ get { return r.soilHeatFlux;}} 
     
        public double cropHeatFlux{ get { return r.cropHeatFlux;}} 
     
        public double netRadiation{ get { return a.netRadiation;}} 
     
        public double netOutGoingLongWaveRadiation{ get { return a.netOutGoingLongWaveRadiation;}} 
     
        public double netRadiationEquivalentEvaporation{ get { return a.netRadiationEquivalentEvaporation;}} 
     
        public double energyLimitedEvaporation{ get { return a.energyLimitedEvaporation;}} 
     
        public double soilEvaporation{ get { return a.soilEvaporation;}} 
		
		// parameters
		double Latitude = 33.069;
     

        public EnergybalanceWrapper(Universe universe, EnergybalanceWrapper toCopy, bool copyAll) : base(universe)
        {
            s = (toCopy.s != null) ? new EnergybalanceState(toCopy.s, copyAll) : null;
            r = (toCopy.r != null) ? new EnergybalanceRate(toCopy.r, copyAll) : null;
            a = (toCopy.a != null) ? new EnergybalanceAuxiliary(toCopy.a, copyAll) : null;
            if (copyAll)
            {
                energybalanceComponent = (toCopy.energybalanceComponent != null) ? new Energybalance(toCopy.energybalanceComponent) : null;
            }
        }

        public void Init(){
            energybalanceComponent.Init(s, r, a);
            loadParameters();
        }

        private void loadParameters()
        {
            energybalanceComponent.albedoCoefficient = albedoCoefficient;
            energybalanceComponent.stefanBoltzman = stefanBoltzman;
            energybalanceComponent.elevation = elevation;
            energybalanceComponent.lambdaV = lambdaV;
            energybalanceComponent.psychrometricConstant = psychrometricConstant;
            energybalanceComponent.Alpha = Alpha;
            energybalanceComponent.vonKarman = vonKarman;
            energybalanceComponent.heightWeatherMeasurements = heightWeatherMeasurements;
            energybalanceComponent.zm = zm;
            energybalanceComponent.d = d;
            energybalanceComponent.zh = zh;
            energybalanceComponent.soilDiffusionConstant = soilDiffusionConstant;
            energybalanceComponent.rhoDensityAir = rhoDensityAir;
            energybalanceComponent.specificHeatCapacityAir = specificHeatCapacityAir;
            energybalanceComponent.tau = tau;
            energybalanceComponent.tauAlpha = tauAlpha;
            energybalanceComponent.isWindVpDefined = isWindVpDefined;
        }

        public void EstimateEnergybalance(double minTair, double maxTair, double solarRadiation, double vaporPressure, double extraSolarRadiation, double hslope, double plantHeight, double wind, double deficitOnTopLayers, double VPDair, double netOutGoingLongWaveRadiation)
        {
			LoadPreviousStates();
            a.minTair = minTair;
            a.maxTair = maxTair;
            a.solarRadiation = solarRadiation;
            a.vaporPressure = vaporPressure;
            a.extraSolarRadiation = extraSolarRadiation;
            a.hslope = hslope;
            a.plantHeight = plantHeight;
            a.wind = wind;
            a.deficitOnTopLayers = deficitOnTopLayers;
            a.VPDair = VPDair;
            a.netOutGoingLongWaveRadiation = netOutGoingLongWaveRadiation;
            energybalanceComponent.EStimate(s,s1, r, a, ex);
        }

        private void LoadPreviousStates()
        {



            previousphenologyState.Calendar = phenologyState.Calendar;

            previousphenologyState.LeafNumber = phenologyState.LeafNumber;

            previousphenologyState.phase_ = phenologyState.phase_;
			
			previousphenologyState.tilleringProfile = new List<double>();
            for (int i = 0; i < phenologyState.tilleringProfile.Count; i++) previousphenologyState.tilleringProfile.Add(phenologyState.tilleringProfile[i]);

		
		}


    }

}
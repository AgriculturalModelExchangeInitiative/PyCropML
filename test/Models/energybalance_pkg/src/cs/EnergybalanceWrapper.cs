using System;
using System.Collections.Generic;
using System.Linq;
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
        energybalanceComponent = new EnergybalanceComponent();
        loadParameters();
    }

        double albedoCoefficient = 0.23d;
    double stefanBoltzman = 4.903e-09d;
    double elevation = 0.0d;
    double lambdaV = 2.454d;
    double psychrometricConstant = 0.66d;
    double Alpha = 1.5d;
    double vonKarman = 0.42d;
    double heightWeatherMeasurements = 2.0d;
    double zm = 0.13d;
    double d = 0.67d;
    double zh = 0.013d;
    double soilDiffusionConstant = 4.2d;
    double rhoDensityAir = 1.225d;
    double specificHeatCapacityAir = 0.00101d;
    double tau = 0.9983d;
    double tauAlpha = 0.3d;
    int isWindVpDefined = 1;

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
     

    public EnergybalanceWrapper(EnergybalanceWrapper toCopy, bool copyAll) : this()
    {
        s = (toCopy.s != null) ? new EnergybalanceState(toCopy.s, copyAll) : null;
        r = (toCopy.r != null) ? new EnergybalanceRate(toCopy.r, copyAll) : null;
        a = (toCopy.a != null) ? new EnergybalanceAuxiliary(toCopy.a, copyAll) : null;
        if (copyAll)
        {
            energybalanceComponent = (toCopy.energybalanceComponent != null) ? new EnergybalanceComponent(toCopy.energybalanceComponent) : null;
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
        energybalanceComponent.Calculate_energybalance(s,s1, r, a);
    }

}
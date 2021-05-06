using System;
using System.Collections.Generic;
using System.Linq;
namespace SiriusModel.Model.Strategies
{
    public class EnergybalanceComponent
    {
        
    public EnergybalanceComponent() { }
    

        Netradiation _Netradiation = new Netradiation();
    Netradiationequivalentevaporation _Netradiationequivalentevaporation = new Netradiationequivalentevaporation();
    Priestlytaylor _Priestlytaylor = new Priestlytaylor();
    Conductance _Conductance = new Conductance();
    Diffusionlimitedevaporation _Diffusionlimitedevaporation = new Diffusionlimitedevaporation();
    Penman _Penman = new Penman();
    Ptsoil _Ptsoil = new Ptsoil();
    Soilevaporation _Soilevaporation = new Soilevaporation();
    Evapotranspiration _Evapotranspiration = new Evapotranspiration();
    Soilheatflux _Soilheatflux = new Soilheatflux();
    Potentialtranspiration _Potentialtranspiration = new Potentialtranspiration();
    Cropheatflux _Cropheatflux = new Cropheatflux();
    Canopytemperature _Canopytemperature = new Canopytemperature();

        public double albedoCoefficient
    {
        get
        { return _Netradiation.albedoCoefficient; }
        set
        { _Netradiation.albedoCoefficient = value; } 
    }
    
        public double stefanBoltzman
    {
        get
        { return _Netradiation.stefanBoltzman; }
        set
        { _Netradiation.stefanBoltzman = value; } 
    }
    
        public double elevation
    {
        get
        { return _Netradiation.elevation; }
        set
        { _Netradiation.elevation = value; } 
    }
    
        public double lambdaV
    {
        get
        { return _Netradiationequivalentevaporation.lambdaV; }
        set
        { _Netradiationequivalentevaporation.lambdaV = value;
            _Penman.lambdaV = value;
            _Canopytemperature.lambdaV = value; } 
    }
    
        public double psychrometricConstant
    {
        get
        { return _Priestlytaylor.psychrometricConstant; }
        set
        { _Priestlytaylor.psychrometricConstant = value;
            _Penman.psychrometricConstant = value; } 
    }
    
        public double Alpha
    {
        get
        { return _Priestlytaylor.Alpha; }
        set
        { _Priestlytaylor.Alpha = value;
            _Penman.Alpha = value;
            _Ptsoil.Alpha = value; } 
    }
    
        public double vonKarman
    {
        get
        { return _Conductance.vonKarman; }
        set
        { _Conductance.vonKarman = value; } 
    }
    
        public double heightWeatherMeasurements
    {
        get
        { return _Conductance.heightWeatherMeasurements; }
        set
        { _Conductance.heightWeatherMeasurements = value; } 
    }
    
        public double zm
    {
        get
        { return _Conductance.zm; }
        set
        { _Conductance.zm = value; } 
    }
    
        public double d
    {
        get
        { return _Conductance.d; }
        set
        { _Conductance.d = value; } 
    }
    
        public double zh
    {
        get
        { return _Conductance.zh; }
        set
        { _Conductance.zh = value; } 
    }
    
        public double soilDiffusionConstant
    {
        get
        { return _Diffusionlimitedevaporation.soilDiffusionConstant; }
        set
        { _Diffusionlimitedevaporation.soilDiffusionConstant = value; } 
    }
    
        public double rhoDensityAir
    {
        get
        { return _Penman.rhoDensityAir; }
        set
        { _Penman.rhoDensityAir = value;
            _Canopytemperature.rhoDensityAir = value; } 
    }
    
        public double specificHeatCapacityAir
    {
        get
        { return _Penman.specificHeatCapacityAir; }
        set
        { _Penman.specificHeatCapacityAir = value;
            _Canopytemperature.specificHeatCapacityAir = value; } 
    }
    
        public double tau
    {
        get
        { return _Ptsoil.tau; }
        set
        { _Ptsoil.tau = value;
            _Soilheatflux.tau = value;
            _Potentialtranspiration.tau = value; } 
    }
    
        public double tauAlpha
    {
        get
        { return _Ptsoil.tauAlpha; }
        set
        { _Ptsoil.tauAlpha = value; } 
    }
    
        public int isWindVpDefined
    {
        get
        { return _Evapotranspiration.isWindVpDefined; }
        set
        { _Evapotranspiration.isWindVpDefined = value; } 
    }
    
        public void  CalculateModel(EnergybalanceState s, EnergybalanceState s1, EnergybalanceRate r, EnergybalanceAuxiliary a)
        {
            _Diffusionlimitedevaporation.CalculateModel(s,s1, r, a);
            _Conductance.CalculateModel(s,s1, r, a);
            _Netradiation.CalculateModel(s,s1, r, a);
            _Netradiationequivalentevaporation.CalculateModel(s,s1, r, a);
            _Priestlytaylor.CalculateModel(s,s1, r, a);
            _Penman.CalculateModel(s,s1, r, a);
            _Evapotranspiration.CalculateModel(s,s1, r, a);
            _Potentialtranspiration.CalculateModel(s,s1, r, a);
            _Ptsoil.CalculateModel(s,s1, r, a);
            _Soilevaporation.CalculateModel(s,s1, r, a);
            _Soilheatflux.CalculateModel(s,s1, r, a);
            _Cropheatflux.CalculateModel(s,s1, r, a);
            _Canopytemperature.CalculateModel(s,s1, r, a);
        }
        
    public EnergybalanceComponent(EnergybalanceComponent toCopy): this() // copy constructor 
    {

            albedoCoefficient = toCopy.albedoCoefficient;
            stefanBoltzman = toCopy.stefanBoltzman;
            elevation = toCopy.elevation;
            lambdaV = toCopy.lambdaV;
            psychrometricConstant = toCopy.psychrometricConstant;
            Alpha = toCopy.Alpha;
            vonKarman = toCopy.vonKarman;
            heightWeatherMeasurements = toCopy.heightWeatherMeasurements;
            zm = toCopy.zm;
            d = toCopy.d;
            zh = toCopy.zh;
            soilDiffusionConstant = toCopy.soilDiffusionConstant;
            rhoDensityAir = toCopy.rhoDensityAir;
            specificHeatCapacityAir = toCopy.specificHeatCapacityAir;
            tau = toCopy.tau;
            tauAlpha = toCopy.tauAlpha;
            isWindVpDefined = toCopy.isWindVpDefined;
        }
    }

}
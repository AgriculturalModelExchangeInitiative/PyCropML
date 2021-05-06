using System;
using System.Collections.Generic;
public class EnergybalanceState
{
    private double _diffusionLimitedEvaporation;
    private double _conductance;
    private double _minCanopyTemperature;
    private double _maxCanopyTemperature;
    
    public EnergybalanceState() { }
    
    
    public EnergybalanceState(EnergybalanceState toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    _diffusionLimitedEvaporation = toCopy._diffusionLimitedEvaporation;
    _conductance = toCopy._conductance;
    _minCanopyTemperature = toCopy._minCanopyTemperature;
    _maxCanopyTemperature = toCopy._maxCanopyTemperature;
    }
    }
    public double diffusionLimitedEvaporation
    {
        get { return this._diffusionLimitedEvaporation; }
        set { this._diffusionLimitedEvaporation= value; } 
    }
    public double conductance
    {
        get { return this._conductance; }
        set { this._conductance= value; } 
    }
    public double minCanopyTemperature
    {
        get { return this._minCanopyTemperature; }
        set { this._minCanopyTemperature= value; } 
    }
    public double maxCanopyTemperature
    {
        get { return this._maxCanopyTemperature; }
        set { this._maxCanopyTemperature= value; } 
    }
}
public class EnergybalanceRate
{
    private double _evapoTranspirationPriestlyTaylor;
    private double _evapoTranspirationPenman;
    private double _evapoTranspiration;
    private double _potentialTranspiration;
    private double _soilHeatFlux;
    private double _cropHeatFlux;
    
    public EnergybalanceRate() { }
    
    
    public EnergybalanceRate(EnergybalanceRate toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    _evapoTranspirationPriestlyTaylor = toCopy._evapoTranspirationPriestlyTaylor;
    _evapoTranspirationPenman = toCopy._evapoTranspirationPenman;
    _evapoTranspiration = toCopy._evapoTranspiration;
    _potentialTranspiration = toCopy._potentialTranspiration;
    _soilHeatFlux = toCopy._soilHeatFlux;
    _cropHeatFlux = toCopy._cropHeatFlux;
    }
    }
    public double evapoTranspirationPriestlyTaylor
    {
        get { return this._evapoTranspirationPriestlyTaylor; }
        set { this._evapoTranspirationPriestlyTaylor= value; } 
    }
    public double evapoTranspirationPenman
    {
        get { return this._evapoTranspirationPenman; }
        set { this._evapoTranspirationPenman= value; } 
    }
    public double evapoTranspiration
    {
        get { return this._evapoTranspiration; }
        set { this._evapoTranspiration= value; } 
    }
    public double potentialTranspiration
    {
        get { return this._potentialTranspiration; }
        set { this._potentialTranspiration= value; } 
    }
    public double soilHeatFlux
    {
        get { return this._soilHeatFlux; }
        set { this._soilHeatFlux= value; } 
    }
    public double cropHeatFlux
    {
        get { return this._cropHeatFlux; }
        set { this._cropHeatFlux= value; } 
    }
}
public class EnergybalanceAuxiliary
{
    private double _minTair;
    private double _maxTair;
    private double _solarRadiation;
    private double _vaporPressure;
    private double _extraSolarRadiation;
    private double _hslope;
    private double _plantHeight;
    private double _wind;
    private double _deficitOnTopLayers;
    private double _VPDair;
    private double _netRadiation;
    private double _netOutGoingLongWaveRadiation;
    private double _netRadiationEquivalentEvaporation;
    private double _energyLimitedEvaporation;
    private double _soilEvaporation;
    
    public EnergybalanceAuxiliary() { }
    
    
    public EnergybalanceAuxiliary(EnergybalanceAuxiliary toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    _minTair = toCopy._minTair;
    _maxTair = toCopy._maxTair;
    _solarRadiation = toCopy._solarRadiation;
    _vaporPressure = toCopy._vaporPressure;
    _extraSolarRadiation = toCopy._extraSolarRadiation;
    _hslope = toCopy._hslope;
    _plantHeight = toCopy._plantHeight;
    _wind = toCopy._wind;
    _deficitOnTopLayers = toCopy._deficitOnTopLayers;
    _VPDair = toCopy._VPDair;
    _netRadiation = toCopy._netRadiation;
    _netOutGoingLongWaveRadiation = toCopy._netOutGoingLongWaveRadiation;
    _netRadiationEquivalentEvaporation = toCopy._netRadiationEquivalentEvaporation;
    _energyLimitedEvaporation = toCopy._energyLimitedEvaporation;
    _soilEvaporation = toCopy._soilEvaporation;
    }
    }
    public double minTair
    {
        get { return this._minTair; }
        set { this._minTair= value; } 
    }
    public double maxTair
    {
        get { return this._maxTair; }
        set { this._maxTair= value; } 
    }
    public double solarRadiation
    {
        get { return this._solarRadiation; }
        set { this._solarRadiation= value; } 
    }
    public double vaporPressure
    {
        get { return this._vaporPressure; }
        set { this._vaporPressure= value; } 
    }
    public double extraSolarRadiation
    {
        get { return this._extraSolarRadiation; }
        set { this._extraSolarRadiation= value; } 
    }
    public double hslope
    {
        get { return this._hslope; }
        set { this._hslope= value; } 
    }
    public double plantHeight
    {
        get { return this._plantHeight; }
        set { this._plantHeight= value; } 
    }
    public double wind
    {
        get { return this._wind; }
        set { this._wind= value; } 
    }
    public double deficitOnTopLayers
    {
        get { return this._deficitOnTopLayers; }
        set { this._deficitOnTopLayers= value; } 
    }
    public double VPDair
    {
        get { return this._VPDair; }
        set { this._VPDair= value; } 
    }
    public double netRadiation
    {
        get { return this._netRadiation; }
        set { this._netRadiation= value; } 
    }
    public double netOutGoingLongWaveRadiation
    {
        get { return this._netOutGoingLongWaveRadiation; }
        set { this._netOutGoingLongWaveRadiation= value; } 
    }
    public double netRadiationEquivalentEvaporation
    {
        get { return this._netRadiationEquivalentEvaporation; }
        set { this._netRadiationEquivalentEvaporation= value; } 
    }
    public double energyLimitedEvaporation
    {
        get { return this._energyLimitedEvaporation; }
        set { this._energyLimitedEvaporation= value; } 
    }
    public double soilEvaporation
    {
        get { return this._soilEvaporation; }
        set { this._soilEvaporation= value; } 
    }
}
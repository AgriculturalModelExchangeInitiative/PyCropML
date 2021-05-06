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
using System;
using System.Collections.Generic;

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
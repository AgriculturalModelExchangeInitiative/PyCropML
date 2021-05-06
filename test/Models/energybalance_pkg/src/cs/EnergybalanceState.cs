using System;
using System.Collections.Generic;
public class IEnergybalance
{
    private double _diffusionLimitedEvaporation;
    private double _conductance;
    private double _minCanopyTemperature;
    private double _maxCanopyTemperature;
    
    public IEnergybalance() { }
    
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
import  java.io.*;
import  java.util.*;
public class EnergybalanceState
{
    private double diffusionLimitedEvaporation;
    private double conductance;
    private double minCanopyTemperature;
    private double maxCanopyTemperature;
    
    public EnergybalanceState()
    {
           
    }
    
    public EnergybalanceState(EnergybalanceState toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.diffusionLimitedEvaporation = toCopy.diffusionLimitedEvaporation;
            this.conductance = toCopy.conductance;
            this.minCanopyTemperature = toCopy.minCanopyTemperature;
            this.maxCanopyTemperature = toCopy.maxCanopyTemperature;
        }
    }
    public double getdiffusionLimitedEvaporation()
    {
        return diffusionLimitedEvaporation;
    }

    public void setdiffusionLimitedEvaporation(double _diffusionLimitedEvaporation)
    {
        this.diffusionLimitedEvaporation= _diffusionLimitedEvaporation;
    } 
    
    public double getconductance()
    {
        return conductance;
    }

    public void setconductance(double _conductance)
    {
        this.conductance= _conductance;
    } 
    
    public double getminCanopyTemperature()
    {
        return minCanopyTemperature;
    }

    public void setminCanopyTemperature(double _minCanopyTemperature)
    {
        this.minCanopyTemperature= _minCanopyTemperature;
    } 
    
    public double getmaxCanopyTemperature()
    {
        return maxCanopyTemperature;
    }

    public void setmaxCanopyTemperature(double _maxCanopyTemperature)
    {
        this.maxCanopyTemperature= _maxCanopyTemperature;
    } 
    
}
import  java.io.*;
import  java.util.*;

public class EnergybalanceRate
{
    private double evapoTranspirationPriestlyTaylor;
    private double evapoTranspirationPenman;
    private double evapoTranspiration;
    private double potentialTranspiration;
    private double soilHeatFlux;
    private double cropHeatFlux;
    
    public EnergybalanceRate()
    {
           
    }
    
    public EnergybalanceRate(EnergybalanceRate toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.evapoTranspirationPriestlyTaylor = toCopy.evapoTranspirationPriestlyTaylor;
            this.evapoTranspirationPenman = toCopy.evapoTranspirationPenman;
            this.evapoTranspiration = toCopy.evapoTranspiration;
            this.potentialTranspiration = toCopy.potentialTranspiration;
            this.soilHeatFlux = toCopy.soilHeatFlux;
            this.cropHeatFlux = toCopy.cropHeatFlux;
        }
    }
    public double getevapoTranspirationPriestlyTaylor()
    {
        return evapoTranspirationPriestlyTaylor;
    }

    public void setevapoTranspirationPriestlyTaylor(double _evapoTranspirationPriestlyTaylor)
    {
        this.evapoTranspirationPriestlyTaylor= _evapoTranspirationPriestlyTaylor;
    } 
    
    public double getevapoTranspirationPenman()
    {
        return evapoTranspirationPenman;
    }

    public void setevapoTranspirationPenman(double _evapoTranspirationPenman)
    {
        this.evapoTranspirationPenman= _evapoTranspirationPenman;
    } 
    
    public double getevapoTranspiration()
    {
        return evapoTranspiration;
    }

    public void setevapoTranspiration(double _evapoTranspiration)
    {
        this.evapoTranspiration= _evapoTranspiration;
    } 
    
    public double getpotentialTranspiration()
    {
        return potentialTranspiration;
    }

    public void setpotentialTranspiration(double _potentialTranspiration)
    {
        this.potentialTranspiration= _potentialTranspiration;
    } 
    
    public double getsoilHeatFlux()
    {
        return soilHeatFlux;
    }

    public void setsoilHeatFlux(double _soilHeatFlux)
    {
        this.soilHeatFlux= _soilHeatFlux;
    } 
    
    public double getcropHeatFlux()
    {
        return cropHeatFlux;
    }

    public void setcropHeatFlux(double _cropHeatFlux)
    {
        this.cropHeatFlux= _cropHeatFlux;
    } 
    
}
import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;

public class PhenologyAuxiliary
{
    private LocalDateTime currentdate;
    private double cumulTT;
    private double dayLength;
    private double deltaTT;
    private double gAI;
    private double pAR;
    private double grainCumulTT;
    private double fixPhyll;
    private double cumulTTFromZC_39;
    private double cumulTTFromZC_91;
    private double cumulTTFromZC_65;
    
    public PhenologyAuxiliary() { }
    
    public PhenologyAuxiliary(PhenologyAuxiliary toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.currentdate = toCopy.currentdate;
            this.cumulTT = toCopy.cumulTT;
            this.dayLength = toCopy.dayLength;
            this.deltaTT = toCopy.deltaTT;
            this.gAI = toCopy.gAI;
            this.pAR = toCopy.pAR;
            this.grainCumulTT = toCopy.grainCumulTT;
            this.fixPhyll = toCopy.fixPhyll;
            this.cumulTTFromZC_39 = toCopy.cumulTTFromZC_39;
            this.cumulTTFromZC_91 = toCopy.cumulTTFromZC_91;
            this.cumulTTFromZC_65 = toCopy.cumulTTFromZC_65;
        }
    }
    public LocalDateTime getcurrentdate()
    { return currentdate; }

    public void setcurrentdate(LocalDateTime _currentdate)
    { this.currentdate= _currentdate; } 
    
    public double getcumulTT()
    { return cumulTT; }

    public void setcumulTT(double _cumulTT)
    { this.cumulTT= _cumulTT; } 
    
    public double getdayLength()
    { return dayLength; }

    public void setdayLength(double _dayLength)
    { this.dayLength= _dayLength; } 
    
    public double getdeltaTT()
    { return deltaTT; }

    public void setdeltaTT(double _deltaTT)
    { this.deltaTT= _deltaTT; } 
    
    public double getgAI()
    { return gAI; }

    public void setgAI(double _gAI)
    { this.gAI= _gAI; } 
    
    public double getpAR()
    { return pAR; }

    public void setpAR(double _pAR)
    { this.pAR= _pAR; } 
    
    public double getgrainCumulTT()
    { return grainCumulTT; }

    public void setgrainCumulTT(double _grainCumulTT)
    { this.grainCumulTT= _grainCumulTT; } 
    
    public double getfixPhyll()
    { return fixPhyll; }

    public void setfixPhyll(double _fixPhyll)
    { this.fixPhyll= _fixPhyll; } 
    
    public double getcumulTTFromZC_39()
    { return cumulTTFromZC_39; }

    public void setcumulTTFromZC_39(double _cumulTTFromZC_39)
    { this.cumulTTFromZC_39= _cumulTTFromZC_39; } 
    
    public double getcumulTTFromZC_91()
    { return cumulTTFromZC_91; }

    public void setcumulTTFromZC_91(double _cumulTTFromZC_91)
    { this.cumulTTFromZC_91= _cumulTTFromZC_91; } 
    
    public double getcumulTTFromZC_65()
    { return cumulTTFromZC_65; }

    public void setcumulTTFromZC_65(double _cumulTTFromZC_65)
    { this.cumulTTFromZC_65= _cumulTTFromZC_65; } 
    
}
import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import javafx.util.*;
import java.time.LocalDateTime;
public class Phyllochron
{
    private double lincr;
    public double getlincr()
    { return lincr; }

    public void setlincr(double _lincr)
    { this.lincr= _lincr; } 
    
    private double ldecr;
    public double getldecr()
    { return ldecr; }

    public void setldecr(double _ldecr)
    { this.ldecr= _ldecr; } 
    
    private double pdecr;
    public double getpdecr()
    { return pdecr; }

    public void setpdecr(double _pdecr)
    { this.pdecr= _pdecr; } 
    
    private double pincr;
    public double getpincr()
    { return pincr; }

    public void setpincr(double _pincr)
    { this.pincr= _pincr; } 
    
    private double kl;
    public double getkl()
    { return kl; }

    public void setkl(double _kl)
    { this.kl= _kl; } 
    
    private double pTQhf;
    public double getpTQhf()
    { return pTQhf; }

    public void setpTQhf(double _pTQhf)
    { this.pTQhf= _pTQhf; } 
    
    private double B;
    public double getB()
    { return B; }

    public void setB(double _B)
    { this.B= _B; } 
    
    private double p;
    public double getp()
    { return p; }

    public void setp(double _p)
    { this.p= _p; } 
    
    private String choosePhyllUse;
    public String getchoosePhyllUse()
    { return choosePhyllUse; }

    public void setchoosePhyllUse(String _choosePhyllUse)
    { this.choosePhyllUse= _choosePhyllUse; } 
    
    private double areaSL;
    public double getareaSL()
    { return areaSL; }

    public void setareaSL(double _areaSL)
    { this.areaSL= _areaSL; } 
    
    private double areaSS;
    public double getareaSS()
    { return areaSS; }

    public void setareaSS(double _areaSS)
    { this.areaSS= _areaSS; } 
    
    private double lARmin;
    public double getlARmin()
    { return lARmin; }

    public void setlARmin(double _lARmin)
    { this.lARmin= _lARmin; } 
    
    private double lARmax;
    public double getlARmax()
    { return lARmax; }

    public void setlARmax(double _lARmax)
    { this.lARmax= _lARmax; } 
    
    private double sowingDensity;
    public double getsowingDensity()
    { return sowingDensity; }

    public void setsowingDensity(double _sowingDensity)
    { this.sowingDensity= _sowingDensity; } 
    
    private double lNeff;
    public double getlNeff()
    { return lNeff; }

    public void setlNeff(double _lNeff)
    { this.lNeff= _lNeff; } 
    
    public Phyllochron() { }
    public void  Calculate_phyllochron(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: Phyllochron -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: Phyllochron Model
    //            * Author: Pierre Martre
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Calculate different types of phyllochron 
        //- inputs:
    //            * name: fixPhyll
    //                          ** description : Sowing date corrected Phyllochron
    //                          ** inputtype : variable
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 5.0
    //                          ** min : 0.0
    //                          ** max : 10000.0
    //                          ** unit : °C d leaf-1
    //                          ** uri : some url
    //            * name: leafNumber
    //                          ** description : Actual number of phytomers
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 25.0
    //                          ** unit : leaf
    //                          ** uri : some url
    //            * name: lincr
    //                          ** description : Leaf number above which the phyllochron is increased by Pincr
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 8.0
    //                          ** min : 0.0
    //                          ** max : 30.0
    //                          ** unit : leaf
    //                          ** uri : some url
    //            * name: ldecr
    //                          ** description : Leaf number up to which the phyllochron is decreased by Pdecr
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 100.0
    //                          ** unit : leaf
    //                          ** uri : some url
    //            * name: pdecr
    //                          ** description : Factor decreasing the phyllochron for leaf number less than Ldecr
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 0.4
    //                          ** min : 0.0
    //                          ** max : 10.0
    //                          ** unit : -
    //                          ** uri : some url
    //            * name: pincr
    //                          ** description : Factor increasing the phyllochron for leaf number higher than Lincr
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 1.5
    //                          ** min : 0.0
    //                          ** max : 10.0
    //                          ** unit : -
    //                          ** uri : some url
    //            * name: ptq
    //                          ** description : Photothermal quotient 
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 10000.0
    //                          ** unit : MJ °C-1 d-1 m-2)
    //                          ** uri : some url
    //            * name: gAImean
    //                          ** description : Green Area Index
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 10000.0
    //                          ** unit : m2 m-2
    //                          ** uri : some url
    //            * name: kl
    //                          ** description : Exctinction Coefficient
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 0.45
    //                          ** min : 0.0
    //                          ** max : 50.0
    //                          ** unit : -
    //                          ** uri : some url
    //            * name: pTQhf
    //                          ** description : Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : °C d leaf-1
    //                          ** uri : some url
    //            * name: B
    //                          ** description : Phyllochron at PTQ equal 1
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 20.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : °C d leaf-1
    //                          ** uri : some url
    //            * name: p
    //                          ** description : Phyllochron (Varietal parameter)
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 120.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : °C d leaf-1
    //                          ** uri : some url
    //            * name: choosePhyllUse
    //                          ** description : Switch to choose the type of phyllochron calculation to be used
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : STRING
    //                          ** default : Default
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : -
    //                          ** uri : some url
    //            * name: areaSL
    //                          ** description :  Area Leaf
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : cm2
    //                          ** uri : some url
    //            * name: areaSS
    //                          ** description : Area Sheath
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : cm2
    //                          ** uri : some url
    //            * name: lARmin
    //                          ** description : LAR minimum
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : leaf-1 °C
    //                          ** uri : some url
    //            * name: lARmax
    //                          ** description : LAR maximum
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : leaf-1 °C
    //                          ** uri : some url
    //            * name: sowingDensity
    //                          ** description : Sowing Density
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : plant m-2
    //                          ** uri : some url
    //            * name: lNeff
    //                          ** description : Leaf Number efficace
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : leaf
    //                          ** uri : some url
        //- outputs:
    //            * name: phyllochron
    //                          ** description :  the rate of leaf appearance 
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit :  °C d leaf-1
    //                          ** uri : some url
        double fixPhyll = a.getfixPhyll();
        double leafNumber = s.getleafNumber();
        double ptq = s.getptq();
        double gAImean = s.getgAImean();
        double phyllochron;
        double gaiLim;
        double LAR;
        phyllochron = 0.0d;
        LAR = 0.0d;
        gaiLim = lNeff * ((areaSL + areaSS) / 10000.0d) * sowingDensity;
        if (choosePhyllUse == "Default")
        {
            if (leafNumber < ldecr)
            {
                phyllochron = fixPhyll * pdecr;
            }
            else if ( leafNumber >= ldecr && leafNumber < lincr)
            {
                phyllochron = fixPhyll;
            }
            else
            {
                phyllochron = fixPhyll * pincr;
            }
        }
        if (choosePhyllUse == "PTQ")
        {
            if (gAImean > gaiLim)
            {
                LAR = (lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B * gAImean);
            }
            else
            {
                LAR = (lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B * gaiLim);
            }
            phyllochron = 1.0d / LAR;
        }
        if (choosePhyllUse == "Test")
        {
            if (leafNumber < ldecr)
            {
                phyllochron = p * pdecr;
            }
            else if ( leafNumber >= ldecr && leafNumber < lincr)
            {
                phyllochron = p;
            }
            else
            {
                phyllochron = p * pincr;
            }
        }
        s.setphyllochron(phyllochron);
    }
}
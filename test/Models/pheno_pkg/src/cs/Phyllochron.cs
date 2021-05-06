using System;
using System.Collections.Generic;
using System.Linq;
public class Phyllochron
{
    private double _lincr;
    public double lincr
    {
        get { return this._lincr; }
        set { this._lincr= value; } 
    }
    private double _ldecr;
    public double ldecr
    {
        get { return this._ldecr; }
        set { this._ldecr= value; } 
    }
    private double _pdecr;
    public double pdecr
    {
        get { return this._pdecr; }
        set { this._pdecr= value; } 
    }
    private double _pincr;
    public double pincr
    {
        get { return this._pincr; }
        set { this._pincr= value; } 
    }
    private double _kl;
    public double kl
    {
        get { return this._kl; }
        set { this._kl= value; } 
    }
    private double _pTQhf;
    public double pTQhf
    {
        get { return this._pTQhf; }
        set { this._pTQhf= value; } 
    }
    private double _B;
    public double B
    {
        get { return this._B; }
        set { this._B= value; } 
    }
    private double _p;
    public double p
    {
        get { return this._p; }
        set { this._p= value; } 
    }
    private string _choosePhyllUse;
    public string choosePhyllUse
    {
        get { return this._choosePhyllUse; }
        set { this._choosePhyllUse= value; } 
    }
    private double _areaSL;
    public double areaSL
    {
        get { return this._areaSL; }
        set { this._areaSL= value; } 
    }
    private double _areaSS;
    public double areaSS
    {
        get { return this._areaSS; }
        set { this._areaSS= value; } 
    }
    private double _lARmin;
    public double lARmin
    {
        get { return this._lARmin; }
        set { this._lARmin= value; } 
    }
    private double _lARmax;
    public double lARmax
    {
        get { return this._lARmax; }
        set { this._lARmax= value; } 
    }
    private double _sowingDensity;
    public double sowingDensity
    {
        get { return this._sowingDensity; }
        set { this._sowingDensity= value; } 
    }
    private double _lNeff;
    public double lNeff
    {
        get { return this._lNeff; }
        set { this._lNeff= value; } 
    }
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
        double fixPhyll = a.fixPhyll;
        double leafNumber = s.leafNumber;
        double ptq = s.ptq;
        double gAImean = s.gAImean;
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
        s.phyllochron= phyllochron;
    }
}
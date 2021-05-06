using System;
using System.Collections.Generic;
using System.Linq;
public class Phylsowingdatecorrection
{
    private int _sowingDay;
    public int sowingDay
    {
        get { return this._sowingDay; }
        set { this._sowingDay= value; } 
    }
    private double _latitude;
    public double latitude
    {
        get { return this._latitude; }
        set { this._latitude= value; } 
    }
    private double _sDsa_sh;
    public double sDsa_sh
    {
        get { return this._sDsa_sh; }
        set { this._sDsa_sh= value; } 
    }
    private double _rp;
    public double rp
    {
        get { return this._rp; }
        set { this._rp= value; } 
    }
    private int _sDws;
    public int sDws
    {
        get { return this._sDws; }
        set { this._sDws= value; } 
    }
    private double _sDsa_nh;
    public double sDsa_nh
    {
        get { return this._sDsa_nh; }
        set { this._sDsa_nh= value; } 
    }
    private double _p;
    public double p
    {
        get { return this._p; }
        set { this._p= value; } 
    }
    public Phylsowingdatecorrection() { }
    
    public void  Calculate_phylsowingdatecorrection(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: PhylSowingDateCorrection -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: PhylSowingDateCorrection Model
    //            * Author: Loic Manceau
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Correction of the Phyllochron Varietal parameter according to sowing date 
        //- inputs:
    //            * name: sowingDay
    //                          ** description : Day of Year at sowing
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** min : 1
    //                          ** max : 365
    //                          ** default : 1
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: latitude
    //                          ** description : Latitude
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLE
    //                          ** min : -90
    //                          ** max : 90
    //                          ** default : 0.0
    //                          ** unit : °
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: sDsa_sh
    //                          ** description : Sowing date at which Phyllochrone is maximum in southern hemispher
    //                          ** parametercategory : species
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 1
    //                          ** max : 365
    //                          ** default : 1.0
    //                          ** unit : d
    //                          ** uri : some url
    //            * name: rp
    //                          ** description : Rate of change of Phyllochrone with sowing date
    //                          ** parametercategory : species
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 365
    //                          ** default : 0
    //                          ** unit : d-1
    //                          ** uri : some url
    //            * name: sDws
    //                          ** description : Sowing date at which Phyllochrone is minimum
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** default : 1
    //                          ** min : 1
    //                          ** max : 365
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: sDsa_nh
    //                          ** description : Sowing date at which Phyllochrone is maximum in northern hemispher
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 1.0
    //                          ** min : 1
    //                          ** max : 365
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: p
    //                          ** description : Phyllochron (Varietal parameter)
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 120
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : °C d leaf-1
    //                          ** uri : some url
    //                          ** inputtype : parameter
        //- outputs:
    //            * name: fixPhyll
    //                          ** description :  Phyllochron Varietal parameter 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : °C d leaf-1
        double fixPhyll;
        if (latitude < 0.0d)
        {
            if (sowingDay > (int)(sDsa_sh))
            {
                fixPhyll = p * (1 - (rp * Math.Min((sowingDay - sDsa_sh), sDws)));
            }
            else
            {
                fixPhyll = p;
            }
        }
        else
        {
            if (sowingDay < (int)(sDsa_nh))
            {
                fixPhyll = p * (1 - (rp * Math.Min(sowingDay, sDws)));
            }
            else
            {
                fixPhyll = p;
            }
        }
        a.fixPhyll= fixPhyll;
    }
}
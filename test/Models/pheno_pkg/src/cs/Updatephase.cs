using System;
using System.Collections.Generic;
using System.Linq;
public class Updatephase
{
    private int _isVernalizable;
    public int isVernalizable
    {
        get { return this._isVernalizable; }
        set { this._isVernalizable= value; } 
    }
    private double _dse;
    public double dse
    {
        get { return this._dse; }
        set { this._dse= value; } 
    }
    private double _pFLLAnth;
    public double pFLLAnth
    {
        get { return this._pFLLAnth; }
        set { this._pFLLAnth= value; } 
    }
    private double _dcd;
    public double dcd
    {
        get { return this._dcd; }
        set { this._dcd= value; } 
    }
    private double _dgf;
    public double dgf
    {
        get { return this._dgf; }
        set { this._dgf= value; } 
    }
    private double _degfm;
    public double degfm
    {
        get { return this._degfm; }
        set { this._degfm= value; } 
    }
    private double _maxDL;
    public double maxDL
    {
        get { return this._maxDL; }
        set { this._maxDL= value; } 
    }
    private double _sLDL;
    public double sLDL
    {
        get { return this._sLDL; }
        set { this._sLDL= value; } 
    }
    private bool _ignoreGrainMaturation;
    public bool ignoreGrainMaturation
    {
        get { return this._ignoreGrainMaturation; }
        set { this._ignoreGrainMaturation= value; } 
    }
    private double _pHEADANTH;
    public double pHEADANTH
    {
        get { return this._pHEADANTH; }
        set { this._pHEADANTH= value; } 
    }
    private string _choosePhyllUse;
    public string choosePhyllUse
    {
        get { return this._choosePhyllUse; }
        set { this._choosePhyllUse= value; } 
    }
    private double _p;
    public double p
    {
        get { return this._p; }
        set { this._p= value; } 
    }
    public Updatephase() { }
    
    public void  Calculate_updatephase(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: UpdatePhase -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: UpdatePhase Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: This strategy advances the phase and calculate the final leaf number
    //    	
        //- inputs:
    //            * name: cumulTT
    //                          ** description : cumul thermal times at current date
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 354.582294511779
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: leafNumber_t1
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default :  4.620511621863958
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //            * name: cumulTTFromZC_39
    //                          ** description : cumul of the thermal time ( DeltaTT) since the moment ZC_39
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0
    //                          ** unit : °C d-1
    //                          ** inputtype : variable
    //            * name: isMomentRegistredZC_39
    //                          ** description : true if ZC_39 is registered in the calendar
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: gAI
    //                          ** description : used to calculate Terminal spikelet
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0.3255196285135
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: grainCumulTT
    //                          ** description : cumulTT used for the grain developpment
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: dayLength
    //                          ** description : length of the day
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : auxiliary
    //                          ** min : 0
    //                          ** max : 24
    //                          ** unit : h
    //                          ** default : 12.7433275303389
    //                          ** inputtype : variable
    //            * name: vernaprog
    //                          ** description : progression on a 0  to 1 scale of the vernalization
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10
    //                          ** default :  1.0532526829571554
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: minFinalNumber
    //                          ** description : minimum final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 6.879410413987549
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //            * name: fixPhyll
    //                          ** description : Phyllochron with sowing date fix
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 91.2
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: isVernalizable
    //                          ** description : true if the plant is vernalizable
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    //                          ** default : 1
    //                          ** inputtype : parameter
    //            * name: dse
    //                          ** description : Thermal time from sowing to emergence
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 105
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: pFLLAnth
    //                          ** description : Phyllochronic duration of the period between flag leaf ligule appearance and anthesis
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : 
    //                          ** default : 2.22
    //                          ** inputtype : parameter
    //            * name: dcd
    //                          ** description : Duration of the endosperm cell division phase
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 100
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: dgf
    //                          ** description : Grain filling duration (from anthesis to physiological maturity)
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 450
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: degfm
    //                          ** description : Grain maturation duration (from physiological maturity to harvest ripeness)
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 50
    //                          ** default : 0
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: maxDL
    //                          ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 24
    //                          ** default : 15
    //                          ** unit : h
    //                          ** inputtype : parameter
    //            * name: sLDL
    //                          ** description : Daylength response of leaf production
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.85
    //                          ** unit : leaf h-1
    //                          ** inputtype : parameter
    //            * name: ignoreGrainMaturation
    //                          ** description : true to ignore grain maturation
    //                          ** parametercategory : species
    //                          ** datatype : BOOLEAN
    //                          ** default : FALSE
    //                          ** unit : 
    //                          ** inputtype : parameter
    //            * name: pHEADANTH
    //                          ** description : Number of phyllochron between heading and anthesiss
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : parameter
    //            * name: choosePhyllUse
    //                          ** description : Switch to choose the type of phyllochron calculation to be used
    //                          ** parametercategory : species
    //                          ** datatype : STRING
    //                          ** unit : 
    //                          ** default : Default
    //                          ** inputtype : parameter
    //            * name: p
    //                          ** description : Phyllochron (Varietal parameter)
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 120
    //                          ** unit : °C d leaf-1
    //                          ** inputtype : parameter
    //            * name: phase_t1
    //                          ** description :  the name of the phase
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: cumulTTFromZC_91
    //                          ** description : cumul of the thermal time (DeltaTT) since the moment ZC_91
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 5000
    //                          ** default : 0
    //                          ** unit : °C d-1
    //                          ** inputtype : variable
    //            * name: phyllochron
    //                          ** description : Phyllochron
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 91.2
    //                          ** unit : °C d leaf-1
    //                          ** inputtype : variable
    //            * name: hasLastPrimordiumAppeared_t1
    //                          ** description : if Last Primordium has Appeared
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: finalLeafNumber_t1
    //                          ** description : final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 0
    //                          ** unit : leaf
    //                          ** inputtype : variable
        //- outputs:
    //            * name: finalLeafNumber
    //                          ** description : final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** unit : leaf
    //            * name: phase
    //                          ** description : the name of the phase
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** unit : 
    //            * name: hasLastPrimordiumAppeared
    //                          ** description : if Last Primordium has Appeared
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
        double cumulTT = a.cumulTT;
        double leafNumber_t1 = s1.leafNumber;
        double cumulTTFromZC_39 = a.cumulTTFromZC_39;
        int isMomentRegistredZC_39 = s.isMomentRegistredZC_39;
        double gAI = a.gAI;
        double grainCumulTT = a.grainCumulTT;
        double dayLength = a.dayLength;
        double vernaprog = s.vernaprog;
        double minFinalNumber = s.minFinalNumber;
        double fixPhyll = a.fixPhyll;
        double phase_t1 = s1.phase;
        double cumulTTFromZC_91 = a.cumulTTFromZC_91;
        double phyllochron = s.phyllochron;
        int hasLastPrimordiumAppeared_t1 = s1.hasLastPrimordiumAppeared;
        double finalLeafNumber_t1 = s1.finalLeafNumber;
        double finalLeafNumber;
        double phase;
        int hasLastPrimordiumAppeared;
        double ttFromLastLeafToHeading;
        double appFLN;
        double localDegfm;
        double ttFromLastLeafToAnthesis;
        hasLastPrimordiumAppeared = hasLastPrimordiumAppeared_t1;
        finalLeafNumber = finalLeafNumber_t1;
        phase = phase_t1;
        if (phase_t1 >= 0.0d && phase_t1 < 1.0d)
        {
            if (cumulTT >= dse)
            {
                phase = 1.0d;
            }
            else
            {
                phase = phase_t1;
            }
        }
        else if ( phase_t1 >= 1.0d && phase_t1 < 2.0d)
        {
            if (isVernalizable == 1 && vernaprog >= 1.0d || isVernalizable == 0)
            {
                if (dayLength > maxDL)
                {
                    finalLeafNumber = minFinalNumber;
                    hasLastPrimordiumAppeared = 1;
                }
                else
                {
                    appFLN = minFinalNumber + (sLDL * (maxDL - dayLength));
                    if (appFLN / 2.0d <= leafNumber_t1)
                    {
                        finalLeafNumber = appFLN;
                        hasLastPrimordiumAppeared = 1;
                    }
                    else
                    {
                        phase = phase_t1;
                    }
                }
                if (hasLastPrimordiumAppeared == 1)
                {
                    phase = 2.0d;
                }
            }
            else
            {
                phase = phase_t1;
            }
        }
        else if ( phase_t1 >= 2.0d && phase_t1 < 4.0d)
        {
            if (isMomentRegistredZC_39 == 1)
            {
                if (phase_t1 < 3.0d)
                {
                    ttFromLastLeafToHeading = 0.0d;
                    if (choosePhyllUse == "Default")
                    {
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * fixPhyll;
                    }
                    else if ( choosePhyllUse == "PTQ")
                    {
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron;
                    }
                    else if ( choosePhyllUse == "Test")
                    {
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p;
                    }
                    if (cumulTTFromZC_39 >= ttFromLastLeafToHeading)
                    {
                        phase = 3.0d;
                    }
                    else
                    {
                        phase = phase_t1;
                    }
                }
                else
                {
                    phase = phase_t1;
                }
                ttFromLastLeafToAnthesis = 0.0d;
                if (choosePhyllUse == "Default")
                {
                    ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll;
                }
                else if ( choosePhyllUse == "PTQ")
                {
                    ttFromLastLeafToAnthesis = pFLLAnth * phyllochron;
                }
                else if ( choosePhyllUse == "Test")
                {
                    ttFromLastLeafToAnthesis = pFLLAnth * p;
                }
                if (cumulTTFromZC_39 >= ttFromLastLeafToAnthesis)
                {
                    phase = 4.0d;
                }
            }
            else
            {
                phase = phase_t1;
            }
        }
        else if ( phase_t1 == 4.0d)
        {
            if (grainCumulTT >= dcd)
            {
                phase = 4.5d;
            }
            else
            {
                phase = phase_t1;
            }
        }
        else if ( phase_t1 == 4.5d)
        {
            if (grainCumulTT >= dgf || gAI <= 0.0d)
            {
                phase = 5.0d;
            }
            else
            {
                phase = phase_t1;
            }
        }
        else if ( phase_t1 >= 5.0d && phase_t1 < 6.0d)
        {
            localDegfm = degfm;
            if (ignoreGrainMaturation)
            {
                localDegfm = -1.0d;
            }
            if (cumulTTFromZC_91 >= localDegfm)
            {
                phase = 6.0d;
            }
            else
            {
                phase = phase_t1;
            }
        }
        else if ( phase_t1 >= 6.0d && phase_t1 < 7.0d)
        {
            phase = phase_t1;
        }
        s.finalLeafNumber= finalLeafNumber;
        s.phase= phase;
        s.hasLastPrimordiumAppeared= hasLastPrimordiumAppeared;
    }
}
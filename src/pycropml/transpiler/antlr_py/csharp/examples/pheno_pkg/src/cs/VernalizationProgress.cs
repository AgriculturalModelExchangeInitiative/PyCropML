using System;
using System.Collections.Generic;
using System.Linq;
public class VernalizationProgress
{
    private double _minTvern;
    public double minTvern
        {
            get { return this._minTvern; }
            set { this._minTvern= value; } 
        }
    private double _intTvern;
    public double intTvern
        {
            get { return this._intTvern; }
            set { this._intTvern= value; } 
        }
    private double _vAI;
    public double vAI
        {
            get { return this._vAI; }
            set { this._vAI= value; } 
        }
    private double _vBEE;
    public double vBEE
        {
            get { return this._vBEE; }
            set { this._vBEE= value; } 
        }
    private double _minDL;
    public double minDL
        {
            get { return this._minDL; }
            set { this._minDL= value; } 
        }
    private double _maxDL;
    public double maxDL
        {
            get { return this._maxDL; }
            set { this._maxDL= value; } 
        }
    private double _maxTvern;
    public double maxTvern
        {
            get { return this._maxTvern; }
            set { this._maxTvern= value; } 
        }
    private double _pNini;
    public double pNini
        {
            get { return this._pNini; }
            set { this._pNini= value; } 
        }
    private double _aMXLFNO;
    public double aMXLFNO
        {
            get { return this._aMXLFNO; }
            set { this._aMXLFNO= value; } 
        }
    private int _isVernalizable;
    public int isVernalizable
        {
            get { return this._isVernalizable; }
            set { this._isVernalizable= value; } 
        }
    public VernalizationProgress() { }
    
    public void  CalculateModel(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: VernalizationProgress -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: VernalizationProgress Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Calculate progress (VernaProg) towards vernalization, but there 
    //        			is no vernalization below minTvern 
    //        			and above maxTvern . The maximum value of VernaProg is 1.
    //        			Progress towards full vernalization is a linear function of shoot 
    //        			temperature (soil temperature until leaf # reach MaxLeafSoil and then
    //        			 canopy temperature)
    //    	
        //- inputs:
    //            * name: dayLength
    //                          ** description : day length
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 12.3037621834005
    //                          ** unit : mm2 m-2
    //                          ** inputtype : variable
    //            * name: deltaTT
    //                          ** description : difference cumul TT between j and j-1 day 
    //                          ** variablecategory : auxiliary
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 100
    //                          ** default : 20.3429985011972
    //                          ** unit : °C d
    //            * name: cumulTT
    //                          ** description : cumul thermal times at currentdate
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 112.330110409888
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: leafNumber_t1
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 0
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //            * name: calendarMoments_t1
    //                          ** description : List containing appearance of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** default : ['Sowing']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarDates_t1
    //                          ** description : List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** default : ['2007/3/21']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarCumuls_t1
    //                          ** description : list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: minTvern
    //                          ** description : Minimum temperature for vernalization to occur
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 60
    //                          ** default : 0.0
    //                          ** unit : °C
    //                          ** inputtype : parameter
    //            * name: intTvern
    //                          ** description : Intermediate temperature for vernalization to occur
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 60
    //                          ** default :  11.0
    //                          ** unit : °C
    //                          ** inputtype : parameter
    //            * name: vAI
    //                          ** description : Response of vernalization rate to temperature
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default :  0.015
    //                          ** unit : d-1 °C-1
    //                          ** inputtype : parameter
    //            * name: vBEE
    //                          ** description : Vernalization rate at 0°C
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.01
    //                          ** unit : d-1
    //                          ** inputtype : parameter
    //            * name: minDL
    //                          ** description : Threshold daylength below which it does influence vernalization rate
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 12
    //                          ** max : 24
    //                          ** default : 8.0
    //                          ** unit : h
    //                          ** inputtype : parameter
    //            * name: maxDL
    //                          ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 24
    //                          ** default : 15.0
    //                          ** unit : h
    //                          ** inputtype : parameter
    //            * name: maxTvern
    //                          ** description : Maximum temperature for vernalization to occur
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 60
    //                          ** default :  23.0
    //                          ** unit : °C
    //                          ** inputtype : parameter
    //            * name: pNini
    //                          ** description : Number of primorida in the apex at emergence
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 24
    //                          ** default : 4.0
    //                          ** unit : primordia
    //                          ** inputtype : parameter
    //            * name: aMXLFNO
    //                          ** description : Absolute maximum leaf number
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 24.0
    //                          ** unit : leaf
    //                          ** inputtype : parameter
    //            * name: vernaprog_t1
    //                          ** description : progression on a 0  to 1 scale of the vernalization
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default :  0.5517254187376879
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: currentdate
    //                          ** description : current date 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DATE
    //                          ** default : 2007/3/27
    //                          ** inputtype : variable
    //                          ** unit : 
    //            * name: isVernalizable
    //                          ** description : true if the plant is vernalizable
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : parameter
    //            * name: minFinalNumber_t1
    //                          ** description : minimum final leaf number
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 5.5
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //                          ** variablecategory : state
        //- outputs:
    //            * name: vernaprog
    //                          ** description : progression on a 0  to 1 scale of the vernalization
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : 
    //            * name: minFinalNumber
    //                          ** description : minimum final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : leaf
    //            * name: calendarMoments
    //                          ** description : List containing appearance of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** unit : 
    //            * name: calendarDates
    //                          ** description : List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** unit : 
    //            * name: calendarCumuls
    //                          ** description : list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** unit : 
        double dayLength = a.dayLength;
        double deltaTT = a.deltaTT;
        double cumulTT = a.cumulTT;
        double leafNumber_t1 = s1.leafNumber;
        List<string> calendarMoments_t1 = s1.calendarMoments;
        List<DateTime> calendarDates_t1 = s1.calendarDates;
        List<double> calendarCumuls_t1 = s1.calendarCumuls;
        double vernaprog_t1 = s1.vernaprog;
        DateTime currentdate = a.currentdate;
        double minFinalNumber_t1 = s1.minFinalNumber;
        double vernaprog;
        double minFinalNumber;
        List<string> calendarMoments = new List<string>();
        List<DateTime> calendarDates = new List<DateTime>();
        List<double> calendarCumuls = new List<double>();
        double maxVernaProg;
        double dLverna;
        double primordno;
        double minLeafNumber;
        double potlfno;
        double tt;
        calendarMoments = new List<string>(calendarMoments_t1);
        calendarCumuls = new List<double>(calendarCumuls_t1);
        calendarDates = new List<DateTime>(calendarDates_t1);
        minFinalNumber = minFinalNumber_t1;
        vernaprog = vernaprog_t1;
        if (isVernalizable == 1 && vernaprog_t1 < 1.0d)
        {
            tt = deltaTT;
            if (tt >= minTvern && tt <= intTvern)
            {
                vernaprog = vernaprog_t1 + (vAI * tt) + vBEE;
            }
            else
            {
                vernaprog = vernaprog_t1;
            }
            if (tt > intTvern)
            {
                maxVernaProg = vAI * intTvern + vBEE;
                dLverna = Math.Max(minDL, Math.Min(maxDL, dayLength));
                vernaprog = vernaprog + Math.Max(0.0d, maxVernaProg * (1.0d + ((intTvern - tt) / (maxTvern - intTvern) * ((dLverna - minDL) / (maxDL - minDL)))));
            }
            primordno = 2.0d * leafNumber_t1 + pNini;
            minLeafNumber = minFinalNumber_t1;
            if (vernaprog >= 1.0d || primordno >= aMXLFNO)
            {
                minFinalNumber = Math.Max(primordno, minFinalNumber_t1);
                calendarMoments.Add("EndVernalisation");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
                vernaprog = Math.Max(1.0d, vernaprog);
            }
            else
            {
                potlfno = aMXLFNO - ((aMXLFNO - minLeafNumber) * vernaprog);
                if (primordno >= potlfno)
                {
                    minFinalNumber = Math.Max((potlfno + primordno) / 2.0d, minFinalNumber_t1);
                    vernaprog = Math.Max(1.0d, vernaprog);
                    calendarMoments.Add("EndVernalisation");
                    calendarCumuls.Add(cumulTT);
                    calendarDates.Add(currentdate);
                }
            }
        }
        s.vernaprog= vernaprog;
        s.minFinalNumber= minFinalNumber;
        s.calendarMoments= calendarMoments;
        s.calendarDates= calendarDates;
        s.calendarCumuls= calendarCumuls;
    }
}
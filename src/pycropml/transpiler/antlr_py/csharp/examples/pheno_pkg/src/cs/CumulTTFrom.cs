using System;
using System.Collections.Generic;
using System.Linq;
public class CumulTTFrom
{
    
    public CumulTTFrom() { }
    
    public void  CalculateModel(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: CumulTTFrom -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: CumulTTFrom Model
    //            * Author: Pierre Martre
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Calculate CumulTT 
        //- inputs:
    //            * name: calendarMoments_t1
    //                          ** description : List containing appearance of each stage at previous day
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** default : ['Sowing']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarCumuls_t1
    //                          ** description : list containing for each stage occured its cumulated thermal times at previous day
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: cumulTT
    //                          ** description : cumul TT at current date
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : auxiliary
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 8.0
    //                          ** unit : °C d
    //                          ** inputtype : variable
        //- outputs:
    //            * name: cumulTTFromZC_65
    //                          ** description :  cumul TT from Anthesis to current date 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 5000
    //                          ** unit : °C d
    //            * name: cumulTTFromZC_39
    //                          ** description :  cumul TT from FlagLeafLiguleJustVisible to current date 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 5000
    //                          ** unit : °C d
    //            * name: cumulTTFromZC_91
    //                          ** description :  cumul TT from EndGrainFilling to current date 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 5000
    //                          ** unit : °C d
        List<string> calendarMoments_t1 = s1.calendarMoments;
        List<double> calendarCumuls_t1 = s1.calendarCumuls;
        double cumulTT = a.cumulTT;
        double cumulTTFromZC_65;
        double cumulTTFromZC_39;
        double cumulTTFromZC_91;
        cumulTTFromZC_65 = 0.0d;
        cumulTTFromZC_39 = 0.0d;
        cumulTTFromZC_91 = 0.0d;
        if (calendarMoments_t1.Contains("Anthesis"))
        {
            cumulTTFromZC_65 = cumulTT - calendarCumuls_t1[calendarMoments_t1.IndexOf("Anthesis")];
        }
        if (calendarMoments_t1.Contains("FlagLeafLiguleJustVisible"))
        {
            cumulTTFromZC_39 = cumulTT - calendarCumuls_t1[calendarMoments_t1.IndexOf("FlagLeafLiguleJustVisible")];
        }
        if (calendarMoments_t1.Contains("EndGrainFilling"))
        {
            cumulTTFromZC_91 = cumulTT - calendarCumuls_t1[calendarMoments_t1.IndexOf("EndGrainFilling")];
        }
        a.cumulTTFromZC_65= cumulTTFromZC_65;
        a.cumulTTFromZC_39= cumulTTFromZC_39;
        a.cumulTTFromZC_91= cumulTTFromZC_91;
    }
}
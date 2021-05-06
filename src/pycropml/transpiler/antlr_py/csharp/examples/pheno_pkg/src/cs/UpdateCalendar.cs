using System;
using System.Collections.Generic;
using System.Linq;
public class UpdateCalendar
{
    
    public UpdateCalendar() { }
    
    public void  CalculateModel(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: UpdateCalendar -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: Calendar Model
    //            * Author: Pierre Martre
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Lists containing for each stage the date it occurs as well as a copy of all types of cumulated thermal times 
        //- inputs:
    //            * name: cumulTT
    //                          ** description : cumul thermal times at current date
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 741.510096671757
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: calendarMoments
    //                          ** description : List containing apparition of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** default : ['Sowing']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarDates
    //                          ** description : List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** default : ['2007/3/21']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarCumuls
    //                          ** description : list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: currentdate
    //                          ** description : current date
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DATE
    //                          ** default : 2007/3/27
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: phase
    //                          ** description :  the name of the phase
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : variable
        //- outputs:
    //            * name: calendarMoments
    //                          ** description :  List containing apparition of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** unit : 
    //            * name: calendarDates
    //                          ** description :  List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** unit : 
    //            * name: calendarCumuls
    //                          ** description :  list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** unit : °C d
        double cumulTT = a.cumulTT;
        List<string> calendarMoments = s.calendarMoments;
        List<DateTime> calendarDates = s.calendarDates;
        List<double> calendarCumuls = s.calendarCumuls;
        DateTime currentdate = a.currentdate;
        double phase = s.phase;
        if (phase >= 1.0d && phase < 2.0d && !calendarMoments.Contains("Emergence"))
        {
            calendarMoments.Add("Emergence");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase >= 2.0d && phase < 3.0d && !calendarMoments.Contains("FloralInitiation"))
        {
            calendarMoments.Add("FloralInitiation");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase >= 3.0d && phase < 4.0d && !calendarMoments.Contains("Heading"))
        {
            calendarMoments.Add("Heading");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase == 4.0d && !calendarMoments.Contains("Anthesis"))
        {
            calendarMoments.Add("Anthesis");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase == 4.5d && !calendarMoments.Contains("EndCellDivision"))
        {
            calendarMoments.Add("EndCellDivision");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase >= 5.0d && phase < 6.0d && !calendarMoments.Contains("EndGrainFilling"))
        {
            calendarMoments.Add("EndGrainFilling");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase >= 6.0d && phase < 7.0d && !calendarMoments.Contains("Maturity"))
        {
            calendarMoments.Add("Maturity");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        s.calendarMoments= calendarMoments;
        s.calendarDates= calendarDates;
        s.calendarCumuls= calendarCumuls;
    }
}
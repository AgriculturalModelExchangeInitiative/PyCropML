using System;
using System.Collections.Generic;
using System.Linq;
public class UpdateLeafFlag
{
    
    public UpdateLeafFlag() { }
    
    public void  CalculateModel(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: UpdateLeafFlag -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: UpdateLeafFlag Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: tells if flag leaf has appeared and update the calendar if so
    //    	
        //- inputs:
    //            * name: cumulTT
    //                          ** description : cumul thermal times at current date
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 741.510096671757
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: leafNumber
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 8.919453833361189
    //                          ** unit : leaf
    //                          ** uri : some url
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
    //                          ** description :  current date
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DATE
    //                          ** default : 2007/4/29
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: finalLeafNumber
    //                          ** description : final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 8.797582013199484
    //                          ** unit : leaf
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: hasFlagLeafLiguleAppeared_t1
    //                          ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 1
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: phase
    //                          ** description :  the name of the phase
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** default : 1
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : variable
        //- outputs:
    //            * name: hasFlagLeafLiguleAppeared
    //                          ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    //                          ** uri : some url
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
        double leafNumber = s.leafNumber;
        List<string> calendarMoments = s.calendarMoments;
        List<DateTime> calendarDates = s.calendarDates;
        List<double> calendarCumuls = s.calendarCumuls;
        DateTime currentdate = a.currentdate;
        double finalLeafNumber = s.finalLeafNumber;
        int hasFlagLeafLiguleAppeared_t1 = s1.hasFlagLeafLiguleAppeared;
        double phase = s.phase;
        int hasFlagLeafLiguleAppeared;
        hasFlagLeafLiguleAppeared = hasFlagLeafLiguleAppeared_t1;
        if (phase >= 1.0d && phase < 4.0d)
        {
            if (leafNumber > 0.0d)
            {
                if (hasFlagLeafLiguleAppeared_t1 == 0 && (finalLeafNumber > 0.0d && leafNumber >= finalLeafNumber))
                {
                    hasFlagLeafLiguleAppeared = 1;
                    if (!calendarMoments.Contains("FlagLeafLiguleJustVisible"))
                    {
                        calendarMoments.Add("FlagLeafLiguleJustVisible");
                        calendarCumuls.Add(cumulTT);
                        calendarDates.Add(currentdate);
                    }
                }
            }
            else
            {
                hasFlagLeafLiguleAppeared = 0;
            }
        }
        s.calendarMoments= calendarMoments;
        s.calendarDates= calendarDates;
        s.calendarCumuls= calendarCumuls;
        s.hasFlagLeafLiguleAppeared= hasFlagLeafLiguleAppeared;
    }
}
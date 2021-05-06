#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
# include<numeric>
# include<algorithm>
# include<array>
#include <map>
# include <tuple>
#include "Updateleafflag.h"
using namespace std;

Updateleafflag::Updateleafflag() { }
void Updateleafflag::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
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
    float cumulTT = a.getcumulTT();
    float leafNumber = s.getleafNumber();
    vector<string> calendarMoments = s.getcalendarMoments();
    vector<string> calendarDates = s.getcalendarDates();
    vector<float> calendarCumuls = s.getcalendarCumuls();
    string currentdate = a.getcurrentdate();
    float finalLeafNumber = s.getfinalLeafNumber();
    int hasFlagLeafLiguleAppeared_t1 = s1.gethasFlagLeafLiguleAppeared();
    float phase = s.getphase();
    int hasFlagLeafLiguleAppeared;
    hasFlagLeafLiguleAppeared = 0;
    if (phase >= 1.0f && phase < 4.0f)
    {
        if (leafNumber > 0.0f)
        {
            if (hasFlagLeafLiguleAppeared == 0 && (finalLeafNumber > 0.0f && leafNumber >= finalLeafNumber))
            {
                hasFlagLeafLiguleAppeared = 1;
                if (!(find(calendarMoments.begin(), calendarMoments.end(), "FlagLeafLiguleJustVisible") != calendarMoments.end()))
                {
                    calendarMoments.push_back("FlagLeafLiguleJustVisible");
                    calendarCumuls.push_back(cumulTT);
                    calendarDates.push_back(currentdate);
                }
            }
        }
    }
    s.setcalendarMoments(calendarMoments);
    s.setcalendarDates(calendarDates);
    s.setcalendarCumuls(calendarCumuls);
    s.sethasFlagLeafLiguleAppeared(hasFlagLeafLiguleAppeared);
}
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
#include "Updatecalendar.h"
using namespace std;

Updatecalendar::Updatecalendar() { }
void Updatecalendar::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
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
    float cumulTT = a.getcumulTT();
    vector<string> calendarMoments = s.getcalendarMoments();
    vector<string> calendarDates = s.getcalendarDates();
    vector<float> calendarCumuls = s.getcalendarCumuls();
    string currentdate = a.getcurrentdate();
    float phase = s.getphase();
    if (phase >= 1.0f && phase < 2.0f && !(find(calendarMoments.begin(), calendarMoments.end(), "Emergence") != calendarMoments.end()))
    {
        calendarMoments.push_back("Emergence");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
    }
    else if ( phase >= 2.0f && phase < 3.0f && !(find(calendarMoments.begin(), calendarMoments.end(), "FloralInitiation") != calendarMoments.end()))
    {
        calendarMoments.push_back("FloralInitiation");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
    }
    else if ( phase >= 3.0f && phase < 4.0f && !(find(calendarMoments.begin(), calendarMoments.end(), "Heading") != calendarMoments.end()))
    {
        calendarMoments.push_back("Heading");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
    }
    else if ( phase == 4.0f && !(find(calendarMoments.begin(), calendarMoments.end(), "Anthesis") != calendarMoments.end()))
    {
        calendarMoments.push_back("Anthesis");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
    }
    else if ( phase == 4.5f && !(find(calendarMoments.begin(), calendarMoments.end(), "EndCellDivision") != calendarMoments.end()))
    {
        calendarMoments.push_back("EndCellDivision");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
    }
    else if ( phase >= 5.0f && phase < 6.0f && !(find(calendarMoments.begin(), calendarMoments.end(), "EndGrainFilling") != calendarMoments.end()))
    {
        calendarMoments.push_back("EndGrainFilling");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
    }
    else if ( phase >= 6.0f && phase < 7.0f && !(find(calendarMoments.begin(), calendarMoments.end(), "Maturity") != calendarMoments.end()))
    {
        calendarMoments.push_back("Maturity");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
    }
    s.setcalendarMoments(calendarMoments);
    s.setcalendarDates(calendarDates);
    s.setcalendarCumuls(calendarCumuls);
}
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
#include "Cumulttfrom.h"
using namespace std;

Cumulttfrom::Cumulttfrom() { }
void Cumulttfrom::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
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
    vector<string> calendarMoments_t1 = s1.getcalendarMoments();
    vector<float> calendarCumuls_t1 = s1.getcalendarCumuls();
    float cumulTT = a.getcumulTT();
    float cumulTTFromZC_65;
    float cumulTTFromZC_39;
    float cumulTTFromZC_91;
    cumulTTFromZC_65 = 0.0f;
    cumulTTFromZC_39 = 0.0f;
    cumulTTFromZC_91 = 0.0f;
    if (find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "Anthesis") != calendarMoments_t1.end())
    {
        cumulTTFromZC_65 = cumulTT - calendarCumuls_t1[find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "Anthesis") - calendarMoments_t1.begin()];
    }
    if (find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "FlagLeafLiguleJustVisible") != calendarMoments_t1.end())
    {
        cumulTTFromZC_39 = cumulTT - calendarCumuls_t1[find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "FlagLeafLiguleJustVisible") - calendarMoments_t1.begin()];
    }
    if (find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "EndGrainFilling") != calendarMoments_t1.end())
    {
        cumulTTFromZC_91 = cumulTT - calendarCumuls_t1[find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "EndGrainFilling") - calendarMoments_t1.begin()];
    }
    a.setcumulTTFromZC_65(cumulTTFromZC_65);
    a.setcumulTTFromZC_39(cumulTTFromZC_39);
    a.setcumulTTFromZC_91(cumulTTFromZC_91);
}
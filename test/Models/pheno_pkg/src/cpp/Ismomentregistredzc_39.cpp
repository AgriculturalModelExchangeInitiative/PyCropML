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
#include "Ismomentregistredzc_39.h"
using namespace std;

Ismomentregistredzc_39::Ismomentregistredzc_39() { }
void Ismomentregistredzc_39::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
{
    //- Name: IsMomentRegistredZC_39 -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: Is FlagLeafLiguleJustVisible Model
    //            * Author: Pierre Martre
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: if FlagLeafLiguleJustVisible is already Registred 
    //- inputs:
    //            * name: calendarMoments_t1
    //                          ** description : List containing appearance of each stage at previous time
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** default : ['Sowing']
    //                          ** unit : 
    //                          ** inputtype : variable
    //- outputs:
    //            * name: isMomentRegistredZC_39
    //                          ** description :  if Flag leaf ligule has already appeared 
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    vector<string> calendarMoments_t1 = s1.getcalendarMoments();
    int isMomentRegistredZC_39;
    isMomentRegistredZC_39 = find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "FlagLeafLiguleJustVisible") != calendarMoments_t1.end() ? 1 : 0;
    s.setisMomentRegistredZC_39(isMomentRegistredZC_39);
}
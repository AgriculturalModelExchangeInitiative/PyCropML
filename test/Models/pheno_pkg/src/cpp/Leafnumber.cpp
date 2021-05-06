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
#include "Leafnumber.h"
using namespace std;

Leafnumber::Leafnumber() { }
void Leafnumber::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
{
    //- Name: LeafNumber -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: CalculateLeafNumber Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day
    //- inputs:
    //            * name: deltaTT
    //                          ** description : daily delta TT 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 100
    //                          ** default : 23.5895677277199
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: phyllochron_t1
    //                          ** description : phyllochron
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 0
    //                          ** unit : °C d leaf-1
    //            * name: hasFlagLeafLiguleAppeared
    //                          ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: leafNumber_t1
    //                          ** description :  Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 0
    //                          ** unit : leaf
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
    //            * name: leafNumber
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : leaf
    //                          ** uri : some url
    float deltaTT = a.getdeltaTT();
    float phyllochron_t1 = s1.getphyllochron();
    int hasFlagLeafLiguleAppeared = s.gethasFlagLeafLiguleAppeared();
    float leafNumber_t1 = s1.getleafNumber();
    float phase = s.getphase();
    float leafNumber;
    leafNumber = leafNumber_t1;
    float phyllochron_;
    if (phase >= 1.0f && phase < 4.0f)
    {
        if (hasFlagLeafLiguleAppeared == 0)
        {
            if (phyllochron_t1 == 0.0f)
            {
                phyllochron_ = 0.0000001f;
            }
            else
            {
                phyllochron_ = phyllochron_t1;
            }
            leafNumber = leafNumber_t1 + min(deltaTT / phyllochron_, 0.999f);
        }
    }
    s.setleafNumber(leafNumber);
}
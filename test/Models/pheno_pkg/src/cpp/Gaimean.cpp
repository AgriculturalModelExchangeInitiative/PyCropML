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
#include "Gaimean.h"
using namespace std;

Gaimean::Gaimean() { }
float Gaimean::gettTWindowForPTQ() {return this-> tTWindowForPTQ; }
void Gaimean::settTWindowForPTQ(float _tTWindowForPTQ) { this->tTWindowForPTQ = _tTWindowForPTQ; }
void Gaimean::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
{
    //- Name: GAImean -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: Average GAI on a specific thermal time window
    //            * Author: Loïc Manceau
    //            * Reference: -
    //            * Institution: INRA
    //            * Abstract: -
    //- inputs:
    //            * name: gAI
    //                          ** description : Green Area Index of the day
    //                          ** inputtype : variable
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 500.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: tTWindowForPTQ
    //                          ** description : Thermal Time window for average
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 5000.0
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: deltaTT
    //                          ** description : Thermal time increase of the day
    //                          ** inputtype : variable
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 100.0
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: pastMaxAI_t1
    //                          ** description : Maximum Leaf Area Index reached the current day
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 5000.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: listTTShootWindowForPTQ1_t1
    //                          ** description : List of daily shoot thermal time in the window dedicated to average
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: listGAITTWindowForPTQ_t1
    //                          ** description : List of daily Green Area Index in the window dedicated to average
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //- outputs:
    //            * name: gAImean
    //                          ** description : Mean Green Area Index
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 500.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: pastMaxAI
    //                          ** description : Maximum Leaf Area Index reached the current day
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 5000.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: listTTShootWindowForPTQ1
    //                          ** description : List of daily shoot thermal time in the window dedicated to average
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: listGAITTWindowForPTQ
    //                          ** description : List of daily Green Area Index in the window dedicated to average
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    float gAI = a.getgAI();
    float deltaTT = a.getdeltaTT();
    float pastMaxAI_t1 = s1.getpastMaxAI();
    vector<float> listTTShootWindowForPTQ1_t1 = s1.getlistTTShootWindowForPTQ1();
    vector<float> listGAITTWindowForPTQ_t1 = s1.getlistGAITTWindowForPTQ();
    float gAImean;
    float pastMaxAI;
    vector<float> listTTShootWindowForPTQ1;
    vector<float> listGAITTWindowForPTQ;
    vector<float> TTList;
    vector<float> GAIList;
    float SumTT;
    int count = 0;
    float gai_ = 0.0f;
    float gaiMean_ = 0.0f;
    int countGaiMean = 0;
    int i;
    for (i=0 ; i<listTTShootWindowForPTQ1_t1.size() ; i+=1)
    {
        TTList.push_back(listTTShootWindowForPTQ1_t1[i]);
        GAIList.push_back(listGAITTWindowForPTQ_t1[i]);
    }
    TTList.push_back(deltaTT);
    GAIList.push_back(gAI);
    SumTT = accumulate(TTList.begin(), TTList.end(), decltype(TTList)::value_type(0));
    while ( SumTT > tTWindowForPTQ)
    {
        SumTT = SumTT - TTList[count];
        count = count + 1;
    }
    for (i=count ; i<TTList.size() ; i+=1)
    {
        listTTShootWindowForPTQ1.push_back(TTList[i]);
        listGAITTWindowForPTQ.push_back(GAIList[i]);
    }
    for (i=0 ; i<listGAITTWindowForPTQ.size() ; i+=1)
    {
        gaiMean_ = gaiMean_ + listGAITTWindowForPTQ[i];
        countGaiMean = countGaiMean + 1;
    }
    gaiMean_ = gaiMean_ / countGaiMean;
    gai_ = max(pastMaxAI_t1, gaiMean_);
    pastMaxAI = gai_;
    gAImean = gai_;
    s.setgAImean(gAImean);
    s.setpastMaxAI(pastMaxAI);
    s.setlistTTShootWindowForPTQ1(listTTShootWindowForPTQ1);
    s.setlistGAITTWindowForPTQ(listGAITTWindowForPTQ);
}
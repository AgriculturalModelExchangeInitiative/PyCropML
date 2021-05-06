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
#include "Ptq.h"
using namespace std;

Ptq::Ptq() { }
float Ptq::gettTWindowForPTQ() {return this-> tTWindowForPTQ; }
float Ptq::getkl() {return this-> kl; }
void Ptq::settTWindowForPTQ(float _tTWindowForPTQ) { this->tTWindowForPTQ = _tTWindowForPTQ; }
void Ptq::setkl(float _kl) { this->kl = _kl; }
void Ptq::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
{
    //- Name: PTQ -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: Phyllochron Model
    //            * Author: Pierre Martre
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Calculate Photothermal Quaotient 
    //- inputs:
    //            * name: tTWindowForPTQ
    //                          ** description : Thermal time window in which averages are computed
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 70000.0
    //                          ** default : 70.0
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: kl
    //                          ** description : Exctinction Coefficient
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 50.0
    //                          ** default : 0.45
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: listTTShootWindowForPTQ_t1
    //                          ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** default : [0.0]
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: listPARTTWindowForPTQ_t1
    //                          ** description : List of Daily PAR during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** default : [0.0]
    //                          ** unit : MJ m2 d
    //                          ** uri : some url
    //            * name: listGAITTWindowForPTQ
    //                          ** description : List of daily GAI over TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** default : [0.0, 5.2]
    //                          ** unit : m2 m-2
    //                          ** uri : some url
    //            * name: pAR
    //                          ** description : Daily Photosyntetically Active Radiation
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 10000.0
    //                          ** unit : MJ m² d
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: deltaTT
    //                          ** description : daily delta TT 
    //                          ** variablecategory : auxiliary
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 100.0
    //                          ** default : 0.0
    //                          ** unit : °C d
    //                          ** uri : some url
    //- outputs:
    //            * name: listPARTTWindowForPTQ
    //                          ** description :  List of Daily PAR during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : MJ m2 d
    //            * name: listTTShootWindowForPTQ
    //                          ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : °C d
    //            * name: ptq
    //                          ** description : Photothermal Quotient
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : MJ °C-1 d m-2)
    vector<float> listTTShootWindowForPTQ_t1 = s1.getlistTTShootWindowForPTQ();
    vector<float> listPARTTWindowForPTQ_t1 = s1.getlistPARTTWindowForPTQ();
    vector<float> listGAITTWindowForPTQ = s.getlistGAITTWindowForPTQ();
    float pAR = a.getpAR();
    float deltaTT = a.getdeltaTT();
    vector<float> listPARTTWindowForPTQ;
    vector<float> listTTShootWindowForPTQ;
    float ptq;
    vector<float> TTList;
    vector<float> PARList;
    int i;
    int count;
    float SumTT;
    float parInt = 0.0f;
    float TTShoot;
    for (i=0 ; i<listTTShootWindowForPTQ_t1.size() ; i+=1)
    {
        TTList.push_back(listTTShootWindowForPTQ_t1[i]);
        PARList.push_back(listPARTTWindowForPTQ_t1[i]);
    }
    TTList.push_back(deltaTT);
    PARList.push_back(pAR);
    SumTT = accumulate(TTList.begin(), TTList.end(), decltype(TTList)::value_type(0));
    count = 0;
    while ( SumTT > tTWindowForPTQ)
    {
        SumTT = SumTT - TTList[count];
        count = count + 1;
    }
    for (i=count ; i<TTList.size() ; i+=1)
    {
        listTTShootWindowForPTQ.push_back(TTList[i]);
        listPARTTWindowForPTQ.push_back(PARList[i]);
    }
    for (i=0 ; i<listTTShootWindowForPTQ.size() ; i+=1)
    {
        parInt = parInt + (listPARTTWindowForPTQ[i] * (1 - exp(-kl * listGAITTWindowForPTQ[i])));
    }
    TTShoot = accumulate(listTTShootWindowForPTQ.begin(), listTTShootWindowForPTQ.end(), decltype(listTTShootWindowForPTQ)::value_type(0));
    ptq = parInt / TTShoot;
    s.setlistPARTTWindowForPTQ(listPARTTWindowForPTQ);
    s.setlistTTShootWindowForPTQ(listTTShootWindowForPTQ);
    s.setptq(ptq);
}
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
#include "Vernalizationprogress.h"
using namespace std;

Vernalizationprogress::Vernalizationprogress() { }
float Vernalizationprogress::getminTvern() {return this-> minTvern; }
float Vernalizationprogress::getintTvern() {return this-> intTvern; }
float Vernalizationprogress::getvAI() {return this-> vAI; }
float Vernalizationprogress::getvBEE() {return this-> vBEE; }
float Vernalizationprogress::getminDL() {return this-> minDL; }
float Vernalizationprogress::getmaxDL() {return this-> maxDL; }
float Vernalizationprogress::getmaxTvern() {return this-> maxTvern; }
float Vernalizationprogress::getpNini() {return this-> pNini; }
float Vernalizationprogress::getaMXLFNO() {return this-> aMXLFNO; }
int Vernalizationprogress::getisVernalizable() {return this-> isVernalizable; }
void Vernalizationprogress::setminTvern(float _minTvern) { this->minTvern = _minTvern; }
void Vernalizationprogress::setintTvern(float _intTvern) { this->intTvern = _intTvern; }
void Vernalizationprogress::setvAI(float _vAI) { this->vAI = _vAI; }
void Vernalizationprogress::setvBEE(float _vBEE) { this->vBEE = _vBEE; }
void Vernalizationprogress::setminDL(float _minDL) { this->minDL = _minDL; }
void Vernalizationprogress::setmaxDL(float _maxDL) { this->maxDL = _maxDL; }
void Vernalizationprogress::setmaxTvern(float _maxTvern) { this->maxTvern = _maxTvern; }
void Vernalizationprogress::setpNini(float _pNini) { this->pNini = _pNini; }
void Vernalizationprogress::setaMXLFNO(float _aMXLFNO) { this->aMXLFNO = _aMXLFNO; }
void Vernalizationprogress::setisVernalizable(int _isVernalizable) { this->isVernalizable = _isVernalizable; }
void Vernalizationprogress::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
{
    //- Name: VernalizationProgress -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: VernalizationProgress Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Calculate progress (VernaProg) towards vernalization, but there 
    //        			is no vernalization below minTvern 
    //        			and above maxTvern . The maximum value of VernaProg is 1.
    //        			Progress towards full vernalization is a linear function of shoot 
    //        			temperature (soil temperature until leaf # reach MaxLeafSoil and then
    //        			 canopy temperature)
    //    	
    //- inputs:
    //            * name: dayLength
    //                          ** description : day length
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 12.3037621834005
    //                          ** unit : mm2 m-2
    //                          ** inputtype : variable
    //            * name: deltaTT
    //                          ** description : difference cumul TT between j and j-1 day 
    //                          ** variablecategory : auxiliary
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 100
    //                          ** default : 20.3429985011972
    //                          ** unit : °C d
    //            * name: cumulTT
    //                          ** description : cumul thermal times at currentdate
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 112.330110409888
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: leafNumber_t1
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 0
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //            * name: calendarMoments_t1
    //                          ** description : List containing appearance of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** default : ['Sowing']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarDates_t1
    //                          ** description : List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** default : ['2007/3/21']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarCumuls_t1
    //                          ** description : list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: minTvern
    //                          ** description : Minimum temperature for vernalization to occur
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 60
    //                          ** default : 0.0
    //                          ** unit : °C
    //                          ** inputtype : parameter
    //            * name: intTvern
    //                          ** description : Intermediate temperature for vernalization to occur
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 60
    //                          ** default :  11.0
    //                          ** unit : °C
    //                          ** inputtype : parameter
    //            * name: vAI
    //                          ** description : Response of vernalization rate to temperature
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default :  0.015
    //                          ** unit : d-1 °C-1
    //                          ** inputtype : parameter
    //            * name: vBEE
    //                          ** description : Vernalization rate at 0°C
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.01
    //                          ** unit : d-1
    //                          ** inputtype : parameter
    //            * name: minDL
    //                          ** description : Threshold daylength below which it does influence vernalization rate
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 12
    //                          ** max : 24
    //                          ** default : 8.0
    //                          ** unit : h
    //                          ** inputtype : parameter
    //            * name: maxDL
    //                          ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 24
    //                          ** default : 15.0
    //                          ** unit : h
    //                          ** inputtype : parameter
    //            * name: maxTvern
    //                          ** description : Maximum temperature for vernalization to occur
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 60
    //                          ** default :  23.0
    //                          ** unit : °C
    //                          ** inputtype : parameter
    //            * name: pNini
    //                          ** description : Number of primorida in the apex at emergence
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 24
    //                          ** default : 4.0
    //                          ** unit : primordia
    //                          ** inputtype : parameter
    //            * name: aMXLFNO
    //                          ** description : Absolute maximum leaf number
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 24.0
    //                          ** unit : leaf
    //                          ** inputtype : parameter
    //            * name: vernaprog_t1
    //                          ** description : progression on a 0  to 1 scale of the vernalization
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default :  0.5517254187376879
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: currentdate
    //                          ** description : current date 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DATE
    //                          ** default : 2007/3/27
    //                          ** inputtype : variable
    //                          ** unit : 
    //            * name: isVernalizable
    //                          ** description : true if the plant is vernalizable
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : parameter
    //            * name: minFinalNumber_t1
    //                          ** description : minimum final leaf number
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 5.5
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //- outputs:
    //            * name: vernaprog
    //                          ** description : progression on a 0  to 1 scale of the vernalization
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : 
    //            * name: minFinalNumber
    //                          ** description : minimum final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : leaf
    //            * name: calendarMoments
    //                          ** description : List containing appearance of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** unit : 
    //            * name: calendarDates
    //                          ** description : List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** unit : 
    //            * name: calendarCumuls
    //                          ** description : list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** unit : 
    float dayLength = a.getdayLength();
    float deltaTT = a.getdeltaTT();
    float cumulTT = a.getcumulTT();
    float leafNumber_t1 = s1.getleafNumber();
    vector<string> calendarMoments_t1 = s1.getcalendarMoments();
    vector<string> calendarDates_t1 = s1.getcalendarDates();
    vector<float> calendarCumuls_t1 = s1.getcalendarCumuls();
    float vernaprog_t1 = s1.getvernaprog();
    string currentdate = a.getcurrentdate();
    float minFinalNumber_t1 = s1.getminFinalNumber();
    float vernaprog;
    float minFinalNumber;
    vector<string> calendarMoments;
    vector<string> calendarDates;
    vector<float> calendarCumuls;
    float maxVernaProg;
    float dLverna;
    float primordno;
    float minLeafNumber;
    float potlfno;
    float tt;
    calendarMoments = calendarMoments_t1;
    calendarCumuls = calendarCumuls_t1;
    calendarDates = calendarDates_t1;
    minFinalNumber = minFinalNumber_t1;
    vernaprog = vernaprog_t1;
    if (isVernalizable == 1 && vernaprog_t1 < 1.0f)
    {
        tt = deltaTT;
        if (tt >= minTvern && tt <= intTvern)
        {
            vernaprog = vernaprog_t1 + (vAI * tt) + vBEE;
        }
        else
        {
            vernaprog = vernaprog_t1;
        }
        if (tt > intTvern)
        {
            maxVernaProg = vAI * intTvern + vBEE;
            dLverna = max(minDL, min(maxDL, dayLength));
            vernaprog = vernaprog + max(0.0f, maxVernaProg * (1.0f + ((intTvern - tt) / (maxTvern - intTvern) * ((dLverna - minDL) / (maxDL - minDL)))));
        }
        primordno = 2.0f * leafNumber_t1 + pNini;
        minLeafNumber = minFinalNumber_t1;
        if (vernaprog >= 1.0f || primordno >= aMXLFNO)
        {
            minFinalNumber = max(primordno, minFinalNumber_t1);
            calendarMoments.push_back("EndVernalisation");
            calendarCumuls.push_back(cumulTT);
            calendarDates.push_back(currentdate);
            vernaprog = max(1.0f, vernaprog);
        }
        else
        {
            potlfno = aMXLFNO - ((aMXLFNO - minLeafNumber) * vernaprog);
            if (primordno >= potlfno)
            {
                minFinalNumber = max((potlfno + primordno) / 2.0f, minFinalNumber_t1);
                vernaprog = max(1.0f, vernaprog);
                calendarMoments.push_back("EndVernalisation");
                calendarCumuls.push_back(cumulTT);
                calendarDates.push_back(currentdate);
            }
        }
    }
    s.setvernaprog(vernaprog);
    s.setminFinalNumber(minFinalNumber);
    s.setcalendarMoments(calendarMoments);
    s.setcalendarDates(calendarDates);
    s.setcalendarCumuls(calendarCumuls);
}
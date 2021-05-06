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
#include "Updatephase.h"
using namespace std;

Updatephase::Updatephase() { }
int Updatephase::getisVernalizable() {return this-> isVernalizable; }
float Updatephase::getdse() {return this-> dse; }
float Updatephase::getpFLLAnth() {return this-> pFLLAnth; }
float Updatephase::getdcd() {return this-> dcd; }
float Updatephase::getdgf() {return this-> dgf; }
float Updatephase::getdegfm() {return this-> degfm; }
float Updatephase::getmaxDL() {return this-> maxDL; }
float Updatephase::getsLDL() {return this-> sLDL; }
bool Updatephase::getignoreGrainMaturation() {return this-> ignoreGrainMaturation; }
float Updatephase::getpHEADANTH() {return this-> pHEADANTH; }
string Updatephase::getchoosePhyllUse() {return this-> choosePhyllUse; }
float Updatephase::getp() {return this-> p; }
void Updatephase::setisVernalizable(int _isVernalizable) { this->isVernalizable = _isVernalizable; }
void Updatephase::setdse(float _dse) { this->dse = _dse; }
void Updatephase::setpFLLAnth(float _pFLLAnth) { this->pFLLAnth = _pFLLAnth; }
void Updatephase::setdcd(float _dcd) { this->dcd = _dcd; }
void Updatephase::setdgf(float _dgf) { this->dgf = _dgf; }
void Updatephase::setdegfm(float _degfm) { this->degfm = _degfm; }
void Updatephase::setmaxDL(float _maxDL) { this->maxDL = _maxDL; }
void Updatephase::setsLDL(float _sLDL) { this->sLDL = _sLDL; }
void Updatephase::setignoreGrainMaturation(bool _ignoreGrainMaturation) { this->ignoreGrainMaturation = _ignoreGrainMaturation; }
void Updatephase::setpHEADANTH(float _pHEADANTH) { this->pHEADANTH = _pHEADANTH; }
void Updatephase::setchoosePhyllUse(string _choosePhyllUse) { this->choosePhyllUse = _choosePhyllUse; }
void Updatephase::setp(float _p) { this->p = _p; }
void Updatephase::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
{
    //- Name: UpdatePhase -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: UpdatePhase Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: This strategy advances the phase and calculate the final leaf number
    //    	
    //- inputs:
    //            * name: cumulTT
    //                          ** description : cumul thermal times at current date
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 354.582294511779
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: leafNumber_t1
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default :  4.620511621863958
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //            * name: cumulTTFromZC_39
    //                          ** description : cumul of the thermal time ( DeltaTT) since the moment ZC_39
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0
    //                          ** unit : °C d-1
    //                          ** inputtype : variable
    //            * name: isMomentRegistredZC_39
    //                          ** description : true if ZC_39 is registered in the calendar
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: gAI
    //                          ** description : used to calculate Terminal spikelet
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0.3255196285135
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: grainCumulTT
    //                          ** description : cumulTT used for the grain developpment
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: dayLength
    //                          ** description : length of the day
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : auxiliary
    //                          ** min : 0
    //                          ** max : 24
    //                          ** unit : h
    //                          ** default : 12.7433275303389
    //                          ** inputtype : variable
    //            * name: vernaprog
    //                          ** description : progression on a 0  to 1 scale of the vernalization
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10
    //                          ** default :  1.0532526829571554
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: minFinalNumber
    //                          ** description : minimum final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 6.879410413987549
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //            * name: fixPhyll
    //                          ** description : Phyllochron with sowing date fix
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 91.2
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: isVernalizable
    //                          ** description : true if the plant is vernalizable
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    //                          ** default : 1
    //                          ** inputtype : parameter
    //            * name: dse
    //                          ** description : Thermal time from sowing to emergence
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 105
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: pFLLAnth
    //                          ** description : Phyllochronic duration of the period between flag leaf ligule appearance and anthesis
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : 
    //                          ** default : 2.22
    //                          ** inputtype : parameter
    //            * name: dcd
    //                          ** description : Duration of the endosperm cell division phase
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 100
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: dgf
    //                          ** description : Grain filling duration (from anthesis to physiological maturity)
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 450
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: degfm
    //                          ** description : Grain maturation duration (from physiological maturity to harvest ripeness)
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 50
    //                          ** default : 0
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: maxDL
    //                          ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 24
    //                          ** default : 15
    //                          ** unit : h
    //                          ** inputtype : parameter
    //            * name: sLDL
    //                          ** description : Daylength response of leaf production
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.85
    //                          ** unit : leaf h-1
    //                          ** inputtype : parameter
    //            * name: ignoreGrainMaturation
    //                          ** description : true to ignore grain maturation
    //                          ** parametercategory : species
    //                          ** datatype : BOOLEAN
    //                          ** default : FALSE
    //                          ** unit : 
    //                          ** inputtype : parameter
    //            * name: pHEADANTH
    //                          ** description : Number of phyllochron between heading and anthesiss
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : parameter
    //            * name: choosePhyllUse
    //                          ** description : Switch to choose the type of phyllochron calculation to be used
    //                          ** parametercategory : species
    //                          ** datatype : STRING
    //                          ** unit : 
    //                          ** default : Default
    //                          ** inputtype : parameter
    //            * name: p
    //                          ** description : Phyllochron (Varietal parameter)
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 120
    //                          ** unit : °C d leaf-1
    //                          ** inputtype : parameter
    //            * name: phase_t1
    //                          ** description :  the name of the phase
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: cumulTTFromZC_91
    //                          ** description : cumul of the thermal time (DeltaTT) since the moment ZC_91
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 5000
    //                          ** default : 0
    //                          ** unit : °C d-1
    //                          ** inputtype : variable
    //            * name: phyllochron
    //                          ** description : Phyllochron
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 91.2
    //                          ** unit : °C d leaf-1
    //                          ** inputtype : variable
    //            * name: hasLastPrimordiumAppeared_t1
    //                          ** description : if Last Primordium has Appeared
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: finalLeafNumber_t1
    //                          ** description : final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 0
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //- outputs:
    //            * name: finalLeafNumber
    //                          ** description : final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** unit : leaf
    //            * name: phase
    //                          ** description : the name of the phase
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** unit : 
    //            * name: hasLastPrimordiumAppeared
    //                          ** description : if Last Primordium has Appeared
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    float cumulTT = a.getcumulTT();
    float leafNumber_t1 = s1.getleafNumber();
    float cumulTTFromZC_39 = a.getcumulTTFromZC_39();
    int isMomentRegistredZC_39 = s.getisMomentRegistredZC_39();
    float gAI = a.getgAI();
    float grainCumulTT = a.getgrainCumulTT();
    float dayLength = a.getdayLength();
    float vernaprog = s.getvernaprog();
    float minFinalNumber = s.getminFinalNumber();
    float fixPhyll = a.getfixPhyll();
    float phase_t1 = s1.getphase();
    float cumulTTFromZC_91 = a.getcumulTTFromZC_91();
    float phyllochron = s.getphyllochron();
    int hasLastPrimordiumAppeared_t1 = s1.gethasLastPrimordiumAppeared();
    float finalLeafNumber_t1 = s1.getfinalLeafNumber();
    float finalLeafNumber;
    float phase;
    int hasLastPrimordiumAppeared;
    float ttFromLastLeafToHeading;
    float appFLN;
    float localDegfm;
    float ttFromLastLeafToAnthesis;
    hasLastPrimordiumAppeared = hasLastPrimordiumAppeared_t1;
    finalLeafNumber = finalLeafNumber_t1;
    phase = phase_t1;
    if (phase_t1 >= 0.0f && phase_t1 < 1.0f)
    {
        if (cumulTT >= dse)
        {
            phase = 1.0f;
        }
        else
        {
            phase = phase_t1;
        }
    }
    else if ( phase_t1 >= 1.0f && phase_t1 < 2.0f)
    {
        if (isVernalizable == 1 && vernaprog >= 1.0f || isVernalizable == 0)
        {
            if (dayLength > maxDL)
            {
                finalLeafNumber = minFinalNumber;
                hasLastPrimordiumAppeared = 1;
            }
            else
            {
                appFLN = minFinalNumber + (sLDL * (maxDL - dayLength));
                if (appFLN / 2.0f <= leafNumber_t1)
                {
                    finalLeafNumber = appFLN;
                    hasLastPrimordiumAppeared = 1;
                }
                else
                {
                    phase = phase_t1;
                }
            }
            if (hasLastPrimordiumAppeared == 1)
            {
                phase = 2.0f;
            }
        }
        else
        {
            phase = phase_t1;
        }
    }
    else if ( phase_t1 >= 2.0f && phase_t1 < 4.0f)
    {
        if (isMomentRegistredZC_39 == 1)
        {
            if (phase_t1 < 3.0f)
            {
                ttFromLastLeafToHeading = 0.0f;
                if (choosePhyllUse == "Default")
                {
                    ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * fixPhyll;
                }
                else if ( choosePhyllUse == "PTQ")
                {
                    ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron;
                }
                else if ( choosePhyllUse == "Test")
                {
                    ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p;
                }
                if (cumulTTFromZC_39 >= ttFromLastLeafToHeading)
                {
                    phase = 3.0f;
                }
                else
                {
                    phase = phase_t1;
                }
            }
            else
            {
                phase = phase_t1;
            }
            ttFromLastLeafToAnthesis = 0.0f;
            if (choosePhyllUse == "Default")
            {
                ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll;
            }
            else if ( choosePhyllUse == "PTQ")
            {
                ttFromLastLeafToAnthesis = pFLLAnth * phyllochron;
            }
            else if ( choosePhyllUse == "Test")
            {
                ttFromLastLeafToAnthesis = pFLLAnth * p;
            }
            if (cumulTTFromZC_39 >= ttFromLastLeafToAnthesis)
            {
                phase = 4.0f;
            }
        }
        else
        {
            phase = phase_t1;
        }
    }
    else if ( phase_t1 == 4.0f)
    {
        if (grainCumulTT >= dcd)
        {
            phase = 4.5f;
        }
        else
        {
            phase = phase_t1;
        }
    }
    else if ( phase_t1 == 4.5f)
    {
        if (grainCumulTT >= dgf || gAI <= 0.0f)
        {
            phase = 5.0f;
        }
        else
        {
            phase = phase_t1;
        }
    }
    else if ( phase_t1 >= 5.0f && phase_t1 < 6.0f)
    {
        localDegfm = degfm;
        if (ignoreGrainMaturation)
        {
            localDegfm = -1.0f;
        }
        if (cumulTTFromZC_91 >= localDegfm)
        {
            phase = 6.0f;
        }
        else
        {
            phase = phase_t1;
        }
    }
    else if ( phase_t1 >= 6.0f && phase_t1 < 7.0f)
    {
        phase = phase_t1;
    }
    s.setfinalLeafNumber(finalLeafNumber);
    s.setphase(phase);
    s.sethasLastPrimordiumAppeared(hasLastPrimordiumAppeared);
}
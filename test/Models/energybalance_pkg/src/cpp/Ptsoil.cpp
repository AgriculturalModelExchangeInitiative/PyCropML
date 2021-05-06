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
#include "Ptsoil.h"
using namespace std;

Ptsoil::Ptsoil() { }
float Ptsoil::getAlpha() {return this-> Alpha; }
float Ptsoil::gettau() {return this-> tau; }
float Ptsoil::gettauAlpha() {return this-> tauAlpha; }
void Ptsoil::setAlpha(float _Alpha) { this->Alpha = _Alpha; }
void Ptsoil::settau(float _tau) { this->tau = _tau; }
void Ptsoil::settauAlpha(float _tauAlpha) { this->tauAlpha = _tauAlpha; }
void Ptsoil::Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a)
{
    //- Name: PtSoil -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: PtSoil EnergyLimitedEvaporation Model
    //            * Author: Pierre Martre
    //            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            * Institution: INRA Montpellier
    //            * Abstract: Evaporation from the soil in the energy-limited stage 
    //- inputs:
    //            * name: evapoTranspirationPriestlyTaylor
    //                          ** description : evapoTranspiration Priestly Taylor
    //                          ** variablecategory : rate
    //                          ** datatype : DOUBLE
    //                          ** default : 120
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : g m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //            * name: Alpha
    //                          ** description : Priestley-Taylor evapotranspiration proportionality constant
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 1.5
    //                          ** min : 0
    //                          ** max : 100
    //                          ** unit : 
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: tau
    //                          ** description : plant cover factor
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 0.9983
    //                          ** min : 0
    //                          ** max : 100
    //                          ** unit : 
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: tauAlpha
    //                          ** description : Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLE
    //                          ** default : 0.3
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //- outputs:
    //            * name: energyLimitedEvaporation
    //                          ** description : energy Limited Evaporation 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 5000
    //                          ** unit : g m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    float evapoTranspirationPriestlyTaylor = r.getevapoTranspirationPriestlyTaylor();
    float energyLimitedEvaporation;
    float AlphaE;
    if (tau < tauAlpha)
    {
        AlphaE = 1.0f;
    }
    else
    {
        AlphaE = Alpha - ((Alpha - 1.0f) * (1.0f - tau) / (1.0f - tauAlpha));
    }
    energyLimitedEvaporation = evapoTranspirationPriestlyTaylor / Alpha * AlphaE * tau;
    a.setenergyLimitedEvaporation(energyLimitedEvaporation);
}
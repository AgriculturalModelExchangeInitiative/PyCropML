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
#include "Conductance.h"
using namespace std;

Conductance::Conductance() { }
float Conductance::getvonKarman() {return this-> vonKarman; }
float Conductance::getheightWeatherMeasurements() {return this-> heightWeatherMeasurements; }
float Conductance::getzm() {return this-> zm; }
float Conductance::getzh() {return this-> zh; }
float Conductance::getd() {return this-> d; }
void Conductance::setvonKarman(float _vonKarman) { this->vonKarman = _vonKarman; }
void Conductance::setheightWeatherMeasurements(float _heightWeatherMeasurements) { this->heightWeatherMeasurements = _heightWeatherMeasurements; }
void Conductance::setzm(float _zm) { this->zm = _zm; }
void Conductance::setzh(float _zh) { this->zh = _zh; }
void Conductance::setd(float _d) { this->d = _d; }
void Conductance::Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a)
{
    //- Name: Conductance -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: Conductance Model
    //            * Author: Pierre Martre
    //            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //        
    //            * Institution: INRA/LEPSE Montpellier
    //            * Abstract: The boundary layer conductance is expressed as the wind speed profile above the
    //            canopy and the canopy structure. The approach does not take into account buoyancy
    //            effects. 
    //        
    //- inputs:
    //            * name: vonKarman
    //                          ** description : von Karman constant
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.42
    //                          ** unit : dimensionless
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //            * name: heightWeatherMeasurements
    //                          ** description : reference height of wind and humidity measurements
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10
    //                          ** default : 2
    //                          ** unit : m
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: zm
    //                          ** description : roughness length governing momentum transfer, FAO
    //                          ** parametercategory : constant
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.13
    //                          ** unit : m
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            * name: zh
    //                          ** description : roughness length governing transfer of heat and vapour, FAO
    //                          ** parametercategory : constant
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.013
    //                          ** unit : m
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            * name: d
    //                          ** description : corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 0.67
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : dimensionless
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547rl
    //            * name: plantHeight
    //                          ** description : plant Height
    //                          ** datatype : DOUBLE
    //                          ** default : 0
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : mm
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //                          ** variablecategory : auxiliary
    //            * name: wind
    //                          ** description : wind
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 124000
    //                          ** min : 0
    //                          ** max : 1000000
    //                          ** unit : m/d
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //- outputs:
    //            * name: conductance
    //                          ** description : the boundary layer conductance
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : m/d
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    float plantHeight = a.getplantHeight();
    float wind = a.getwind();
    float conductance;
    float h;
    h = max(10.0f, plantHeight) / 100.0f;
    conductance = wind * pow(vonKarman, 2) / (log((heightWeatherMeasurements - (d * h)) / (zm * h)) * log((heightWeatherMeasurements - (d * h)) / (zh * h)));
    s.setconductance(conductance);
}
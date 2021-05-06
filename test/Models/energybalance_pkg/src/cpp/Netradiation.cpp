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
#include "Netradiation.h"
using namespace std;

Netradiation::Netradiation() { }
float Netradiation::getalbedoCoefficient() {return this-> albedoCoefficient; }
float Netradiation::getstefanBoltzman() {return this-> stefanBoltzman; }
float Netradiation::getelevation() {return this-> elevation; }
void Netradiation::setalbedoCoefficient(float _albedoCoefficient) { this->albedoCoefficient = _albedoCoefficient; }
void Netradiation::setstefanBoltzman(float _stefanBoltzman) { this->stefanBoltzman = _stefanBoltzman; }
void Netradiation::setelevation(float _elevation) { this->elevation = _elevation; }
void Netradiation::Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a)
{
    //- Name: NetRadiation -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: NetRadiation Model
    //            * Author: Pierre Martre
    //            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            * Institution: INRA Montpellier
    //            * Abstract: It is calculated at the surface of the canopy and is givenby the difference between incoming and outgoing radiation of both short
    //                     and long wavelength radiation 
    //- inputs:
    //            * name: minTair
    //                          ** description : minimum air temperature
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -30
    //                          ** max : 45
    //                          ** default : 0.7
    //                          ** unit : °C
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //            * name: maxTair
    //                          ** description : maximum air Temperature
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -30
    //                          ** max : 45
    //                          ** default : 7.2
    //                          ** unit : °C
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //            * name: albedoCoefficient
    //                          ** description : albedo Coefficient
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 0.23
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: stefanBoltzman
    //                          ** description : stefan Boltzman constant
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 4.903E-09
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: elevation
    //                          ** description : elevation
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 0
    //                          ** min : -500
    //                          ** max : 10000
    //                          ** unit : m
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: solarRadiation
    //                          ** description : solar Radiation
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 3
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : MJ m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //            * name: vaporPressure
    //                          ** description : vapor Pressure
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 6.1
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : hPa
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //            * name: extraSolarRadiation
    //                          ** description : extra Solar Radiation
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 11.7
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : MJ m2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //- outputs:
    //            * name: netRadiation
    //                          ** description :  net radiation 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 5000
    //                          ** unit : MJ m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            * name: netOutGoingLongWaveRadiation
    //                          ** description : net OutGoing Long Wave Radiation 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 5000
    //                          ** unit : g m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    float minTair = a.getminTair();
    float maxTair = a.getmaxTair();
    float solarRadiation = a.getsolarRadiation();
    float vaporPressure = a.getvaporPressure();
    float extraSolarRadiation = a.getextraSolarRadiation();
    float netRadiation;
    float netOutGoingLongWaveRadiation;
    float Nsr;
    float clearSkySolarRadiation;
    float averageT;
    float surfaceEmissivity;
    float cloudCoverFactor;
    float Nolr;
    Nsr = (1.0f - albedoCoefficient) * solarRadiation;
    clearSkySolarRadiation = (0.75f + (2 * pow(10.0f, -5) * elevation)) * extraSolarRadiation;
    averageT = (pow(maxTair + 273.16f, 4) + pow(minTair + 273.16f, 4)) / 2.0f;
    surfaceEmissivity = 0.34f - (0.14f * sqrt(vaporPressure / 10.0f));
    cloudCoverFactor = 1.35f * (solarRadiation / clearSkySolarRadiation) - 0.35f;
    Nolr = stefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor;
    netRadiation = Nsr - Nolr;
    netOutGoingLongWaveRadiation = Nolr;
    a.setnetRadiation(netRadiation);
    a.setnetOutGoingLongWaveRadiation(netOutGoingLongWaveRadiation);
}
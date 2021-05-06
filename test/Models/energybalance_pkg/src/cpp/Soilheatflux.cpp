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
#include "Soilheatflux.h"
using namespace std;

Soilheatflux::Soilheatflux() { }
float Soilheatflux::gettau() {return this-> tau; }
void Soilheatflux::settau(float _tau) { this->tau = _tau; }
void Soilheatflux::Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a)
{
    //- Name: SoilHeatFlux -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: SoilHeatFlux Model
    //            * Author: Pierre Martre
    //            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            * Institution: INRA/LEPSE Montpellier
    //            * Abstract: The available energy in the soil 
    //- inputs:
    //            * name: netRadiationEquivalentEvaporation
    //                          ** variablecategory : state
    //                          ** description : net Radiation Equivalent Evaporation
    //                          ** datatype : DOUBLE
    //                          ** default : 638.142
    //                          ** min : 0
    //                          ** max : 5000
    //                          ** unit : g m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
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
    //            * name: soilEvaporation
    //                          ** description : soil Evaporation
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** default : 448.240
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : g m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //- outputs:
    //            * name: soilHeatFlux
    //                          ** description : soil Heat Flux 
    //                          ** variablecategory : rate
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : g m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    float netRadiationEquivalentEvaporation = s.getnetRadiationEquivalentEvaporation();
    float soilEvaporation = s.getsoilEvaporation();
    float soilHeatFlux;
    soilHeatFlux = tau * netRadiationEquivalentEvaporation - soilEvaporation;
    r.setsoilHeatFlux(soilHeatFlux);
}
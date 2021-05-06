# coding: utf8
from pycropml.units import u
from copy import copy

import numpy
from math import *

def model_cropheatflux(netRadiationEquivalentEvaporation = 638.142,
         soilHeatFlux = 188.817,
         potentialTranspiration = 1.413):
    """
     - Name: CropHeatFlux -Version: 1.0, -Time step: 1
     - Description:
                 * Title: CropHeatFlux Model
                 * Author: Pierre Martre
                 * Reference: abModelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA/LEPSE Montpellier
                 * Abstract: It is calculated from net Radiation, soil heat flux and potential transpiration 
     - inputs:
                 * name: netRadiationEquivalentEvaporation
                               ** min : 0
                               ** default : 638.142
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : g m-2 d-1
                               ** description : net Radiation Equivalent Evaporation
                 * name: soilHeatFlux
                               ** min : 0
                               ** default : 188.817
                               ** max : 1000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : g m-2 d-1
                               ** description : soil Heat Flux
                 * name: potentialTranspiration
                               ** min : 0
                               ** default :  1.413
                               ** max : 1000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : g m-2 d-1
                               ** description : potential Transpiration
     - outputs:
                 * name: cropHeatFlux
                               ** min : 0
                               ** variablecategory : rate
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** unit : g m-2 d-1
                               ** description :  crop Heat Flux
    """

    cropHeatFlux = netRadiationEquivalentEvaporation - soilHeatFlux - potentialTranspiration
    return cropHeatFlux
# coding: utf8
from pycropml.units import u
from copy import copy

import numpy
from math import *

def model_diffusionlimitedevaporation(deficitOnTopLayers = 5341.0,
         soilDiffusionConstant = 4.2):
    """
     - Name: DiffusionLimitedEvaporation -Version: 1.0, -Time step: 1
     - Description:
                 * Title: DiffusionLimitedEvaporation Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA Montpellier
                 * Abstract: the evaporation from the diffusion limited soil 
     - inputs:
                 * name: deficitOnTopLayers
                               ** min : 0
                               ** default : 5341
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : g m-2 d-1
                               ** description : deficit On TopLayers
                 * name: soilDiffusionConstant
                               ** parametercategory : soil
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 4.2
                               ** inputtype : parameter
                               ** unit : 
                               ** description : soil Diffusion Constant
     - outputs:
                 * name: diffusionLimitedEvaporation
                               ** min : 0
                               ** variablecategory : state
                               ** max : 5000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** unit : g m-2 d-1
                               ** description : the evaporation from the diffusion limited soil 
    """

    if deficitOnTopLayers / 1000.0 <= 0.0:
        diffusionLimitedEvaporation = 8.3 * 1000.0
    else:
        if deficitOnTopLayers / 1000.0 < 25.0:
            diffusionLimitedEvaporation = 2.0 * soilDiffusionConstant * soilDiffusionConstant / (deficitOnTopLayers / 1000.0) * 1000.0
        else:
            diffusionLimitedEvaporation = 0.0
    return diffusionLimitedEvaporation
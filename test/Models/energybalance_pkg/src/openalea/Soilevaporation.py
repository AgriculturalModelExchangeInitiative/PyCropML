# coding: utf8
from pycropml.units import u
from copy import copy

import numpy
from math import *

def model_soilevaporation(diffusionLimitedEvaporation = 6605.505,
         energyLimitedEvaporation = 448.24):
    """
     - Name: SoilEvaporation -Version: 1.0, -Time step: 1
     - Description:
                 * Title: SoilEvaporation Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA Montpellier
                 * Abstract: Starting from a soil at field capacity, soil evaporation  is assumed to
                     be energy limited during the first phase of evaporation and diffusion limited thereafter.
                     Hence, the soil evaporation model considers these two processes taking the minimum between
                     the energy limited evaporation (PtSoil) and the diffused limited
                     evaporation 
     - inputs:
                 * name: diffusionLimitedEvaporation
                               ** min : 0
                               ** default : 6605.505
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : g m-2 d-1
                               ** description : diffusion Limited Evaporation
                 * name: energyLimitedEvaporation
                               ** min : 0
                               ** default : 448.240
                               ** max : 1000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : g m-2 d-1
                               ** description : energy Limited Evaporation
     - outputs:
                 * name: soilEvaporation
                               ** min : 0
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** unit : g m-2 d-1
                               ** description : soil Evaporation
    """

    soilEvaporation = min(diffusionLimitedEvaporation, energyLimitedEvaporation)
    return soilEvaporation
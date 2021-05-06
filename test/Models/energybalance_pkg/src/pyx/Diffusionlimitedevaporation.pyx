import numpy 
from math import *
def model_diffusionlimitedevaporation(float deficitOnTopLayers=5341.0,
                                      float soilDiffusionConstant=4.2):
    """

    DiffusionLimitedEvaporation Model
    Author: Pierre Martre
    Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
            Evapotranspiration and canopy and soil temperature calculations
    Institution: INRA Montpellier
    Abstract: the evaporation from the diffusion limited soil 

    """
    cdef float diffusionLimitedEvaporation
    if (deficitOnTopLayers / 1000.0 <= 0.0): diffusionLimitedEvaporation = 8.3 * 1000.0
    else :
        if (deficitOnTopLayers / 1000.0 < 25.0):
            diffusionLimitedEvaporation = (2.0 * soilDiffusionConstant * soilDiffusionConstant / (deficitOnTopLayers / 1000.0)) * 1000.0
        else:
            diffusionLimitedEvaporation = 0.0
    return  diffusionLimitedEvaporation

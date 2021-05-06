import numpy 
from math import *
def model_soilheatflux(float netRadiationEquivalentEvaporation=638.142,
                       float tau=0.9983,
                       float soilEvaporation=448.24):
    """

    SoilHeatFlux Model
    Author: Pierre Martre
    Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
            Evapotranspiration and canopy and soil temperature calculations
    Institution: INRA/LEPSE Montpellier
    Abstract: The available energy in the soil 

    """
    cdef float soilHeatFlux
    soilHeatFlux = tau * netRadiationEquivalentEvaporation - soilEvaporation
    return  soilHeatFlux

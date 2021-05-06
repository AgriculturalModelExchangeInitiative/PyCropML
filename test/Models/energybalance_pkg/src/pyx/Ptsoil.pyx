import numpy 
from math import *
def model_ptsoil(float evapoTranspirationPriestlyTaylor=120.0,
                 float Alpha=1.5,
                 float tau=0.9983,
                 float tauAlpha=0.3):
    """

    PtSoil EnergyLimitedEvaporation Model
    Author: Pierre Martre
    Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
            Evapotranspiration and canopy and soil temperature calculations
    Institution: INRA Montpellier
    Abstract: Evaporation from the soil in the energy-limited stage 

    """
    cdef float energyLimitedEvaporation
    cdef float AlphaE
    if (tau < tauAlpha):
        AlphaE = 1.0
    else :
        AlphaE = Alpha - ((Alpha - 1.0) * (1.0 - tau) / (1.0 - tauAlpha))
    energyLimitedEvaporation= (evapoTranspirationPriestlyTaylor / Alpha) * AlphaE * tau
    return  energyLimitedEvaporation

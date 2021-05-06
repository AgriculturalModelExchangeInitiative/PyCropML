import numpy 
from math import *
def model_priestlytaylor(float netRadiationEquivalentEvaporation=638.142,
                         float hslope=0.584,
                         float psychrometricConstant=0.66,
                         float Alpha=1.5):
    """

    evapoTranspirationPriestlyTaylor  Model
    Author: Pierre Martre
    Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
            Evapotranspiration and canopy and soil temperature calculations
    Institution: INRA Montpellier
    Abstract: Calculate Energy Balance 

    """
    cdef float evapoTranspirationPriestlyTaylor
    evapoTranspirationPriestlyTaylor = max((Alpha * hslope * (netRadiationEquivalentEvaporation) / (hslope + psychrometricConstant)), 0.0)
    return  evapoTranspirationPriestlyTaylor

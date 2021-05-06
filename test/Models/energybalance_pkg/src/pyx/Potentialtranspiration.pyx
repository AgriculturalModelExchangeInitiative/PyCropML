import numpy 
from math import *
def model_potentialtranspiration(float evapoTranspiration=830.958,
                                 float tau=0.9983):
    """

    PotentialTranspiration Model
    Author: Pierre Martre
    Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
            Evapotranspiration and canopy and soil temperature calculations
    Institution: INRA/LEPSE Montpellier
    Abstract: SiriusQuality2 uses availability of water from the soil reservoir as a method to restrict
                    transpiration as soil moisture is depleted 

    """
    cdef float potentialTranspiration
    potentialTranspiration= evapoTranspiration * (1.0 - tau)
    return  potentialTranspiration

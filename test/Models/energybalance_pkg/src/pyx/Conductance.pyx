import numpy 
from math import *
def model_conductance(float vonKarman=0.42,
                      float heightWeatherMeasurements=2.0,
                      float zm=0.13,
                      float zh=0.013,
                      float d=0.67,
                      float plantHeight=0.0,
                      float wind=124000.0):
    """

    Conductance Model
    Author: Pierre Martre
    Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
            Evapotranspiration and canopy and soil temperature calculations
        
    Institution: INRA/LEPSE Montpellier
    Abstract: The boundary layer conductance is expressed as the wind speed profile above the
            canopy and the canopy structure. The approach does not take into account buoyancy
            effects. 
        

    """
    cdef float conductance
    cdef float h
    h = max(10.0, plantHeight) / 100.0
    conductance = (wind * pow(vonKarman, 2)) / (log((heightWeatherMeasurements - d * h) / (zm * h)) * log((heightWeatherMeasurements - d * h) / (zh * h)))
    return  conductance

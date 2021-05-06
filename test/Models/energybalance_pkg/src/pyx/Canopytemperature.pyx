import numpy 
from math import *
def model_canopytemperature(float minTair=0.7,
                            float maxTair=7.2,
                            float cropHeatFlux=447.912,
                            float conductance=598.685,
                            float lambdaV=2.454,
                            float rhoDensityAir=1.225,
                            float specificHeatCapacityAir=0.00101):
    """

    CanopyTemperature Model
    Author: Pierre Martre
    Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
            Evapotranspiration and canopy and soil temperature calculations
    Institution: INRA/LEPSE Montpellier
    Abstract: It is calculated from the crop heat flux and the boundary layer conductance 

    """
    cdef float minCanopyTemperature
    cdef float maxCanopyTemperature
    minCanopyTemperature = minTair + cropHeatFlux / ((rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV) * 1000.0)
    maxCanopyTemperature = maxTair + cropHeatFlux / ((rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV) * 1000.0)
    return  minCanopyTemperature, maxCanopyTemperature

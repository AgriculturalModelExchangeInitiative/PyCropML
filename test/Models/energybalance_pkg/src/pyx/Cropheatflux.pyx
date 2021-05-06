import numpy 
from math import *
def model_cropheatflux(float netRadiationEquivalentEvaporation=638.142,
                       float soilHeatFlux=188.817,
                       float potentialTranspiration=1.413):
    """

    CropHeatFlux Model
    Author: Pierre Martre
    Reference: abModelling energy balance in the wheat crop model SiriusQuality2:
            Evapotranspiration and canopy and soil temperature calculations
    Institution: INRA/LEPSE Montpellier
    Abstract: It is calculated from net Radiation, soil heat flux and potential transpiration 

    """
    cdef float cropHeatFlux
    cropHeatFlux = netRadiationEquivalentEvaporation - soilHeatFlux - potentialTranspiration
    return  cropHeatFlux

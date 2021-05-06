import numpy 
from math import *
def model_netradiation(float minTair=0.7,
                       float maxTair=7.2,
                       float albedoCoefficient=0.23,
                       float stefanBoltzman=4.903e-09,
                       float elevation=0.0,
                       float solarRadiation=3.0,
                       float vaporPressure=6.1,
                       float extraSolarRadiation=11.7):
    """

    NetRadiation Model
    Author: Pierre Martre
    Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
            Evapotranspiration and canopy and soil temperature calculations
    Institution: INRA Montpellier
    Abstract: It is calculated at the surface of the canopy and is givenby the difference between incoming and outgoing radiation of both short
                     and long wavelength radiation 

    """
    cdef float netRadiation
    cdef float netOutGoingLongWaveRadiation
    cdef float Nsr, clearSkySolarRadiation, averageT, surfaceEmissivity, cloudCoverFactor, Nolr
    Nsr = (1.0 - albedoCoefficient) * solarRadiation
    clearSkySolarRadiation = (0.75 + 2 * pow(10.0, -5) * elevation) * extraSolarRadiation
    averageT = (pow(maxTair + 273.16, 4) + pow(minTair + 273.16, 4)) / 2.0
    surfaceEmissivity = (0.34 - 0.14 * sqrt(vaporPressure / 10.0))
    cloudCoverFactor = (1.35 * (solarRadiation / clearSkySolarRadiation) - 0.35)
    Nolr = stefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor
    netRadiation= Nsr - Nolr
    netOutGoingLongWaveRadiation = Nolr
    return  netRadiation, netOutGoingLongWaveRadiation

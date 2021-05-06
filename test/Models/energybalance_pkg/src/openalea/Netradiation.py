# coding: utf8
from pycropml.units import u
from copy import copy

import numpy
from math import *

def model_netradiation(minTair = 0.7,
         maxTair = 7.2,
         albedoCoefficient = 0.23,
         stefanBoltzman = 4.903e-09,
         elevation = 0.0,
         solarRadiation = 3.0,
         vaporPressure = 6.1,
         extraSolarRadiation = 11.7):
    """
     - Name: NetRadiation -Version: 1.0, -Time step: 1
     - Description:
                 * Title: NetRadiation Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA Montpellier
                 * Abstract: It is calculated at the surface of the canopy and is givenby the difference between incoming and outgoing radiation of both short
                          and long wavelength radiation 
     - inputs:
                 * name: minTair
                               ** min : -30
                               ** default : 0.7
                               ** max : 45
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C
                               ** description : minimum air temperature
                 * name: maxTair
                               ** min : -30
                               ** default : 7.2
                               ** max : 45
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C
                               ** description : maximum air Temperature
                 * name: albedoCoefficient
                               ** parametercategory : constant
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 0.23
                               ** inputtype : parameter
                               ** unit : 
                               ** description : albedo Coefficient
                 * name: stefanBoltzman
                               ** parametercategory : constant
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 4.903E-09
                               ** inputtype : parameter
                               ** unit : 
                               ** description : stefan Boltzman constant
                 * name: elevation
                               ** parametercategory : constant
                               ** min : -500
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 0
                               ** inputtype : parameter
                               ** unit : m
                               ** description : elevation
                 * name: solarRadiation
                               ** min : 0
                               ** default : 3
                               ** max : 1000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : MJ m-2 d-1
                               ** description : solar Radiation
                 * name: vaporPressure
                               ** min : 0
                               ** default : 6.1
                               ** max : 1000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : hPa
                               ** description : vapor Pressure
                 * name: extraSolarRadiation
                               ** min : 0
                               ** default : 11.7
                               ** max : 1000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : MJ m2 d-1
                               ** description : extra Solar Radiation
     - outputs:
                 * name: netRadiation
                               ** min : 0
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** unit : MJ m-2 d-1
                               ** description :  net radiation 
                 * name: netOutGoingLongWaveRadiation
                               ** min : 0
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** unit : g m-2 d-1
                               ** description : net OutGoing Long Wave Radiation 
    """

    Nsr = (1.0 - albedoCoefficient) * solarRadiation
    clearSkySolarRadiation = (0.75 + (2 * pow(10.0, -5) * elevation)) * extraSolarRadiation
    averageT = (pow(maxTair + 273.16, 4) + pow(minTair + 273.16, 4)) / 2.0
    surfaceEmissivity = 0.34 - (0.14 * sqrt(vaporPressure / 10.0))
    cloudCoverFactor = 1.35 * (solarRadiation / clearSkySolarRadiation) - 0.35
    Nolr = stefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor
    netRadiation = Nsr - Nolr
    netOutGoingLongWaveRadiation = Nolr
    return (netRadiation, netOutGoingLongWaveRadiation)
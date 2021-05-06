# coding: utf8
from pycropml.units import u
from copy import copy

import numpy
from math import *

def model_canopytemperature(minTair = 0.7,
         maxTair = 7.2,
         cropHeatFlux = 447.912,
         conductance = 598.685,
         lambdaV = 2.454,
         rhoDensityAir = 1.225,
         specificHeatCapacityAir = 0.00101):
    """
     - Name: CanopyTemperature -Version: 1.0, -Time step: 1
     - Description:
                 * Title: CanopyTemperature Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA/LEPSE Montpellier
                 * Abstract: It is calculated from the crop heat flux and the boundary layer conductance 
     - inputs:
                 * name: minTair
                               ** min : -30
                               ** default : 0.7
                               ** max : 45
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** inputtype : variable
                               ** unit : degC
                               ** description : minimum air temperature
                 * name: maxTair
                               ** min : -30
                               ** default : 7.2
                               ** max : 45
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** inputtype : variable
                               ** unit : degC
                               ** description : maximum air Temperature
                 * name: cropHeatFlux
                               ** min : 0
                               ** default : 447.912
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : g/m**2/d
                               ** description : Crop heat flux
                 * name: conductance
                               ** min : 0
                               ** default : 598.685
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : m/d
                               ** description : the boundary layer conductance
                 * name: lambdaV
                               ** parametercategory : constant
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 2.454
                               ** inputtype : parameter
                               ** unit : MJ/kg
                               ** description : latent heat of vaporization of water
                 * name: rhoDensityAir
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 1.225
                               ** inputtype : parameter
                               ** unit : kg/m**3
                               ** description : Density of air
                 * name: specificHeatCapacityAir
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 0.00101
                               ** inputtype : parameter
                               ** unit : MJ/kg/degC
                               ** description : Specific heat capacity of dry air
     - outputs:
                 * name: minCanopyTemperature
                               ** min : -30
                               ** datatype : DOUBLE
                               ** max : 45
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : state
                               ** unit : degC
                               ** description : minimal Canopy Temperature  
                 * name: maxCanopyTemperature
                               ** min : -30
                               ** datatype : DOUBLE
                               ** max : 45
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : state
                               ** unit : degC
                               ** description : maximal Canopy Temperature 
    """

    minCanopyTemperature = minTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0))
    maxCanopyTemperature = maxTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0))
    return (minCanopyTemperature, maxCanopyTemperature)
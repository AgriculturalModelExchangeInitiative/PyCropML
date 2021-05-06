# coding: utf8
from pycropml.units import u
from copy import copy

import numpy
from math import *

def model_conductance(vonKarman = 0.42,
         heightWeatherMeasurements = 2.0,
         zm = 0.13,
         zh = 0.013,
         d = 0.67,
         plantHeight = 0.0,
         wind = 124000.0):
    """
     - Name: Conductance -Version: 1.0, -Time step: 1
     - Description:
                 * Title: Conductance Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
             
                 * Institution: INRA/LEPSE Montpellier
                 * Abstract: The boundary layer conductance is expressed as the wind speed profile above the
                 canopy and the canopy structure. The approach does not take into account buoyancy
                 effects. 
             
     - inputs:
                 * name: vonKarman
                               ** parametercategory : constant
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 0.42
                               ** inputtype : parameter
                               ** unit : dimensionless
                               ** description : von Karman constant
                 * name: heightWeatherMeasurements
                               ** parametercategory : soil
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 2
                               ** inputtype : parameter
                               ** unit : m
                               ** description : reference height of wind and humidity measurements
                 * name: zm
                               ** parametercategory : constant
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 0.13
                               ** inputtype : parameter
                               ** unit : m
                               ** description : roughness length governing momentum transfer, FAO
                 * name: zh
                               ** parametercategory : constant
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 0.013
                               ** inputtype : parameter
                               ** unit : m
                               ** description : roughness length governing transfer of heat and vapour, FAO
                 * name: d
                               ** parametercategory : constant
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547rl
                               ** default : 0.67
                               ** inputtype : parameter
                               ** unit : dimensionless
                               ** description : corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO
                 * name: plantHeight
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 0
                               ** variablecategory : auxiliary
                               ** inputtype : variable
                               ** unit : mm
                               ** description : plant Height
                 * name: wind
                               ** min : 0
                               ** default : 124000
                               ** max : 1000000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : m/d
                               ** description : wind
     - outputs:
                 * name: conductance
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** unit : m/d
                               ** description : the boundary layer conductance
    """

    h = max(10.0, plantHeight) / 100.0
    conductance = wind * pow(vonKarman, 2) / (log((heightWeatherMeasurements - (d * h)) / (zm * h)) * log((heightWeatherMeasurements - (d * h)) / (zh * h)))
    return conductance
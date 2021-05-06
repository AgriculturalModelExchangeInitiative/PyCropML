# coding: utf8
from pycropml.units import u
from copy import copy

import numpy
from math import *

def model_netradiationequivalentevaporation(lambdaV = 2.454,
         netRadiation = 1.566):
    """
     - Name: NetRadiationEquivalentEvaporation -Version: 1.0, -Time step: 1
     - Description:
                 * Title: NetRadiationEquivalentEvaporation Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA/LEPSE Montpellier
                 * Abstract:  It is given by dividing net radiation by latent heat of vaporization of water 
     - inputs:
                 * name: lambdaV
                               ** parametercategory : constant
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 2.454
                               ** inputtype : parameter
                               ** unit : MJ kg-1
                               ** description : latent heat of vaporization of water
                 * name: netRadiation
                               ** min : 0
                               ** default : 1.566
                               ** max : 5000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : MJ m-2 d-1
                               ** description : net radiation
     - outputs:
                 * name: netRadiationEquivalentEvaporation
                               ** min : 0
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** unit : g m-2 d-1
                               ** description : net Radiation in Equivalent Evaporation 
    """

    netRadiationEquivalentEvaporation = netRadiation / lambdaV * 1000.0
    return netRadiationEquivalentEvaporation
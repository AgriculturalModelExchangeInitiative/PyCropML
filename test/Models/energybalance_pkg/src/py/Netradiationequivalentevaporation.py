# coding: utf8
from pycropml.units import u
from copy import copy
from array import array

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
                               ** description : latent heat of vaporization of water
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 2.454
                               ** min : 0
                               ** max : 10
                               ** unit : MJ kg-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: netRadiation
                               ** description : net radiation
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** default : 1.566
                               ** min : 0
                               ** max : 5000
                               ** unit : MJ m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
     - outputs:
                 * name: netRadiationEquivalentEvaporation
                               ** variablecategory : auxiliary
                               ** description : net Radiation in Equivalent Evaporation 
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    netRadiationEquivalentEvaporation = netRadiation / lambdaV * 1000.0
    return netRadiationEquivalentEvaporation
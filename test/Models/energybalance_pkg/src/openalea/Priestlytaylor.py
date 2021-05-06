# coding: utf8
from pycropml.units import u
from copy import copy

import numpy
from math import *

def model_priestlytaylor(netRadiationEquivalentEvaporation = 638.142,
         hslope = 0.584,
         psychrometricConstant = 0.66,
         Alpha = 1.5):
    """
     - Name: PriestlyTaylor -Version: 1.0, -Time step: 1
     - Description:
                 * Title: evapoTranspirationPriestlyTaylor  Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA Montpellier
                 * Abstract: Calculate Energy Balance 
     - inputs:
                 * name: netRadiationEquivalentEvaporation
                               ** min : 0
                               ** default : 638.142
                               ** max : 5000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : g m-2 d-1
                               ** description : net Radiation in Equivalent Evaporation
                 * name: hslope
                               ** min : 0
                               ** default : 0.584
                               ** max : 1000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : hPa °C-1
                               ** description : the slope of saturated vapor pressure temperature curve at a given temperature 
                 * name: psychrometricConstant
                               ** parametercategory : constant
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 0.66
                               ** inputtype : parameter
                               ** unit : 
                               ** description : psychrometric constant
                 * name: Alpha
                               ** parametercategory : constant
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 100
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 1.5
                               ** inputtype : parameter
                               ** unit : 
                               ** description : Priestley-Taylor evapotranspiration proportionality constant
     - outputs:
                 * name: evapoTranspirationPriestlyTaylor
                               ** min : 0
                               ** variablecategory : rate
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** unit : g m-2 d-1
                               ** description : evapoTranspiration of Priestly Taylor 
    """

    evapoTranspirationPriestlyTaylor = max(Alpha * hslope * netRadiationEquivalentEvaporation / (hslope + psychrometricConstant), 0.0)
    return evapoTranspirationPriestlyTaylor
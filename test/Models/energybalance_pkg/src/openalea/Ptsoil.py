# coding: utf8
from pycropml.units import u
from copy import copy

import numpy
from math import *

def model_ptsoil(evapoTranspirationPriestlyTaylor = 120.0,
         Alpha = 1.5,
         tau = 0.9983,
         tauAlpha = 0.3):
    """
     - Name: PtSoil -Version: 1.0, -Time step: 1
     - Description:
                 * Title: PtSoil EnergyLimitedEvaporation Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA Montpellier
                 * Abstract: Evaporation from the soil in the energy-limited stage 
     - inputs:
                 * name: evapoTranspirationPriestlyTaylor
                               ** min : 0
                               ** default : 120
                               ** max : 1000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : g m-2 d-1
                               ** description : evapoTranspiration Priestly Taylor
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
                 * name: tau
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 100
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 0.9983
                               ** inputtype : parameter
                               ** unit : 
                               ** description : plant cover factor
                 * name: tauAlpha
                               ** parametercategory : soil
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 0.3
                               ** inputtype : parameter
                               ** unit : 
                               ** description : Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1
     - outputs:
                 * name: energyLimitedEvaporation
                               ** min : 0
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** unit : g m-2 d-1
                               ** description : energy Limited Evaporation 
    """

    if tau < tauAlpha:
        AlphaE = 1.0
    else:
        AlphaE = Alpha - ((Alpha - 1.0) * (1.0 - tau) / (1.0 - tauAlpha))
    energyLimitedEvaporation = evapoTranspirationPriestlyTaylor / Alpha * AlphaE * tau
    return energyLimitedEvaporation
# coding: utf8
from pycropml.units import u
from copy import copy

import numpy
from math import *

def model_potentialtranspiration(evapoTranspiration = 830.958,
         tau = 0.9983):
    """
     - Name: PotentialTranspiration -Version: 1.0, -Time step: 1
     - Description:
                 * Title: PotentialTranspiration Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA/LEPSE Montpellier
                 * Abstract: SiriusQuality2 uses availability of water from the soil reservoir as a method to restrict
                         transpiration as soil moisture is depleted 
     - inputs:
                 * name: evapoTranspiration
                               ** min : 0
                               ** default : 830.958
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : mm
                               ** description : evapoTranspiration
                 * name: tau
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 0.9983
                               ** inputtype : parameter
                               ** unit : 
                               ** description : plant cover factor
     - outputs:
                 * name: potentialTranspiration
                               ** min : 0
                               ** variablecategory : rate
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** unit : g m-2 d-1
                               ** description : potential Transpiration 
    """

    potentialTranspiration = evapoTranspiration * (1.0 - tau)
    return potentialTranspiration
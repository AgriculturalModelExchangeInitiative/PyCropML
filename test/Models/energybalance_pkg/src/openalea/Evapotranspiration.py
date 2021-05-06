# coding: utf8
from pycropml.units import u
from copy import copy

import numpy
from math import *

def model_evapotranspiration(isWindVpDefined = 1,
         evapoTranspirationPriestlyTaylor = 449.367,
         evapoTranspirationPenman = 830.958):
    """
     - Name: EvapoTranspiration -Version: 1.0, -Time step: 1
     - Description:
                 * Title: Evapotranspiration Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA Montpellier
                 * Abstract: According to the availability of wind and/or vapor pressure daily data, the
                 SiriusQuality2 model calculates the evapotranspiration rate using the Penman (if wind
                 and vapor pressure data are available) (Penman 1948) or the Priestly-Taylor
                 (Priestley and Taylor 1972) method 
     - inputs:
                 * name: isWindVpDefined
                               ** parametercategory : constant
                               ** min : 0
                               ** datatype : INT
                               ** max : 1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** default : 1
                               ** inputtype : parameter
                               ** unit : 
                               ** description : if wind and vapour pressure are defined
                 * name: evapoTranspirationPriestlyTaylor
                               ** default : 449.367
                               ** description : evapoTranspiration of Priestly Taylor 
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** variablecategory : rate
                               ** inputtype : variable
                               ** unit : mm
                 * name: evapoTranspirationPenman
                               ** min : 0
                               ** default : 830.958
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** inputtype : variable
                               ** unit : mm
                               ** description : evapoTranspiration of Penman 
     - outputs:
                 * name: evapoTranspiration
                               ** min : 0
                               ** variablecategory : rate
                               ** max : 10000
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** datatype : DOUBLE
                               ** unit : mm
                               ** description : evapoTranspiration
    """

    if isWindVpDefined == 1:
        evapoTranspiration = evapoTranspirationPenman
    else:
        evapoTranspiration = evapoTranspirationPriestlyTaylor
    return evapoTranspiration
# coding: utf8
from pycropml.units import u
from copy import copy
from array import array

import numpy
from math import *

def model_penman(evapoTranspirationPriestlyTaylor = 449.367,
         hslope = 0.584,
         VPDair = 2.19,
         psychrometricConstant = 0.66,
         Alpha = 1.5,
         lambdaV = 2.454,
         rhoDensityAir = 1.225,
         specificHeatCapacityAir = 0.00101,
         conductance = 598.685):
    """
     - Name: Penman -Version: 1.0, -Time step: 1
     - Description:
                 * Title: Penman Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA/LEPSE Montpellier
                 * Abstract: This method is used when wind and vapor pressure daily data are available
             
     - inputs:
                 * name: evapoTranspirationPriestlyTaylor
                               ** description : evapoTranspiration of Priestly Taylor 
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** default : 449.367
                               ** min : 0
                               ** max : 10000
                               ** unit : g/m**2/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: hslope
                               ** description : the slope of saturated vapor pressure temperature curve at a given temperature 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 0.584
                               ** min : 0
                               ** max : 1000
                               ** unit : hPa/degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: VPDair
                               ** description :  vapour pressure density
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 2.19
                               ** min : 0
                               ** max : 1000
                               ** unit : hPa
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: psychrometricConstant
                               ** description : psychrometric constant
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.66
                               ** min : 0
                               ** max : 1
                               ** unit : hPa/degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: Alpha
                               ** description : Priestley-Taylor evapotranspiration proportionality constant
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 1.5
                               ** min : 0
                               ** max : 100
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: lambdaV
                               ** description : latent heat of vaporization of water
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 2.454
                               ** min : 0
                               ** max : 10
                               ** unit : MJ/kg
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: rhoDensityAir
                               ** description : Density of air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 1.225
                               ** unit : kg*m**3
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: specificHeatCapacityAir
                               ** description : Specific heat capacity of dry air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.00101
                               ** min : 0
                               ** max : 1
                               ** unit : MJ/kg/degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: conductance
                               ** description : conductance
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** default : 598.685
                               ** unit : m/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
     - outputs:
                 * name: evapoTranspirationPenman
                               ** description :  evapoTranspiration of Penman Monteith
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g/m**2/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    evapoTranspirationPenman = evapoTranspirationPriestlyTaylor / Alpha + (1000.0 * (rhoDensityAir * specificHeatCapacityAir * VPDair * conductance / (lambdaV * (hslope + psychrometricConstant))))
    return evapoTranspirationPenman
# coding: utf8
from copy import copy

import numpy
from math import *

def model_phylsowingdatecorrection(sowingDay = 1,
         latitude = 0.0,
         sDsa_sh = 1.0,
         rp = 0.0,
         sDws = 1,
         sDsa_nh = 1.0,
         p = 120.0):
    """
     - Name: PhylSowingDateCorrection -Version: 1.0, -Time step: 1
     - Description:
                 * Title: PhylSowingDateCorrection Model
                 * Author: Loic Manceau
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA Montpellier
                 * Abstract: Correction of the Phyllochron Varietal parameter according to sowing date 
     - inputs:
                 * name: sowingDay
                               ** parametercategory : species
                               ** min : 1
                               ** datatype : INT
                               ** max : 365
                               ** uri : some url
                               ** default : 1
                               ** inputtype : parameter
                               ** unit : d
                               ** description : Day of Year at sowing
                 * name: latitude
                               ** parametercategory : soil
                               ** min : -90
                               ** datatype : DOUBLE
                               ** max : 90
                               ** uri : some url
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : °
                               ** description : Latitude
                 * name: sDsa_sh
                               ** parametercategory : species
                               ** min : 1
                               ** datatype : DOUBLE
                               ** max : 365
                               ** uri : some url
                               ** default : 1.0
                               ** inputtype : parameter
                               ** unit : d
                               ** description : Sowing date at which Phyllochrone is maximum in southern hemispher
                 * name: rp
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 365
                               ** uri : some url
                               ** default : 0
                               ** inputtype : parameter
                               ** unit : d-1
                               ** description : Rate of change of Phyllochrone with sowing date
                 * name: sDws
                               ** parametercategory : species
                               ** min : 1
                               ** datatype : INT
                               ** max : 365
                               ** uri : some url
                               ** default : 1
                               ** inputtype : parameter
                               ** unit : d
                               ** description : Sowing date at which Phyllochrone is minimum
                 * name: sDsa_nh
                               ** parametercategory : species
                               ** min : 1
                               ** datatype : DOUBLE
                               ** max : 365
                               ** uri : some url
                               ** default : 1.0
                               ** inputtype : parameter
                               ** unit : d
                               ** description : Sowing date at which Phyllochrone is maximum in northern hemispher
                 * name: p
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** uri : some url
                               ** default : 120
                               ** inputtype : parameter
                               ** unit : °C d leaf-1
                               ** description : Phyllochron (Varietal parameter)
     - outputs:
                 * name: fixPhyll
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : auxiliary
                               ** max : 1000
                               ** unit : °C d leaf-1
                               ** description :  Phyllochron Varietal parameter 
    """

    if latitude < 0.0:
        if sowingDay > int(sDsa_sh):
            fixPhyll = p * (1 - (rp * min((sowingDay - sDsa_sh), sDws)))
        else:
            fixPhyll = p
    else:
        if sowingDay < int(sDsa_nh):
            fixPhyll = p * (1 - (rp * min(sowingDay, sDws)))
        else:
            fixPhyll = p
    return fixPhyll
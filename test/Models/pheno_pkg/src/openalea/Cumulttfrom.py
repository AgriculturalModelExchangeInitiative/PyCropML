# coding: utf8
from copy import copy

import numpy
from math import *

def model_cumulttfrom(calendarMoments_t1 = ["Sowing"],
         calendarCumuls_t1 = [0.0],
         cumulTT = 8.0):
    """
     - Name: CumulTTFrom -Version: 1.0, -Time step: 1
     - Description:
                 * Title: CumulTTFrom Model
                 * Author: Pierre Martre
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA Montpellier
                 * Abstract: Calculate CumulTT 
     - inputs:
                 * name: calendarMoments_t1
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** default : ['Sowing']
                               ** inputtype : variable
                               ** unit : 
                               ** description : List containing appearance of each stage at previous day
                 * name: calendarCumuls_t1
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** default : [0.0]
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : list containing for each stage occured its cumulated thermal times at previous day
                 * name: cumulTT
                               ** min : -200
                               ** default : 8.0
                               ** max : 10000
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : cumul TT at current date
     - outputs:
                 * name: cumulTTFromZC_65
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** unit : °C d
                               ** description :  cumul TT from Anthesis to current date 
                 * name: cumulTTFromZC_39
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** unit : °C d
                               ** description :  cumul TT from FlagLeafLiguleJustVisible to current date 
                 * name: cumulTTFromZC_91
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** unit : °C d
                               ** description :  cumul TT from EndGrainFilling to current date 
    """

    cumulTTFromZC_65 = 0.0
    cumulTTFromZC_39 = 0.0
    cumulTTFromZC_91 = 0.0
    if "Anthesis" in calendarMoments_t1:
        cumulTTFromZC_65 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("Anthesis")]
    if "FlagLeafLiguleJustVisible" in calendarMoments_t1:
        cumulTTFromZC_39 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("FlagLeafLiguleJustVisible")]
    if "EndGrainFilling" in calendarMoments_t1:
        cumulTTFromZC_91 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("EndGrainFilling")]
    return (cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91)
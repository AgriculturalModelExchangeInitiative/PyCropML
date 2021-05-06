# coding: utf8
from pycropml.units import u
from copy import copy
from array import array

import numpy
from math import *

def model_IsMomentRegistredZC_39(calendarMoments_t1 = ["Sowing"]):
    """
     - Name: IsMomentRegistredZC_39 -Version: 1.0, -Time step: 1
     - Description:
                 * Title: Is FlagLeafLiguleJustVisible Model
                 * Author: Pierre Martre
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA Montpellier
                 * Abstract: if FlagLeafLiguleJustVisible is already Registred 
     - inputs:
                 * name: calendarMoments_t1
                               ** description : List containing appearance of each stage at previous time
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** default : ['Sowing']
                               ** unit : 
                               ** inputtype : variable
     - outputs:
                 * name: isMomentRegistredZC_39
                               ** description :  if Flag leaf ligule has already appeared 
                               ** variablecategory : state
                               ** datatype : INT
                               ** min : 0
                               ** max : 1
                               ** unit : 
    """

    isMomentRegistredZC_39 = 1 if "FlagLeafLiguleJustVisible" in calendarMoments_t1 else 0
    return isMomentRegistredZC_39
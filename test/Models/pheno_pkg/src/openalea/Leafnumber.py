# coding: utf8
from copy import copy

import numpy
from math import *

def model_leafnumber(deltaTT = 23.5895677277,
         phyllochron_t1 = 0.0,
         hasFlagLeafLiguleAppeared = 0,
         leafNumber_t1 = 0.0,
         phase = 1.0):
    """
     - Name: LeafNumber -Version: 1.0, -Time step: 1
     - Description:
                 * Title: CalculateLeafNumber Model
                 * Author: Pierre MARTRE
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA Montpellier
                 * Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day
     - inputs:
                 * name: deltaTT
                               ** min : -20
                               ** default : 23.5895677277199
                               ** max : 100
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : daily delta TT 
                 * name: phyllochron_t1
                               ** min : 0
                               ** default : 0
                               ** max : 1000
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d leaf-1
                               ** description : phyllochron
                 * name: hasFlagLeafLiguleAppeared
                               ** min : 0
                               ** default : 0
                               ** max : 1
                               ** variablecategory : state
                               ** datatype : INT
                               ** inputtype : variable
                               ** unit : 
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                 * name: leafNumber_t1
                               ** min : 0
                               ** default : 0
                               ** max : 25
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : leaf
                               ** description :  Actual number of phytomers
                 * name: phase
                               ** min : 0
                               ** default : 1
                               ** max : 7
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit :  
                               ** description :  the name of the phase
     - outputs:
                 * name: leafNumber
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** uri : some url
                               ** datatype : DOUBLE
                               ** unit : leaf
                               ** description : Actual number of phytomers
    """

    leafNumber = leafNumber_t1
    if phase >= 1.0 and phase < 4.0:
        if hasFlagLeafLiguleAppeared == 0:
            if phyllochron_t1 == 0.0:
                phyllochron_ = 0.0000001
            else:
                phyllochron_ = phyllochron_t1
            leafNumber = leafNumber_t1 + min(deltaTT / phyllochron_, 0.999)
    return leafNumber
# coding: utf8
from copy import copy

import numpy
from math import *
from datetime import datetime

def model_updateleafflag(cumulTT = 741.510096672,
         leafNumber = 8.91945383336,
         calendarMoments = ["Sowing"],
         calendarDates = [datetime(2007, 3, 21)],
         calendarCumuls = [0.0],
         currentdate = datetime(2007, 4, 29),
         finalLeafNumber = 8.7975820132,
         hasFlagLeafLiguleAppeared_t1 = 1,
         phase = 1.0):
    """
     - Name: UpdateLeafFlag -Version: 1.0, -Time step: 1
     - Description:
                 * Title: UpdateLeafFlag Model
                 * Author: Pierre MARTRE
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA Montpellier
                 * Abstract: tells if flag leaf has appeared and update the calendar if so
         	
     - inputs:
                 * name: cumulTT
                               ** min : -200
                               ** default : 741.510096671757
                               ** max : 10000
                               ** uri : some url
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : cumul thermal times at current date
                 * name: leafNumber
                               ** min : 0
                               ** default : 8.919453833361189
                               ** max : 25
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : Actual number of phytomers
                 * name: calendarMoments
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** default : ['Sowing']
                               ** inputtype : variable
                               ** unit : 
                               ** description : List containing apparition of each stage
                 * name: calendarDates
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** default : ['2007/3/21']
                               ** inputtype : variable
                               ** unit : 
                               ** description : List containing  the dates of the wheat developmental phases
                 * name: calendarCumuls
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** default : [0.0]
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : list containing for each stage occured its cumulated thermal times
                 * name: currentdate
                               ** default : 2007/4/29
                               ** uri : some url
                               ** variablecategory : auxiliary
                               ** datatype : DATE
                               ** inputtype : variable
                               ** unit : 
                               ** description :  current date
                 * name: finalLeafNumber
                               ** min : 0
                               ** default : 8.797582013199484
                               ** max : 10000
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : final leaf number
                 * name: hasFlagLeafLiguleAppeared_t1
                               ** min : 0
                               ** default : 1
                               ** max : 1
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : INT
                               ** inputtype : variable
                               ** unit : 
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
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
                 * name: hasFlagLeafLiguleAppeared
                               ** min : 0
                               ** variablecategory : state
                               ** max : 1
                               ** uri : some url
                               ** datatype : INT
                               ** unit : 
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                 * name: calendarMoments
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** unit : 
                               ** description :  List containing apparition of each stage
                 * name: calendarDates
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** unit : 
                               ** description :  List containing  the dates of the wheat developmental phases
                 * name: calendarCumuls
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** unit : °C d
                               ** description :  list containing for each stage occured its cumulated thermal times
    """

    hasFlagLeafLiguleAppeared = 0
    if phase >= 1.0 and phase < 4.0:
        if leafNumber > 0.0:
            if hasFlagLeafLiguleAppeared == 0 and (finalLeafNumber > 0.0 and leafNumber >= finalLeafNumber):
                hasFlagLeafLiguleAppeared = 1
                if "FlagLeafLiguleJustVisible" not in calendarMoments:
                    calendarMoments.append("FlagLeafLiguleJustVisible")
                    calendarCumuls.append(cumulTT)
                    calendarDates.append(currentdate)
    return (hasFlagLeafLiguleAppeared, calendarMoments, calendarDates, calendarCumuls)
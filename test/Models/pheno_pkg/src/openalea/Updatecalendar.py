# coding: utf8
from copy import copy

import numpy
from math import *
from datetime import datetime

def model_updatecalendar(cumulTT = 741.510096672,
         calendarMoments = ["Sowing"],
         calendarDates = [datetime(2007, 3, 21)],
         calendarCumuls = [0.0],
         currentdate = datetime(2007, 3, 27),
         phase = 1.0):
    """
     - Name: UpdateCalendar -Version: 1.0, -Time step: 1
     - Description:
                 * Title: Calendar Model
                 * Author: Pierre Martre
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA Montpellier
                 * Abstract: Lists containing for each stage the date it occurs as well as a copy of all types of cumulated thermal times 
     - inputs:
                 * name: cumulTT
                               ** min : -200
                               ** default : 741.510096671757
                               ** max : 10000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : cumul thermal times at current date
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
                               ** variablecategory : auxiliary
                               ** datatype : DATE
                               ** default : 2007/3/27
                               ** inputtype : variable
                               ** unit : 
                               ** description : current date
                 * name: phase
                               ** min : 0
                               ** default : 1
                               ** max : 7
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : 
                               ** description :  the name of the phase
     - outputs:
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

    if phase >= 1.0 and phase < 2.0 and "Emergence" not in calendarMoments:
        calendarMoments.append("Emergence")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase >= 2.0 and phase < 3.0 and "FloralInitiation" not in calendarMoments:
        calendarMoments.append("FloralInitiation")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase >= 3.0 and phase < 4.0 and "Heading" not in calendarMoments:
        calendarMoments.append("Heading")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase == 4.0 and "Anthesis" not in calendarMoments:
        calendarMoments.append("Anthesis")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase == 4.5 and "EndCellDivision" not in calendarMoments:
        calendarMoments.append("EndCellDivision")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase >= 5.0 and phase < 6.0 and "EndGrainFilling" not in calendarMoments:
        calendarMoments.append("EndGrainFilling")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase >= 6.0 and phase < 7.0 and "Maturity" not in calendarMoments:
        calendarMoments.append("Maturity")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    return (calendarMoments, calendarDates, calendarCumuls)
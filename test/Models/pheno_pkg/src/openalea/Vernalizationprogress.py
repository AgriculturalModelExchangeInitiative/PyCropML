# coding: utf8
from copy import copy

import numpy
from math import *
from datetime import datetime

def model_vernalizationprogress(dayLength = 12.3037621834,
         deltaTT = 20.3429985012,
         cumulTT = 112.33011041,
         leafNumber_t1 = 0.0,
         calendarMoments_t1 = ["Sowing"],
         calendarDates_t1 = [datetime(2007, 3, 21)],
         calendarCumuls_t1 = [0.0],
         minTvern = 0.0,
         intTvern = 11.0,
         vAI = 0.015,
         vBEE = 0.01,
         minDL = 8.0,
         maxDL = 15.0,
         maxTvern = 23.0,
         pNini = 4.0,
         aMXLFNO = 24.0,
         vernaprog_t1 = 0.551725418738,
         currentdate = datetime(2007, 3, 27),
         isVernalizable = 1,
         minFinalNumber_t1 = 5.5):
    """
     - Name: VernalizationProgress -Version: 1.0, -Time step: 1
     - Description:
                 * Title: VernalizationProgress Model
                 * Author: Pierre MARTRE
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA Montpellier
                 * Abstract: Calculate progress (VernaProg) towards vernalization, but there 
             			is no vernalization below minTvern 
             			and above maxTvern . The maximum value of VernaProg is 1.
             			Progress towards full vernalization is a linear function of shoot 
             			temperature (soil temperature until leaf # reach MaxLeafSoil and then
             			 canopy temperature)
         	
     - inputs:
                 * name: dayLength
                               ** min : 0
                               ** default : 12.3037621834005
                               ** max : 10000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : mm2 m-2
                               ** description : day length
                 * name: deltaTT
                               ** min : -20
                               ** default : 20.3429985011972
                               ** max : 100
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : difference cumul TT between j and j-1 day 
                 * name: cumulTT
                               ** min : -200
                               ** default : 112.330110409888
                               ** max : 10000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : cumul thermal times at currentdate
                 * name: leafNumber_t1
                               ** min : 0
                               ** default : 0
                               ** max : 25
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : Actual number of phytomers
                 * name: calendarMoments_t1
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** default : ['Sowing']
                               ** inputtype : variable
                               ** unit : 
                               ** description : List containing appearance of each stage
                 * name: calendarDates_t1
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** default : ['2007/3/21']
                               ** inputtype : variable
                               ** unit : 
                               ** description : List containing  the dates of the wheat developmental phases
                 * name: calendarCumuls_t1
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** default : [0.0]
                               ** inputtype : variable
                               ** unit : 
                               ** description : list containing for each stage occured its cumulated thermal times
                 * name: minTvern
                               ** parametercategory : species
                               ** min : -20
                               ** datatype : DOUBLE
                               ** max : 60
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : °C
                               ** description : Minimum temperature for vernalization to occur
                 * name: intTvern
                               ** parametercategory : species
                               ** min : -20
                               ** datatype : DOUBLE
                               ** max : 60
                               ** default :  11.0
                               ** inputtype : parameter
                               ** unit : °C
                               ** description : Intermediate temperature for vernalization to occur
                 * name: vAI
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** default :  0.015
                               ** inputtype : parameter
                               ** unit : d-1 °C-1
                               ** description : Response of vernalization rate to temperature
                 * name: vBEE
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** default : 0.01
                               ** inputtype : parameter
                               ** unit : d-1
                               ** description : Vernalization rate at 0°C
                 * name: minDL
                               ** parametercategory : species
                               ** min : 12
                               ** datatype : DOUBLE
                               ** max : 24
                               ** default : 8.0
                               ** inputtype : parameter
                               ** unit : h
                               ** description : Threshold daylength below which it does influence vernalization rate
                 * name: maxDL
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 24
                               ** default : 15.0
                               ** inputtype : parameter
                               ** unit : h
                               ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
                 * name: maxTvern
                               ** parametercategory : species
                               ** min : -20
                               ** datatype : DOUBLE
                               ** max : 60
                               ** default :  23.0
                               ** inputtype : parameter
                               ** unit : °C
                               ** description : Maximum temperature for vernalization to occur
                 * name: pNini
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 24
                               ** default : 4.0
                               ** inputtype : parameter
                               ** unit : primordia
                               ** description : Number of primorida in the apex at emergence
                 * name: aMXLFNO
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 25
                               ** default : 24.0
                               ** inputtype : parameter
                               ** unit : leaf
                               ** description : Absolute maximum leaf number
                 * name: vernaprog_t1
                               ** min : 0
                               ** default :  0.5517254187376879
                               ** max : 1
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : 
                               ** description : progression on a 0  to 1 scale of the vernalization
                 * name: currentdate
                               ** variablecategory : auxiliary
                               ** datatype : DATE
                               ** default : 2007/3/27
                               ** inputtype : variable
                               ** unit : 
                               ** description : current date 
                 * name: isVernalizable
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : INT
                               ** max : 1
                               ** default : 1
                               ** inputtype : parameter
                               ** unit : 
                               ** description : true if the plant is vernalizable
                 * name: minFinalNumber_t1
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 25
                               ** default : 5.5
                               ** variablecategory : state
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : minimum final leaf number
     - outputs:
                 * name: vernaprog
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : 
                               ** description : progression on a 0  to 1 scale of the vernalization
                 * name: minFinalNumber
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : leaf
                               ** description : minimum final leaf number
                 * name: calendarMoments
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** unit : 
                               ** description : List containing appearance of each stage
                 * name: calendarDates
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** unit : 
                               ** description : List containing  the dates of the wheat developmental phases
                 * name: calendarCumuls
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** unit : 
                               ** description : list containing for each stage occured its cumulated thermal times
    """

    calendarMoments = []
    calendarDates = []
    calendarCumuls = []
    calendarMoments = copy(calendarMoments_t1)
    calendarCumuls = copy(calendarCumuls_t1)
    calendarDates = copy(calendarDates_t1)
    minFinalNumber = minFinalNumber_t1
    vernaprog = vernaprog_t1
    if isVernalizable == 1 and vernaprog_t1 < 1.0:
        tt = deltaTT
        if tt >= minTvern and tt <= intTvern:
            vernaprog = vernaprog_t1 + (vAI * tt) + vBEE
        else:
            vernaprog = vernaprog_t1
        if tt > intTvern:
            maxVernaProg = vAI * intTvern + vBEE
            dLverna = max(minDL, min(maxDL, dayLength))
            vernaprog = vernaprog + max(0.0, maxVernaProg * (1.0 + ((intTvern - tt) / (maxTvern - intTvern) * ((dLverna - minDL) / (maxDL - minDL)))))
        primordno = 2.0 * leafNumber_t1 + pNini
        minLeafNumber = minFinalNumber_t1
        if vernaprog >= 1.0 or primordno >= aMXLFNO:
            minFinalNumber = max(primordno, minFinalNumber_t1)
            calendarMoments.append("EndVernalisation")
            calendarCumuls.append(cumulTT)
            calendarDates.append(currentdate)
            vernaprog = max(1.0, vernaprog)
        else:
            potlfno = aMXLFNO - ((aMXLFNO - minLeafNumber) * vernaprog)
            if primordno >= potlfno:
                minFinalNumber = max((potlfno + primordno) / 2.0, minFinalNumber_t1)
                vernaprog = max(1.0, vernaprog)
                calendarMoments.append("EndVernalisation")
                calendarCumuls.append(cumulTT)
                calendarDates.append(currentdate)
    return (vernaprog, minFinalNumber, calendarMoments, calendarDates, calendarCumuls)
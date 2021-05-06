# coding: utf8
from pycropml.units import u
from copy import copy
from array import array

import numpy
from math import *
from datetime import datetime

def model_registerzadok(cumulTT = 354.582294511779,
         phase = 2.0,
         leafNumber = 4.8854219661087575,
         calendarMoments = ["Sowing"],
         calendarDates = [datetime(2007, 3, 21)],
         calendarCumuls = [0.0],
         cumulTTFromZC_65 = 0.0,
         currentdate = datetime(2007, 4, 9),
         der = 300.0,
         slopeTSFLN = 0.9,
         intTSFLN = 0.9,
         finalLeafNumber = 8.797582013199484,
         currentZadokStage = "MainShootPlus1Tiller",
         hasZadokStageChanged_t1 = 0,
         sowingDate = datetime(2007, 3, 21)):
    """
     - Name: RegisterZadok -Version: 1.0, -Time step: 1
     - Description:
                 * Title: RegisterZadok Model
                 * Author: Pierre MARTRE
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA/LEPSE Montpellier
                 * Abstract: Record the zadok stage in the calendar
         	
     - inputs:
                 * name: cumulTT
                               ** description : 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : -200
                               ** max : 10000
                               ** default : 354.582294511779
                               ** unit : °C d
                               ** uri : some url
                               ** inputtype : variable
                 * name: phase
                               ** description : instance of the phase class . You can get the name of the phase using phase.getPhaseAsString(PhaseValue) 
                               ** variablecategory : state
                               ** inputtype : variable
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 7
                               ** default : 2
                               ** unit : 
                               ** uri : some url
                 * name: leafNumber
                               ** description : Actual number of phytomers
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 25
                               ** default : 4.8854219661087575
                               ** unit : leaf
                               ** uri : some url
                               ** inputtype : variable
                 * name: calendarMoments
                               ** description : List containing apparition of each stage
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** default : ['Sowing']
                               ** unit : 
                               ** inputtype : variable
                 * name: calendarDates
                               ** description : List containing  the dates of the wheat developmental phases
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** default : ['2007/3/21']
                               ** unit : 
                               ** inputtype : variable
                 * name: calendarCumuls
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** default : [0.0]
                               ** unit : °C d
                               ** inputtype : variable
                 * name: cumulTTFromZC_65
                               ** description : cumul of the thermal time (DeltaTT) since the moment ZC_65
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : -200
                               ** max : 10000
                               ** default : 0
                               ** unit : °C d
                               ** uri : some url
                               ** inputtype : variable
                 * name: currentdate
                               ** description : current date
                               ** variablecategory : auxiliary
                               ** datatype : DATE
                               ** min : 
                               ** max : 
                               ** default : 2007/4/9
                               ** unit : 
                               ** uri : some url
                               ** inputtype : variable
                 * name: der
                               ** description : Duration of the endosperm endoreduplication phase
                               ** parametercategory : species
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** default : 300.0
                               ** unit : °C d
                               ** uri : some url
                               ** inputtype : parameter
                 * name: slopeTSFLN
                               ** description : used to calculate Terminal spikelet
                               ** parametercategory : species
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** default : 0.9
                               ** unit : 
                               ** uri : some url
                               ** inputtype : parameter
                 * name: intTSFLN
                               ** description : used to calculate Terminal spikelet
                               ** parametercategory : species
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** default : 0.9
                               ** unit : 
                               ** uri : some url
                               ** inputtype : parameter
                 * name: finalLeafNumber
                               ** description : final leaf number
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** default : 8.797582013199484
                               ** unit : leaf
                               ** uri : some url
                               ** inputtype : variable
                 * name: currentZadokStage
                               ** description : current zadok stage
                               ** variablecategory : state
                               ** datatype : STRING
                               ** min : 
                               ** max : 
                               ** default : MainShootPlus1Tiller
                               ** unit : 
                               ** uri : some url
                               ** inputtype : variable
                 * name: hasZadokStageChanged_t1
                               ** description : true if the zadok stage has changed this time step
                               ** variablecategory : state
                               ** datatype : INT
                               ** min : 0
                               ** max : 1
                               ** default : 0
                               ** unit : 
                               ** uri : some url
                               ** inputtype : variable
                 * name: sowingDate
                               ** description :  Date of Sowing
                               ** parametercategory : constant
                               ** datatype : DATE
                               ** min : 
                               ** max : 
                               ** default : 2007/3/21
                               ** unit : 
                               ** inputtype : parameter
     - outputs:
                 * name: hasZadokStageChanged
                               ** description : true if the zadok stage has changed this time step
                               ** variablecategory : state
                               ** datatype : INT
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : some url
                 * name: currentZadokStage
                               ** description : current zadok stage
                               ** variablecategory : state
                               ** datatype : STRING
                               ** unit :  
                               ** uri : some url
                 * name: calendarMoments
                               ** description :  List containing apparition of each stage
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** unit : 
                 * name: calendarDates
                               ** description :  List containing  the dates of the wheat developmental phases
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** unit : 
                 * name: calendarCumuls
                               ** description :  list containing for each stage occured its cumulated thermal times
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** unit : °C d
    """

    roundedFinalLeafNumber = int(finalLeafNumber + 0.5)
    if leafNumber >= 4.0 and "MainShootPlus1Tiller" not in calendarMoments:
        calendarMoments.append("MainShootPlus1Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus1Tiller"
    elif leafNumber >= 5.0 and "MainShootPlus2Tiller" not in calendarMoments:
        calendarMoments.append("MainShootPlus2Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus2Tiller"
    elif leafNumber >= 6.0 and "MainShootPlus3Tiller" not in calendarMoments:
        calendarMoments.append("MainShootPlus3Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus3Tiller"
    elif finalLeafNumber > 0.0 and (leafNumber >= slopeTSFLN * finalLeafNumber - intTSFLN and "TerminalSpikelet" not in calendarMoments):
        calendarMoments.append("TerminalSpikelet")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "TerminalSpikelet"
    elif leafNumber >= roundedFinalLeafNumber - 4.0 and roundedFinalLeafNumber - 4 > 0 and "PseudoStemErection" not in calendarMoments:
        calendarMoments.append("PseudoStemErection")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "PseudoStemErection"
    elif leafNumber >= roundedFinalLeafNumber - 3.0 and roundedFinalLeafNumber - 3 > 0 and "1stNodeDetectable" not in calendarMoments:
        calendarMoments.append("1stNodeDetectable")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "1stNodeDetectable"
    elif leafNumber >= roundedFinalLeafNumber - 2.0 and roundedFinalLeafNumber - 2 > 0 and "2ndNodeDetectable" not in calendarMoments:
        calendarMoments.append("2ndNodeDetectable")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "2ndNodeDetectable"
    elif leafNumber >= roundedFinalLeafNumber - 1.0 and roundedFinalLeafNumber - 1 > 0 and "FlagLeafJustVisible" not in calendarMoments:
        calendarMoments.append("FlagLeafJustVisible")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "FlagLeafJustVisible"
    elif "MidGrainFilling" not in calendarMoments and (phase == 4.5 and cumulTTFromZC_65 >= der):
        calendarMoments.append("MidGrainFilling")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MidGrainFilling"
    else:
        hasZadokStageChanged = 0
    return (hasZadokStageChanged, currentZadokStage, calendarMoments, calendarDates, calendarCumuls)
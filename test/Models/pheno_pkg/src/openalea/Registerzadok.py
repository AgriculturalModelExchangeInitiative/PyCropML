# coding: utf8
from copy import copy

import numpy
from math import *
from datetime import datetime

def model_registerzadok(cumulTT = 354.582294512,
         phase = 2.0,
         leafNumber = 4.88542196611,
         calendarMoments = ["Sowing"],
         calendarDates = [datetime(2007, 3, 21)],
         calendarCumuls = [0.0],
         cumulTTFromZC_65 = 0.0,
         currentdate = datetime(2007, 4, 9),
         der = 300.0,
         slopeTSFLN = 0.9,
         intTSFLN = 0.9,
         finalLeafNumber = 8.7975820132,
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
                               ** min : -200
                               ** default : 354.582294511779
                               ** max : 10000
                               ** uri : some url
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : 
                 * name: phase
                               ** min : 0
                               ** default : 2
                               ** max : 7
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : 
                               ** description : instance of the phase class . You can get the name of the phase using phase.getPhaseAsString(PhaseValue) 
                 * name: leafNumber
                               ** min : 0
                               ** default : 4.8854219661087575
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
                 * name: cumulTTFromZC_65
                               ** min : -200
                               ** default : 0
                               ** max : 10000
                               ** uri : some url
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : cumul of the thermal time (DeltaTT) since the moment ZC_65
                 * name: currentdate
                               ** min : 
                               ** default : 2007/4/9
                               ** max : 
                               ** uri : some url
                               ** variablecategory : auxiliary
                               ** datatype : DATE
                               ** inputtype : variable
                               ** unit : 
                               ** description : current date
                 * name: der
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** uri : some url
                               ** default : 300.0
                               ** inputtype : parameter
                               ** unit : °C d
                               ** description : Duration of the endosperm endoreduplication phase
                 * name: slopeTSFLN
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** uri : some url
                               ** default : 0.9
                               ** inputtype : parameter
                               ** unit : 
                               ** description : used to calculate Terminal spikelet
                 * name: intTSFLN
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** uri : some url
                               ** default : 0.9
                               ** inputtype : parameter
                               ** unit : 
                               ** description : used to calculate Terminal spikelet
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
                 * name: currentZadokStage
                               ** min : 
                               ** default : MainShootPlus1Tiller
                               ** max : 
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : STRING
                               ** inputtype : variable
                               ** unit : 
                               ** description : current zadok stage
                 * name: hasZadokStageChanged_t1
                               ** min : 0
                               ** default : 0
                               ** max : 1
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : INT
                               ** inputtype : variable
                               ** unit : 
                               ** description : true if the zadok stage has changed this time step
                 * name: sowingDate
                               ** parametercategory : constant
                               ** min : 
                               ** datatype : DATE
                               ** max : 
                               ** default : 2007/3/21
                               ** inputtype : parameter
                               ** unit : 
                               ** description :  Date of Sowing
     - outputs:
                 * name: hasZadokStageChanged
                               ** min : 0
                               ** variablecategory : state
                               ** max : 1
                               ** uri : some url
                               ** datatype : INT
                               ** unit : 
                               ** description : true if the zadok stage has changed this time step
                 * name: currentZadokStage
                               ** datatype : STRING
                               ** variablecategory : state
                               ** uri : some url
                               ** unit :  
                               ** description : current zadok stage
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
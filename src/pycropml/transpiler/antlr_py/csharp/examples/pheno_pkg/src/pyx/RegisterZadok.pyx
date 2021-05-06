import numpy 
from math import *
from datetime import datetime

def model_RegisterZadok(float cumulTT=354.582294511779,
                        float phase=2.0,
                        float leafNumber=4.8854219661087575,
                        list calendarMoments=['Sowing'],
                        list calendarDates=[datetime(2007, 3, 21) ,],
                        list calendarCumuls=[0.0],
                        float cumulTTFromZC_65=0.0,
                        datetime currentdate=datetime(2007, 4, 9) ,
                        float der=300.0,
                        float slopeTSFLN=0.9,
                        float intTSFLN=2.6,
                        float finalLeafNumber=8.797582013199484,
                        str currentZadokStage_t1='MainShootPlus1Tiller',
                        int hasZadokStageChanged_t1=0):
    """

    RegisterZadok Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA/LEPSE Montpellier
    Abstract: Record the zadok stage in the calendar
    	

    """
    cdef int hasZadokStageChanged
    cdef str currentZadokStage
    cdef int roundedFinalLeafNumber
    currentZadokStage = currentZadokStage_t1
    roundedFinalLeafNumber = int(finalLeafNumber+0.5)
    if (leafNumber>=4.0 and "MainShootPlus1Tiller" not in calendarMoments):
        calendarMoments.append("MainShootPlus1Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus1Tiller"
    elif (leafNumber>=5.0 and "MainShootPlus2Tiller" not in calendarMoments):
        calendarMoments.append("MainShootPlus2Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus2Tiller"
    elif (leafNumber>=6.0 and "MainShootPlus3Tiller" not in calendarMoments):
        calendarMoments.append("MainShootPlus3Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus3Tiller"      
    elif (finalLeafNumber > 0.0 and leafNumber>=(slopeTSFLN * finalLeafNumber - intTSFLN) and "TerminalSpikelet" not in calendarMoments):
        calendarMoments.append("TerminalSpikelet")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "TerminalSpikelet"      
    elif ((leafNumber >= (roundedFinalLeafNumber-4.0) and (roundedFinalLeafNumber-4) > 0) and "PseudoStemErection" not in calendarMoments):
        calendarMoments.append("PseudoStemErection")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "PseudoStemErection"
    elif ((leafNumber >= (roundedFinalLeafNumber-3.0) and (roundedFinalLeafNumber-3) > 0) and "1stNodeDetectable" not in calendarMoments):
        calendarMoments.append("1stNodeDetectable")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "1stNodeDetectable"
    elif ((leafNumber >= (roundedFinalLeafNumber-2.0) and (roundedFinalLeafNumber-2) > 0) and "2ndNodeDetectable" not in calendarMoments):
        calendarMoments.append("2ndNodeDetectable")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "2ndNodeDetectable"
    elif ((leafNumber >= (roundedFinalLeafNumber-1.0) and (roundedFinalLeafNumber-1) > 0) and "FlagLeafJustVisible" not in calendarMoments):
        calendarMoments.append("FlagLeafJustVisible")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "FlagLeafJustVisible"
    elif (("MidGrainFilling" not in calendarMoments) and phase == 4.5 and cumulTTFromZC_65 >= der):
        calendarMoments.append("MidGrainFilling")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MidGrainFilling"                 
    else:
        hasZadokStageChanged = 0;
    return  hasZadokStageChanged, currentZadokStage, calendarMoments, calendarDates, calendarCumuls

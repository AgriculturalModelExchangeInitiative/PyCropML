cdef int roundedFinalLeafNumber 
currentZadokStage = currentZadokStage_t1
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
elif finalLeafNumber > 0.0 and leafNumber >= slopeTSFLN * finalLeafNumber - intTSFLN and "TerminalSpikelet" not in calendarMoments:
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
elif "MidGrainFilling" not in calendarMoments and phase == 4.5 and cumulTTFromZC_65 >= der:
    calendarMoments.append("MidGrainFilling")
    calendarCumuls.append(cumulTT)
    calendarDates.append(currentdate)
    hasZadokStageChanged = 1
    currentZadokStage = "MidGrainFilling"
else:
    hasZadokStageChanged = 0
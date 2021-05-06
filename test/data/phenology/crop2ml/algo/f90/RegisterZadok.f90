
    !use crop2mlModules
        INTEGER::  roundedfinalLeafNumber
        roundedfinalLeafNumber = INT(finalLeafNumber+0.5)
        IF ((leafNumber>=4) .AND. (ALL(calendarMoments/="MainShootPlus1Tiller"))) THEN
            CALL AddToListchar(calendarMoments,"MainShootPlus1Tiller")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListchar(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = "MainShootPlus1Tiller"
        ELSE IF ((leafNumber>=5 ).AND. (ALL(calendarMoments/="MainShootPlus2Tiller"))) THEN
            CALL AddToListchar(calendarMoments,"MainShootPlus2Tiller")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListchar(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = "MainShootPlus2Tiller"
        ELSE IF ((leafNumber>=6) .AND. (ALL(calendarMoments/="MainShootPlus3Tiller"))) THEN
            CALL AddToListchar(calendarMoments,"MainShootPlus3Tiller")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListchar(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = "MainShootPlus3Tiller"
        ELSE IF ((finalLeafNumber > 0 ).AND. (leafNumber>=(slopeTSFLN * finalLeafNumber - intTSFLN)) .AND. &
            (ALL(calendarMoments/="TerminalSpikelet"))) THEN
            CALL AddToListchar(calendarMoments,"TerminalSpikelet")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListchar(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = "TerminalSpikelet"
        ELSE IF ((leafNumber >= (roundedfinalLeafNumber-4)) .AND. ((roundedfinalLeafNumber-4) > 0) .AND. &
            (ALL(calendarMoments/="PseudoStemErection"))) THEN
            CALL AddToListchar(calendarMoments,"PseudoStemErection")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListchar(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = "PseudoStemErection"
        ELSE IF ((leafNumber >= (roundedfinalLeafNumber-3)) .AND. ((roundedfinalLeafNumber-3) > 0) .AND. &
            (ALL(calendarMoments/="1stNodeDetectable"))) THEN
            CALL AddToListchar(calendarMoments,"1stNodeDetectable")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListchar(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = "1stNodeDetectable"
        ELSE IF ((leafNumber >= (roundedfinalLeafNumber-2)) .AND. ((roundedfinalLeafNumber-2) > 0) .AND.  &
            (ALL(calendarMoments/="2ndNodeDetectable"))) THEN
            CALL AddToListchar(calendarMoments,"2ndNodeDetectable")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListchar(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = "2ndNodeDetectable"
        ELSE IF ((leafNumber >= (roundedfinalLeafNumber-1)) .AND. ((roundedfinalLeafNumber-1) > 0) .AND. &
            (ALL(calendarMoments/="FlagLeafJustVisible"))) THEN
            CALL AddToListchar(calendarMoments,"FlagLeafJustVisible")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListchar(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = "FlagLeafJustVisible"
        ELSE IF ((ALL(calendarMoments/="MidGrainFilling")) .AND. (phase == 4.5) .AND. &
            (cumulTTFromZC_65 >= der))   THEN
            CALL AddToListchar(calendarMoments,"MidGrainFilling")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListchar(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = "MidGrainFilling"
        ELSE
            hasZadokStageChanged = 0
        END IF
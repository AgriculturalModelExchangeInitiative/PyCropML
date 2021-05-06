
    !use crop2mlModules
        
        IF ((phase >= 1) .AND. (phase< 4)) THEN
            IF (leafNumber > 0) THEN
                IF ((hasFlagLeafLiguleAppeared == 0) .AND. (finalLeafNumber > 0) .AND. (leafNumber >= finalLeafNumber)) THEN
                    hasFlagLeafLiguleAppeared = 1;
                    IF  (ALL(calendarMoments/="FlagLeafLiguleJustVisible")) THEN
                        CALL AddToListChar(calendarMoments,"FlagLeafLiguleJustVisible")
                        CALL AddToList(calendarCumuls,cumulTT)
                        CALL AddToListChar(calendarDates, currentdate)
                    END IF
                END IF
            ELSE
                hasFlagLeafLiguleAppeared = 0
            END IF
        END IF




    !use crop2mlModules

       IF ((phase >= 1) .AND. (phase < 2) .AND. (ALL(calendarMoments/="Emergence"))) THEN
            CALL AddToListChar(calendarMoments,"Emergence")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListChar(calendarDates,currentdate)
        ELSE IF ((phase >= 2 .AND. phase < 3)  .AND. ( ALL(calendarMoments/="FloralInitiation")  )) THEN
            CALL AddToListChar(calendarMoments,"FloralInitiation")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListChar(calendarDates,currentdate)
        ELSE IF ((phase >= 3 .AND. phase < 4)  .AND. (ALL(calendarMoments/="Heading")  )) THEN
            CALL AddToListChar(calendarMoments,"Heading")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListChar(calendarDates,currentdate)
        ELSE IF ((phase == 4)  .AND. (ALL(calendarMoments/="Anthesis" )  )) THEN
            CALL AddToListChar(calendarMoments,"Anthesis")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListChar(calendarDates,currentdate)
        ELSE IF ((phase == 4.5)  .AND. (ALL(calendarMoments/="EndCellDivision" )  )) THEN
            CALL AddToListChar(calendarMoments,"EndCellDivision")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListChar(calendarDates,currentdate)
        ELSE IF ((phase >= 5 .AND. phase < 6) .AND. (ALL( calendarMoments/="EndGrainFilling")  )) THEN
            CALL AddToListChar(calendarMoments,"EndGrainFilling")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListChar(calendarDates,currentdate)
        ELSE IF ((phase >= 6 .AND. phase < 7)  .AND. (ALL(calendarMoments/="Maturity" ) )) THEN
            CALL AddToListChar(calendarMoments,"Maturity")
            CALL AddToList(calendarCumuls,cumulTT)
            CALL AddToListChar(calendarDates,currentdate)
        END IF

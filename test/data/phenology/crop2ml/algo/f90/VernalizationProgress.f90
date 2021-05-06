
    !use crop2mlModules
        REAL:: tt, maxVernaProg, dLverna, primordno, minLeafNumber, potlfno
        IF ((isVernalizable==1) .AND. (vernaprog < 1)) THEN
            tt = deltaTT
            IF ((tt >= minTvern) .AND. (TT <= intTvern)) THEN
                vernaprog = vernaprog + vAI * tt + vBEE
            END IF
            IF (tt > intTvern) THEN
                maxVernaProg = vAI * intTvern + vBEE
                dLverna = MAX(minDL, MIN(maxDL, dayLength))
                vernaprog =vernaprog + MAX(0.0, maxVernaProg * (1 + ((intTvern - tt) / (maxTvern - intTvern))&
                    * ((dLverna - minDL) / (maxDL - minDL))))
            END IF
            primordno = 2.0 * leafNumber + pNini
            minLeafNumber = minFinalNumber
            IF ((vernaprog >= 1.0) .OR. (primordno >= aMXLFNO)) THEN
                minFinalNumber = MAX(primordno, minFinalNumber)
                CALL AddToListChar(calendarMoments, "EndVernalisation")
                CALL AddToList(calendarCumuls, cumulTT)
                CALL AddToListChar(calendarDates, currentdate)
            ELSE
                potlfno = aMXLFNO - (aMXLFNO - minLeafNumber) * vernaprog
                IF (primordno >= potlfno) THEN
                    minFinalNumber = MAX((potlfno + primordno) / 2.0, minFinalNumber)
                    CALL AddToListChar(calendarMoments,"EndVernalisation")
                    CALL AddToList(calendarCumuls,cumulTT)
                    CALL AddToListChar(calendarDates,currentdate)
                    vernaprog = MAX(1, INT(vernaprog))
                END IF
            END IF
        END IF






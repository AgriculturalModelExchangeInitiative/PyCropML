
    !use crop2mlModules
        REAL::appFLN, ttFromLastLeafToHeading, localDegfm, ttFromLastLeafToAnthesis        
        IF ((phase >= 0.0) .AND. (phase < 1.0)) THEN
            IF (cumulTT>= dse) THEN
                phase = 1.0
            END IF
        ELSE IF ((phase >= 1.0) .AND. (phase < 2.0)) THEN
            IF ((isVernalizable==1 .AND. vernaprog >= 1.0) .OR. (isVernalizable==0)) THEN
                IF (dayLength > maxDL) THEN
                    finalLeafNumber = minFinalNumber
                    hasLastPrimordiumAppeared = 1
                ELSE
                    appFLN = minFinalNumber + sLDL * (maxDL - dayLength)
                        !calculation of final leaf number from dayLength at inflexion plus 2 leaves
                    IF ((appFLN / 2.0) <= leafNumber) THEN
                        finalLeafNumber = appFLN;
                        hasLastPrimordiumAppeared =1
                    END IF
                END IF
                IF (hasLastPrimordiumAppeared==1) THEN
                    phase = 2.0
                END IF
            END IF
        ELSE IF ((phase >= 2.0) .AND. (phase < 4.0)) THEN
            IF (isMomentRegistredZC_39==1) THEN
                IF (phase < 3.0) THEN
                    ttFromLastLeafToHeading = 0.0
                    IF(choosePhyllUse=="Default") THEN
                        ttFromLastLeafToHeading =(pFLLAnth - pHEADANTH) * fixPhyll
                    ELSE IF (choosePhyllUse == "PTQ") THEN
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron;
                    ELSE IF (choosePhyllUse == "Test")  THEN
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p
                    END IF
                    IF (cumulTTFromZC_39 >= ttFromLastLeafToHeading) THEN
                        phase = 3.0
                    END IF
                END IF
                ttFromLastLeafToAnthesis =0.0;
                IF (choosePhyllUse == "Default") THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll
                ELSE IF (choosePhyllUse == "PTQ") THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * phyllochron
                ELSE IF (choosePhyllUse == "Test") THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * p
                END IF
                IF (cumulTTFromZC_39 >= ttFromLastLeafToAnthesis) THEN
                    phase = 4.0
                END IF
            END IF
        ELSE IF (phase == 4.0) THEN
            IF (grainCumulTT >= dcd) THEN
                phase = 4.5
            END IF
        ELSE IF (phase == 4.5) THEN
            IF ((grainCumulTT >= dgf) .OR. (gai <= 0)) THEN
                phase = 5.0
            END IF
        ELSE IF ((phase >= 5.0) .AND. (phase < 6.0)) THEN
            localDegfm = degfm
            IF (ignoreGrainMaturation .EQV. .TRUE.) THEN
                localDegfm = -1
            END IF
            IF (cumulTTFromZC_91 >= localDegfm) THEN
                phase = 6.0
            END IF
        END IF




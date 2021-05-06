    !use crop2mlModules
        IF (choosePhyllUse .EQ. 'Default') THEN
            IF (leafNumber < ldecr) THEN
                phyllochron = fixPhyll * pdecr
            ELSE IF ((leafNumber >= ldecr) .AND. (leafNumber < lincr)) THEN
                phyllochron = fixPhyll
            ELSE
                phyllochron = fixPhyll * pincr
            END IF
        END IF
        IF (choosePhyllUse .EQ. 'PTQ') THEN
            gai = MAX(pastMaxAI,gai)
            pastMaxAI = gai
            IF (gai > 0.0) THEN
                phyllochron = phylPTQ1 * ((gai * kl) / (1 - EXP(-kl * gai))) / (ptq + aPTQ)
            ELSE
                phyllochron = phylPTQ1
            END IF
        END IF
        IF (choosePhyllUse == 'Test') THEN

            IF (leafNumber < ldecr) THEN
                phyllochron = p * pdecr
            ELSE IF ((leafNumber >= ldecr) .AND. (leafNumber < lincr)) THEN
                phyllochron = p
            ELSE
                phyllochron = p * pincr
            END IF
        END IF


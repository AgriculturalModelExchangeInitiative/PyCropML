
    !use crop2mlModules
        IF ((phase .GE. 1.0) .AND. (phase .LT. 4.0)) THEN
            IF (hasFlagLeafLiguleAppeared .EQ. 0) THEN
                IF (phyllochron .EQ. 0.0) THEN
                    phyllochron = 0.0000001
                END IF
                leafNumber = leafNumber + MIN(deltaTT / phyllochron, 0.999)
            END IF
        END IF

    !use crop2mlModules
        REAL::oldcanopyShootNumber, calc
        INTEGER:: emergedLeaves, i
        oldcanopyShootNumber = canopyShootNumber
        emergedLeaves = INT(MAX(1, CEILING(leafNumber - 1)))
        shoots = fibonacci(emergedLeaves)
        canopyShootNumber = MIN(shoots * sowingDensity, INT(targetFertileShoot))
        averageShootNumberPerPlant = canopyShootNumber / sowingDensity
        IF (canopyShootNumber /= oldcanopyShootNumber) THEN
            CALL AddToList(tilleringProfile,canopyShootNumber - oldcanopyShootNumber)
        END IF
         tillerNumber = SIZE(tilleringProfile)
        DO i=SIZE(leafTillerNumberArray), CEILING(leafNumber)-1
            CALL AddToListInt(leafTillerNumberArray,tillerNumber)
        END DO
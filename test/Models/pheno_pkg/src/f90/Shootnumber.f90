        DO i = SIZE(leafTillerNumberArray_t1) , CEILING(leafNumber)-1, 1
            call Add(lNumberArray_rate, numberTillerCohort)
        END DO
        
        leafTillerNumberArray = leafTillerNumberArray_t1
        call Add(leafTillerNumberArray,lNumberArray_rate)
    END SUBROUTINE model_shootnumber

    RECURSIVE FUNCTION fibonacci(n) RESULT(res_cyml)
        IMPLICIT NONE
        INTEGER, INTENT(IN) :: n
        INTEGER:: res_cyml
        IF(n .LE. 1) THEN
            res_cyml = n
        ELSE
            res_cyml = fibonacci(n - 1) + fibonacci(n - 2)
        END IF
    END FUNCTION fibonacci

    SUBROUTINE init_shootnumber(sowingDensity, &
        targetFertileShoot, &
        averageShootNumberPerPlant, &
        canopyShootNumber, &
        leafTillerNumberArray, &
        tilleringProfile, &
        numberTillerCohort)
        IMPLICIT NONE
        REAL, INTENT(IN) :: sowingDensity
        REAL, INTENT(IN) :: targetFertileShoot
        REAL:: canopyShootNumber_t1
        REAL:: leafNumber
        REAL, ALLOCATABLE , DIMENSION(:):: tilleringProfile_t1
        INTEGER, ALLOCATABLE , DIMENSION(:):: leafTillerNumberArray_t1
        INTEGER:: numberTillerCohort_t1
        REAL, INTENT(OUT) :: averageShootNumberPerPlant
        REAL, INTENT(OUT) :: canopyShootNumber
        INTEGER, ALLOCATABLE , DIMENSION(:), INTENT(OUT) ::  &
                leafTillerNumberArray
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(OUT) :: tilleringProfile
        INTEGER, INTENT(OUT) :: numberTillerCohort
        canopyShootNumber = sowingDensity
        averageShootNumberPerPlant = 1.0
        call Add(tilleringProfile, sowingDensity)
        numberTillerCohort = 1
        deallocate(leafTillerNumberArray)

    END SUBROUTINE init_shootnumber

END MODULE

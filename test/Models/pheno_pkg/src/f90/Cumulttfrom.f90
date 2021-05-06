MODULE Cumulttfrommod
    USE list_sub
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_cumulttfrom(calendarMoments_t1, &
        calendarCumuls_t1, &
        cumulTT, &
        cumulTTFromZC_65, &
        cumulTTFromZC_39, &
        cumulTTFromZC_91)
        IMPLICIT NONE
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(IN) ::  &
                calendarMoments_t1
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(IN) :: calendarCumuls_t1
        REAL, INTENT(IN) :: cumulTT
        REAL, INTENT(OUT) :: cumulTTFromZC_65
        REAL, INTENT(OUT) :: cumulTTFromZC_39
        REAL, INTENT(OUT) :: cumulTTFromZC_91
        !- Description:
    !            * Title: CumulTTFrom Model
    !            * Author: Pierre Martre
    !            * Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            * Institution: INRA Montpellier
    !            * Abstract: Calculate CumulTT 
        !- inputs:
    !            * name: calendarMoments_t1
    !                          ** description : List containing appearance of each stage at previous day
    !                          ** variablecategory : state
    !                          ** datatype : STRINGLIST
    !                          ** default : ['Sowing']
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: calendarCumuls_t1
    !                          ** description : list containing for each stage occured its cumulated thermal times at previous day
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLELIST
    !                          ** default : [0.0]
    !                          ** unit : °C d
    !                          ** inputtype : variable
    !            * name: cumulTT
    !                          ** description : cumul TT at current date
    !                          ** datatype : DOUBLE
    !                          ** variablecategory : auxiliary
    !                          ** min : -200
    !                          ** max : 10000
    !                          ** default : 8.0
    !                          ** unit : °C d
    !                          ** inputtype : variable
        !- outputs:
    !            * name: cumulTTFromZC_65
    !                          ** description :  cumul TT from Anthesis to current date 
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 5000
    !                          ** unit : °C d
    !            * name: cumulTTFromZC_39
    !                          ** description :  cumul TT from FlagLeafLiguleJustVisible to current date 
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 5000
    !                          ** unit : °C d
    !            * name: cumulTTFromZC_91
    !                          ** description :  cumul TT from EndGrainFilling to current date 
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 5000
    !                          ** unit : °C d
        cumulTTFromZC_65 = 0.0
        cumulTTFromZC_39 = 0.0
        cumulTTFromZC_91 = 0.0
        IF(ANY(calendarMoments_t1 .EQ. 'Anthesis')) THEN
            cumulTTFromZC_65 = cumulTT -  &
                    calendarCumuls_t1(indice(calendarMoments_t1, 'Anthesis'))
        END IF
        IF(ANY(calendarMoments_t1 .EQ. 'FlagLeafLiguleJustVisible')) THEN
            cumulTTFromZC_39 = cumulTT -  &
                    calendarCumuls_t1(indice(calendarMoments_t1,  &
                    'FlagLeafLiguleJustVisible'))
        END IF
        IF(ANY(calendarMoments_t1 .EQ. 'EndGrainFilling')) THEN
            cumulTTFromZC_91 = cumulTT -  &
                    calendarCumuls_t1(indice(calendarMoments_t1, 'EndGrainFilling'))
        END IF
    END SUBROUTINE model_cumulttfrom

END MODULE

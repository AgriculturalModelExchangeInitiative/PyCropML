MODULE Ismomentregistredzc_39mod
    USE list_sub
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_ismomentregistredzc_39(calendarMoments_t1, &
        isMomentRegistredZC_39)
        IMPLICIT NONE
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(IN) ::  &
                calendarMoments_t1
        INTEGER, INTENT(OUT) :: isMomentRegistredZC_39
        !- Description:
    !            * Title: Is FlagLeafLiguleJustVisible Model
    !            * Author: Pierre Martre
    !            * Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            * Institution: INRA Montpellier
    !            * Abstract: if FlagLeafLiguleJustVisible is already Registred 
        !- inputs:
    !            * name: calendarMoments_t1
    !                          ** description : List containing appearance of each stage at previous time
    !                          ** variablecategory : state
    !                          ** datatype : STRINGLIST
    !                          ** default : ['Sowing']
    !                          ** unit : 
    !                          ** inputtype : variable
        !- outputs:
    !            * name: isMomentRegistredZC_39
    !                          ** description :  if Flag leaf ligule has already appeared 
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 1
    !                          ** unit : 
        IF (ANY(calendarMoments_t1 .EQ. 'FlagLeafLiguleJustVisible')) THEN
            isMomentRegistredZC_39=1
        ELSE
            isMomentRegistredZC_39=0
        END IF
    END SUBROUTINE model_ismomentregistredzc_39

END MODULE

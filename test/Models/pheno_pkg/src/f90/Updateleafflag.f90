MODULE Updateleafflagmod
    USE list_sub
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_updateleafflag(cumulTT, &
        leafNumber, &
        calendarMoments, &
        calendarDates, &
        calendarCumuls, &
        currentdate, &
        finalLeafNumber, &
        hasFlagLeafLiguleAppeared_t1, &
        phase, &
        hasFlagLeafLiguleAppeared)
        IMPLICIT NONE
        REAL, INTENT(IN) :: cumulTT
        REAL, INTENT(IN) :: leafNumber
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  &
                calendarMoments
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  &
                calendarDates
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(INOUT) :: calendarCumuls
        CHARACTER(65), INTENT(IN) :: currentdate
        REAL, INTENT(IN) :: finalLeafNumber
        INTEGER, INTENT(IN) :: hasFlagLeafLiguleAppeared_t1
        REAL, INTENT(IN) :: phase
        INTEGER, INTENT(OUT) :: hasFlagLeafLiguleAppeared
        !- Description:
    !            * Title: UpdateLeafFlag Model
    !            * Author: Pierre MARTRE
    !            * Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            * Institution: INRA Montpellier
    !            * Abstract: tells if flag leaf has appeared and update the calendar if so
    !    	
        !- inputs:
    !            * name: cumulTT
    !                          ** description : cumul thermal times at current date
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : -200
    !                          ** max : 10000
    !                          ** default : 741.510096671757
    !                          ** unit : °C d
    !                          ** uri : some url
    !                          ** inputtype : variable
    !            * name: leafNumber
    !                          ** description : Actual number of phytomers
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 25
    !                          ** default : 8.919453833361189
    !                          ** unit : leaf
    !                          ** uri : some url
    !                          ** inputtype : variable
    !            * name: calendarMoments
    !                          ** description : List containing apparition of each stage
    !                          ** variablecategory : state
    !                          ** datatype : STRINGLIST
    !                          ** default : ['Sowing']
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: calendarDates
    !                          ** description : List containing  the dates of the wheat developmental phases
    !                          ** variablecategory : state
    !                          ** datatype : DATELIST
    !                          ** default : ['2007/3/21']
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: calendarCumuls
    !                          ** description : list containing for each stage occured its cumulated thermal times
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLELIST
    !                          ** default : [0.0]
    !                          ** unit : °C d
    !                          ** inputtype : variable
    !            * name: currentdate
    !                          ** description :  current date
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DATE
    !                          ** default : 2007/4/29
    !                          ** unit : 
    !                          ** uri : some url
    !                          ** inputtype : variable
    !            * name: finalLeafNumber
    !                          ** description : final leaf number
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 8.797582013199484
    !                          ** unit : leaf
    !                          ** uri : some url
    !                          ** inputtype : variable
    !            * name: hasFlagLeafLiguleAppeared_t1
    !                          ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 1
    !                          ** default : 1
    !                          ** unit : 
    !                          ** uri : some url
    !                          ** inputtype : variable
    !            * name: phase
    !                          ** description :  the name of the phase
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 7
    !                          ** default : 1
    !                          ** unit : 
    !                          ** uri : some url
    !                          ** inputtype : variable
        !- outputs:
    !            * name: hasFlagLeafLiguleAppeared
    !                          ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 1
    !                          ** unit : 
    !                          ** uri : some url
    !            * name: calendarMoments
    !                          ** description :  List containing apparition of each stage
    !                          ** variablecategory : state
    !                          ** datatype : STRINGLIST
    !                          ** unit : 
    !            * name: calendarDates
    !                          ** description :  List containing  the dates of the wheat developmental phases
    !                          ** variablecategory : state
    !                          ** datatype : DATELIST
    !                          ** unit : 
    !            * name: calendarCumuls
    !                          ** description :  list containing for each stage occured its cumulated thermal times
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLELIST
    !                          ** unit : °C d
        hasFlagLeafLiguleAppeared = 0
        IF(phase .GE. 1.0 .AND. phase .LT. 4.0) THEN
            IF(leafNumber .GT. 0.0) THEN
                IF(hasFlagLeafLiguleAppeared .EQ. 0 .AND. (finalLeafNumber .GT. 0.0  &
                        .AND. leafNumber .GE. finalLeafNumber)) THEN
                    hasFlagLeafLiguleAppeared = 1
                    IF(ALL(calendarMoments .NE. 'FlagLeafLiguleJustVisible')) THEN
                        call Add(calendarMoments, 'FlagLeafLiguleJustVisible')
                        call Add(calendarCumuls, cumulTT)
                        call Add(calendarDates, currentdate)
                    END IF
                END IF
            END IF
        END IF
    END SUBROUTINE model_updateleafflag

END MODULE

MODULE Updatecalendarmod
    USE list_sub
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_updatecalendar(cumulTT, &
        calendarMoments, &
        calendarDates, &
        calendarCumuls, &
        currentdate, &
        phase)
        IMPLICIT NONE
        REAL, INTENT(IN) :: cumulTT
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  &
                calendarMoments
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  &
                calendarDates
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(INOUT) :: calendarCumuls
        CHARACTER(65), INTENT(IN) :: currentdate
        REAL, INTENT(IN) :: phase
        !- Description:
    !            * Title: Calendar Model
    !            * Author: Pierre Martre
    !            * Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            * Institution: INRA Montpellier
    !            * Abstract: Lists containing for each stage the date it occurs as well as a copy of all types of cumulated thermal times 
        !- inputs:
    !            * name: cumulTT
    !                          ** description : cumul thermal times at current date
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : -200
    !                          ** max : 10000
    !                          ** default : 741.510096671757
    !                          ** unit : °C d
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
    !                          ** description : current date
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DATE
    !                          ** default : 2007/3/27
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: phase
    !                          ** description :  the name of the phase
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 7
    !                          ** default : 1
    !                          ** unit : 
    !                          ** inputtype : variable
        !- outputs:
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
        IF(phase .GE. 1.0 .AND. phase .LT. 2.0 .AND. ALL(calendarMoments .NE.  &
                'Emergence')) THEN
            call Add(calendarMoments, 'Emergence')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .GE. 2.0 .AND. phase .LT. 3.0 .AND.  &
                ALL(calendarMoments .NE. 'FloralInitiation')) THEN
            call Add(calendarMoments, 'FloralInitiation')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .GE. 3.0 .AND. phase .LT. 4.0 .AND.  &
                ALL(calendarMoments .NE. 'Heading')) THEN
            call Add(calendarMoments, 'Heading')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .EQ. 4.0 .AND. ALL(calendarMoments .NE. 'Anthesis'))  &
                THEN
            call Add(calendarMoments, 'Anthesis')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .EQ. 4.5 .AND. ALL(calendarMoments .NE.  &
                'EndCellDivision')) THEN
            call Add(calendarMoments, 'EndCellDivision')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .GE. 5.0 .AND. phase .LT. 6.0 .AND.  &
                ALL(calendarMoments .NE. 'EndGrainFilling')) THEN
            call Add(calendarMoments, 'EndGrainFilling')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .GE. 6.0 .AND. phase .LT. 7.0 .AND.  &
                ALL(calendarMoments .NE. 'Maturity')) THEN
            call Add(calendarMoments, 'Maturity')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        END IF
    END SUBROUTINE model_updatecalendar

END MODULE

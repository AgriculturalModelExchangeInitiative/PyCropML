MODULE Registerzadokmod
    USE list_sub
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_registerzadok(cumulTT, &
        phase, &
        leafNumber, &
        calendarMoments, &
        calendarDates, &
        calendarCumuls, &
        cumulTTFromZC_65, &
        currentdate, &
        der, &
        slopeTSFLN, &
        intTSFLN, &
        finalLeafNumber, &
        currentZadokStage, &
        hasZadokStageChanged_t1, &
        sowingDate, &
        hasZadokStageChanged)
        IMPLICIT NONE
        REAL, INTENT(IN) :: cumulTT
        REAL, INTENT(IN) :: phase
        REAL, INTENT(IN) :: leafNumber
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  &
                calendarMoments
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  &
                calendarDates
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(INOUT) :: calendarCumuls
        REAL, INTENT(IN) :: cumulTTFromZC_65
        CHARACTER(65), INTENT(IN) :: currentdate
        REAL, INTENT(IN) :: der
        REAL, INTENT(IN) :: slopeTSFLN
        REAL, INTENT(IN) :: intTSFLN
        REAL, INTENT(IN) :: finalLeafNumber
        CHARACTER(65), INTENT(INOUT) :: currentZadokStage
        INTEGER, INTENT(IN) :: hasZadokStageChanged_t1
        CHARACTER(65), INTENT(IN) :: sowingDate
        INTEGER, INTENT(OUT) :: hasZadokStageChanged
        INTEGER:: roundedFinalLeafNumber
        !- Description:
    !            * Title: RegisterZadok Model
    !            * Author: Pierre MARTRE
    !            * Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            * Institution: INRA/LEPSE Montpellier
    !            * Abstract: Record the zadok stage in the calendar
    !    	
        !- inputs:
    !            * name: cumulTT
    !                          ** description : 
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : -200
    !                          ** max : 10000
    !                          ** default : 354.582294511779
    !                          ** unit : °C d
    !                          ** uri : some url
    !                          ** inputtype : variable
    !            * name: phase
    !                          ** description : instance of the phase class . You can get the name of the phase using phase.getPhaseAsString(PhaseValue) 
    !                          ** variablecategory : state
    !                          ** inputtype : variable
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 7
    !                          ** default : 2
    !                          ** unit : 
    !                          ** uri : some url
    !            * name: leafNumber
    !                          ** description : Actual number of phytomers
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 25
    !                          ** default : 4.8854219661087575
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
    !            * name: cumulTTFromZC_65
    !                          ** description : cumul of the thermal time (DeltaTT) since the moment ZC_65
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : -200
    !                          ** max : 10000
    !                          ** default : 0
    !                          ** unit : °C d
    !                          ** uri : some url
    !                          ** inputtype : variable
    !            * name: currentdate
    !                          ** description : current date
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DATE
    !                          ** min : 
    !                          ** max : 
    !                          ** default : 2007/4/9
    !                          ** unit : 
    !                          ** uri : some url
    !                          ** inputtype : variable
    !            * name: der
    !                          ** description : Duration of the endosperm endoreduplication phase
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 300.0
    !                          ** unit : °C d
    !                          ** uri : some url
    !                          ** inputtype : parameter
    !            * name: slopeTSFLN
    !                          ** description : used to calculate Terminal spikelet
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 0.9
    !                          ** unit : 
    !                          ** uri : some url
    !                          ** inputtype : parameter
    !            * name: intTSFLN
    !                          ** description : used to calculate Terminal spikelet
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 0.9
    !                          ** unit : 
    !                          ** uri : some url
    !                          ** inputtype : parameter
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
    !            * name: currentZadokStage
    !                          ** description : current zadok stage
    !                          ** variablecategory : state
    !                          ** datatype : STRING
    !                          ** min : 
    !                          ** max : 
    !                          ** default : MainShootPlus1Tiller
    !                          ** unit : 
    !                          ** uri : some url
    !                          ** inputtype : variable
    !            * name: hasZadokStageChanged_t1
    !                          ** description : true if the zadok stage has changed this time step
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 1
    !                          ** default : 0
    !                          ** unit : 
    !                          ** uri : some url
    !                          ** inputtype : variable
    !            * name: sowingDate
    !                          ** description :  Date of Sowing
    !                          ** parametercategory : constant
    !                          ** datatype : DATE
    !                          ** min : 
    !                          ** max : 
    !                          ** default : 2007/3/21
    !                          ** unit : 
    !                          ** inputtype : parameter
        !- outputs:
    !            * name: hasZadokStageChanged
    !                          ** description : true if the zadok stage has changed this time step
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 1
    !                          ** unit : 
    !                          ** uri : some url
    !            * name: currentZadokStage
    !                          ** description : current zadok stage
    !                          ** variablecategory : state
    !                          ** datatype : STRING
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
        roundedFinalLeafNumber = INT(finalLeafNumber + 0.5)
        IF(leafNumber .GE. 4.0 .AND. ALL(calendarMoments .NE.  &
                'MainShootPlus1Tiller')) THEN
            call Add(calendarMoments, 'MainShootPlus1Tiller')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'MainShootPlus1Tiller'
        ELSE IF ( leafNumber .GE. 5.0 .AND. ALL(calendarMoments .NE.  &
                'MainShootPlus2Tiller')) THEN
            call Add(calendarMoments, 'MainShootPlus2Tiller')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'MainShootPlus2Tiller'
        ELSE IF ( leafNumber .GE. 6.0 .AND. ALL(calendarMoments .NE.  &
                'MainShootPlus3Tiller')) THEN
            call Add(calendarMoments, 'MainShootPlus3Tiller')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'MainShootPlus3Tiller'
        ELSE IF ( finalLeafNumber .GT. 0.0 .AND. (leafNumber .GE. slopeTSFLN  &
                * finalLeafNumber - intTSFLN .AND. ALL(calendarMoments .NE.  &
                'TerminalSpikelet'))) THEN
            call Add(calendarMoments, 'TerminalSpikelet')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'TerminalSpikelet'
        ELSE IF ( leafNumber .GE. roundedFinalLeafNumber - 4.0 .AND.  &
                roundedFinalLeafNumber - 4 .GT. 0 .AND. ALL(calendarMoments .NE.  &
                'PseudoStemErection')) THEN
            call Add(calendarMoments, 'PseudoStemErection')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'PseudoStemErection'
        ELSE IF ( leafNumber .GE. roundedFinalLeafNumber - 3.0 .AND.  &
                roundedFinalLeafNumber - 3 .GT. 0 .AND. ALL(calendarMoments .NE.  &
                '1stNodeDetectable')) THEN
            call Add(calendarMoments, '1stNodeDetectable')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = '1stNodeDetectable'
        ELSE IF ( leafNumber .GE. roundedFinalLeafNumber - 2.0 .AND.  &
                roundedFinalLeafNumber - 2 .GT. 0 .AND. ALL(calendarMoments .NE.  &
                '2ndNodeDetectable')) THEN
            call Add(calendarMoments, '2ndNodeDetectable')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = '2ndNodeDetectable'
        ELSE IF ( leafNumber .GE. roundedFinalLeafNumber - 1.0 .AND.  &
                roundedFinalLeafNumber - 1 .GT. 0 .AND. ALL(calendarMoments .NE.  &
                'FlagLeafJustVisible')) THEN
            call Add(calendarMoments, 'FlagLeafJustVisible')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'FlagLeafJustVisible'
        ELSE IF ( ALL(calendarMoments .NE. 'MidGrainFilling') .AND. (phase  &
                .EQ. 4.5 .AND. cumulTTFromZC_65 .GE. der)) THEN
            call Add(calendarMoments, 'MidGrainFilling')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'MidGrainFilling'
        ELSE
            hasZadokStageChanged = 0
        END IF
    END SUBROUTINE model_registerzadok

END MODULE

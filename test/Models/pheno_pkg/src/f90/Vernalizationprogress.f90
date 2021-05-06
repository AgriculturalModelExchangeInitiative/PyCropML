MODULE Vernalizationprogressmod
    USE list_sub
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_vernalizationprogress(dayLength, &
        deltaTT, &
        cumulTT, &
        leafNumber_t1, &
        calendarMoments_t1, &
        calendarDates_t1, &
        calendarCumuls_t1, &
        minTvern, &
        intTvern, &
        vAI, &
        vBEE, &
        minDL, &
        maxDL, &
        maxTvern, &
        pNini, &
        aMXLFNO, &
        vernaprog_t1, &
        currentdate, &
        isVernalizable, &
        minFinalNumber_t1, &
        vernaprog, &
        minFinalNumber, &
        calendarMoments, &
        calendarDates, &
        calendarCumuls)
        IMPLICIT NONE
        REAL, INTENT(IN) :: dayLength
        REAL, INTENT(IN) :: deltaTT
        REAL, INTENT(IN) :: cumulTT
        REAL, INTENT(IN) :: leafNumber_t1
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(IN) ::  &
                calendarMoments_t1
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(IN) ::  &
                calendarDates_t1
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(IN) :: calendarCumuls_t1
        REAL, INTENT(IN) :: minTvern
        REAL, INTENT(IN) :: intTvern
        REAL, INTENT(IN) :: vAI
        REAL, INTENT(IN) :: vBEE
        REAL, INTENT(IN) :: minDL
        REAL, INTENT(IN) :: maxDL
        REAL, INTENT(IN) :: maxTvern
        REAL, INTENT(IN) :: pNini
        REAL, INTENT(IN) :: aMXLFNO
        REAL, INTENT(IN) :: vernaprog_t1
        CHARACTER(65), INTENT(IN) :: currentdate
        INTEGER, INTENT(IN) :: isVernalizable
        REAL, INTENT(IN) :: minFinalNumber_t1
        REAL, INTENT(OUT) :: vernaprog
        REAL, INTENT(OUT) :: minFinalNumber
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(OUT) ::  &
                calendarMoments
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(OUT) ::  &
                calendarDates
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(OUT) :: calendarCumuls
        REAL:: maxVernaProg
        REAL:: dLverna
        REAL:: primordno
        REAL:: minLeafNumber
        REAL:: potlfno
        REAL:: tt
        !- Description:
    !            * Title: VernalizationProgress Model
    !            * Author: Pierre MARTRE
    !            * Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            * Institution: INRA Montpellier
    !            * Abstract: Calculate progress (VernaProg) towards vernalization, but there 
    !        			is no vernalization below minTvern 
    !        			and above maxTvern . The maximum value of VernaProg is 1.
    !        			Progress towards full vernalization is a linear function of shoot 
    !        			temperature (soil temperature until leaf # reach MaxLeafSoil and then
    !        			 canopy temperature)
    !    	
        !- inputs:
    !            * name: dayLength
    !                          ** description : day length
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 12.3037621834005
    !                          ** unit : mm2 m-2
    !                          ** inputtype : variable
    !            * name: deltaTT
    !                          ** description : difference cumul TT between j and j-1 day 
    !                          ** variablecategory : auxiliary
    !                          ** inputtype : variable
    !                          ** datatype : DOUBLE
    !                          ** min : -20
    !                          ** max : 100
    !                          ** default : 20.3429985011972
    !                          ** unit : °C d
    !            * name: cumulTT
    !                          ** description : cumul thermal times at currentdate
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : -200
    !                          ** max : 10000
    !                          ** default : 112.330110409888
    !                          ** unit : °C d
    !                          ** inputtype : variable
    !            * name: leafNumber_t1
    !                          ** description : Actual number of phytomers
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 25
    !                          ** default : 0
    !                          ** unit : leaf
    !                          ** inputtype : variable
    !            * name: calendarMoments_t1
    !                          ** description : List containing appearance of each stage
    !                          ** variablecategory : state
    !                          ** datatype : STRINGLIST
    !                          ** default : ['Sowing']
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: calendarDates_t1
    !                          ** description : List containing  the dates of the wheat developmental phases
    !                          ** variablecategory : state
    !                          ** datatype : DATELIST
    !                          ** default : ['2007/3/21']
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: calendarCumuls_t1
    !                          ** description : list containing for each stage occured its cumulated thermal times
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLELIST
    !                          ** default : [0.0]
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: minTvern
    !                          ** description : Minimum temperature for vernalization to occur
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : -20
    !                          ** max : 60
    !                          ** default : 0.0
    !                          ** unit : °C
    !                          ** inputtype : parameter
    !            * name: intTvern
    !                          ** description : Intermediate temperature for vernalization to occur
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : -20
    !                          ** max : 60
    !                          ** default :  11.0
    !                          ** unit : °C
    !                          ** inputtype : parameter
    !            * name: vAI
    !                          ** description : Response of vernalization rate to temperature
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 1
    !                          ** default :  0.015
    !                          ** unit : d-1 °C-1
    !                          ** inputtype : parameter
    !            * name: vBEE
    !                          ** description : Vernalization rate at 0°C
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 1
    !                          ** default : 0.01
    !                          ** unit : d-1
    !                          ** inputtype : parameter
    !            * name: minDL
    !                          ** description : Threshold daylength below which it does influence vernalization rate
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 12
    !                          ** max : 24
    !                          ** default : 8.0
    !                          ** unit : h
    !                          ** inputtype : parameter
    !            * name: maxDL
    !                          ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 24
    !                          ** default : 15.0
    !                          ** unit : h
    !                          ** inputtype : parameter
    !            * name: maxTvern
    !                          ** description : Maximum temperature for vernalization to occur
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : -20
    !                          ** max : 60
    !                          ** default :  23.0
    !                          ** unit : °C
    !                          ** inputtype : parameter
    !            * name: pNini
    !                          ** description : Number of primorida in the apex at emergence
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 24
    !                          ** default : 4.0
    !                          ** unit : primordia
    !                          ** inputtype : parameter
    !            * name: aMXLFNO
    !                          ** description : Absolute maximum leaf number
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 25
    !                          ** default : 24.0
    !                          ** unit : leaf
    !                          ** inputtype : parameter
    !            * name: vernaprog_t1
    !                          ** description : progression on a 0  to 1 scale of the vernalization
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 1
    !                          ** default :  0.5517254187376879
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: currentdate
    !                          ** description : current date 
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DATE
    !                          ** default : 2007/3/27
    !                          ** inputtype : variable
    !                          ** unit : 
    !            * name: isVernalizable
    !                          ** description : true if the plant is vernalizable
    !                          ** parametercategory : species
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 1
    !                          ** default : 1
    !                          ** unit : 
    !                          ** inputtype : parameter
    !            * name: minFinalNumber_t1
    !                          ** description : minimum final leaf number
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 25
    !                          ** default : 5.5
    !                          ** unit : leaf
    !                          ** inputtype : variable
    !                          ** variablecategory : state
        !- outputs:
    !            * name: vernaprog
    !                          ** description : progression on a 0  to 1 scale of the vernalization
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : 
    !            * name: minFinalNumber
    !                          ** description : minimum final leaf number
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : leaf
    !            * name: calendarMoments
    !                          ** description : List containing appearance of each stage
    !                          ** variablecategory : state
    !                          ** datatype : STRINGLIST
    !                          ** unit : 
    !            * name: calendarDates
    !                          ** description : List containing  the dates of the wheat developmental phases
    !                          ** variablecategory : state
    !                          ** datatype : DATELIST
    !                          ** unit : 
    !            * name: calendarCumuls
    !                          ** description : list containing for each stage occured its cumulated thermal times
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLELIST
    !                          ** unit : 
        calendarMoments = calendarMoments_t1
        calendarCumuls = calendarCumuls_t1
        calendarDates = calendarDates_t1
        minFinalNumber = minFinalNumber_t1
        vernaprog = vernaprog_t1
        IF(isVernalizable .EQ. 1 .AND. vernaprog_t1 .LT. 1.0) THEN
            tt = deltaTT
            IF(tt .GE. minTvern .AND. tt .LE. intTvern) THEN
                vernaprog = vernaprog_t1 + (vAI * tt) + vBEE
            ELSE
                vernaprog = vernaprog_t1
            END IF
            IF(tt .GT. intTvern) THEN
                maxVernaProg = vAI * intTvern + vBEE
                dLverna = MAX(minDL, min(maxDL, dayLength))
                vernaprog = vernaprog + MAX(0.0, maxVernaProg * (1.0 + ((intTvern -  &
                        tt) / (maxTvern - intTvern) * ((dLverna - minDL) / (maxDL - minDL)))))
            END IF
            primordno = 2.0 * leafNumber_t1 + pNini
            minLeafNumber = minFinalNumber_t1
            IF(vernaprog .GE. 1.0 .OR. primordno .GE. aMXLFNO) THEN
                minFinalNumber = MAX(primordno, minFinalNumber_t1)
                call Add(calendarMoments, 'EndVernalisation')
                call Add(calendarCumuls, cumulTT)
                call Add(calendarDates, currentdate)
                vernaprog = MAX(1.0, vernaprog)
            ELSE
                potlfno = aMXLFNO - ((aMXLFNO - minLeafNumber) * vernaprog)
                IF(primordno .GE. potlfno) THEN
                    minFinalNumber = MAX((potlfno + primordno) / 2.0, minFinalNumber_t1)
                    vernaprog = MAX(1.0, vernaprog)
                    call Add(calendarMoments, 'EndVernalisation')
                    call Add(calendarCumuls, cumulTT)
                    call Add(calendarDates, currentdate)
                END IF
            END IF
        END IF
    END SUBROUTINE model_vernalizationprogress

END MODULE

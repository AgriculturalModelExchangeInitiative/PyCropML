MODULE Updatephasemod
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_updatephase(cumulTT, &
        leafNumber_t1, &
        cumulTTFromZC_39, &
        isMomentRegistredZC_39, &
        gAI, &
        grainCumulTT, &
        dayLength, &
        vernaprog, &
        minFinalNumber, &
        fixPhyll, &
        isVernalizable, &
        dse, &
        pFLLAnth, &
        dcd, &
        dgf, &
        degfm, &
        maxDL, &
        sLDL, &
        ignoreGrainMaturation, &
        pHEADANTH, &
        choosePhyllUse, &
        p, &
        phase_t1, &
        cumulTTFromZC_91, &
        phyllochron, &
        hasLastPrimordiumAppeared_t1, &
        finalLeafNumber_t1, &
        finalLeafNumber, &
        phase, &
        hasLastPrimordiumAppeared)
        IMPLICIT NONE
        REAL, INTENT(IN) :: cumulTT
        REAL, INTENT(IN) :: leafNumber_t1
        REAL, INTENT(IN) :: cumulTTFromZC_39
        INTEGER, INTENT(IN) :: isMomentRegistredZC_39
        REAL, INTENT(IN) :: gAI
        REAL, INTENT(IN) :: grainCumulTT
        REAL, INTENT(IN) :: dayLength
        REAL, INTENT(IN) :: vernaprog
        REAL, INTENT(IN) :: minFinalNumber
        REAL, INTENT(IN) :: fixPhyll
        INTEGER, INTENT(IN) :: isVernalizable
        REAL, INTENT(IN) :: dse
        REAL, INTENT(IN) :: pFLLAnth
        REAL, INTENT(IN) :: dcd
        REAL, INTENT(IN) :: dgf
        REAL, INTENT(IN) :: degfm
        REAL, INTENT(IN) :: maxDL
        REAL, INTENT(IN) :: sLDL
        LOGICAL, INTENT(IN) :: ignoreGrainMaturation
        REAL, INTENT(IN) :: pHEADANTH
        CHARACTER(65), INTENT(IN) :: choosePhyllUse
        REAL, INTENT(IN) :: p
        REAL, INTENT(IN) :: phase_t1
        REAL, INTENT(IN) :: cumulTTFromZC_91
        REAL, INTENT(IN) :: phyllochron
        INTEGER, INTENT(IN) :: hasLastPrimordiumAppeared_t1
        REAL, INTENT(IN) :: finalLeafNumber_t1
        REAL, INTENT(OUT) :: finalLeafNumber
        REAL, INTENT(OUT) :: phase
        INTEGER, INTENT(OUT) :: hasLastPrimordiumAppeared
        REAL:: ttFromLastLeafToHeading
        REAL:: appFLN
        REAL:: localDegfm
        REAL:: ttFromLastLeafToAnthesis
        !- Description:
    !            * Title: UpdatePhase Model
    !            * Author: Pierre MARTRE
    !            * Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            * Institution: INRA Montpellier
    !            * Abstract: This strategy advances the phase and calculate the final leaf number
    !    	
        !- inputs:
    !            * name: cumulTT
    !                          ** description : cumul thermal times at current date
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : -200
    !                          ** max : 10000
    !                          ** default : 354.582294511779
    !                          ** unit : °C d
    !                          ** inputtype : variable
    !            * name: leafNumber_t1
    !                          ** description : Actual number of phytomers
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 25
    !                          ** default :  4.620511621863958
    !                          ** unit : leaf
    !                          ** inputtype : variable
    !            * name: cumulTTFromZC_39
    !                          ** description : cumul of the thermal time ( DeltaTT) since the moment ZC_39
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 0
    !                          ** unit : °C d-1
    !                          ** inputtype : variable
    !            * name: isMomentRegistredZC_39
    !                          ** description : true if ZC_39 is registered in the calendar
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 1
    !                          ** default : 0
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: gAI
    !                          ** description : used to calculate Terminal spikelet
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 0.3255196285135
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: grainCumulTT
    !                          ** description : cumulTT used for the grain developpment
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 0
    !                          ** unit : °C d
    !                          ** inputtype : variable
    !            * name: dayLength
    !                          ** description : length of the day
    !                          ** datatype : DOUBLE
    !                          ** variablecategory : auxiliary
    !                          ** min : 0
    !                          ** max : 24
    !                          ** unit : h
    !                          ** default : 12.7433275303389
    !                          ** inputtype : variable
    !            * name: vernaprog
    !                          ** description : progression on a 0  to 1 scale of the vernalization
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10
    !                          ** default :  1.0532526829571554
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: minFinalNumber
    !                          ** description : minimum final leaf number
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 25
    !                          ** default : 6.879410413987549
    !                          ** unit : leaf
    !                          ** inputtype : variable
    !            * name: fixPhyll
    !                          ** description : Phyllochron with sowing date fix
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 91.2
    !                          ** unit : °C d
    !                          ** inputtype : variable
    !            * name: isVernalizable
    !                          ** description : true if the plant is vernalizable
    !                          ** parametercategory : species
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 1
    !                          ** unit : 
    !                          ** default : 1
    !                          ** inputtype : parameter
    !            * name: dse
    !                          ** description : Thermal time from sowing to emergence
    !                          ** parametercategory : genotypic
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 1000
    !                          ** default : 105
    !                          ** unit : °C d
    !                          ** inputtype : parameter
    !            * name: pFLLAnth
    !                          ** description : Phyllochronic duration of the period between flag leaf ligule appearance and anthesis
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 1000
    !                          ** unit : 
    !                          ** default : 2.22
    !                          ** inputtype : parameter
    !            * name: dcd
    !                          ** description : Duration of the endosperm cell division phase
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 100
    !                          ** unit : °C d
    !                          ** inputtype : parameter
    !            * name: dgf
    !                          ** description : Grain filling duration (from anthesis to physiological maturity)
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 450
    !                          ** unit : °C d
    !                          ** inputtype : parameter
    !            * name: degfm
    !                          ** description : Grain maturation duration (from physiological maturity to harvest ripeness)
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 50
    !                          ** default : 0
    !                          ** unit : °C d
    !                          ** inputtype : parameter
    !            * name: maxDL
    !                          ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 24
    !                          ** default : 15
    !                          ** unit : h
    !                          ** inputtype : parameter
    !            * name: sLDL
    !                          ** description : Daylength response of leaf production
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 1
    !                          ** default : 0.85
    !                          ** unit : leaf h-1
    !                          ** inputtype : parameter
    !            * name: ignoreGrainMaturation
    !                          ** description : true to ignore grain maturation
    !                          ** parametercategory : species
    !                          ** datatype : BOOLEAN
    !                          ** default : FALSE
    !                          ** unit : 
    !                          ** inputtype : parameter
    !            * name: pHEADANTH
    !                          ** description : Number of phyllochron between heading and anthesiss
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 1000
    !                          ** default : 1
    !                          ** unit : 
    !                          ** inputtype : parameter
    !            * name: choosePhyllUse
    !                          ** description : Switch to choose the type of phyllochron calculation to be used
    !                          ** parametercategory : species
    !                          ** datatype : STRING
    !                          ** unit : 
    !                          ** default : Default
    !                          ** inputtype : parameter
    !            * name: p
    !                          ** description : Phyllochron (Varietal parameter)
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 1000
    !                          ** default : 120
    !                          ** unit : °C d leaf-1
    !                          ** inputtype : parameter
    !            * name: phase_t1
    !                          ** description :  the name of the phase
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 7
    !                          ** default : 1
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: cumulTTFromZC_91
    !                          ** description : cumul of the thermal time (DeltaTT) since the moment ZC_91
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 5000
    !                          ** default : 0
    !                          ** unit : °C d-1
    !                          ** inputtype : variable
    !            * name: phyllochron
    !                          ** description : Phyllochron
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 1000
    !                          ** default : 91.2
    !                          ** unit : °C d leaf-1
    !                          ** inputtype : variable
    !            * name: hasLastPrimordiumAppeared_t1
    !                          ** description : if Last Primordium has Appeared
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 1
    !                          ** default : 0
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: finalLeafNumber_t1
    !                          ** description : final leaf number
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 25
    !                          ** default : 0
    !                          ** unit : leaf
    !                          ** inputtype : variable
        !- outputs:
    !            * name: finalLeafNumber
    !                          ** description : final leaf number
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 25
    !                          ** unit : leaf
    !            * name: phase
    !                          ** description : the name of the phase
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 7
    !                          ** unit : 
    !            * name: hasLastPrimordiumAppeared
    !                          ** description : if Last Primordium has Appeared
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 1
    !                          ** unit : 
        hasLastPrimordiumAppeared = hasLastPrimordiumAppeared_t1
        finalLeafNumber = finalLeafNumber_t1
        phase = phase_t1
        IF(phase_t1 .GE. 0.0 .AND. phase_t1 .LT. 1.0) THEN
            IF(cumulTT .GE. dse) THEN
                phase = 1.0
            ELSE
                phase = phase_t1
            END IF
        ELSE IF ( phase_t1 .GE. 1.0 .AND. phase_t1 .LT. 2.0) THEN
            IF(isVernalizable .EQ. 1 .AND. vernaprog .GE. 1.0 .OR. isVernalizable  &
                    .EQ. 0) THEN
                IF(dayLength .GT. maxDL) THEN
                    finalLeafNumber = minFinalNumber
                    hasLastPrimordiumAppeared = 1
                ELSE
                    appFLN = minFinalNumber + (sLDL * (maxDL - dayLength))
                    IF(appFLN / 2.0 .LE. leafNumber_t1) THEN
                        finalLeafNumber = appFLN
                        hasLastPrimordiumAppeared = 1
                    ELSE
                        phase = phase_t1
                    END IF
                END IF
                IF(hasLastPrimordiumAppeared .EQ. 1) THEN
                    phase = 2.0
                END IF
            ELSE
                phase = phase_t1
            END IF
        ELSE IF ( phase_t1 .GE. 2.0 .AND. phase_t1 .LT. 4.0) THEN
            IF(isMomentRegistredZC_39 .EQ. 1) THEN
                IF(phase_t1 .LT. 3.0) THEN
                    ttFromLastLeafToHeading = 0.0
                    IF(choosePhyllUse .EQ. 'Default') THEN
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * fixPhyll
                    ELSE IF ( choosePhyllUse .EQ. 'PTQ') THEN
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron
                    ELSE IF ( choosePhyllUse .EQ. 'Test') THEN
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p
                    END IF
                    IF(cumulTTFromZC_39 .GE. ttFromLastLeafToHeading) THEN
                        phase = 3.0
                    ELSE
                        phase = phase_t1
                    END IF
                ELSE
                    phase = phase_t1
                END IF
                ttFromLastLeafToAnthesis = 0.0
                IF(choosePhyllUse .EQ. 'Default') THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll
                ELSE IF ( choosePhyllUse .EQ. 'PTQ') THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * phyllochron
                ELSE IF ( choosePhyllUse .EQ. 'Test') THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * p
                END IF
                IF(cumulTTFromZC_39 .GE. ttFromLastLeafToAnthesis) THEN
                    phase = 4.0
                END IF
            ELSE
                phase = phase_t1
            END IF
        ELSE IF ( phase_t1 .EQ. 4.0) THEN
            IF(grainCumulTT .GE. dcd) THEN
                phase = 4.5
            ELSE
                phase = phase_t1
            END IF
        ELSE IF ( phase_t1 .EQ. 4.5) THEN
            IF(grainCumulTT .GE. dgf .OR. gAI .LE. 0.0) THEN
                phase = 5.0
            ELSE
                phase = phase_t1
            END IF
        ELSE IF ( phase_t1 .GE. 5.0 .AND. phase_t1 .LT. 6.0) THEN
            localDegfm = degfm
            IF(ignoreGrainMaturation) THEN
                localDegfm = -1.0
            END IF
            IF(cumulTTFromZC_91 .GE. localDegfm) THEN
                phase = 6.0
            ELSE
                phase = phase_t1
            END IF
        ELSE IF ( phase_t1 .GE. 6.0 .AND. phase_t1 .LT. 7.0) THEN
            phase = phase_t1
        END IF
    END SUBROUTINE model_updatephase

END MODULE

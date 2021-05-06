MODULE Leafnumbermod
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_leafnumber(deltaTT, &
        phyllochron_t1, &
        hasFlagLeafLiguleAppeared, &
        leafNumber_t1, &
        phase, &
        leafNumber)
        IMPLICIT NONE
        REAL, INTENT(IN) :: deltaTT
        REAL, INTENT(IN) :: phyllochron_t1
        INTEGER, INTENT(IN) :: hasFlagLeafLiguleAppeared
        REAL, INTENT(IN) :: leafNumber_t1
        REAL, INTENT(IN) :: phase
        REAL, INTENT(OUT) :: leafNumber
        REAL:: phyllochron_
        !- Description:
    !            * Title: CalculateLeafNumber Model
    !            * Author: Pierre MARTRE
    !            * Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            * Institution: INRA Montpellier
    !            * Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day
        !- inputs:
    !            * name: deltaTT
    !                          ** description : daily delta TT 
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** min : -20
    !                          ** max : 100
    !                          ** default : 23.5895677277199
    !                          ** unit : °C d
    !                          ** inputtype : variable
    !            * name: phyllochron_t1
    !                          ** description : phyllochron
    !                          ** variablecategory : state
    !                          ** inputtype : variable
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 1000
    !                          ** default : 0
    !                          ** unit : °C d leaf-1
    !            * name: hasFlagLeafLiguleAppeared
    !                          ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 1
    !                          ** default : 0
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: leafNumber_t1
    !                          ** description :  Actual number of phytomers
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 25
    !                          ** default : 0
    !                          ** unit : leaf
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
    !            * name: leafNumber
    !                          ** description : Actual number of phytomers
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : leaf
    !                          ** uri : some url
        leafNumber = leafNumber_t1
        IF(phase .GE. 1.0 .AND. phase .LT. 4.0) THEN
            IF(hasFlagLeafLiguleAppeared .EQ. 0) THEN
                IF(phyllochron_t1 .EQ. 0.0) THEN
                    phyllochron_ = 0.0000001
                ELSE
                    phyllochron_ = phyllochron_t1
                END IF
                leafNumber = leafNumber_t1 + min(deltaTT / phyllochron_, 0.999)
            END IF
        END IF
    END SUBROUTINE model_leafnumber

END MODULE

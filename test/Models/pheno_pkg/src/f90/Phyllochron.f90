MODULE Phyllochronmod
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_phyllochron(fixPhyll, &
        leafNumber, &
        lincr, &
        ldecr, &
        pdecr, &
        pincr, &
        ptq, &
        gAImean, &
        kl, &
        pTQhf, &
        B, &
        p, &
        choosePhyllUse, &
        areaSL, &
        areaSS, &
        lARmin, &
        lARmax, &
        sowingDensity, &
        lNeff, &
        phyllochron)
        IMPLICIT NONE
        REAL, INTENT(IN) :: fixPhyll
        REAL, INTENT(IN) :: leafNumber
        REAL, INTENT(IN) :: lincr
        REAL, INTENT(IN) :: ldecr
        REAL, INTENT(IN) :: pdecr
        REAL, INTENT(IN) :: pincr
        REAL, INTENT(IN) :: ptq
        REAL, INTENT(IN) :: gAImean
        REAL, INTENT(IN) :: kl
        REAL, INTENT(IN) :: pTQhf
        REAL, INTENT(IN) :: B
        REAL, INTENT(IN) :: p
        CHARACTER(65), INTENT(IN) :: choosePhyllUse
        REAL, INTENT(IN) :: areaSL
        REAL, INTENT(IN) :: areaSS
        REAL, INTENT(IN) :: lARmin
        REAL, INTENT(IN) :: lARmax
        REAL, INTENT(IN) :: sowingDensity
        REAL, INTENT(IN) :: lNeff
        REAL, INTENT(OUT) :: phyllochron
        REAL:: gaiLim
        REAL:: LAR
        !- Description:
    !            * Title: Phyllochron Model
    !            * Author: Pierre Martre
    !            * Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            * Institution: INRA Montpellier
    !            * Abstract: Calculate different types of phyllochron 
        !- inputs:
    !            * name: fixPhyll
    !                          ** description : Sowing date corrected Phyllochron
    !                          ** inputtype : variable
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** default : 5.0
    !                          ** min : 0.0
    !                          ** max : 10000.0
    !                          ** unit : °C d leaf-1
    !                          ** uri : some url
    !            * name: leafNumber
    !                          ** description : Actual number of phytomers
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 25.0
    !                          ** unit : leaf
    !                          ** uri : some url
    !            * name: lincr
    !                          ** description : Leaf number above which the phyllochron is increased by Pincr
    !                          ** inputtype : parameter
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** default : 8.0
    !                          ** min : 0.0
    !                          ** max : 30.0
    !                          ** unit : leaf
    !                          ** uri : some url
    !            * name: ldecr
    !                          ** description : Leaf number up to which the phyllochron is decreased by Pdecr
    !                          ** inputtype : parameter
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 100.0
    !                          ** unit : leaf
    !                          ** uri : some url
    !            * name: pdecr
    !                          ** description : Factor decreasing the phyllochron for leaf number less than Ldecr
    !                          ** inputtype : parameter
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** default : 0.4
    !                          ** min : 0.0
    !                          ** max : 10.0
    !                          ** unit : -
    !                          ** uri : some url
    !            * name: pincr
    !                          ** description : Factor increasing the phyllochron for leaf number higher than Lincr
    !                          ** inputtype : parameter
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** default : 1.5
    !                          ** min : 0.0
    !                          ** max : 10.0
    !                          ** unit : -
    !                          ** uri : some url
    !            * name: ptq
    !                          ** description : Photothermal quotient 
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 10000.0
    !                          ** unit : MJ °C-1 d-1 m-2)
    !                          ** uri : some url
    !            * name: gAImean
    !                          ** description : Green Area Index
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 10000.0
    !                          ** unit : m2 m-2
    !                          ** uri : some url
    !            * name: kl
    !                          ** description : Exctinction Coefficient
    !                          ** inputtype : parameter
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** default : 0.45
    !                          ** min : 0.0
    !                          ** max : 50.0
    !                          ** unit : -
    !                          ** uri : some url
    !            * name: pTQhf
    !                          ** description : Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient
    !                          ** inputtype : parameter
    !                          ** parametercategory : genotypic
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 1000.0
    !                          ** unit : °C d leaf-1
    !                          ** uri : some url
    !            * name: B
    !                          ** description : Phyllochron at PTQ equal 1
    !                          ** inputtype : parameter
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** default : 20.0
    !                          ** min : 0.0
    !                          ** max : 1000.0
    !                          ** unit : °C d leaf-1
    !                          ** uri : some url
    !            * name: p
    !                          ** description : Phyllochron (Varietal parameter)
    !                          ** inputtype : parameter
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** default : 120.0
    !                          ** min : 0.0
    !                          ** max : 1000.0
    !                          ** unit : °C d leaf-1
    !                          ** uri : some url
    !            * name: choosePhyllUse
    !                          ** description : Switch to choose the type of phyllochron calculation to be used
    !                          ** inputtype : parameter
    !                          ** parametercategory : species
    !                          ** datatype : STRING
    !                          ** default : Default
    !                          ** min : 
    !                          ** max : 
    !                          ** unit : -
    !                          ** uri : some url
    !            * name: areaSL
    !                          ** description :  Area Leaf
    !                          ** inputtype : parameter
    !                          ** parametercategory : genotypic
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 1000.0
    !                          ** unit : cm2
    !                          ** uri : some url
    !            * name: areaSS
    !                          ** description : Area Sheath
    !                          ** inputtype : parameter
    !                          ** parametercategory : genotypic
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 1000.0
    !                          ** unit : cm2
    !                          ** uri : some url
    !            * name: lARmin
    !                          ** description : LAR minimum
    !                          ** inputtype : parameter
    !                          ** parametercategory : genotypic
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 1000.0
    !                          ** unit : leaf-1 °C
    !                          ** uri : some url
    !            * name: lARmax
    !                          ** description : LAR maximum
    !                          ** inputtype : parameter
    !                          ** parametercategory : genotypic
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 1000.0
    !                          ** unit : leaf-1 °C
    !                          ** uri : some url
    !            * name: sowingDensity
    !                          ** description : Sowing Density
    !                          ** inputtype : parameter
    !                          ** parametercategory : genotypic
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 1000.0
    !                          ** unit : plant m-2
    !                          ** uri : some url
    !            * name: lNeff
    !                          ** description : Leaf Number efficace
    !                          ** inputtype : parameter
    !                          ** parametercategory : genotypic
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 1000.0
    !                          ** unit : leaf
    !                          ** uri : some url
        !- outputs:
    !            * name: phyllochron
    !                          ** description :  the rate of leaf appearance 
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 1000
    !                          ** unit :  °C d leaf-1
    !                          ** uri : some url
        phyllochron = 0.0
        LAR = 0.0
        gaiLim = lNeff * ((areaSL + areaSS) / 10000.0) * sowingDensity
        IF(choosePhyllUse .EQ. 'Default') THEN
            IF(leafNumber .LT. ldecr) THEN
                phyllochron = fixPhyll * pdecr
            ELSE IF ( leafNumber .GE. ldecr .AND. leafNumber .LT. lincr) THEN
                phyllochron = fixPhyll
            ELSE
                phyllochron = fixPhyll * pincr
            END IF
        END IF
        IF(choosePhyllUse .EQ. 'PTQ') THEN
            IF(gAImean .GT. gaiLim) THEN
                LAR = (lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B *  &
                        gAImean)
            ELSE
                LAR = (lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B *  &
                        gaiLim)
            END IF
            phyllochron = 1.0 / LAR
        END IF
        IF(choosePhyllUse .EQ. 'Test') THEN
            IF(leafNumber .LT. ldecr) THEN
                phyllochron = p * pdecr
            ELSE IF ( leafNumber .GE. ldecr .AND. leafNumber .LT. lincr) THEN
                phyllochron = p
            ELSE
                phyllochron = p * pincr
            END IF
        END IF
    END SUBROUTINE model_phyllochron

END MODULE

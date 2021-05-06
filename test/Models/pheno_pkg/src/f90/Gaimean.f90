MODULE Gaimeanmod
    USE list_sub
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_gaimean(gAI, &
        tTWindowForPTQ, &
        deltaTT, &
        pastMaxAI_t1, &
        listTTShootWindowForPTQ1_t1, &
        listGAITTWindowForPTQ_t1, &
        gAImean, &
        pastMaxAI, &
        listTTShootWindowForPTQ1, &
        listGAITTWindowForPTQ)
        IMPLICIT NONE
        REAL, INTENT(IN) :: gAI
        REAL, INTENT(IN) :: tTWindowForPTQ
        REAL, INTENT(IN) :: deltaTT
        REAL, INTENT(IN) :: pastMaxAI_t1
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(IN) ::  &
                listTTShootWindowForPTQ1_t1
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(IN) ::  &
                listGAITTWindowForPTQ_t1
        REAL, INTENT(OUT) :: gAImean
        REAL, INTENT(OUT) :: pastMaxAI
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(OUT) ::  &
                listTTShootWindowForPTQ1
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(OUT) :: listGAITTWindowForPTQ
        REAL, ALLOCATABLE , DIMENSION(:):: TTList
        REAL, ALLOCATABLE , DIMENSION(:):: GAIList
        REAL:: SumTT
        INTEGER:: count
        REAL:: gai_
        REAL:: gaiMean_
        INTEGER:: countGaiMean
        INTEGER:: i
        count = 0
        gai_ = 0.0
        gaiMean_ = 0.0
        countGaiMean = 0
        !- Description:
    !            * Title: Average GAI on a specific thermal time window
    !            * Author: Loïc Manceau
    !            * Reference: -
    !            * Institution: INRA
    !            * Abstract: -
        !- inputs:
    !            * name: gAI
    !                          ** description : Green Area Index of the day
    !                          ** inputtype : variable
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 500.0
    !                          ** unit : m2 leaf m-2 ground
    !                          ** uri : 
    !            * name: tTWindowForPTQ
    !                          ** description : Thermal Time window for average
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 5000.0
    !                          ** unit : °C d
    !                          ** uri : 
    !            * name: deltaTT
    !                          ** description : Thermal time increase of the day
    !                          ** inputtype : variable
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 100.0
    !                          ** unit : °C d
    !                          ** uri : 
    !            * name: pastMaxAI_t1
    !                          ** description : Maximum Leaf Area Index reached the current day
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** default : 0.0
    !                          ** min : 0.0
    !                          ** max : 5000.0
    !                          ** unit : m2 leaf m-2 ground
    !                          ** uri : 
    !            * name: listTTShootWindowForPTQ1_t1
    !                          ** description : List of daily shoot thermal time in the window dedicated to average
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLELIST
    !                          ** default : [0.0]
    !                          ** min : 
    !                          ** max : 
    !                          ** unit : °C d
    !                          ** uri : 
    !            * name: listGAITTWindowForPTQ_t1
    !                          ** description : List of daily Green Area Index in the window dedicated to average
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLELIST
    !                          ** default : [0.0]
    !                          ** min : 
    !                          ** max : 
    !                          ** unit : m2 leaf m-2 ground
    !                          ** uri : 
        !- outputs:
    !            * name: gAImean
    !                          ** description : Mean Green Area Index
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0.0
    !                          ** max : 500.0
    !                          ** unit : m2 leaf m-2 ground
    !                          ** uri : 
    !            * name: pastMaxAI
    !                          ** description : Maximum Leaf Area Index reached the current day
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0.0
    !                          ** max : 5000.0
    !                          ** unit : m2 leaf m-2 ground
    !                          ** uri : 
    !            * name: listTTShootWindowForPTQ1
    !                          ** description : List of daily shoot thermal time in the window dedicated to average
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLELIST
    !                          ** min : 
    !                          ** max : 
    !                          ** unit : °C d
    !                          ** uri : 
    !            * name: listGAITTWindowForPTQ
    !                          ** description : List of daily Green Area Index in the window dedicated to average
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLELIST
    !                          ** min : 
    !                          ** max : 
    !                          ** unit : m2 leaf m-2 ground
    !                          ** uri : 
        DO i = 0 , SIZE(listTTShootWindowForPTQ1_t1)-1, 1
            call Add(TTList, listTTShootWindowForPTQ1_t1(i+1))
            call Add(GAIList, listGAITTWindowForPTQ_t1(i+1))
        END DO
        call Add(TTList, deltaTT)
        call Add(GAIList, gAI)
        SumTT = sum(TTList)
        DO WHILE ( SumTT .GT. tTWindowForPTQ )
            SumTT = SumTT - TTList(count+1)
            count = count + 1
        END DO
        DO i = count , SIZE(TTList)-1, 1
            call Add(listTTShootWindowForPTQ1, TTList(i+1))
            call Add(listGAITTWindowForPTQ, GAIList(i+1))
        END DO
        DO i = 0 , SIZE(listGAITTWindowForPTQ)-1, 1
            gaiMean_ = gaiMean_ + listGAITTWindowForPTQ(i+1)
            countGaiMean = countGaiMean + 1
        END DO
        gaiMean_ = gaiMean_ / countGaiMean
        gai_ = MAX(pastMaxAI_t1, gaiMean_)
        pastMaxAI = gai_
        gAImean = gai_
    END SUBROUTINE model_gaimean

END MODULE

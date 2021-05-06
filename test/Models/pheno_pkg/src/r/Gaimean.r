model_gaimean <- function (gAI = 0.0,
         tTWindowForPTQ = 0.0,
         deltaTT = 0.0,
         pastMaxAI_t1 = 0.0,
         listTTShootWindowForPTQ1_t1 = c(0.0),
         listGAITTWindowForPTQ_t1 = c(0.0)){
    #'- Name: GAImean -Version: 1.0, -Time step: 1
    #'- Description:
    #'            * Title: Average GAI on a specific thermal time window
    #'            * Author: Loïc Manceau
    #'            * Reference: -
    #'            * Institution: INRA
    #'            * Abstract: -
    #'- inputs:
    #'            * name: gAI
    #'                          ** description : Green Area Index of the day
    #'                          ** inputtype : variable
    #'                          ** variablecategory : auxiliary
    #'                          ** datatype : DOUBLE
    #'                          ** default : 0.0
    #'                          ** min : 0.0
    #'                          ** max : 500.0
    #'                          ** unit : m2 leaf m-2 ground
    #'                          ** uri : 
    #'            * name: tTWindowForPTQ
    #'                          ** description : Thermal Time window for average
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** default : 0.0
    #'                          ** min : 0.0
    #'                          ** max : 5000.0
    #'                          ** unit : °C d
    #'                          ** uri : 
    #'            * name: deltaTT
    #'                          ** description : Thermal time increase of the day
    #'                          ** inputtype : variable
    #'                          ** variablecategory : auxiliary
    #'                          ** datatype : DOUBLE
    #'                          ** default : 0.0
    #'                          ** min : 0.0
    #'                          ** max : 100.0
    #'                          ** unit : °C d
    #'                          ** uri : 
    #'            * name: pastMaxAI_t1
    #'                          ** description : Maximum Leaf Area Index reached the current day
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** default : 0.0
    #'                          ** min : 0.0
    #'                          ** max : 5000.0
    #'                          ** unit : m2 leaf m-2 ground
    #'                          ** uri : 
    #'            * name: listTTShootWindowForPTQ1_t1
    #'                          ** description : List of daily shoot thermal time in the window dedicated to average
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLELIST
    #'                          ** default : [0.0]
    #'                          ** min : 
    #'                          ** max : 
    #'                          ** unit : °C d
    #'                          ** uri : 
    #'            * name: listGAITTWindowForPTQ_t1
    #'                          ** description : List of daily Green Area Index in the window dedicated to average
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLELIST
    #'                          ** default : [0.0]
    #'                          ** min : 
    #'                          ** max : 
    #'                          ** unit : m2 leaf m-2 ground
    #'                          ** uri : 
    #'- outputs:
    #'            * name: gAImean
    #'                          ** description : Mean Green Area Index
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0.0
    #'                          ** max : 500.0
    #'                          ** unit : m2 leaf m-2 ground
    #'                          ** uri : 
    #'            * name: pastMaxAI
    #'                          ** description : Maximum Leaf Area Index reached the current day
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0.0
    #'                          ** max : 5000.0
    #'                          ** unit : m2 leaf m-2 ground
    #'                          ** uri : 
    #'            * name: listTTShootWindowForPTQ1
    #'                          ** description : List of daily shoot thermal time in the window dedicated to average
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLELIST
    #'                          ** min : 
    #'                          ** max : 
    #'                          ** unit : °C d
    #'                          ** uri : 
    #'            * name: listGAITTWindowForPTQ
    #'                          ** description : List of daily Green Area Index in the window dedicated to average
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLELIST
    #'                          ** min : 
    #'                          ** max : 
    #'                          ** unit : m2 leaf m-2 ground
    #'                          ** uri : 
    listTTShootWindowForPTQ1 <- vector()
    listGAITTWindowForPTQ <- vector()
    TTList <- vector()
    GAIList <- vector()
    count <- 0
    gai_ <- 0.0
    gaiMean_ <- 0.0
    countGaiMean <- 0
    for( i in seq(0, length(listTTShootWindowForPTQ1_t1)-1, 1)){
        TTList <- c(TTList, listTTShootWindowForPTQ1_t1[i+1])
        GAIList <- c(GAIList, listGAITTWindowForPTQ_t1[i+1])
    }
    TTList <- c(TTList, deltaTT)
    GAIList <- c(GAIList, gAI)
    SumTT <- sum(TTList)
    while( SumTT > tTWindowForPTQ){
        SumTT <- SumTT - TTList[count+1]
        count <- count + 1}
    for( i in seq(count, length(TTList)-1, 1)){
        listTTShootWindowForPTQ1 <- c(listTTShootWindowForPTQ1, TTList[i+1])
        listGAITTWindowForPTQ <- c(listGAITTWindowForPTQ, GAIList[i+1])
    }
    for( i in seq(0, length(listGAITTWindowForPTQ)-1, 1)){
        gaiMean_ <- gaiMean_ + listGAITTWindowForPTQ[i+1]
        countGaiMean <- countGaiMean + 1
    }
    gaiMean_ <- gaiMean_ / countGaiMean
    gai_ <- max(pastMaxAI_t1, gaiMean_)
    pastMaxAI <- gai_
    gAImean <- gai_
    return (list ("gAImean" = gAImean,"pastMaxAI" = pastMaxAI,"listTTShootWindowForPTQ1" = listTTShootWindowForPTQ1,"listGAITTWindowForPTQ" = listGAITTWindowForPTQ))
}
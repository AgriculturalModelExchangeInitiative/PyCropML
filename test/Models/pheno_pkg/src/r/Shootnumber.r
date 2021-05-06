model_shootnumber <- function (canopyShootNumber_t1 = 288.0,
         leafNumber = 3.34,
         sowingDensity = 288.0,
         targetFertileShoot = 600.0,
         tilleringProfile_t1 = c(288.0),
         leafTillerNumberArray_t1 = c(1, 1, 1),
         numberTillerCohort_t1 = 1){
    #'- Name: ShootNumber -Version: 1.0, -Time step: 1
    #'- Description:
    #'            * Title: CalculateShootNumber Model
    #'            * Author: Pierre MARTRE
    #'            * Reference: Modeling development phase in the 
    #'                Wheat Simulation Model SiriusQuality.
    #'                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    #'            * Institution: INRA/LEPSE Montpellier
    #'            * Abstract: calculate the shoot number and update the related variables if needed
    #'- inputs:
    #'            * name: canopyShootNumber_t1
    #'                          ** description : shoot number for the whole canopy
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** default : 288.0
    #'                          ** unit : shoot m-2
    #'                          ** inputtype : variable
    #'            * name: leafNumber
    #'                          ** description : Leaf number 
    #'                          ** variablecategory : state
    #'                          ** inputtype : variable
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** default : 3.34
    #'                          ** unit : leaf
    #'            * name: sowingDensity
    #'                          ** description : number of plant /m²
    #'                          ** parametercategory : species
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 500
    #'                          ** default : 288.0
    #'                          ** unit : plant m-2
    #'                          ** inputtype : parameter
    #'            * name: targetFertileShoot
    #'                          ** description : max value of shoot number for the canopy
    #'                          ** parametercategory : species
    #'                          ** datatype : DOUBLE
    #'                          ** min : 280
    #'                          ** max : 1000
    #'                          ** default : 600.0
    #'                          ** unit : shoot
    #'                          ** inputtype : variable
    #'            * name: tilleringProfile_t1
    #'                          ** description :  store the amount of new tiller created at each time a new tiller appears
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLELIST
    #'                          ** default : [288.0]
    #'                          ** unit : 
    #'                          ** inputtype : variable
    #'            * name: leafTillerNumberArray_t1
    #'                          ** description : store the number of tiller for each leaf layer
    #'                          ** variablecategory : state
    #'                          ** datatype : INTLIST
    #'                          ** unit : leaf
    #'                          ** default : [1, 1, 1]
    #'                          ** inputtype : variable
    #'            * name: numberTillerCohort_t1
    #'                          ** description :  Number of tiller which appears
    #'                          ** variablecategory : state
    #'                          ** datatype : INT
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** default : 1
    #'                          ** unit : 
    #'                          ** inputtype : variable
    #'- outputs:
    #'            * name: averageShootNumberPerPlant
    #'                          ** description : average shoot number per plant in the canopy
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** unit : shoot m-2
    #'            * name: canopyShootNumber
    #'                          ** description : shoot number for the whole canopy
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** unit : shoot m-2
    #'            * name: leafTillerNumberArray
    #'                          ** description : store the number of tiller for each leaf layer
    #'                          ** variablecategory : state
    #'                          ** datatype : INTLIST
    #'                          ** unit : leaf
    #'            * name: tilleringProfile
    #'                          ** description :  store the amount of new tiller created at each time a new tiller appears
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLELIST
    #'                          ** unit : dimensionless
    #'            * name: numberTillerCohort
    #'                          ** description : Number of tiller which appears
    #'                          ** variablecategory : state
    #'                          ** datatype : INT
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** unit : dimensionless
    leafTillerNumberArray <- vector()
    tilleringProfile <- vector()
    lNumberArray_rate <- vector()
    emergedLeaves <- max(1, ceiling(leafNumber - 1.0))
    shoots <- fibonacci(emergedLeaves)
    canopyShootNumber <- min(shoots * sowingDensity, targetFertileShoot)
    averageShootNumberPerPlant <- canopyShootNumber / sowingDensity
    if (canopyShootNumber != canopyShootNumber_t1)
    {
        tilleringProfile <- 
    }
    numberTillerCohort <- length(tilleringProfile)
    for( i in seq(length(leafTillerNumberArray_t1), ceiling(leafNumber)-1, 1)){
        lNumberArray_rate <- c(lNumberArray_rate, numberTillerCohort)
    }
    leafTillerNumberArray <- 
    return (list ("averageShootNumberPerPlant" = averageShootNumberPerPlant,"canopyShootNumber" = canopyShootNumber,"leafTillerNumberArray" = leafTillerNumberArray,"tilleringProfile" = tilleringProfile,"numberTillerCohort" = numberTillerCohort))
}

fibonacci <- function (n){
    if (n <= 1)
    {
        return( n)
    }
    else
    {
        return( fibonacci(n - 1) + fibonacci(n - 2))
    }
}

init_shootnumber <- function (sowingDensity = 288.0,
         targetFertileShoot = 600.0){
    tilleringProfile_t1 <- vector()
    leafTillerNumberArray_t1 <- vector()
    leafTillerNumberArray <- vector()
    tilleringProfile <- vector()
    canopyShootNumber <- sowingDensity
    averageShootNumberPerPlant <- 1.0
    tilleringProfile <- c(tilleringProfile, sowingDensity)
    numberTillerCohort <- 1
    leafTillerNumberArray <- vector()
    return (list ("averageShootNumberPerPlant" = averageShootNumberPerPlant,"canopyShootNumber" = canopyShootNumber,"leafTillerNumberArray" = leafTillerNumberArray,"tilleringProfile" = tilleringProfile,"numberTillerCohort" = numberTillerCohort))
}
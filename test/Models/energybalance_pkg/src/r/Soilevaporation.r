model_soilevaporation <- function (diffusionLimitedEvaporation = 6605.505,
         energyLimitedEvaporation = 448.24){
    #'- Name: SoilEvaporation -Version: 1.0, -Time step: 1
    #'- Description:
    #'            * Title: SoilEvaporation Model
    #'            * Author: Pierre Martre
    #'            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    #'            Evapotranspiration and canopy and soil temperature calculations
    #'            * Institution: INRA Montpellier
    #'            * Abstract: Starting from a soil at field capacity, soil evaporation  is assumed to
    #'                be energy limited during the first phase of evaporation and diffusion limited thereafter.
    #'                Hence, the soil evaporation model considers these two processes taking the minimum between
    #'                the energy limited evaporation (PtSoil) and the diffused limited
    #'                evaporation 
    #'- inputs:
    #'            * name: diffusionLimitedEvaporation
    #'                          ** description : diffusion Limited Evaporation
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** default : 6605.505
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** unit : g m-2 d-1
    #'                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    #'                          ** inputtype : variable
    #'            * name: energyLimitedEvaporation
    #'                          ** description : energy Limited Evaporation
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** default : 448.240
    #'                          ** min : 0
    #'                          ** max : 1000
    #'                          ** unit : g m-2 d-1
    #'                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    #'                          ** inputtype : variable
    #'- outputs:
    #'            * name: soilEvaporation
    #'                          ** description : soil Evaporation
    #'                          ** variablecategory : auxiliary
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 5000
    #'                          ** unit : g m-2 d-1
    #'                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    soilEvaporation <- min(diffusionLimitedEvaporation, energyLimitedEvaporation)
    return (list('soilEvaporation' = soilEvaporation))
}
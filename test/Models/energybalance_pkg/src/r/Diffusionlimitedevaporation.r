model_diffusionlimitedevaporation <- function (deficitOnTopLayers = 5341.0,
         soilDiffusionConstant = 4.2){
    #'- Name: DiffusionLimitedEvaporation -Version: 1.0, -Time step: 1
    #'- Description:
    #'            * Title: DiffusionLimitedEvaporation Model
    #'            * Author: Pierre Martre
    #'            * Reference:  From the wheat simulation model SiriusQuality
    #'                    Published in 2009
    #'                    doi:http://dx.doi.org/10.1016/j.eja.2006.04.007          
    #'        
    #'            * Institution: INRA Montpellier
    #'            * Abstract: the evaporation from the diffusion limited soil when the surface has 
    #'            dried sufficiently to provide a significant barrier to water vapor diffusion 
    #'        
    #'- inputs:
    #'            * name: deficitOnTopLayers
    #'                          ** description : deficit On TopLayers
    #'                          ** variablecategory : auxiliary
    #'                          ** datatype : DOUBLE
    #'                          ** default : 5341
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** unit : g m-2 d-1
    #'                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    #'                          ** inputtype : variable
    #'            * name: soilDiffusionConstant
    #'                          ** description : soil Diffusion Constant
    #'                          ** parametercategory : soil
    #'                          ** datatype : DOUBLE
    #'                          ** default : 4.2
    #'                          ** min : 0
    #'                          ** max : 10
    #'                          ** unit : 
    #'                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    #'                          ** inputtype : parameter
    #'- outputs:
    #'            * name: diffusionLimitedEvaporation
    #'                          ** description : the evaporation from the diffusion limited soil 
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 5000
    #'                          ** unit : g m-2 d-1
    #'                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    if (deficitOnTopLayers / 1000.0 <= 0.0)
    {
        diffusionLimitedEvaporation <- 8.3 * 1000.0
    }
    else
    {
        if (deficitOnTopLayers / 1000.0 < 25.0)
        {
            diffusionLimitedEvaporation <- 2.0 * soilDiffusionConstant * soilDiffusionConstant / (deficitOnTopLayers / 1000.0) * 1000.0
        }
        else
        {
            diffusionLimitedEvaporation <- 0.0
        }
    }
    return (list('diffusionLimitedEvaporation' = diffusionLimitedEvaporation))
}
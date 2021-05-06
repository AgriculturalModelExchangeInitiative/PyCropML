model_phylsowingdatecorrection <- function (sowingDay = 1,
         latitude = 0.0,
         sDsa_sh = 1.0,
         rp = 0.0,
         sDws = 1,
         sDsa_nh = 1.0,
         p = 120.0){
    #'- Name: PhylSowingDateCorrection -Version: 1.0, -Time step: 1
    #'- Description:
    #'            * Title: PhylSowingDateCorrection Model
    #'            * Author: Loic Manceau
    #'            * Reference: Modeling development phase in the 
    #'                Wheat Simulation Model SiriusQuality.
    #'                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    #'            * Institution: INRA Montpellier
    #'            * Abstract: Correction of the Phyllochron Varietal parameter according to sowing date 
    #'- inputs:
    #'            * name: sowingDay
    #'                          ** description : Day of Year at sowing
    #'                          ** parametercategory : species
    #'                          ** datatype : INT
    #'                          ** min : 1
    #'                          ** max : 365
    #'                          ** default : 1
    #'                          ** unit : d
    #'                          ** uri : some url
    #'                          ** inputtype : parameter
    #'            * name: latitude
    #'                          ** description : Latitude
    #'                          ** parametercategory : soil
    #'                          ** datatype : DOUBLE
    #'                          ** min : -90
    #'                          ** max : 90
    #'                          ** default : 0.0
    #'                          ** unit : °
    #'                          ** uri : some url
    #'                          ** inputtype : parameter
    #'            * name: sDsa_sh
    #'                          ** description : Sowing date at which Phyllochrone is maximum in southern hemispher
    #'                          ** parametercategory : species
    #'                          ** inputtype : parameter
    #'                          ** datatype : DOUBLE
    #'                          ** min : 1
    #'                          ** max : 365
    #'                          ** default : 1.0
    #'                          ** unit : d
    #'                          ** uri : some url
    #'            * name: rp
    #'                          ** description : Rate of change of Phyllochrone with sowing date
    #'                          ** parametercategory : species
    #'                          ** inputtype : parameter
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 365
    #'                          ** default : 0
    #'                          ** unit : d-1
    #'                          ** uri : some url
    #'            * name: sDws
    #'                          ** description : Sowing date at which Phyllochrone is minimum
    #'                          ** parametercategory : species
    #'                          ** datatype : INT
    #'                          ** default : 1
    #'                          ** min : 1
    #'                          ** max : 365
    #'                          ** unit : d
    #'                          ** uri : some url
    #'                          ** inputtype : parameter
    #'            * name: sDsa_nh
    #'                          ** description : Sowing date at which Phyllochrone is maximum in northern hemispher
    #'                          ** parametercategory : species
    #'                          ** datatype : DOUBLE
    #'                          ** default : 1.0
    #'                          ** min : 1
    #'                          ** max : 365
    #'                          ** unit : d
    #'                          ** uri : some url
    #'                          ** inputtype : parameter
    #'            * name: p
    #'                          ** description : Phyllochron (Varietal parameter)
    #'                          ** parametercategory : species
    #'                          ** datatype : DOUBLE
    #'                          ** default : 120
    #'                          ** min : 0
    #'                          ** max : 1000
    #'                          ** unit : °C d leaf-1
    #'                          ** uri : some url
    #'                          ** inputtype : parameter
    #'- outputs:
    #'            * name: fixPhyll
    #'                          ** description :  Phyllochron Varietal parameter 
    #'                          ** variablecategory : auxiliary
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 1000
    #'                          ** unit : °C d leaf-1
    if (latitude < 0.0)
    {
        if (sowingDay > as.integer(sDsa_sh))
        {
            fixPhyll <- p * (1 - (rp * min((sowingDay - sDsa_sh), sDws)))
        }
        else
        {
            fixPhyll <- p
        }
    }
    else
    {
        if (sowingDay < as.integer(sDsa_nh))
        {
            fixPhyll <- p * (1 - (rp * min(sowingDay, sDws)))
        }
        else
        {
            fixPhyll <- p
        }
    }
    return (list('fixPhyll' = fixPhyll))
}
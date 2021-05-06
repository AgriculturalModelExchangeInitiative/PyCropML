model_leafnumber <- function (deltaTT = 23.5895677277199,
         phyllochron_t1 = 0.0,
         hasFlagLeafLiguleAppeared = 0,
         leafNumber_t1 = 0.0,
         phase = 1.0){
    #'- Name: LeafNumber -Version: 1.0, -Time step: 1
    #'- Description:
    #'            * Title: CalculateLeafNumber Model
    #'            * Author: Pierre MARTRE
    #'            * Reference: Modeling development phase in the 
    #'                Wheat Simulation Model SiriusQuality.
    #'                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    #'            * Institution: INRA Montpellier
    #'            * Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day
    #'- inputs:
    #'            * name: deltaTT
    #'                          ** description : daily delta TT 
    #'                          ** variablecategory : auxiliary
    #'                          ** datatype : DOUBLE
    #'                          ** min : -20
    #'                          ** max : 100
    #'                          ** default : 23.5895677277199
    #'                          ** unit : °C d
    #'                          ** inputtype : variable
    #'            * name: phyllochron_t1
    #'                          ** description : phyllochron
    #'                          ** variablecategory : state
    #'                          ** inputtype : variable
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 1000
    #'                          ** default : 0
    #'                          ** unit : °C d leaf-1
    #'            * name: hasFlagLeafLiguleAppeared
    #'                          ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    #'                          ** variablecategory : state
    #'                          ** datatype : INT
    #'                          ** min : 0
    #'                          ** max : 1
    #'                          ** default : 0
    #'                          ** unit : 
    #'                          ** inputtype : variable
    #'            * name: leafNumber_t1
    #'                          ** description :  Actual number of phytomers
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 25
    #'                          ** default : 0
    #'                          ** unit : leaf
    #'                          ** inputtype : variable
    #'            * name: phase
    #'                          ** description :  the name of the phase
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 7
    #'                          ** default : 1
    #'                          ** unit :  
    #'                          ** uri : some url
    #'                          ** inputtype : variable
    #'- outputs:
    #'            * name: leafNumber
    #'                          ** description : Actual number of phytomers
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** unit : leaf
    #'                          ** uri : some url
    leafNumber <- leafNumber_t1
    if (phase >= 1.0 && phase < 4.0)
    {
        if (hasFlagLeafLiguleAppeared == 0)
        {
            if (phyllochron_t1 == 0.0)
            {
                phyllochron_ <- 0.0000001
            }
            else
            {
                phyllochron_ <- phyllochron_t1
            }
            leafNumber <- leafNumber_t1 + min(deltaTT / phyllochron_, 0.999)
        }
    }
    return (list('leafNumber' = leafNumber))
}
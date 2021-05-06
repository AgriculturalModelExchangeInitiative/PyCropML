MODULE Priestlytaylormod
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_priestlytaylor(netRadiationEquivalentEvaporation, &
        hslope, &
        psychrometricConstant, &
        Alpha, &
        evapoTranspirationPriestlyTaylor)
        IMPLICIT NONE
        REAL, INTENT(IN) :: netRadiationEquivalentEvaporation
        REAL, INTENT(IN) :: hslope
        REAL, INTENT(IN) :: psychrometricConstant
        REAL, INTENT(IN) :: Alpha
        REAL, INTENT(OUT) :: evapoTranspirationPriestlyTaylor
        !- Description:
    !            * Title: evapoTranspirationPriestlyTaylor  Model
    !            * Author: Pierre Martre
    !            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    !            Evapotranspiration and canopy and soil temperature calculations
    !            * Institution: INRA Montpellier
    !            * Abstract: Calculate Energy Balance 
        !- inputs:
    !            * name: netRadiationEquivalentEvaporation
    !                          ** description : net Radiation in Equivalent Evaporation
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** default : 638.142
    !                          ** min : 0
    !                          ** max : 5000
    !                          ** unit : g m-2 d-1
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          ** inputtype : variable
    !            * name: hslope
    !                          ** description : the slope of saturated vapor pressure temperature curve at a given temperature 
    !                          ** variablecategory : auxiliary
    !                          ** datatype : DOUBLE
    !                          ** default : 0.584
    !                          ** min : 0
    !                          ** max : 1000
    !                          ** unit : hPa °C-1
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          ** inputtype : variable
    !            * name: psychrometricConstant
    !                          ** description : psychrometric constant
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** default : 0.66
    !                          ** min : 0
    !                          ** max : 1
    !                          ** unit : 
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          ** inputtype : parameter
    !            * name: Alpha
    !                          ** description : Priestley-Taylor evapotranspiration proportionality constant
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** default : 1.5
    !                          ** min : 0
    !                          ** max : 100
    !                          ** unit : 
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          ** inputtype : parameter
        !- outputs:
    !            * name: evapoTranspirationPriestlyTaylor
    !                          ** description : evapoTranspiration of Priestly Taylor 
    !                          ** variablecategory : rate
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : g m-2 d-1
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        evapoTranspirationPriestlyTaylor = MAX(Alpha * hslope *  &
                netRadiationEquivalentEvaporation / (hslope + psychrometricConstant),  &
                0.0)
    END SUBROUTINE model_priestlytaylor

END MODULE

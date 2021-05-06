MODULE Penmanmod
    IMPLICIT NONE
CONTAINS
    SUBROUTINE model_penman(evapoTranspirationPriestlyTaylor, &
        hslope, &
        VPDair, &
        psychrometricConstant, &
        Alpha, &
        lambdaV, &
        rhoDensityAir, &
        specificHeatCapacityAir, &
        conductance, &
        evapoTranspirationPenman)
        REAL, INTENT(IN) :: evapoTranspirationPriestlyTaylor
        REAL, INTENT(IN) :: hslope
        REAL, INTENT(IN) :: VPDair
        REAL, INTENT(IN) :: psychrometricConstant
        REAL, INTENT(IN) :: Alpha
        REAL, INTENT(IN) :: lambdaV
        REAL, INTENT(IN) :: rhoDensityAir
        REAL, INTENT(IN) :: specificHeatCapacityAir
        REAL, INTENT(IN) :: conductance
        REAL, INTENT(OUT) :: evapoTranspirationPenman
        !- Description:
    !            - Model Name: Penman Model
    !            - Author: Pierre Martre
    !            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    !            Evapotranspiration and canopy and soil temperature calculations
    !            - Institution: INRA/LEPSE Montpellier
    !            - Abstract: This method is used when wind and vapor pressure daily data are available
    !        
        !- inputs:
    !            - name: evapoTranspirationPriestlyTaylor
    !                          - description : evapoTranspiration of Priestly Taylor 
    !                          - variablecategory : rate
    !                          - datatype : DOUBLE
    !                          - default : 449.367
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: hslope
    !                          - description : the slope of saturated vapor pressure temperature curve at a given temperature 
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - default : 0.584
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : hPa °C-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: VPDair
    !                          - description :  vapour pressure density
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - default : 2.19
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : hPa
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: psychrometricConstant
    !                          - description : psychrometric constant
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 0.66
    !                          - min : 0
    !                          - max : 1
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: Alpha
    !                          - description : Priestley-Taylor evapotranspiration proportionality constant
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 1.5
    !                          - min : 0
    !                          - max : 100
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: lambdaV
    !                          - description : latent heat of vaporization of water
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 2.454
    !                          - min : 0
    !                          - max : 10
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: rhoDensityAir
    !                          - description : Density of air
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 1.225
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: specificHeatCapacityAir
    !                          - description : Specific heat capacity of dry air
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 0.00101
    !                          - min : 0
    !                          - max : 1
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: conductance
    !                          - description : conductance
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - default : 598.685
    !                          - unit : m d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
        !- outputs:
    !            - name: evapoTranspirationPenman
    !                          - description :  evapoTranspiration of Penman Monteith
    !                          - variablecategory : rate
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        evapoTranspirationPenman = evapoTranspirationPriestlyTaylor / Alpha +  &
                (1000.0 * (rhoDensityAir * specificHeatCapacityAir * VPDair *  &
                conductance / (lambdaV * (hslope + psychrometricConstant))))
    END SUBROUTINE model_penman

END MODULE

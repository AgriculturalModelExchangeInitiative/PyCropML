MODULE Soilheatfluxmod
    IMPLICIT NONE
CONTAINS
    SUBROUTINE model_soilheatflux(netRadiationEquivalentEvaporation, &
        tau, &
        soilEvaporation, &
        soilHeatFlux)
        REAL, INTENT(IN) :: netRadiationEquivalentEvaporation
        REAL, INTENT(IN) :: tau
        REAL, INTENT(IN) :: soilEvaporation
        REAL, INTENT(OUT) :: soilHeatFlux
        !- Description:
    !            - Model Name: SoilHeatFlux Model
    !            - Author: Pierre Martre
    !            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    !            Evapotranspiration and canopy and soil temperature calculations
    !            - Institution: INRA/LEPSE Montpellier
    !            - Abstract: The available energy in the soil 
        !- inputs:
    !            - name: netRadiationEquivalentEvaporation
    !                          - variablecategory : state
    !                          - description : net Radiation Equivalent Evaporation
    !                          - datatype : DOUBLE
    !                          - default : 638.142
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: tau
    !                          - description : plant cover factor
    !                          - parametercategory : species
    !                          - datatype : DOUBLE
    !                          - default : 0.9983
    !                          - min : 0
    !                          - max : 100
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: soilEvaporation
    !                          - description : soil Evaporation
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - default : 448.240
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
        !- outputs:
    !            - name: soilHeatFlux
    !                          - description : soil Heat Flux 
    !                          - variablecategory : rate
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        soilHeatFlux = tau * netRadiationEquivalentEvaporation -  &
                soilEvaporation
    END SUBROUTINE model_soilheatflux

END MODULE

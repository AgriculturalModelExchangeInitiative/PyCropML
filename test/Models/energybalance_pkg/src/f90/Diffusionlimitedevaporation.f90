MODULE Diffusionlimitedevaporationmod
    IMPLICIT NONE
CONTAINS
    SUBROUTINE model_diffusionlimitedevaporation(deficitOnTopLayers, &
        soilDiffusionConstant, &
        diffusionLimitedEvaporation)
        REAL, INTENT(IN) :: deficitOnTopLayers
        REAL, INTENT(IN) :: soilDiffusionConstant
        REAL, INTENT(OUT) :: diffusionLimitedEvaporation
        !- Description:
    !            - Model Name: DiffusionLimitedEvaporation Model
    !            - Author: Pierre Martre
    !            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    !            Evapotranspiration and canopy and soil temperature calculations
    !            - Institution: INRA Montpellier
    !            - Abstract: the evaporation from the diffusion limited soil 
        !- inputs:
    !            - name: deficitOnTopLayers
    !                          - description : deficit On TopLayers
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - default : 5341
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: soilDiffusionConstant
    !                          - description : soil Diffusion Constant
    !                          - parametercategory : soil
    !                          - datatype : DOUBLE
    !                          - default : 4.2
    !                          - min : 0
    !                          - max : 10
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
        !- outputs:
    !            - name: diffusionLimitedEvaporation
    !                          - description : the evaporation from the diffusion limited soil 
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        IF(deficitOnTopLayers / 1000.0 .LE. 0.0) THEN
            diffusionLimitedEvaporation = 8.3 * 1000.0
        ELSE
            IF(deficitOnTopLayers / 1000.0 .LT. 25.0) THEN
                diffusionLimitedEvaporation = 2.0 * soilDiffusionConstant *  &
                        soilDiffusionConstant / (deficitOnTopLayers / 1000.0) * 1000.0
            ELSE
                diffusionLimitedEvaporation = 0.0
            END IF
        END IF
    END SUBROUTINE model_diffusionlimitedevaporation

END MODULE

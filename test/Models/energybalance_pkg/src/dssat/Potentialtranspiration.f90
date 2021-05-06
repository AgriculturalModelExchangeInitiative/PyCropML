MODULE Potentialtranspirationmod
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_potentialtranspiration(evapoTranspiration, &
        tau, &
        potentialTranspiration)
        IMPLICIT NONE
        REAL, INTENT(IN) :: evapoTranspiration
        REAL, INTENT(IN) :: tau
        REAL, INTENT(OUT) :: potentialTranspiration
        !- Description:
    !            * Title: PotentialTranspiration Model
    !            * Author: Pierre Martre
    !            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    !            Evapotranspiration and canopy and soil temperature calculations
    !            * Institution: INRA/LEPSE Montpellier
    !            * Abstract: SiriusQuality2 uses availability of water from the soil reservoir as a method to restrict
    !                    transpiration as soil moisture is depleted 
        !- inputs:
    !            * name: evapoTranspiration
    !                          ** description : evapoTranspiration
    !                          ** variablecategory : rate
    !                          ** datatype : DOUBLE
    !                          ** default : 830.958
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : mm
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          ** inputtype : variable
    !            * name: tau
    !                          ** description : plant cover factor
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** default : 0.9983
    !                          ** min : 0
    !                          ** max : 1
    !                          ** unit : 
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          ** inputtype : parameter
        !- outputs:
    !            * name: potentialTranspiration
    !                          ** description : potential Transpiration 
    !                          ** variablecategory : rate
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : g m-2 d-1
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        potentialTranspiration = evapoTranspiration * (1.0 - tau)
    END SUBROUTINE model_potentialtranspiration

END MODULE

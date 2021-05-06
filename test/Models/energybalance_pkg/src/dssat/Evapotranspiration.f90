MODULE Evapotranspirationmod
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_evapotranspiration(isWindVpDefined, &
        evapoTranspirationPriestlyTaylor, &
        evapoTranspirationPenman, &
        evapoTranspiration)
        IMPLICIT NONE
        INTEGER, INTENT(IN) :: isWindVpDefined
        REAL, INTENT(IN) :: evapoTranspirationPriestlyTaylor
        REAL, INTENT(IN) :: evapoTranspirationPenman
        REAL, INTENT(OUT) :: evapoTranspiration
        !- Description:
    !            * Title: Evapotranspiration Model
    !            * Author: Pierre Martre
    !            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    !            Evapotranspiration and canopy and soil temperature calculations
    !            * Institution: INRA Montpellier
    !            * Abstract: According to the availability of wind and/or vapor pressure daily data, the
    !            SiriusQuality2 model calculates the evapotranspiration rate using the Penman (if wind
    !            and vapor pressure data are available) (Penman 1948) or the Priestly-Taylor
    !            (Priestley and Taylor 1972) method 
        !- inputs:
    !            * name: isWindVpDefined
    !                          ** description : if wind and vapour pressure are defined
    !                          ** parametercategory : constant
    !                          ** datatype : INT
    !                          ** default : 1
    !                          ** min : 0
    !                          ** max : 1
    !                          ** unit : 
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          ** inputtype : parameter
    !            * name: evapoTranspirationPriestlyTaylor
    !                          ** description : evapoTranspiration of Priestly Taylor 
    !                          ** variablecategory : rate
    !                          ** default : 449.367
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : mm
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          ** inputtype : variable
    !            * name: evapoTranspirationPenman
    !                          ** description : evapoTranspiration of Penman 
    !                          ** datatype : DOUBLE
    !                          ** variablecategory : rate
    !                          ** default : 830.958
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : mm
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          ** inputtype : variable
        !- outputs:
    !            * name: evapoTranspiration
    !                          ** description : evapoTranspiration
    !                          ** variablecategory : rate
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : mm
    !                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        IF(isWindVpDefined .EQ. 1) THEN
            evapoTranspiration = evapoTranspirationPenman
        ELSE
            evapoTranspiration = evapoTranspirationPriestlyTaylor
        END IF
    END SUBROUTINE model_evapotranspiration

END MODULE

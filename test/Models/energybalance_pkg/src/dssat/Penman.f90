    SUBROUTINE model_penman(evapoTranspirationPriestlyTaylor, ...)
        REAL, INTENT(IN) :: evapoTranspirationPriestlyTaylor
        ... 
        evapoTranspirationPenman = evapoTranspirationPriestlyTaylor / Alpha +  &
                (1000.0 * (rhoDensityAir * specificHeatCapacityAir * VPDair *  &
                conductance / (lambdaV * (hslope + psychrometricConstant))))
    END SUBROUTINE model_penman


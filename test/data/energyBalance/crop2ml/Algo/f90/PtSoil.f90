REAL AlphaE
IF (tau .LE. tauAlpha) THEN
	AlphaE = 1
ELSE
	AlphaE = Alpha - ((Alpha - 1) * (1 - tau) / (1 - tauAlpha))
ENDIF
energyLimitedEvaporation = (evapoTranspirationPriestlyTaylor / Alpha) * AlphaE * tau     
     
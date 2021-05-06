IF(isWindVpDefined .EQ. 1) THEN
	evapoTranspiration = evapoTranspirationPenman
ELSE
	evapoTranspiration = evapoTranspirationPriestlyTaylor
ENDIF 
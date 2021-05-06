IF (deficitOnTopLayers / 1000 .LE. 0.0) THEN
	diffusionLimitedEvaporation = 8.3 * 1000
ELSE 
	IF (deficitOnTopLayers / 1000 .LE. 25.0) THEN
		diffusionLimitedEvaporation = (2 * soilDiffusionConstant * soilDiffusionConstant / (deficitOnTopLayers / 1000)) * 1000
	ELSE
		diffusionLimitedEvaporation = 0
ENDIF
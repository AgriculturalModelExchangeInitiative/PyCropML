
if (deficitOnTopLayers / 1000.0 <= 0.0): diffusionLimitedEvaporation = 8.3 * 1000.0
else :
    if (deficitOnTopLayers / 1000.0 < 25.0):
        diffusionLimitedEvaporation = (2.0 * soilDiffusionConstant * soilDiffusionConstant / (deficitOnTopLayers / 1000.0)) * 1000.0
    else:
        diffusionLimitedEvaporation = 0.0


Nsr = (1 - albedoCoefficient) * solarRadiation
clearSkySolarRadiation = (0.75 + 2 * 10**(-5) * elevation) * extraSolarRadiation
averageT = ((maxTair + 273.16)** 4 + (minTair + 273.16)** 4) / 2
surfaceEmissivity = (0.34 - 0.14 * sqrt(vaporPressure / 10))
cloudCoverFactor = (1.35 * (solarRadiation / clearSkySolarRadiation) - 0.35)
Nolr = stefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor
netRadiation= Nsr - Nolr
netOutGoingLongWaveRadiation = Nolr


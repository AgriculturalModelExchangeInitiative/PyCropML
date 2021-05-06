cdef float Nsr, clearSkySolarRadiation, averageT, surfaceEmissivity, cloudCoverFactor, Nolr
Nsr = (1.0 - albedoCoefficient) * solarRadiation
clearSkySolarRadiation = (0.75 + 2 * pow(10.0, -5) * elevation) * extraSolarRadiation
averageT = (pow(maxTair + 273.16, 4) + pow(minTair + 273.16, 4)) / 2.0
surfaceEmissivity = (0.34 - 0.14 * sqrt(vaporPressure / 10.0))
cloudCoverFactor = (1.35 * (solarRadiation / clearSkySolarRadiation) - 0.35)
Nolr = stefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor
netRadiation= Nsr - Nolr
netOutGoingLongWaveRadiation = Nolr


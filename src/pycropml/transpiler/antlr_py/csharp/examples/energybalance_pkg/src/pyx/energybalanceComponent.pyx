from datetime import datetime
from math import *
from Netradiation import model_netradiation
from Netradiationequivalentevaporation import model_netradiationequivalentevaporation
from Priestlytaylor import model_priestlytaylor
from Conductance import model_conductance
from Diffusionlimitedevaporation import model_diffusionlimitedevaporation
from Penman import model_penman
from Ptsoil import model_ptsoil
from Soilevaporation import model_soilevaporation
from Evapotranspiration import model_evapotranspiration
from Soilheatflux import model_soilheatflux
from Potentialtranspiration import model_potentialtranspiration
from Cropheatflux import model_cropheatflux
from Canopytemperature import model_canopytemperature
def model_energybalance(float minTair=0.7,
      float maxTair=7.2,
      float albedoCoefficient=0.23,
      float stefanBoltzman=4.903e-09,
      float elevation=0.0,
      float solarRadiation=3.0,
      float vaporPressure=6.1,
      float extraSolarRadiation=11.7,
      float lambdaV=2.454,
      float hslope=0.584,
      float psychrometricConstant=0.66,
      float Alpha=1.5,
      float vonKarman=0.42,
      float heightWeatherMeasurements=2.0,
      float zm=0.13,
      float d=0.67,
      float zh=0.013,
      float plantHeight=0.0,
      float wind=124000.0,
      float deficitOnTopLayers=5341.0,
      float soilDiffusionConstant=4.2,
      float VPDair=2.19,
      float rhoDensityAir=1.225,
      float specificHeatCapacityAir=0.00101,
      float tau=0.9983,
      float tauAlpha=0.3,
      int isWindVpDefined=1):
    cdef float netRadiation
    cdef float netOutGoingLongWaveRadiation
    cdef float netRadiationEquivalentEvaporation
    cdef float evapoTranspirationPriestlyTaylor
    cdef float conductance
    cdef float diffusionLimitedEvaporation
    cdef float evapoTranspirationPenman
    cdef float energyLimitedEvaporation
    cdef float soilEvaporation
    cdef float evapoTranspiration
    cdef float soilHeatFlux
    cdef float potentialTranspiration
    cdef float cropHeatFlux
    cdef float minCanopyTemperature
    cdef float maxCanopyTemperature
    diffusionLimitedEvaporation = model_diffusionlimitedevaporation( deficitOnTopLayers,soilDiffusionConstant)
    conductance = model_conductance( vonKarman,heightWeatherMeasurements,zm,zh,d,plantHeight,wind)
    netRadiation, netOutGoingLongWaveRadiation = model_netradiation( minTair,maxTair,albedoCoefficient,stefanBoltzman,elevation,solarRadiation,vaporPressure,extraSolarRadiation)
    netRadiationEquivalentEvaporation = model_netradiationequivalentevaporation( lambdaV,netRadiation)
    evapoTranspirationPriestlyTaylor = model_priestlytaylor( netRadiationEquivalentEvaporation,hslope,psychrometricConstant,Alpha)
    evapoTranspirationPenman = model_penman( evapoTranspirationPriestlyTaylor,hslope,VPDair,psychrometricConstant,Alpha,lambdaV,rhoDensityAir,specificHeatCapacityAir,conductance)
    evapoTranspiration = model_evapotranspiration( isWindVpDefined,evapoTranspirationPriestlyTaylor,evapoTranspirationPenman)
    potentialTranspiration = model_potentialtranspiration( evapoTranspiration,tau)
    energyLimitedEvaporation = model_ptsoil( evapoTranspirationPriestlyTaylor,Alpha,tau,tauAlpha)
    soilEvaporation = model_soilevaporation( diffusionLimitedEvaporation,energyLimitedEvaporation)
    soilHeatFlux = model_soilheatflux( netRadiationEquivalentEvaporation,tau,soilEvaporation)
    cropHeatFlux = model_cropheatflux( netRadiationEquivalentEvaporation,soilHeatFlux,potentialTranspiration)
    minCanopyTemperature, maxCanopyTemperature = model_canopytemperature( minTair,maxTair,cropHeatFlux,conductance,lambdaV,rhoDensityAir,specificHeatCapacityAir)
    return netRadiation, netOutGoingLongWaveRadiation, netRadiationEquivalentEvaporation, evapoTranspirationPriestlyTaylor, diffusionLimitedEvaporation, energyLimitedEvaporation, conductance, evapoTranspirationPenman, soilEvaporation, evapoTranspiration, potentialTranspiration, soilHeatFlux, cropHeatFlux, minCanopyTemperature, maxCanopyTemperature
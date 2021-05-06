# coding: utf8
from pycropml.units import u
from copy import copy
from array import array

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

def model_energybalance(minTair = 0.7,
         maxTair = 7.2,
         albedoCoefficient = 0.23,
         stefanBoltzman = 4.903e-09,
         elevation = 0.0,
         solarRadiation = 3.0,
         vaporPressure = 6.1,
         extraSolarRadiation = 11.7,
         lambdaV = 2.454,
         hslope = 0.584,
         psychrometricConstant = 0.66,
         Alpha = 1.5,
         vonKarman = 0.42,
         heightWeatherMeasurements = 2.0,
         zm = 0.13,
         d = 0.67,
         zh = 0.013,
         plantHeight = 0.0,
         wind = 124000.0,
         deficitOnTopLayers = 5341.0,
         soilDiffusionConstant = 4.2,
         VPDair = 2.19,
         rhoDensityAir = 1.225,
         specificHeatCapacityAir = 0.00101,
         tau = 0.9983,
         tauAlpha = 0.3,
         isWindVpDefined = 1):
    """
     - Name: EnergyBalance -Version: 001, -Time step: 1
     - Description:
                 * Title: EnergyBalance
                 * Author: Pierre MARTRE
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2: Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA/LEPSE
                 * Abstract: see documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=547
     - inputs:
                 * name: minTair
                               ** description : minimum air temperature
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : -30
                               ** max : 45
                               ** default : 0.7
                               ** unit : °C
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: maxTair
                               ** description : maximum air Temperature
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : -30
                               ** max : 45
                               ** default : 7.2
                               ** unit : °C
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: albedoCoefficient
                               ** description : albedo Coefficient
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.23
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: stefanBoltzman
                               ** description : stefan Boltzman constant
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 4.903E-09
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: elevation
                               ** description : elevation
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0
                               ** min : -500
                               ** max : 10000
                               ** unit : m
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: solarRadiation
                               ** description : solar Radiation
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 3
                               ** min : 0
                               ** max : 1000
                               ** unit : MJ m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: vaporPressure
                               ** description : vapor Pressure
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 6.1
                               ** min : 0
                               ** max : 1000
                               ** unit : hPa
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: extraSolarRadiation
                               ** description : extra Solar Radiation
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 11.7
                               ** min : 0
                               ** max : 1000
                               ** unit : MJ m2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: lambdaV
                               ** description : latent heat of vaporization of water
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 2.454
                               ** min : 0
                               ** max : 10
                               ** unit : MJ kg-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: hslope
                               ** description : the slope of saturated vapor pressure temperature curve at a given temperature 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 0.584
                               ** min : 0
                               ** max : 1000
                               ** unit : hPa °C-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: psychrometricConstant
                               ** description : psychrometric constant
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.66
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: Alpha
                               ** description : Priestley-Taylor evapotranspiration proportionality constant
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 1.5
                               ** min : 0
                               ** max : 100
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: vonKarman
                               ** description : von Karman constant
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 1
                               ** default : 0.42
                               ** unit : dimensionless
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                               ** parametercategory : constant
                 * name: heightWeatherMeasurements
                               ** description : reference height of wind and humidity measurements
                               ** parametercategory : soil
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10
                               ** default : 2
                               ** unit : m
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: zm
                               ** description : roughness length governing momentum transfer, FAO
                               ** parametercategory : constant
                               ** inputtype : parameter
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 1
                               ** default : 0.13
                               ** unit : m
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: d
                               ** description : corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.67
                               ** min : 0
                               ** max : 1
                               ** unit : dimensionless
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547rl
                 * name: zh
                               ** description : roughness length governing transfer of heat and vapour, FAO
                               ** parametercategory : constant
                               ** inputtype : parameter
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 1
                               ** default : 0.013
                               ** unit : m
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: plantHeight
                               ** description : plant Height
                               ** datatype : DOUBLE
                               ** default : 0
                               ** min : 0
                               ** max : 1000
                               ** unit : mm
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                 * name: wind
                               ** description : wind
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 124000
                               ** min : 0
                               ** max : 1000000
                               ** unit : m/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: deficitOnTopLayers
                               ** description : deficit On TopLayers
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 5341
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: soilDiffusionConstant
                               ** description : soil Diffusion Constant
                               ** parametercategory : soil
                               ** datatype : DOUBLE
                               ** default : 4.2
                               ** min : 0
                               ** max : 10
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: VPDair
                               ** description :  vapour pressure density
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 2.19
                               ** min : 0
                               ** max : 1000
                               ** unit : hPa
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: rhoDensityAir
                               ** description : Density of air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 1.225
                               ** unit : kg*m**3
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: specificHeatCapacityAir
                               ** description : Specific heat capacity of dry air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.00101
                               ** min : 0
                               ** max : 1
                               ** unit : MJ/kg/degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: tau
                               ** description : plant cover factor
                               ** parametercategory : species
                               ** datatype : DOUBLE
                               ** default : 0.9983
                               ** min : 0
                               ** max : 100
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: tauAlpha
                               ** description : Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1
                               ** parametercategory : soil
                               ** datatype : DOUBLE
                               ** default : 0.3
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: isWindVpDefined
                               ** description : if wind and vapour pressure are defined
                               ** parametercategory : constant
                               ** datatype : INT
                               ** default : 1
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
     - outputs:
                 * name: netRadiation
                               ** description :  net radiation 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : MJ m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: netOutGoingLongWaveRadiation
                               ** description : net OutGoing Long Wave Radiation 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: netRadiationEquivalentEvaporation
                               ** variablecategory : auxiliary
                               ** description : net Radiation in Equivalent Evaporation 
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: evapoTranspirationPriestlyTaylor
                               ** description : evapoTranspiration of Priestly Taylor 
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: diffusionLimitedEvaporation
                               ** description : the evaporation from the diffusion limited soil 
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: energyLimitedEvaporation
                               ** description : energy Limited Evaporation 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: conductance
                               ** description : the boundary layer conductance
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : m/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: evapoTranspirationPenman
                               ** description :  evapoTranspiration of Penman Monteith
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g/m**2/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: soilEvaporation
                               ** description : soil Evaporation
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: evapoTranspiration
                               ** description : evapoTranspiration
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : mm
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: potentialTranspiration
                               ** description : potential Transpiration 
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: soilHeatFlux
                               ** description : soil Heat Flux 
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: cropHeatFlux
                               ** description :  crop Heat Flux
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: minCanopyTemperature
                               ** description : minimal Canopy Temperature  
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** min : -30
                               ** max : 45
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: maxCanopyTemperature
                               ** description : maximal Canopy Temperature 
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** min : -30
                               ** max : 45
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    diffusionLimitedEvaporation = model_diffusionlimitedevaporation(deficitOnTopLayers, soilDiffusionConstant)
    conductance = model_conductance(vonKarman, heightWeatherMeasurements, zm, zh, d, plantHeight, wind)
    (netRadiation, netOutGoingLongWaveRadiation) = model_netradiation(minTair, maxTair, albedoCoefficient, stefanBoltzman, elevation, solarRadiation, vaporPressure, extraSolarRadiation)
    netRadiationEquivalentEvaporation = model_netradiationequivalentevaporation(lambdaV, netRadiation)
    evapoTranspirationPriestlyTaylor = model_priestlytaylor(netRadiationEquivalentEvaporation, hslope, psychrometricConstant, Alpha)
    evapoTranspirationPenman = model_penman(evapoTranspirationPriestlyTaylor, hslope, VPDair, psychrometricConstant, Alpha, lambdaV, rhoDensityAir, specificHeatCapacityAir, conductance)
    evapoTranspiration = model_evapotranspiration(isWindVpDefined, evapoTranspirationPriestlyTaylor, evapoTranspirationPenman)
    potentialTranspiration = model_potentialtranspiration(evapoTranspiration, tau)
    energyLimitedEvaporation = model_ptsoil(evapoTranspirationPriestlyTaylor, Alpha, tau, tauAlpha)
    soilEvaporation = model_soilevaporation(diffusionLimitedEvaporation, energyLimitedEvaporation)
    soilHeatFlux = model_soilheatflux(netRadiationEquivalentEvaporation, tau, soilEvaporation)
    cropHeatFlux = model_cropheatflux(netRadiationEquivalentEvaporation, soilHeatFlux, potentialTranspiration)
    (minCanopyTemperature, maxCanopyTemperature) = model_canopytemperature(minTair, maxTair, cropHeatFlux, conductance, lambdaV, rhoDensityAir, specificHeatCapacityAir)
    return (netRadiation, netOutGoingLongWaveRadiation, netRadiationEquivalentEvaporation, evapoTranspirationPriestlyTaylor, diffusionLimitedEvaporation, energyLimitedEvaporation, conductance, evapoTranspirationPenman, soilEvaporation, evapoTranspiration, potentialTranspiration, soilHeatFlux, cropHeatFlux, minCanopyTemperature, maxCanopyTemperature)
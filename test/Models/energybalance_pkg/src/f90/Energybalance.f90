MODULE Energybalancemod
    USE Netradiationmod
    USE Netradiationequivalentevaporationmod
    USE Priestlytaylormod
    USE Conductancemod
    USE Diffusionlimitedevaporationmod
    USE Penmanmod
    USE Ptsoilmod
    USE Soilevaporationmod
    USE Evapotranspirationmod
    USE Soilheatfluxmod
    USE Potentialtranspirationmod
    USE Cropheatfluxmod
    USE Canopytemperaturemod
    IMPLICIT NONE
CONTAINS
    SUBROUTINE model_energybalance(minTair, &
        maxTair, &
        albedoCoefficient, &
        stefanBoltzman, &
        elevation, &
        solarRadiation, &
        vaporPressure, &
        extraSolarRadiation, &
        lambdaV, &
        hslope, &
        psychrometricConstant, &
        Alpha, &
        vonKarman, &
        heightWeatherMeasurements, &
        zm, &
        d, &
        zh, &
        plantHeight, &
        wind, &
        deficitOnTopLayers, &
        soilDiffusionConstant, &
        VPDair, &
        rhoDensityAir, &
        specificHeatCapacityAir, &
        tau, &
        tauAlpha, &
        isWindVpDefined, &
        netRadiation, &
        netOutGoingLongWaveRadiation, &
        netRadiationEquivalentEvaporation, &
        evapoTranspirationPriestlyTaylor, &
        diffusionLimitedEvaporation, &
        energyLimitedEvaporation, &
        conductance, &
        evapoTranspirationPenman, &
        soilEvaporation, &
        evapoTranspiration, &
        potentialTranspiration, &
        soilHeatFlux, &
        cropHeatFlux, &
        minCanopyTemperature, &
        maxCanopyTemperature)
        REAL, INTENT(IN) :: minTair
        REAL, INTENT(IN) :: maxTair
        REAL, INTENT(IN) :: albedoCoefficient
        REAL, INTENT(IN) :: stefanBoltzman
        REAL, INTENT(IN) :: elevation
        REAL, INTENT(IN) :: solarRadiation
        REAL, INTENT(IN) :: vaporPressure
        REAL, INTENT(IN) :: extraSolarRadiation
        REAL, INTENT(IN) :: lambdaV
        REAL, INTENT(IN) :: hslope
        REAL, INTENT(IN) :: psychrometricConstant
        REAL, INTENT(IN) :: Alpha
        REAL, INTENT(IN) :: vonKarman
        REAL, INTENT(IN) :: heightWeatherMeasurements
        REAL, INTENT(IN) :: zm
        REAL, INTENT(IN) :: d
        REAL, INTENT(IN) :: zh
        REAL, INTENT(IN) :: plantHeight
        REAL, INTENT(IN) :: wind
        REAL, INTENT(IN) :: deficitOnTopLayers
        REAL, INTENT(IN) :: soilDiffusionConstant
        REAL, INTENT(IN) :: VPDair
        REAL, INTENT(IN) :: rhoDensityAir
        REAL, INTENT(IN) :: specificHeatCapacityAir
        REAL, INTENT(IN) :: tau
        REAL, INTENT(IN) :: tauAlpha
        INTEGER, INTENT(IN) :: isWindVpDefined
        REAL, INTENT(OUT) :: netRadiation
        REAL, INTENT(OUT) :: netOutGoingLongWaveRadiation
        REAL, INTENT(OUT) :: netRadiationEquivalentEvaporation
        REAL, INTENT(OUT) :: evapoTranspirationPriestlyTaylor
        REAL, INTENT(OUT) :: conductance
        REAL, INTENT(OUT) :: diffusionLimitedEvaporation
        REAL, INTENT(OUT) :: evapoTranspirationPenman
        REAL, INTENT(OUT) :: energyLimitedEvaporation
        REAL, INTENT(OUT) :: soilEvaporation
        REAL, INTENT(OUT) :: evapoTranspiration
        REAL, INTENT(OUT) :: soilHeatFlux
        REAL, INTENT(OUT) :: potentialTranspiration
        REAL, INTENT(OUT) :: cropHeatFlux
        REAL, INTENT(OUT) :: minCanopyTemperature
        REAL, INTENT(OUT) :: maxCanopyTemperature
        !- Description:
    !            - Model Name: EnergyBalance
    !            - Author: Pierre MARTRE
    !            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2: Evapotranspiration and canopy and soil temperature calculations
    !            - Institution: INRA/LEPSE
    !            - Abstract: see documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=547
        !- inputs:
    !            - name: minTair
    !                          - description : minimum air temperature
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : -30
    !                          - max : 45
    !                          - default : 0.7
    !                          - unit : °C
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: maxTair
    !                          - description : maximum air Temperature
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : -30
    !                          - max : 45
    !                          - default : 7.2
    !                          - unit : °C
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: albedoCoefficient
    !                          - description : albedo Coefficient
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 0.23
    !                          - min : 0
    !                          - max : 1
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: stefanBoltzman
    !                          - description : stefan Boltzman constant
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 4.903E-09
    !                          - min : 0
    !                          - max : 1
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: elevation
    !                          - description : elevation
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 0
    !                          - min : -500
    !                          - max : 10000
    !                          - unit : m
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: solarRadiation
    !                          - description : solar Radiation
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - default : 3
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : MJ m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: vaporPressure
    !                          - description : vapor Pressure
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - default : 6.1
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : hPa
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: extraSolarRadiation
    !                          - description : extra Solar Radiation
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - default : 11.7
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : MJ m2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: lambdaV
    !                          - description : latent heat of vaporization of water
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 2.454
    !                          - min : 0
    !                          - max : 10
    !                          - unit : MJ kg-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: hslope
    !                          - description : the slope of saturated vapor pressure temperature curve at a given temperature 
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - default : 0.584
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : hPa °C-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: psychrometricConstant
    !                          - description : psychrometric constant
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 0.66
    !                          - min : 0
    !                          - max : 1
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: Alpha
    !                          - description : Priestley-Taylor evapotranspiration proportionality constant
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 1.5
    !                          - min : 0
    !                          - max : 100
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: vonKarman
    !                          - description : von Karman constant
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 1
    !                          - default : 0.42
    !                          - unit :  
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !                          - parametercategory : constant
    !            - name: heightWeatherMeasurements
    !                          - description : reference height of wind and humidity measurements
    !                          - parametercategory : soil
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10
    !                          - default : 2
    !                          - unit : m
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: zm
    !                          - description : roughness length governing momentum transfer, FAO
    !                          - parametercategory : constant
    !                          - inputtype : parameter
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 1
    !                          - default : 0.13
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: d
    !                          - description : corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO
    !                          - inputtype : parameter
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 0.67
    !                          - min : 0
    !                          - max : 1
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547rl
    !            - name: zh
    !                          - description : roughness length governing transfer of heat and vapour, FAO
    !                          - parametercategory : constant
    !                          - inputtype : parameter
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 1
    !                          - default : 0.013
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: plantHeight
    !                          - description : plant Height
    !                          - datatype : DOUBLE
    !                          - default : 0
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : mm
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !                          - variablecategory : auxiliary
    !            - name: wind
    !                          - description : wind
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - default : 124000
    !                          - min : 0
    !                          - max : 1000000
    !                          - unit : m d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: deficitOnTopLayers
    !                          - description : deficit On TopLayers
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - default : 5341
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: soilDiffusionConstant
    !                          - description : soil Diffusion Constant
    !                          - parametercategory : soil
    !                          - datatype : DOUBLE
    !                          - default : 4.2
    !                          - min : 0
    !                          - max : 10
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: VPDair
    !                          - description :  vapour pressure density
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - default : 2.19
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : hPa
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: rhoDensityAir
    !                          - description : Density of air
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 1.225
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: specificHeatCapacityAir
    !                          - description : Specific heat capacity of dry air
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 0.00101
    !                          - min : 0
    !                          - max : 1
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: tau
    !                          - description : plant cover factor
    !                          - parametercategory : species
    !                          - datatype : DOUBLE
    !                          - default : 0.9983
    !                          - min : 0
    !                          - max : 100
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: tauAlpha
    !                          - description : Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1
    !                          - parametercategory : soil
    !                          - datatype : DOUBLE
    !                          - default : 0.3
    !                          - min : 0
    !                          - max : 1
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: isWindVpDefined
    !                          - description : if wind and vapour pressure are defined
    !                          - parametercategory : constant
    !                          - datatype : INT
    !                          - default : 1
    !                          - min : 0
    !                          - max : 1
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
        !- outputs:
    !            - name: netRadiation
    !                          - description :  net radiation 
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : MJ m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: netOutGoingLongWaveRadiation
    !                          - description : net OutGoing Long Wave Radiation 
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: netRadiationEquivalentEvaporation
    !                          - variablecategory : auxiliary
    !                          - description : net Radiation in Equivalent Evaporation 
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: evapoTranspirationPriestlyTaylor
    !                          - description : evapoTranspiration of Priestly Taylor 
    !                          - variablecategory : rate
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: diffusionLimitedEvaporation
    !                          - description : the evaporation from the diffusion limited soil 
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: energyLimitedEvaporation
    !                          - description : energy Limited Evaporation 
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: conductance
    !                          - description : the boundary layer conductance
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : m d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: evapoTranspirationPenman
    !                          - description :  evapoTranspiration of Penman Monteith
    !                          - variablecategory : rate
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: soilEvaporation
    !                          - description : soil Evaporation
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: evapoTranspiration
    !                          - description : evapoTranspiration
    !                          - variablecategory : rate
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : mm
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: potentialTranspiration
    !                          - description : potential Transpiration 
    !                          - variablecategory : rate
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: soilHeatFlux
    !                          - description : soil Heat Flux 
    !                          - variablecategory : rate
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: cropHeatFlux
    !                          - description :  crop Heat Flux
    !                          - variablecategory : rate
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: minCanopyTemperature
    !                          - description : minimal Canopy Temperature  
    !                          - datatype : DOUBLE
    !                          - variablecategory : state
    !                          - min : -30
    !                          - max : 45
    !                          - unit : °C
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: maxCanopyTemperature
    !                          - description : maximal Canopy Temperature 
    !                          - datatype : DOUBLE
    !                          - variablecategory : state
    !                          - min : -30
    !                          - max : 45
    !                          - unit : °C
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        call model_diffusionlimitedevaporation(deficitOnTopLayers,  &
                soilDiffusionConstant,diffusionLimitedEvaporation)
        call model_conductance(vonKarman, heightWeatherMeasurements, zm, zh,  &
                d, plantHeight, wind,conductance)
        call model_netradiation(minTair, maxTair, albedoCoefficient,  &
                stefanBoltzman, elevation, solarRadiation, vaporPressure,  &
                extraSolarRadiation,netRadiation,netOutGoingLongWaveRadiation)
        call model_netradiationequivalentevaporation(lambdaV,  &
                netRadiation,netRadiationEquivalentEvaporation)
        call model_priestlytaylor(netRadiationEquivalentEvaporation, hslope,  &
                psychrometricConstant, Alpha,evapoTranspirationPriestlyTaylor)
        call model_penman(evapoTranspirationPriestlyTaylor, hslope, VPDair,  &
                psychrometricConstant, Alpha, lambdaV, rhoDensityAir,  &
                specificHeatCapacityAir, conductance,evapoTranspirationPenman)
        call model_evapotranspiration(isWindVpDefined,  &
                evapoTranspirationPriestlyTaylor,  &
                evapoTranspirationPenman,evapoTranspiration)
        call model_potentialtranspiration(evapoTranspiration,  &
                tau,potentialTranspiration)
        call model_ptsoil(evapoTranspirationPriestlyTaylor, Alpha, tau,  &
                tauAlpha,energyLimitedEvaporation)
        call model_soilevaporation(diffusionLimitedEvaporation,  &
                energyLimitedEvaporation,soilEvaporation)
        call model_soilheatflux(netRadiationEquivalentEvaporation, tau,  &
                soilEvaporation,soilHeatFlux)
        call model_cropheatflux(netRadiationEquivalentEvaporation,  &
                soilHeatFlux, potentialTranspiration,cropHeatFlux)
        call model_canopytemperature(minTair, maxTair, cropHeatFlux,  &
                conductance, lambdaV, rhoDensityAir,  &
                specificHeatCapacityAir,minCanopyTemperature,maxCanopyTemperature)
    END SUBROUTINE model_energybalance

END MODULE

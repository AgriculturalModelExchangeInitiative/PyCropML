
# This file has been generated at Wed Jun 24 23:29:10 2020

from openalea.core import *


__name__ = 'EnergyBalance'

__editable__ = True
__description__ = 'CropML Model library.'
__license__ = 'CECILL-C'
__url__ = 'http://pycropml.rtfd.org'
__version__ = '0.0.1'
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRA/CIRAD'
__icon__ = ''


__all__ = ['Potentialtranspiration_model_potentialtranspiration', 'Diffusionlimitedevaporation_model_diffusionlimitedevaporation', 'Cropheatflux_model_cropheatflux', 'Ptsoil_model_ptsoil', 'Netradiation_model_netradiation', 'Priestlytaylor_model_priestlytaylor', 'Canopytemperature_model_canopytemperature', 'Evapotranspiration_model_evapotranspiration', 'Soilevaporation_model_soilevaporation', 'Penman_model_penman', 'Soilheatflux_model_soilheatflux', 'Netradiationequivalentevaporation_model_netradiationequivalentevaporation', 'Conductance_model_conductance']



Potentialtranspiration_model_potentialtranspiration = Factory(name='PotentialTranspiration',
                authors='OpenAlea Consortium (wralea authors)',
                description='SiriusQuality2 uses availability of water from the soil reservoir as a method to restrict\n                    transpiration as soil moisture is depleted ',
                category='',
                nodemodule='Potentialtranspiration',
                nodeclass='model_potentialtranspiration',
                inputs=[{'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'evapoTranspiration', 'value': 830.958}, {'interface': IFloat(min=0, max=1, step=1.000000), 'name': 'tau', 'value': 0.9983}],
                outputs=[{'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'potentialTranspiration'}],
                widgetmodule=None,
                widgetclass=None,
               )




Diffusionlimitedevaporation_model_diffusionlimitedevaporation = Factory(name='DiffusionLimitedEvaporation',
                authors='OpenAlea Consortium (wralea authors)',
                description='the evaporation from the diffusion limited soil ',
                category='',
                nodemodule='Diffusionlimitedevaporation',
                nodeclass='model_diffusionlimitedevaporation',
                inputs=[{'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'deficitOnTopLayers', 'value': 5341}, {'interface': IFloat(min=0, max=10, step=1.000000), 'name': 'soilDiffusionConstant', 'value': 4.2}],
                outputs=[{'interface': IFloat(min=0, max=5000, step=1.000000), 'name': 'diffusionLimitedEvaporation'}],
                widgetmodule=None,
                widgetclass=None,
               )




Cropheatflux_model_cropheatflux = Factory(name='CropHeatFlux',
                authors='OpenAlea Consortium (wralea authors)',
                description='It is calculated from net Radiation, soil heat flux and potential transpiration ',
                category='',
                nodemodule='Cropheatflux',
                nodeclass='model_cropheatflux',
                inputs=[{'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'netRadiationEquivalentEvaporation', 'value': 638.142}, {'interface': IFloat(min=0, max=1000, step=1.000000), 'name': 'soilHeatFlux', 'value': 188.817}, {'interface': IFloat(min=0, max=1000, step=1.000000), 'name': 'potentialTranspiration', 'value': 1.413}],
                outputs=[{'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'cropHeatFlux'}],
                widgetmodule=None,
                widgetclass=None,
               )




Ptsoil_model_ptsoil = Factory(name='PtSoil',
                authors='OpenAlea Consortium (wralea authors)',
                description='Evaporation from the soil in the energy-limited stage ',
                category='',
                nodemodule='Ptsoil',
                nodeclass='model_ptsoil',
                inputs=[{'interface': IFloat(min=0, max=1000, step=1.000000), 'name': 'evapoTranspirationPriestlyTaylor', 'value': 120}, {'interface': IFloat(min=0, max=100, step=1.000000), 'name': 'Alpha', 'value': 1.5}, {'interface': IFloat(min=0, max=100, step=1.000000), 'name': 'tau', 'value': 0.9983}, {'interface': IFloat(min=0, max=1, step=1.000000), 'name': 'tauAlpha', 'value': 0.3}],
                outputs=[{'interface': IFloat(min=0, max=5000, step=1.000000), 'name': 'energyLimitedEvaporation'}],
                widgetmodule=None,
                widgetclass=None,
               )




Netradiation_model_netradiation = Factory(name='NetRadiation',
                authors='OpenAlea Consortium (wralea authors)',
                description='It is calculated at the surface of the canopy and is givenby the difference between incoming and outgoing radiation of both short\n                     and long wavelength radiation ',
                category='',
                nodemodule='Netradiation',
                nodeclass='model_netradiation',
                inputs=[{'interface': IFloat(min=-30, max=45, step=1.000000), 'name': 'minTair', 'value': 0.7}, {'interface': IFloat(min=-30, max=45, step=1.000000), 'name': 'maxTair', 'value': 7.2}, {'interface': IFloat(min=0, max=1, step=1.000000), 'name': 'albedoCoefficient', 'value': 0.23}, {'interface': IFloat(min=0, max=1, step=1.000000), 'name': 'stefanBoltzman', 'value': 4.903e-09}, {'interface': IFloat(min=-500, max=10000, step=1.000000), 'name': 'elevation', 'value': 0}, {'interface': IFloat(min=0, max=1000, step=1.000000), 'name': 'solarRadiation', 'value': 3}, {'interface': IFloat(min=0, max=1000, step=1.000000), 'name': 'vaporPressure', 'value': 6.1}, {'interface': IFloat(min=0, max=1000, step=1.000000), 'name': 'extraSolarRadiation', 'value': 11.7}],
                outputs=[{'interface': IFloat(min=0, max=5000, step=1.000000), 'name': 'netRadiation'}, {'interface': IFloat(min=0, max=5000, step=1.000000), 'name': 'netOutGoingLongWaveRadiation'}],
                widgetmodule=None,
                widgetclass=None,
               )




Priestlytaylor_model_priestlytaylor = Factory(name='PriestlyTaylor',
                authors='OpenAlea Consortium (wralea authors)',
                description='Calculate Energy Balance ',
                category='',
                nodemodule='Priestlytaylor',
                nodeclass='model_priestlytaylor',
                inputs=[{'interface': IFloat(min=0, max=5000, step=1.000000), 'name': 'netRadiationEquivalentEvaporation', 'value': 638.142}, {'interface': IFloat(min=0, max=1000, step=1.000000), 'name': 'hslope', 'value': 0.584}, {'interface': IFloat(min=0, max=1, step=1.000000), 'name': 'psychrometricConstant', 'value': 0.66}, {'interface': IFloat(min=0, max=100, step=1.000000), 'name': 'Alpha', 'value': 1.5}],
                outputs=[{'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'evapoTranspirationPriestlyTaylor'}],
                widgetmodule=None,
                widgetclass=None,
               )




Canopytemperature_model_canopytemperature = Factory(name='CanopyTemperature',
                authors='OpenAlea Consortium (wralea authors)',
                description='It is calculated from the crop heat flux and the boundary layer conductance ',
                category='',
                nodemodule='Canopytemperature',
                nodeclass='model_canopytemperature',
                inputs=[{'interface': IFloat(min=-30, max=45, step=1.000000), 'name': 'minTair', 'value': 0.7}, {'interface': IFloat(min=-30, max=45, step=1.000000), 'name': 'maxTair', 'value': 7.2}, {'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'cropHeatFlux', 'value': 447.912}, {'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'conductance', 'value': 598.685}, {'interface': IFloat(min=0, max=10, step=1.000000), 'name': 'lambdaV', 'value': 2.454}, {'interface': IFloat, 'name': 'rhoDensityAir', 'value': 1.225}, {'interface': IFloat, 'name': 'specificHeatCapacityAir', 'value': 0.00101}],
                outputs=[{'interface': IFloat(min=-30, max=45, step=1.000000), 'name': 'minCanopyTemperature'}, {'interface': IFloat(min=-30, max=45, step=1.000000), 'name': 'maxCanopyTemperature'}],
                widgetmodule=None,
                widgetclass=None,
               )




Evapotranspiration_model_evapotranspiration = Factory(name='EvapoTranspiration',
                authors='OpenAlea Consortium (wralea authors)',
                description='According to the availability of wind and/or vapor pressure daily data, the\n            SiriusQuality2 model calculates the evapotranspiration rate using the Penman (if wind\n            and vapor pressure data are available) (Penman 1948) or the Priestly-Taylor\n            (Priestley and Taylor 1972) method ',
                category='',
                nodemodule='Evapotranspiration',
                nodeclass='model_evapotranspiration',
                inputs=[{'interface': IInt(min=0, max=1, step=1), 'name': 'isWindVpDefined', 'value': 1}, {'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'evapoTranspirationPriestlyTaylor', 'value': 449.367}, {'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'evapoTranspirationPenman', 'value': 830.958}],
                outputs=[{'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'evapoTranspiration'}],
                widgetmodule=None,
                widgetclass=None,
               )




Soilevaporation_model_soilevaporation = Factory(name='SoilEvaporation',
                authors='OpenAlea Consortium (wralea authors)',
                description='Starting from a soil at field capacity, soil evaporation  is assumed to\n                be energy limited during the first phase of evaporation and diffusion limited thereafter.\n                Hence, the soil evaporation model considers these two processes taking the minimum between\n                the energy limited evaporation (PtSoil) and the diffused limited\n                evaporation ',
                category='',
                nodemodule='Soilevaporation',
                nodeclass='model_soilevaporation',
                inputs=[{'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'diffusionLimitedEvaporation', 'value': 6605.505}, {'interface': IFloat(min=0, max=1000, step=1.000000), 'name': 'energyLimitedEvaporation', 'value': 448.24}],
                outputs=[{'interface': IFloat(min=0, max=5000, step=1.000000), 'name': 'soilEvaporation'}],
                widgetmodule=None,
                widgetclass=None,
               )




Penman_model_penman = Factory(name='Penman',
                authors='OpenAlea Consortium (wralea authors)',
                description='This method is used when wind and vapor pressure daily data are available\n        ',
                category='',
                nodemodule='Penman',
                nodeclass='model_penman',
                inputs=[{'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'evapoTranspirationPriestlyTaylor', 'value': 449.367}, {'interface': IFloat(min=0, max=1000, step=1.000000), 'name': 'hslope', 'value': 0.584}, {'interface': IFloat(min=0, max=1000, step=1.000000), 'name': 'VPDair', 'value': 2.19}, {'interface': IFloat(min=0, max=1, step=1.000000), 'name': 'psychrometricConstant', 'value': 0.66}, {'interface': IFloat(min=0, max=100, step=1.000000), 'name': 'Alpha', 'value': 1.5}, {'interface': IFloat(min=0, max=10, step=1.000000), 'name': 'lambdaV', 'value': 2.454}, {'interface': IFloat, 'name': 'rhoDensityAir', 'value': 1.225}, {'interface': IFloat(min=0, max=1, step=1.000000), 'name': 'specificHeatCapacityAir', 'value': 0.00101}, {'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'conductance', 'value': 598.685}],
                outputs=[{'interface': IFloat(min=0, max=5000, step=1.000000), 'name': 'evapoTranspirationPenman'}],
                widgetmodule=None,
                widgetclass=None,
               )




Soilheatflux_model_soilheatflux = Factory(name='SoilHeatFlux',
                authors='OpenAlea Consortium (wralea authors)',
                description='The available energy in the soil ',
                category='',
                nodemodule='Soilheatflux',
                nodeclass='model_soilheatflux',
                inputs=[{'interface': IFloat(min=0, max=5000, step=1.000000), 'name': 'netRadiationEquivalentEvaporation', 'value': 638.142}, {'interface': IFloat(min=0, max=100, step=1.000000), 'name': 'tau', 'value': 0.9983}, {'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'soilEvaporation', 'value': 448.24}],
                outputs=[{'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'soilHeatFlux'}],
                widgetmodule=None,
                widgetclass=None,
               )




Netradiationequivalentevaporation_model_netradiationequivalentevaporation = Factory(name='NetRadiationEquivalentEvaporation',
                authors='OpenAlea Consortium (wralea authors)',
                description=' It is given by dividing net radiation by latent heat of vaporization of water ',
                category='',
                nodemodule='Netradiationequivalentevaporation',
                nodeclass='model_netradiationequivalentevaporation',
                inputs=[{'interface': IFloat(min=0, max=10, step=1.000000), 'name': 'lambdaV', 'value': 2.454}, {'interface': IFloat(min=0, max=5000, step=1.000000), 'name': 'netRadiation', 'value': 1.566}],
                outputs=[{'interface': IFloat(min=0, max=5000, step=1.000000), 'name': 'netRadiationEquivalentEvaporation'}],
                widgetmodule=None,
                widgetclass=None,
               )




Conductance_model_conductance = Factory(name='Conductance',
                authors='OpenAlea Consortium (wralea authors)',
                description='The boundary layer conductance is expressed as the wind speed profile above the\n            canopy and the canopy structure. The approach does not take into account buoyancy\n            effects. \n        ',
                category='',
                nodemodule='Conductance',
                nodeclass='model_conductance',
                inputs=[{'interface': IFloat(min=0, max=1, step=1.000000), 'name': 'vonKarman', 'value': 0.42}, {'interface': IFloat(min=0, max=10, step=1.000000), 'name': 'heightWeatherMeasurements', 'value': 2}, {'interface': IFloat(min=0, max=1, step=1.000000), 'name': 'zm', 'value': 0.13}, {'interface': IFloat(min=0, max=1, step=1.000000), 'name': 'zh', 'value': 0.013}, {'interface': IFloat(min=0, max=1, step=1.000000), 'name': 'd', 'value': 0.67}, {'interface': IFloat(min=0, max=1000, step=1.000000), 'name': 'plantHeight', 'value': 0}, {'interface': IFloat(min=0, max=1000000, step=1.000000), 'name': 'wind', 'value': 124000}],
                outputs=[{'interface': IFloat(min=0, max=10000, step=1.000000), 'name': 'conductance'}],
                widgetmodule=None,
                widgetclass=None,
               )





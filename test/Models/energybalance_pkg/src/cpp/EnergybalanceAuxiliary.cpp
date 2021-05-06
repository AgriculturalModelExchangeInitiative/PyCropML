#include "EnergybalanceAuxiliary.h"
EnergybalanceAuxiliary::EnergybalanceAuxiliary() { }

float EnergybalanceAuxiliary::getminTair() {return this-> minTair; }
float EnergybalanceAuxiliary::getmaxTair() {return this-> maxTair; }
float EnergybalanceAuxiliary::getsolarRadiation() {return this-> solarRadiation; }
float EnergybalanceAuxiliary::getvaporPressure() {return this-> vaporPressure; }
float EnergybalanceAuxiliary::getextraSolarRadiation() {return this-> extraSolarRadiation; }
float EnergybalanceAuxiliary::gethslope() {return this-> hslope; }
float EnergybalanceAuxiliary::getplantHeight() {return this-> plantHeight; }
float EnergybalanceAuxiliary::getwind() {return this-> wind; }
float EnergybalanceAuxiliary::getdeficitOnTopLayers() {return this-> deficitOnTopLayers; }
float EnergybalanceAuxiliary::getVPDair() {return this-> VPDair; }
float EnergybalanceAuxiliary::getnetRadiation() {return this-> netRadiation; }
float EnergybalanceAuxiliary::getnetOutGoingLongWaveRadiation() {return this-> netOutGoingLongWaveRadiation; }
float EnergybalanceAuxiliary::getnetRadiationEquivalentEvaporation() {return this-> netRadiationEquivalentEvaporation; }
float EnergybalanceAuxiliary::getenergyLimitedEvaporation() {return this-> energyLimitedEvaporation; }
float EnergybalanceAuxiliary::getsoilEvaporation() {return this-> soilEvaporation; }

void EnergybalanceAuxiliary::setminTair(float _minTair) { this->minTair = _minTair; }
void EnergybalanceAuxiliary::setmaxTair(float _maxTair) { this->maxTair = _maxTair; }
void EnergybalanceAuxiliary::setsolarRadiation(float _solarRadiation) { this->solarRadiation = _solarRadiation; }
void EnergybalanceAuxiliary::setvaporPressure(float _vaporPressure) { this->vaporPressure = _vaporPressure; }
void EnergybalanceAuxiliary::setextraSolarRadiation(float _extraSolarRadiation) { this->extraSolarRadiation = _extraSolarRadiation; }
void EnergybalanceAuxiliary::sethslope(float _hslope) { this->hslope = _hslope; }
void EnergybalanceAuxiliary::setplantHeight(float _plantHeight) { this->plantHeight = _plantHeight; }
void EnergybalanceAuxiliary::setwind(float _wind) { this->wind = _wind; }
void EnergybalanceAuxiliary::setdeficitOnTopLayers(float _deficitOnTopLayers) { this->deficitOnTopLayers = _deficitOnTopLayers; }
void EnergybalanceAuxiliary::setVPDair(float _VPDair) { this->VPDair = _VPDair; }
void EnergybalanceAuxiliary::setnetRadiation(float _netRadiation) { this->netRadiation = _netRadiation; }
void EnergybalanceAuxiliary::setnetOutGoingLongWaveRadiation(float _netOutGoingLongWaveRadiation) { this->netOutGoingLongWaveRadiation = _netOutGoingLongWaveRadiation; }
void EnergybalanceAuxiliary::setnetRadiationEquivalentEvaporation(float _netRadiationEquivalentEvaporation) { this->netRadiationEquivalentEvaporation = _netRadiationEquivalentEvaporation; }
void EnergybalanceAuxiliary::setenergyLimitedEvaporation(float _energyLimitedEvaporation) { this->energyLimitedEvaporation = _energyLimitedEvaporation; }
void EnergybalanceAuxiliary::setsoilEvaporation(float _soilEvaporation) { this->soilEvaporation = _soilEvaporation; }
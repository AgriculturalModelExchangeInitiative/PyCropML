#include "EnergybalanceState.h"
EnergybalanceState::EnergybalanceState() { }

float EnergybalanceState::getdiffusionLimitedEvaporation() {return this-> diffusionLimitedEvaporation; }
float EnergybalanceState::getconductance() {return this-> conductance; }
float EnergybalanceState::getminCanopyTemperature() {return this-> minCanopyTemperature; }
float EnergybalanceState::getmaxCanopyTemperature() {return this-> maxCanopyTemperature; }

void EnergybalanceState::setdiffusionLimitedEvaporation(float _diffusionLimitedEvaporation) { this->diffusionLimitedEvaporation = _diffusionLimitedEvaporation; }
void EnergybalanceState::setconductance(float _conductance) { this->conductance = _conductance; }
void EnergybalanceState::setminCanopyTemperature(float _minCanopyTemperature) { this->minCanopyTemperature = _minCanopyTemperature; }
void EnergybalanceState::setmaxCanopyTemperature(float _maxCanopyTemperature) { this->maxCanopyTemperature = _maxCanopyTemperature; }
#include "EnergybalanceRate.h"
EnergybalanceRate::EnergybalanceRate() { }

float EnergybalanceRate::getevapoTranspirationPriestlyTaylor() {return this-> evapoTranspirationPriestlyTaylor; }
float EnergybalanceRate::getevapoTranspirationPenman() {return this-> evapoTranspirationPenman; }
float EnergybalanceRate::getevapoTranspiration() {return this-> evapoTranspiration; }
float EnergybalanceRate::getpotentialTranspiration() {return this-> potentialTranspiration; }
float EnergybalanceRate::getsoilHeatFlux() {return this-> soilHeatFlux; }
float EnergybalanceRate::getcropHeatFlux() {return this-> cropHeatFlux; }

void EnergybalanceRate::setevapoTranspirationPriestlyTaylor(float _evapoTranspirationPriestlyTaylor) { this->evapoTranspirationPriestlyTaylor = _evapoTranspirationPriestlyTaylor; }
void EnergybalanceRate::setevapoTranspirationPenman(float _evapoTranspirationPenman) { this->evapoTranspirationPenman = _evapoTranspirationPenman; }
void EnergybalanceRate::setevapoTranspiration(float _evapoTranspiration) { this->evapoTranspiration = _evapoTranspiration; }
void EnergybalanceRate::setpotentialTranspiration(float _potentialTranspiration) { this->potentialTranspiration = _potentialTranspiration; }
void EnergybalanceRate::setsoilHeatFlux(float _soilHeatFlux) { this->soilHeatFlux = _soilHeatFlux; }
void EnergybalanceRate::setcropHeatFlux(float _cropHeatFlux) { this->cropHeatFlux = _cropHeatFlux; }
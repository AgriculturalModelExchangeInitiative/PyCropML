#include "PhenologyAuxiliary.h"

PhenologyAuxiliary::PhenologyAuxiliary() { }

string PhenologyAuxiliary::getcurrentdate() {return this-> currentdate; }
float PhenologyAuxiliary::getcumulTT() {return this-> cumulTT; }
float PhenologyAuxiliary::getdayLength() {return this-> dayLength; }
float PhenologyAuxiliary::getdeltaTT() {return this-> deltaTT; }
float PhenologyAuxiliary::getgAI() {return this-> gAI; }
float PhenologyAuxiliary::getpAR() {return this-> pAR; }
float PhenologyAuxiliary::getgrainCumulTT() {return this-> grainCumulTT; }
float PhenologyAuxiliary::getfixPhyll() {return this-> fixPhyll; }
float PhenologyAuxiliary::getcumulTTFromZC_39() {return this-> cumulTTFromZC_39; }
float PhenologyAuxiliary::getcumulTTFromZC_91() {return this-> cumulTTFromZC_91; }
float PhenologyAuxiliary::getcumulTTFromZC_65() {return this-> cumulTTFromZC_65; }

void PhenologyAuxiliary::setcurrentdate(string _currentdate) { this->currentdate = _currentdate; }
void PhenologyAuxiliary::setcumulTT(float _cumulTT) { this->cumulTT = _cumulTT; }
void PhenologyAuxiliary::setdayLength(float _dayLength) { this->dayLength = _dayLength; }
void PhenologyAuxiliary::setdeltaTT(float _deltaTT) { this->deltaTT = _deltaTT; }
void PhenologyAuxiliary::setgAI(float _gAI) { this->gAI = _gAI; }
void PhenologyAuxiliary::setpAR(float _pAR) { this->pAR = _pAR; }
void PhenologyAuxiliary::setgrainCumulTT(float _grainCumulTT) { this->grainCumulTT = _grainCumulTT; }
void PhenologyAuxiliary::setfixPhyll(float _fixPhyll) { this->fixPhyll = _fixPhyll; }
void PhenologyAuxiliary::setcumulTTFromZC_39(float _cumulTTFromZC_39) { this->cumulTTFromZC_39 = _cumulTTFromZC_39; }
void PhenologyAuxiliary::setcumulTTFromZC_91(float _cumulTTFromZC_91) { this->cumulTTFromZC_91 = _cumulTTFromZC_91; }
void PhenologyAuxiliary::setcumulTTFromZC_65(float _cumulTTFromZC_65) { this->cumulTTFromZC_65 = _cumulTTFromZC_65; }
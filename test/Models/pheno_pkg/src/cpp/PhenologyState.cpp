#include "PhenologyState.h"
PhenologyState::PhenologyState() { }

float PhenologyState::getptq() {return this-> ptq; }
string PhenologyState::getcurrentZadokStage() {return this-> currentZadokStage; }
int PhenologyState::gethasFlagLeafLiguleAppeared() {return this-> hasFlagLeafLiguleAppeared; }
int PhenologyState::gethasZadokStageChanged() {return this-> hasZadokStageChanged; }
vector<float>& PhenologyState::getlistPARTTWindowForPTQ() {return this-> listPARTTWindowForPTQ; }
int PhenologyState::gethasLastPrimordiumAppeared() {return this-> hasLastPrimordiumAppeared; }
vector<float>& PhenologyState::getlistTTShootWindowForPTQ() {return this-> listTTShootWindowForPTQ; }
vector<float>& PhenologyState::getlistTTShootWindowForPTQ1() {return this-> listTTShootWindowForPTQ1; }
vector<string>& PhenologyState::getcalendarMoments() {return this-> calendarMoments; }
float PhenologyState::getcanopyShootNumber() {return this-> canopyShootNumber; }
vector<string>& PhenologyState::getcalendarDates() {return this-> calendarDates; }
vector<int>& PhenologyState::getleafTillerNumberArray() {return this-> leafTillerNumberArray; }
float PhenologyState::getvernaprog() {return this-> vernaprog; }
float PhenologyState::getphyllochron() {return this-> phyllochron; }
float PhenologyState::getleafNumber() {return this-> leafNumber; }
int PhenologyState::getnumberTillerCohort() {return this-> numberTillerCohort; }
vector<float>& PhenologyState::gettilleringProfile() {return this-> tilleringProfile; }
float PhenologyState::getaverageShootNumberPerPlant() {return this-> averageShootNumberPerPlant; }
float PhenologyState::getminFinalNumber() {return this-> minFinalNumber; }
float PhenologyState::getfinalLeafNumber() {return this-> finalLeafNumber; }
float PhenologyState::getphase() {return this-> phase; }
vector<float>& PhenologyState::getlistGAITTWindowForPTQ() {return this-> listGAITTWindowForPTQ; }
vector<float>& PhenologyState::getcalendarCumuls() {return this-> calendarCumuls; }
float PhenologyState::getgAImean() {return this-> gAImean; }
float PhenologyState::getpastMaxAI() {return this-> pastMaxAI; }
int PhenologyState::getisMomentRegistredZC_39() {return this-> isMomentRegistredZC_39; }

void PhenologyState::setptq(float _ptq) { this->ptq = _ptq; }
void PhenologyState::setcurrentZadokStage(string _currentZadokStage) { this->currentZadokStage = _currentZadokStage; }
void PhenologyState::sethasFlagLeafLiguleAppeared(int _hasFlagLeafLiguleAppeared) { this->hasFlagLeafLiguleAppeared = _hasFlagLeafLiguleAppeared; }
void PhenologyState::sethasZadokStageChanged(int _hasZadokStageChanged) { this->hasZadokStageChanged = _hasZadokStageChanged; }
void PhenologyState::setlistPARTTWindowForPTQ(vector<float>& _listPARTTWindowForPTQ){
    this->listPARTTWindowForPTQ = _listPARTTWindowForPTQ;
}
void PhenologyState::sethasLastPrimordiumAppeared(int _hasLastPrimordiumAppeared) { this->hasLastPrimordiumAppeared = _hasLastPrimordiumAppeared; }
void PhenologyState::setlistTTShootWindowForPTQ(vector<float>& _listTTShootWindowForPTQ){
    this->listTTShootWindowForPTQ = _listTTShootWindowForPTQ;
}
void PhenologyState::setlistTTShootWindowForPTQ1(vector<float>& _listTTShootWindowForPTQ1){
    this->listTTShootWindowForPTQ1 = _listTTShootWindowForPTQ1;
}
void PhenologyState::setcalendarMoments(vector<string>& _calendarMoments){
    this->calendarMoments = _calendarMoments;
}
void PhenologyState::setcanopyShootNumber(float _canopyShootNumber) { this->canopyShootNumber = _canopyShootNumber; }
void PhenologyState::setcalendarDates(vector<string>& _calendarDates){
    this->calendarDates = _calendarDates;
}
void PhenologyState::setleafTillerNumberArray(vector<int>& _leafTillerNumberArray){
    this->leafTillerNumberArray = _leafTillerNumberArray;
}
void PhenologyState::setvernaprog(float _vernaprog) { this->vernaprog = _vernaprog; }
void PhenologyState::setphyllochron(float _phyllochron) { this->phyllochron = _phyllochron; }
void PhenologyState::setleafNumber(float _leafNumber) { this->leafNumber = _leafNumber; }
void PhenologyState::setnumberTillerCohort(int _numberTillerCohort) { this->numberTillerCohort = _numberTillerCohort; }
void PhenologyState::settilleringProfile(vector<float>& _tilleringProfile){
    this->tilleringProfile = _tilleringProfile;
}
void PhenologyState::setaverageShootNumberPerPlant(float _averageShootNumberPerPlant) { this->averageShootNumberPerPlant = _averageShootNumberPerPlant; }
void PhenologyState::setminFinalNumber(float _minFinalNumber) { this->minFinalNumber = _minFinalNumber; }
void PhenologyState::setfinalLeafNumber(float _finalLeafNumber) { this->finalLeafNumber = _finalLeafNumber; }
void PhenologyState::setphase(float _phase) { this->phase = _phase; }
void PhenologyState::setlistGAITTWindowForPTQ(vector<float>& _listGAITTWindowForPTQ){
    this->listGAITTWindowForPTQ = _listGAITTWindowForPTQ;
}
void PhenologyState::setcalendarCumuls(vector<float>& _calendarCumuls){
    this->calendarCumuls = _calendarCumuls;
}
void PhenologyState::setgAImean(float _gAImean) { this->gAImean = _gAImean; }
void PhenologyState::setpastMaxAI(float _pastMaxAI) { this->pastMaxAI = _pastMaxAI; }
void PhenologyState::setisMomentRegistredZC_39(int _isMomentRegistredZC_39) { this->isMomentRegistredZC_39 = _isMomentRegistredZC_39; }
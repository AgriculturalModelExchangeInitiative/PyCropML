#ifndef _PhenologyState_
#define _PhenologyState_
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
using namespace std;
class PhenologyState
{
    private:
        float ptq;
        string currentZadokStage;
        int hasFlagLeafLiguleAppeared;
        int hasZadokStageChanged;
        vector<float> listPARTTWindowForPTQ;
        int hasLastPrimordiumAppeared;
        vector<float> listTTShootWindowForPTQ;
        vector<float> listTTShootWindowForPTQ1;
        vector<string> calendarMoments;
        float canopyShootNumber;
        vector<string> calendarDates;
        vector<int> leafTillerNumberArray;
        float vernaprog;
        float phyllochron;
        float leafNumber;
        int numberTillerCohort;
        vector<float> tilleringProfile;
        float averageShootNumberPerPlant;
        float minFinalNumber;
        float finalLeafNumber;
        float phase;
        vector<float> listGAITTWindowForPTQ;
        vector<float> calendarCumuls;
        float gAImean;
        float pastMaxAI;
        int isMomentRegistredZC_39;
    public:
        PhenologyState();
        float getptq();
        void setptq(float _ptq);
        string getcurrentZadokStage();
        void setcurrentZadokStage(string _currentZadokStage);
        int gethasFlagLeafLiguleAppeared();
        void sethasFlagLeafLiguleAppeared(int _hasFlagLeafLiguleAppeared);
        int gethasZadokStageChanged();
        void sethasZadokStageChanged(int _hasZadokStageChanged);
        vector<float>& getlistPARTTWindowForPTQ();
        void setlistPARTTWindowForPTQ(vector<float>& _listPARTTWindowForPTQ);
        int gethasLastPrimordiumAppeared();
        void sethasLastPrimordiumAppeared(int _hasLastPrimordiumAppeared);
        vector<float>& getlistTTShootWindowForPTQ();
        void setlistTTShootWindowForPTQ(vector<float>& _listTTShootWindowForPTQ);
        vector<float>& getlistTTShootWindowForPTQ1();
        void setlistTTShootWindowForPTQ1(vector<float>& _listTTShootWindowForPTQ1);
        vector<string>& getcalendarMoments();
        void setcalendarMoments(vector<string>& _calendarMoments);
        float getcanopyShootNumber();
        void setcanopyShootNumber(float _canopyShootNumber);
        vector<string>& getcalendarDates();
        void setcalendarDates(vector<string>& _calendarDates);
        vector<int>& getleafTillerNumberArray();
        void setleafTillerNumberArray(vector<int>& _leafTillerNumberArray);
        float getvernaprog();
        void setvernaprog(float _vernaprog);
        float getphyllochron();
        void setphyllochron(float _phyllochron);
        float getleafNumber();
        void setleafNumber(float _leafNumber);
        int getnumberTillerCohort();
        void setnumberTillerCohort(int _numberTillerCohort);
        vector<float>& gettilleringProfile();
        void settilleringProfile(vector<float>& _tilleringProfile);
        float getaverageShootNumberPerPlant();
        void setaverageShootNumberPerPlant(float _averageShootNumberPerPlant);
        float getminFinalNumber();
        void setminFinalNumber(float _minFinalNumber);
        float getfinalLeafNumber();
        void setfinalLeafNumber(float _finalLeafNumber);
        float getphase();
        void setphase(float _phase);
        vector<float>& getlistGAITTWindowForPTQ();
        void setlistGAITTWindowForPTQ(vector<float>& _listGAITTWindowForPTQ);
        vector<float>& getcalendarCumuls();
        void setcalendarCumuls(vector<float>& _calendarCumuls);
        float getgAImean();
        void setgAImean(float _gAImean);
        float getpastMaxAI();
        void setpastMaxAI(float _pastMaxAI);
        int getisMomentRegistredZC_39();
        void setisMomentRegistredZC_39(int _isMomentRegistredZC_39);

};
#endif
#ifndef _PhenologyAuxiliary_
#define _PhenologyAuxiliary_
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
using namespace std;
class PhenologyAuxiliary
{
    private:
        string currentdate;
        float cumulTT;
        float dayLength;
        float deltaTT;
        float gAI;
        float pAR;
        float grainCumulTT;
        float fixPhyll;
        float cumulTTFromZC_39;
        float cumulTTFromZC_91;
        float cumulTTFromZC_65;
    public:
        PhenologyAuxiliary();
        string getcurrentdate();
        void setcurrentdate(string _currentdate);
        float getcumulTT();
        void setcumulTT(float _cumulTT);
        float getdayLength();
        void setdayLength(float _dayLength);
        float getdeltaTT();
        void setdeltaTT(float _deltaTT);
        float getgAI();
        void setgAI(float _gAI);
        float getpAR();
        void setpAR(float _pAR);
        float getgrainCumulTT();
        void setgrainCumulTT(float _grainCumulTT);
        float getfixPhyll();
        void setfixPhyll(float _fixPhyll);
        float getcumulTTFromZC_39();
        void setcumulTTFromZC_39(float _cumulTTFromZC_39);
        float getcumulTTFromZC_91();
        void setcumulTTFromZC_91(float _cumulTTFromZC_91);
        float getcumulTTFromZC_65();
        void setcumulTTFromZC_65(float _cumulTTFromZC_65);

};
#endif
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "PhenologyState.h"
#include "PhenologyRate.h"
#include "PhenologyAuxiliary.h"
using namespace std;
class Updatephase
{
    private:
        int isVernalizable;
        float dse;
        float pFLLAnth;
        float dcd;
        float dgf;
        float degfm;
        float maxDL;
        float sLDL;
        bool ignoreGrainMaturation;
        float pHEADANTH;
        string choosePhyllUse;
        float p;
    public:
        Updatephase();
        void  Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        void  Init(PhenologyState& s,PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        int getisVernalizable();
        void setisVernalizable(int _isVernalizable);
        float getdse();
        void setdse(float _dse);
        float getpFLLAnth();
        void setpFLLAnth(float _pFLLAnth);
        float getdcd();
        void setdcd(float _dcd);
        float getdgf();
        void setdgf(float _dgf);
        float getdegfm();
        void setdegfm(float _degfm);
        float getmaxDL();
        void setmaxDL(float _maxDL);
        float getsLDL();
        void setsLDL(float _sLDL);
        bool getignoreGrainMaturation();
        void setignoreGrainMaturation(bool _ignoreGrainMaturation);
        float getpHEADANTH();
        void setpHEADANTH(float _pHEADANTH);
        string getchoosePhyllUse();
        void setchoosePhyllUse(string _choosePhyllUse);
        float getp();
        void setp(float _p);

};
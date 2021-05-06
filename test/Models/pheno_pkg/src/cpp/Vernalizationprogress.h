#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "PhenologyState.h"
#include "PhenologyRate.h"
#include "PhenologyAuxiliary.h"
using namespace std;
class Vernalizationprogress
{
    private:
        float minTvern;
        float intTvern;
        float vAI;
        float vBEE;
        float minDL;
        float maxDL;
        float maxTvern;
        float pNini;
        float aMXLFNO;
        int isVernalizable;
    public:
        Vernalizationprogress();
        void  Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        void  Init(PhenologyState& s,PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        float getminTvern();
        void setminTvern(float _minTvern);
        float getintTvern();
        void setintTvern(float _intTvern);
        float getvAI();
        void setvAI(float _vAI);
        float getvBEE();
        void setvBEE(float _vBEE);
        float getminDL();
        void setminDL(float _minDL);
        float getmaxDL();
        void setmaxDL(float _maxDL);
        float getmaxTvern();
        void setmaxTvern(float _maxTvern);
        float getpNini();
        void setpNini(float _pNini);
        float getaMXLFNO();
        void setaMXLFNO(float _aMXLFNO);
        int getisVernalizable();
        void setisVernalizable(int _isVernalizable);

};
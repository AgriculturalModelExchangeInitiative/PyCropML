#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "PhenologyState.h"
#include "PhenologyRate.h"
#include "PhenologyAuxiliary.h"
using namespace std;
class Phyllochron
{
    private:
        float lincr;
        float ldecr;
        float pdecr;
        float pincr;
        float kl;
        float pTQhf;
        float B;
        float p;
        string choosePhyllUse;
        float areaSL;
        float areaSS;
        float lARmin;
        float lARmax;
        float sowingDensity;
        float lNeff;
    public:
        Phyllochron();
        void  Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        float getlincr();
        void setlincr(float _lincr);
        float getldecr();
        void setldecr(float _ldecr);
        float getpdecr();
        void setpdecr(float _pdecr);
        float getpincr();
        void setpincr(float _pincr);
        float getkl();
        void setkl(float _kl);
        float getpTQhf();
        void setpTQhf(float _pTQhf);
        float getB();
        void setB(float _B);
        float getp();
        void setp(float _p);
        string getchoosePhyllUse();
        void setchoosePhyllUse(string _choosePhyllUse);
        float getareaSL();
        void setareaSL(float _areaSL);
        float getareaSS();
        void setareaSS(float _areaSS);
        float getlARmin();
        void setlARmin(float _lARmin);
        float getlARmax();
        void setlARmax(float _lARmax);
        float getsowingDensity();
        void setsowingDensity(float _sowingDensity);
        float getlNeff();
        void setlNeff(float _lNeff);

};
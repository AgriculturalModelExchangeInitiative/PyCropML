#include "Phyllochron.h"
#include "Phylsowingdatecorrection.h"
#include "Shootnumber.h"
#include "Updateleafflag.h"
#include "Updatephase.h"
#include "Leafnumber.h"
#include "Vernalizationprogress.h"
#include "Ismomentregistredzc_39.h"
#include "Cumulttfrom.h"
#include "Updatecalendar.h"
#include "Registerzadok.h"
#include "Ptq.h"
#include "Gaimean.h"
using namespace std;

class PhenologyComponent
{
    private:
        float aMXLFNO;
        float pNini;
        float sDsa_sh;
        float latitude;
        float kl;
        float lincr;
        float ldecr;
        float pincr;
        float pTQhf;
        float B;
        float areaSL;
        float areaSS;
        float lARmin;
        float sowingDensity;
        float lARmax;
        float lNeff;
        float rp;
        float p;
        float pdecr;
        float maxTvern;
        float tTWindowForPTQ;
        float vBEE;
        int isVernalizable;
        float minTvern;
        float intTvern;
        float vAI;
        float maxDL;
        string choosePhyllUse;
        float minDL;
        float pFLLAnth;
        float dcd;
        float dgf;
        float degfm;
        bool ignoreGrainMaturation;
        float pHEADANTH;
        float sLDL;
        int sowingDay;
        string sowingDate;
        int sDws;
        float sDsa_nh;
        float der;
        float targetFertileShoot;
        float dse;
        float slopeTSFLN;
        float intTSFLN;
    public:
        PhenologyComponent();
        PhenologyComponent(const PhenologyComponent& copy);
        void  Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        void  Init(PhenologyState& s,PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        float getaMXLFNO();
        void setaMXLFNO(float _aMXLFNO);
        float getpNini();
        void setpNini(float _pNini);
        float getsDsa_sh();
        void setsDsa_sh(float _sDsa_sh);
        float getlatitude();
        void setlatitude(float _latitude);
        float getkl();
        void setkl(float _kl);
        float getlincr();
        void setlincr(float _lincr);
        float getldecr();
        void setldecr(float _ldecr);
        float getpincr();
        void setpincr(float _pincr);
        float getpTQhf();
        void setpTQhf(float _pTQhf);
        float getB();
        void setB(float _B);
        float getareaSL();
        void setareaSL(float _areaSL);
        float getareaSS();
        void setareaSS(float _areaSS);
        float getlARmin();
        void setlARmin(float _lARmin);
        float getsowingDensity();
        void setsowingDensity(float _sowingDensity);
        float getlARmax();
        void setlARmax(float _lARmax);
        float getlNeff();
        void setlNeff(float _lNeff);
        float getrp();
        void setrp(float _rp);
        float getp();
        void setp(float _p);
        float getpdecr();
        void setpdecr(float _pdecr);
        float getmaxTvern();
        void setmaxTvern(float _maxTvern);
        float gettTWindowForPTQ();
        void settTWindowForPTQ(float _tTWindowForPTQ);
        float getvBEE();
        void setvBEE(float _vBEE);
        int getisVernalizable();
        void setisVernalizable(int _isVernalizable);
        float getminTvern();
        void setminTvern(float _minTvern);
        float getintTvern();
        void setintTvern(float _intTvern);
        float getvAI();
        void setvAI(float _vAI);
        float getmaxDL();
        void setmaxDL(float _maxDL);
        string getchoosePhyllUse();
        void setchoosePhyllUse(string _choosePhyllUse);
        float getminDL();
        void setminDL(float _minDL);
        float getpFLLAnth();
        void setpFLLAnth(float _pFLLAnth);
        float getdcd();
        void setdcd(float _dcd);
        float getdgf();
        void setdgf(float _dgf);
        float getdegfm();
        void setdegfm(float _degfm);
        bool getignoreGrainMaturation();
        void setignoreGrainMaturation(bool _ignoreGrainMaturation);
        float getpHEADANTH();
        void setpHEADANTH(float _pHEADANTH);
        float getsLDL();
        void setsLDL(float _sLDL);
        int getsowingDay();
        void setsowingDay(int _sowingDay);
        string getsowingDate();
        void setsowingDate(string _sowingDate);
        int getsDws();
        void setsDws(int _sDws);
        float getsDsa_nh();
        void setsDsa_nh(float _sDsa_nh);
        float getder();
        void setder(float _der);
        float gettargetFertileShoot();
        void settargetFertileShoot(float _targetFertileShoot);
        float getdse();
        void setdse(float _dse);
        float getslopeTSFLN();
        void setslopeTSFLN(float _slopeTSFLN);
        float getintTSFLN();
        void setintTSFLN(float _intTSFLN);

        Phyllochron _Phyllochron;
        Phylsowingdatecorrection _Phylsowingdatecorrection;
        Shootnumber _Shootnumber;
        Updateleafflag _Updateleafflag;
        Updatephase _Updatephase;
        Leafnumber _Leafnumber;
        Vernalizationprogress _Vernalizationprogress;
        Ismomentregistredzc_39 _Ismomentregistredzc_39;
        Cumulttfrom _Cumulttfrom;
        Updatecalendar _Updatecalendar;
        Registerzadok _Registerzadok;
        Ptq _Ptq;
        Gaimean _Gaimean;

};
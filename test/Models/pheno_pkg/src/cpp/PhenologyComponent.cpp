#include "PhenologyComponent.h"

    PhenologyComponent::PhenologyComponent()
    {
           
    }
    

float PhenologyComponent::getaMXLFNO() {return this-> aMXLFNO; }
float PhenologyComponent::getpNini() {return this-> pNini; }
float PhenologyComponent::getsDsa_sh() {return this-> sDsa_sh; }
float PhenologyComponent::getlatitude() {return this-> latitude; }
float PhenologyComponent::getkl() {return this-> kl; }
float PhenologyComponent::getlincr() {return this-> lincr; }
float PhenologyComponent::getldecr() {return this-> ldecr; }
float PhenologyComponent::getpincr() {return this-> pincr; }
float PhenologyComponent::getpTQhf() {return this-> pTQhf; }
float PhenologyComponent::getB() {return this-> B; }
float PhenologyComponent::getareaSL() {return this-> areaSL; }
float PhenologyComponent::getareaSS() {return this-> areaSS; }
float PhenologyComponent::getlARmin() {return this-> lARmin; }
float PhenologyComponent::getsowingDensity() {return this-> sowingDensity; }
float PhenologyComponent::getlARmax() {return this-> lARmax; }
float PhenologyComponent::getlNeff() {return this-> lNeff; }
float PhenologyComponent::getrp() {return this-> rp; }
float PhenologyComponent::getp() {return this-> p; }
float PhenologyComponent::getpdecr() {return this-> pdecr; }
float PhenologyComponent::getmaxTvern() {return this-> maxTvern; }
float PhenologyComponent::gettTWindowForPTQ() {return this-> tTWindowForPTQ; }
float PhenologyComponent::getvBEE() {return this-> vBEE; }
int PhenologyComponent::getisVernalizable() {return this-> isVernalizable; }
float PhenologyComponent::getminTvern() {return this-> minTvern; }
float PhenologyComponent::getintTvern() {return this-> intTvern; }
float PhenologyComponent::getvAI() {return this-> vAI; }
float PhenologyComponent::getmaxDL() {return this-> maxDL; }
string PhenologyComponent::getchoosePhyllUse() {return this-> choosePhyllUse; }
float PhenologyComponent::getminDL() {return this-> minDL; }
float PhenologyComponent::getpFLLAnth() {return this-> pFLLAnth; }
float PhenologyComponent::getdcd() {return this-> dcd; }
float PhenologyComponent::getdgf() {return this-> dgf; }
float PhenologyComponent::getdegfm() {return this-> degfm; }
bool PhenologyComponent::getignoreGrainMaturation() {return this-> ignoreGrainMaturation; }
float PhenologyComponent::getpHEADANTH() {return this-> pHEADANTH; }
float PhenologyComponent::getsLDL() {return this-> sLDL; }
int PhenologyComponent::getsowingDay() {return this-> sowingDay; }
string PhenologyComponent::getsowingDate() {return this-> sowingDate; }
int PhenologyComponent::getsDws() {return this-> sDws; }
float PhenologyComponent::getsDsa_nh() {return this-> sDsa_nh; }
float PhenologyComponent::getder() {return this-> der; }
float PhenologyComponent::gettargetFertileShoot() {return this-> targetFertileShoot; }
float PhenologyComponent::getdse() {return this-> dse; }
float PhenologyComponent::getslopeTSFLN() {return this-> slopeTSFLN; }
float PhenologyComponent::getintTSFLN() {return this-> intTSFLN; }

void PhenologyComponent::setaMXLFNO(float _aMXLFNO)
{
    _Vernalizationprogress.setaMXLFNO(_aMXLFNO);
}
void PhenologyComponent::setpNini(float _pNini)
{
    _Vernalizationprogress.setpNini(_pNini);
}
void PhenologyComponent::setsDsa_sh(float _sDsa_sh)
{
    _Phylsowingdatecorrection.setsDsa_sh(_sDsa_sh);
}
void PhenologyComponent::setlatitude(float _latitude)
{
    _Phylsowingdatecorrection.setlatitude(_latitude);
}
void PhenologyComponent::setkl(float _kl)
{
    _Phyllochron.setkl(_kl);
    _Ptq.setkl(_kl);
}
void PhenologyComponent::setlincr(float _lincr)
{
    _Phyllochron.setlincr(_lincr);
}
void PhenologyComponent::setldecr(float _ldecr)
{
    _Phyllochron.setldecr(_ldecr);
}
void PhenologyComponent::setpincr(float _pincr)
{
    _Phyllochron.setpincr(_pincr);
}
void PhenologyComponent::setpTQhf(float _pTQhf)
{
    _Phyllochron.setpTQhf(_pTQhf);
}
void PhenologyComponent::setB(float _B)
{
    _Phyllochron.setB(_B);
}
void PhenologyComponent::setareaSL(float _areaSL)
{
    _Phyllochron.setareaSL(_areaSL);
}
void PhenologyComponent::setareaSS(float _areaSS)
{
    _Phyllochron.setareaSS(_areaSS);
}
void PhenologyComponent::setlARmin(float _lARmin)
{
    _Phyllochron.setlARmin(_lARmin);
}
void PhenologyComponent::setsowingDensity(float _sowingDensity)
{
    _Phyllochron.setsowingDensity(_sowingDensity);
    _Shootnumber.setsowingDensity(_sowingDensity);
}
void PhenologyComponent::setlARmax(float _lARmax)
{
    _Phyllochron.setlARmax(_lARmax);
}
void PhenologyComponent::setlNeff(float _lNeff)
{
    _Phyllochron.setlNeff(_lNeff);
}
void PhenologyComponent::setrp(float _rp)
{
    _Phylsowingdatecorrection.setrp(_rp);
}
void PhenologyComponent::setp(float _p)
{
    _Phyllochron.setp(_p);
    _Phylsowingdatecorrection.setp(_p);
    _Updatephase.setp(_p);
}
void PhenologyComponent::setpdecr(float _pdecr)
{
    _Phyllochron.setpdecr(_pdecr);
}
void PhenologyComponent::setmaxTvern(float _maxTvern)
{
    _Vernalizationprogress.setmaxTvern(_maxTvern);
}
void PhenologyComponent::settTWindowForPTQ(float _tTWindowForPTQ)
{
    _Gaimean.settTWindowForPTQ(_tTWindowForPTQ);
    _Ptq.settTWindowForPTQ(_tTWindowForPTQ);
}
void PhenologyComponent::setvBEE(float _vBEE)
{
    _Vernalizationprogress.setvBEE(_vBEE);
}
void PhenologyComponent::setisVernalizable(int _isVernalizable)
{
    _Vernalizationprogress.setisVernalizable(_isVernalizable);
    _Updatephase.setisVernalizable(_isVernalizable);
}
void PhenologyComponent::setminTvern(float _minTvern)
{
    _Vernalizationprogress.setminTvern(_minTvern);
}
void PhenologyComponent::setintTvern(float _intTvern)
{
    _Vernalizationprogress.setintTvern(_intTvern);
}
void PhenologyComponent::setvAI(float _vAI)
{
    _Vernalizationprogress.setvAI(_vAI);
}
void PhenologyComponent::setmaxDL(float _maxDL)
{
    _Vernalizationprogress.setmaxDL(_maxDL);
    _Updatephase.setmaxDL(_maxDL);
}
void PhenologyComponent::setchoosePhyllUse(string _choosePhyllUse)
{
    _Phyllochron.setchoosePhyllUse(_choosePhyllUse);
    _Updatephase.setchoosePhyllUse(_choosePhyllUse);
}
void PhenologyComponent::setminDL(float _minDL)
{
    _Vernalizationprogress.setminDL(_minDL);
}
void PhenologyComponent::setpFLLAnth(float _pFLLAnth)
{
    _Updatephase.setpFLLAnth(_pFLLAnth);
}
void PhenologyComponent::setdcd(float _dcd)
{
    _Updatephase.setdcd(_dcd);
}
void PhenologyComponent::setdgf(float _dgf)
{
    _Updatephase.setdgf(_dgf);
}
void PhenologyComponent::setdegfm(float _degfm)
{
    _Updatephase.setdegfm(_degfm);
}
void PhenologyComponent::setignoreGrainMaturation(bool _ignoreGrainMaturation)
{
    _Updatephase.setignoreGrainMaturation(_ignoreGrainMaturation);
}
void PhenologyComponent::setpHEADANTH(float _pHEADANTH)
{
    _Updatephase.setpHEADANTH(_pHEADANTH);
}
void PhenologyComponent::setsLDL(float _sLDL)
{
    _Updatephase.setsLDL(_sLDL);
}
void PhenologyComponent::setsowingDay(int _sowingDay)
{
    _Phylsowingdatecorrection.setsowingDay(_sowingDay);
}
void PhenologyComponent::setsowingDate(string _sowingDate)
{
    _Registerzadok.setsowingDate(_sowingDate);
}
void PhenologyComponent::setsDws(int _sDws)
{
    _Phylsowingdatecorrection.setsDws(_sDws);
}
void PhenologyComponent::setsDsa_nh(float _sDsa_nh)
{
    _Phylsowingdatecorrection.setsDsa_nh(_sDsa_nh);
}
void PhenologyComponent::setder(float _der)
{
    _Registerzadok.setder(_der);
}
void PhenologyComponent::settargetFertileShoot(float _targetFertileShoot)
{
    _Shootnumber.settargetFertileShoot(_targetFertileShoot);
}
void PhenologyComponent::setdse(float _dse)
{
    _Updatephase.setdse(_dse);
}
void PhenologyComponent::setslopeTSFLN(float _slopeTSFLN)
{
    _Registerzadok.setslopeTSFLN(_slopeTSFLN);
}
void PhenologyComponent::setintTSFLN(float _intTSFLN)
{
    _Registerzadok.setintTSFLN(_intTSFLN);
}
void PhenologyComponent::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
{
    _Gaimean.Calculate_Model(s, s1, r, a);
    _Ptq.Calculate_Model(s, s1, r, a);
    _Cumulttfrom.Calculate_Model(s, s1, r, a);
    _Ismomentregistredzc_39.Calculate_Model(s, s1, r, a);
    _Vernalizationprogress.Calculate_Model(s, s1, r, a);
    _Phylsowingdatecorrection.Calculate_Model(s, s1, r, a);
    _Updatephase.Calculate_Model(s, s1, r, a);
    _Leafnumber.Calculate_Model(s, s1, r, a);
    _Shootnumber.Calculate_Model(s, s1, r, a);
    _Updateleafflag.Calculate_Model(s, s1, r, a);
    _Registerzadok.Calculate_Model(s, s1, r, a);
    _Updatecalendar.Calculate_Model(s, s1, r, a);
    _Phyllochron.Calculate_Model(s, s1, r, a);
}
PhenologyComponent::PhenologyComponent(const PhenologyComponent& toCopy)
{
    aMXLFNO = toCopy.aMXLFNO;
    pNini = toCopy.pNini;
    sDsa_sh = toCopy.sDsa_sh;
    latitude = toCopy.latitude;
    kl = toCopy.kl;
    lincr = toCopy.lincr;
    ldecr = toCopy.ldecr;
    pincr = toCopy.pincr;
    pTQhf = toCopy.pTQhf;
    B = toCopy.B;
    areaSL = toCopy.areaSL;
    areaSS = toCopy.areaSS;
    lARmin = toCopy.lARmin;
    sowingDensity = toCopy.sowingDensity;
    lARmax = toCopy.lARmax;
    lNeff = toCopy.lNeff;
    rp = toCopy.rp;
    p = toCopy.p;
    pdecr = toCopy.pdecr;
    maxTvern = toCopy.maxTvern;
    tTWindowForPTQ = toCopy.tTWindowForPTQ;
    vBEE = toCopy.vBEE;
    isVernalizable = toCopy.isVernalizable;
    minTvern = toCopy.minTvern;
    intTvern = toCopy.intTvern;
    vAI = toCopy.vAI;
    maxDL = toCopy.maxDL;
    choosePhyllUse = toCopy.choosePhyllUse;
    minDL = toCopy.minDL;
    pFLLAnth = toCopy.pFLLAnth;
    dcd = toCopy.dcd;
    dgf = toCopy.dgf;
    degfm = toCopy.degfm;
    ignoreGrainMaturation = toCopy.ignoreGrainMaturation;
    pHEADANTH = toCopy.pHEADANTH;
    sLDL = toCopy.sLDL;
    sowingDay = toCopy.sowingDay;
    sowingDate = toCopy.sowingDate;
    sDws = toCopy.sDws;
    sDsa_nh = toCopy.sDsa_nh;
    der = toCopy.der;
    targetFertileShoot = toCopy.targetFertileShoot;
    dse = toCopy.dse;
    slopeTSFLN = toCopy.slopeTSFLN;
    intTSFLN = toCopy.intTSFLN;
}


void PhenologyComponent::Init(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
{
    s.calendarMoments.push_back("Sowing");
    s.calendarCumuls.push_back(0.0f);
    s.calendarDates.push_back(sowingDate);
    s.minFinalNumber = 5.5f;
}

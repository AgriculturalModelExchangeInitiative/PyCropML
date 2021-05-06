#include "PhenologyComponent.h"

    PhenologyComponent::PhenologyComponent()
    {
           
    }
    

double PhenologyComponent::getaMXLFNO() {return this-> aMXLFNO; }
double PhenologyComponent::getpNini() {return this-> pNini; }
double PhenologyComponent::getsDsa_sh() {return this-> sDsa_sh; }
double PhenologyComponent::getlatitude() {return this-> latitude; }
double PhenologyComponent::getkl() {return this-> kl; }
double PhenologyComponent::getlincr() {return this-> lincr; }
double PhenologyComponent::getldecr() {return this-> ldecr; }
double PhenologyComponent::getpincr() {return this-> pincr; }
double PhenologyComponent::getpTQhf() {return this-> pTQhf; }
double PhenologyComponent::getB() {return this-> B; }
double PhenologyComponent::getareaSL() {return this-> areaSL; }
double PhenologyComponent::getareaSS() {return this-> areaSS; }
double PhenologyComponent::getlARmin() {return this-> lARmin; }
double PhenologyComponent::getsowingDensity() {return this-> sowingDensity; }
double PhenologyComponent::getlARmax() {return this-> lARmax; }
double PhenologyComponent::getlNeff() {return this-> lNeff; }
double PhenologyComponent::getrp() {return this-> rp; }
double PhenologyComponent::getp() {return this-> p; }
double PhenologyComponent::getpdecr() {return this-> pdecr; }
double PhenologyComponent::getmaxTvern() {return this-> maxTvern; }
double PhenologyComponent::gettTWindowForPTQ() {return this-> tTWindowForPTQ; }
double PhenologyComponent::getvBEE() {return this-> vBEE; }
int PhenologyComponent::getisVernalizable() {return this-> isVernalizable; }
double PhenologyComponent::getminTvern() {return this-> minTvern; }
double PhenologyComponent::getintTvern() {return this-> intTvern; }
double PhenologyComponent::getvAI() {return this-> vAI; }
double PhenologyComponent::getmaxDL() {return this-> maxDL; }
string PhenologyComponent::getchoosePhyllUse() {return this-> choosePhyllUse; }
double PhenologyComponent::getminDL() {return this-> minDL; }
double PhenologyComponent::getpFLLAnth() {return this-> pFLLAnth; }
double PhenologyComponent::getdcd() {return this-> dcd; }
double PhenologyComponent::getdgf() {return this-> dgf; }
double PhenologyComponent::getdegfm() {return this-> degfm; }
bool PhenologyComponent::getignoreGrainMaturation() {return this-> ignoreGrainMaturation; }
double PhenologyComponent::getpHEADANTH() {return this-> pHEADANTH; }
double PhenologyComponent::getsLDL() {return this-> sLDL; }
int PhenologyComponent::getsowingDay() {return this-> sowingDay; }
string PhenologyComponent::getsowingDate() {return this-> sowingDate; }
int PhenologyComponent::getsDws() {return this-> sDws; }
double PhenologyComponent::getsDsa_nh() {return this-> sDsa_nh; }
double PhenologyComponent::getder() {return this-> der; }
double PhenologyComponent::gettargetFertileShoot() {return this-> targetFertileShoot; }
double PhenologyComponent::getdse() {return this-> dse; }
double PhenologyComponent::getslopeTSFLN() {return this-> slopeTSFLN; }
double PhenologyComponent::getintTSFLN() {return this-> intTSFLN; }

void PhenologyComponent::setaMXLFNO(double _aMXLFNO)
{
    _Vernalizationprogress.setaMXLFNO(_aMXLFNO);
}
void PhenologyComponent::setpNini(double _pNini)
{
    _Vernalizationprogress.setpNini(_pNini);
}
void PhenologyComponent::setsDsa_sh(double _sDsa_sh)
{
    _Phylsowingdatecorrection.setsDsa_sh(_sDsa_sh);
}
void PhenologyComponent::setlatitude(double _latitude)
{
    _Phylsowingdatecorrection.setlatitude(_latitude);
}
void PhenologyComponent::setkl(double _kl)
{
    _Phyllochron.setkl(_kl);
    _Ptq.setkl(_kl);
}
void PhenologyComponent::setlincr(double _lincr)
{
    _Phyllochron.setlincr(_lincr);
}
void PhenologyComponent::setldecr(double _ldecr)
{
    _Phyllochron.setldecr(_ldecr);
}
void PhenologyComponent::setpincr(double _pincr)
{
    _Phyllochron.setpincr(_pincr);
}
void PhenologyComponent::setpTQhf(double _pTQhf)
{
    _Phyllochron.setpTQhf(_pTQhf);
}
void PhenologyComponent::setB(double _B)
{
    _Phyllochron.setB(_B);
}
void PhenologyComponent::setareaSL(double _areaSL)
{
    _Phyllochron.setareaSL(_areaSL);
}
void PhenologyComponent::setareaSS(double _areaSS)
{
    _Phyllochron.setareaSS(_areaSS);
}
void PhenologyComponent::setlARmin(double _lARmin)
{
    _Phyllochron.setlARmin(_lARmin);
}
void PhenologyComponent::setsowingDensity(double _sowingDensity)
{
    _Phyllochron.setsowingDensity(_sowingDensity);
    _Shootnumber.setsowingDensity(_sowingDensity);
}
void PhenologyComponent::setlARmax(double _lARmax)
{
    _Phyllochron.setlARmax(_lARmax);
}
void PhenologyComponent::setlNeff(double _lNeff)
{
    _Phyllochron.setlNeff(_lNeff);
}
void PhenologyComponent::setrp(double _rp)
{
    _Phylsowingdatecorrection.setrp(_rp);
}
void PhenologyComponent::setp(double _p)
{
    _Phyllochron.setp(_p);
    _Phylsowingdatecorrection.setp(_p);
    _Updatephase.setp(_p);
}
void PhenologyComponent::setpdecr(double _pdecr)
{
    _Phyllochron.setpdecr(_pdecr);
}
void PhenologyComponent::setmaxTvern(double _maxTvern)
{
    _Vernalizationprogress.setmaxTvern(_maxTvern);
}
void PhenologyComponent::settTWindowForPTQ(double _tTWindowForPTQ)
{
    _Gaimean.settTWindowForPTQ(_tTWindowForPTQ);
    _Ptq.settTWindowForPTQ(_tTWindowForPTQ);
}
void PhenologyComponent::setvBEE(double _vBEE)
{
    _Vernalizationprogress.setvBEE(_vBEE);
}
void PhenologyComponent::setisVernalizable(int _isVernalizable)
{
    _Vernalizationprogress.setisVernalizable(_isVernalizable);
    _Updatephase.setisVernalizable(_isVernalizable);
}
void PhenologyComponent::setminTvern(double _minTvern)
{
    _Vernalizationprogress.setminTvern(_minTvern);
}
void PhenologyComponent::setintTvern(double _intTvern)
{
    _Vernalizationprogress.setintTvern(_intTvern);
}
void PhenologyComponent::setvAI(double _vAI)
{
    _Vernalizationprogress.setvAI(_vAI);
}
void PhenologyComponent::setmaxDL(double _maxDL)
{
    _Vernalizationprogress.setmaxDL(_maxDL);
    _Updatephase.setmaxDL(_maxDL);
}
void PhenologyComponent::setchoosePhyllUse(string _choosePhyllUse)
{
    _Phyllochron.setchoosePhyllUse(_choosePhyllUse);
    _Updatephase.setchoosePhyllUse(_choosePhyllUse);
}
void PhenologyComponent::setminDL(double _minDL)
{
    _Vernalizationprogress.setminDL(_minDL);
}
void PhenologyComponent::setpFLLAnth(double _pFLLAnth)
{
    _Updatephase.setpFLLAnth(_pFLLAnth);
}
void PhenologyComponent::setdcd(double _dcd)
{
    _Updatephase.setdcd(_dcd);
}
void PhenologyComponent::setdgf(double _dgf)
{
    _Updatephase.setdgf(_dgf);
}
void PhenologyComponent::setdegfm(double _degfm)
{
    _Updatephase.setdegfm(_degfm);
}
void PhenologyComponent::setignoreGrainMaturation(bool _ignoreGrainMaturation)
{
    _Updatephase.setignoreGrainMaturation(_ignoreGrainMaturation);
}
void PhenologyComponent::setpHEADANTH(double _pHEADANTH)
{
    _Updatephase.setpHEADANTH(_pHEADANTH);
}
void PhenologyComponent::setsLDL(double _sLDL)
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
void PhenologyComponent::setsDsa_nh(double _sDsa_nh)
{
    _Phylsowingdatecorrection.setsDsa_nh(_sDsa_nh);
}
void PhenologyComponent::setder(double _der)
{
    _Registerzadok.setder(_der);
}
void PhenologyComponent::settargetFertileShoot(double _targetFertileShoot)
{
    _Shootnumber.settargetFertileShoot(_targetFertileShoot);
}
void PhenologyComponent::setdse(double _dse)
{
    _Updatephase.setdse(_dse);
}
void PhenologyComponent::setslopeTSFLN(double _slopeTSFLN)
{
    _Registerzadok.setslopeTSFLN(_slopeTSFLN);
}
void PhenologyComponent::setintTSFLN(double _intTSFLN)
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
    s.calendarCumuls.push_back(0.0d);
    s.calendarDates.push_back(sowingDate);
    s.minFinalNumber = 5.5d;
}

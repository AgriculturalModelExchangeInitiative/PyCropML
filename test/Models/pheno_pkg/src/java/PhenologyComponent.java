public class PhenologyComponent
{
    
    public PhenologyComponent() { }

    Phyllochron _Phyllochron = new Phyllochron();
    Phylsowingdatecorrection _Phylsowingdatecorrection = new Phylsowingdatecorrection();
    Shootnumber _Shootnumber = new Shootnumber();
    Updateleafflag _Updateleafflag = new Updateleafflag();
    Updatephase _Updatephase = new Updatephase();
    Leafnumber _Leafnumber = new Leafnumber();
    Vernalizationprogress _Vernalizationprogress = new Vernalizationprogress();
    Ismomentregistredzc_39 _Ismomentregistredzc_39 = new Ismomentregistredzc_39();
    Cumulttfrom _Cumulttfrom = new Cumulttfrom();
    Updatecalendar _Updatecalendar = new Updatecalendar();
    Registerzadok _Registerzadok = new Registerzadok();
    Ptq _Ptq = new Ptq();
    Gaimean _Gaimean = new Gaimean();

    public double getaMXLFNO()
    { return _Vernalizationprogress.getaMXLFNO(); }
    public void setaMXLFNO(double aMXLFNO)
    { _Vernalizationprogress.setaMXLFNO(aMXLFNO); } 

    public double getpNini()
    { return _Vernalizationprogress.getpNini(); }
    public void setpNini(double pNini)
    { _Vernalizationprogress.setpNini(pNini); } 

    public double getsDsa_sh()
    { return _Phylsowingdatecorrection.getsDsa_sh(); }
    public void setsDsa_sh(double sDsa_sh)
    { _Phylsowingdatecorrection.setsDsa_sh(sDsa_sh); } 

    public double getlatitude()
    { return _Phylsowingdatecorrection.getlatitude(); }
    public void setlatitude(double latitude)
    { _Phylsowingdatecorrection.setlatitude(latitude); } 

    public double getkl()
    { return _Phyllochron.getkl(); }
    public void setkl(double kl)
    { _Phyllochron.setkl(kl);
        _Ptq.setkl(kl); } 

    public double getlincr()
    { return _Phyllochron.getlincr(); }
    public void setlincr(double lincr)
    { _Phyllochron.setlincr(lincr); } 

    public double getldecr()
    { return _Phyllochron.getldecr(); }
    public void setldecr(double ldecr)
    { _Phyllochron.setldecr(ldecr); } 

    public double getpincr()
    { return _Phyllochron.getpincr(); }
    public void setpincr(double pincr)
    { _Phyllochron.setpincr(pincr); } 

    public double getpTQhf()
    { return _Phyllochron.getpTQhf(); }
    public void setpTQhf(double pTQhf)
    { _Phyllochron.setpTQhf(pTQhf); } 

    public double getB()
    { return _Phyllochron.getB(); }
    public void setB(double B)
    { _Phyllochron.setB(B); } 

    public double getareaSL()
    { return _Phyllochron.getareaSL(); }
    public void setareaSL(double areaSL)
    { _Phyllochron.setareaSL(areaSL); } 

    public double getareaSS()
    { return _Phyllochron.getareaSS(); }
    public void setareaSS(double areaSS)
    { _Phyllochron.setareaSS(areaSS); } 

    public double getlARmin()
    { return _Phyllochron.getlARmin(); }
    public void setlARmin(double lARmin)
    { _Phyllochron.setlARmin(lARmin); } 

    public double getsowingDensity()
    { return _Phyllochron.getsowingDensity(); }
    public void setsowingDensity(double sowingDensity)
    { _Phyllochron.setsowingDensity(sowingDensity);
        _Shootnumber.setsowingDensity(sowingDensity); } 

    public double getlARmax()
    { return _Phyllochron.getlARmax(); }
    public void setlARmax(double lARmax)
    { _Phyllochron.setlARmax(lARmax); } 

    public double getlNeff()
    { return _Phyllochron.getlNeff(); }
    public void setlNeff(double lNeff)
    { _Phyllochron.setlNeff(lNeff); } 

    public double getrp()
    { return _Phylsowingdatecorrection.getrp(); }
    public void setrp(double rp)
    { _Phylsowingdatecorrection.setrp(rp); } 

    public double getp()
    { return _Phyllochron.getp(); }
    public void setp(double p)
    { _Phyllochron.setp(p);
        _Phylsowingdatecorrection.setp(p);
        _Updatephase.setp(p); } 

    public double getpdecr()
    { return _Phyllochron.getpdecr(); }
    public void setpdecr(double pdecr)
    { _Phyllochron.setpdecr(pdecr); } 

    public double getmaxTvern()
    { return _Vernalizationprogress.getmaxTvern(); }
    public void setmaxTvern(double maxTvern)
    { _Vernalizationprogress.setmaxTvern(maxTvern); } 

    public double gettTWindowForPTQ()
    { return _Gaimean.gettTWindowForPTQ(); }
    public void settTWindowForPTQ(double tTWindowForPTQ)
    { _Gaimean.settTWindowForPTQ(tTWindowForPTQ);
        _Ptq.settTWindowForPTQ(tTWindowForPTQ); } 

    public double getvBEE()
    { return _Vernalizationprogress.getvBEE(); }
    public void setvBEE(double vBEE)
    { _Vernalizationprogress.setvBEE(vBEE); } 

    public int getisVernalizable()
    { return _Vernalizationprogress.getisVernalizable(); }
    public void setisVernalizable(int isVernalizable)
    { _Vernalizationprogress.setisVernalizable(isVernalizable);
        _Updatephase.setisVernalizable(isVernalizable); } 

    public double getminTvern()
    { return _Vernalizationprogress.getminTvern(); }
    public void setminTvern(double minTvern)
    { _Vernalizationprogress.setminTvern(minTvern); } 

    public double getintTvern()
    { return _Vernalizationprogress.getintTvern(); }
    public void setintTvern(double intTvern)
    { _Vernalizationprogress.setintTvern(intTvern); } 

    public double getvAI()
    { return _Vernalizationprogress.getvAI(); }
    public void setvAI(double vAI)
    { _Vernalizationprogress.setvAI(vAI); } 

    public double getmaxDL()
    { return _Vernalizationprogress.getmaxDL(); }
    public void setmaxDL(double maxDL)
    { _Vernalizationprogress.setmaxDL(maxDL);
        _Updatephase.setmaxDL(maxDL); } 

    public String getchoosePhyllUse()
    { return _Phyllochron.getchoosePhyllUse(); }
    public void setchoosePhyllUse(String choosePhyllUse)
    { _Phyllochron.setchoosePhyllUse(choosePhyllUse);
        _Updatephase.setchoosePhyllUse(choosePhyllUse); } 

    public double getminDL()
    { return _Vernalizationprogress.getminDL(); }
    public void setminDL(double minDL)
    { _Vernalizationprogress.setminDL(minDL); } 

    public double getpFLLAnth()
    { return _Updatephase.getpFLLAnth(); }
    public void setpFLLAnth(double pFLLAnth)
    { _Updatephase.setpFLLAnth(pFLLAnth); } 

    public double getdcd()
    { return _Updatephase.getdcd(); }
    public void setdcd(double dcd)
    { _Updatephase.setdcd(dcd); } 

    public double getdgf()
    { return _Updatephase.getdgf(); }
    public void setdgf(double dgf)
    { _Updatephase.setdgf(dgf); } 

    public double getdegfm()
    { return _Updatephase.getdegfm(); }
    public void setdegfm(double degfm)
    { _Updatephase.setdegfm(degfm); } 

    public boolean getignoreGrainMaturation()
    { return _Updatephase.getignoreGrainMaturation(); }
    public void setignoreGrainMaturation(boolean ignoreGrainMaturation)
    { _Updatephase.setignoreGrainMaturation(ignoreGrainMaturation); } 

    public double getpHEADANTH()
    { return _Updatephase.getpHEADANTH(); }
    public void setpHEADANTH(double pHEADANTH)
    { _Updatephase.setpHEADANTH(pHEADANTH); } 

    public double getsLDL()
    { return _Updatephase.getsLDL(); }
    public void setsLDL(double sLDL)
    { _Updatephase.setsLDL(sLDL); } 

    public int getsowingDay()
    { return _Phylsowingdatecorrection.getsowingDay(); }
    public void setsowingDay(int sowingDay)
    { _Phylsowingdatecorrection.setsowingDay(sowingDay); } 

    public LocalDateTime getsowingDate()
    { return _Registerzadok.getsowingDate(); }
    public void setsowingDate(LocalDateTime sowingDate)
    { _Registerzadok.setsowingDate(sowingDate); } 

    public int getsDws()
    { return _Phylsowingdatecorrection.getsDws(); }
    public void setsDws(int sDws)
    { _Phylsowingdatecorrection.setsDws(sDws); } 

    public double getsDsa_nh()
    { return _Phylsowingdatecorrection.getsDsa_nh(); }
    public void setsDsa_nh(double sDsa_nh)
    { _Phylsowingdatecorrection.setsDsa_nh(sDsa_nh); } 

    public double getder()
    { return _Registerzadok.getder(); }
    public void setder(double der)
    { _Registerzadok.setder(der); } 

    public double gettargetFertileShoot()
    { return _Shootnumber.gettargetFertileShoot(); }
    public void settargetFertileShoot(double targetFertileShoot)
    { _Shootnumber.settargetFertileShoot(targetFertileShoot); } 

    public double getdse()
    { return _Updatephase.getdse(); }
    public void setdse(double dse)
    { _Updatephase.setdse(dse); } 

    public double getslopeTSFLN()
    { return _Registerzadok.getslopeTSFLN(); }
    public void setslopeTSFLN(double slopeTSFLN)
    { _Registerzadok.setslopeTSFLN(slopeTSFLN); } 

    public double getintTSFLN()
    { return _Registerzadok.getintTSFLN(); }
    public void setintTSFLN(double intTSFLN)
    { _Registerzadok.setintTSFLN(intTSFLN); } 
    public void  Calculate_phenology(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        _Gaimean.Calculate_gaimean(s, s1, r, a);
        _Ptq.Calculate_ptq(s, s1, r, a);
        _Cumulttfrom.Calculate_cumulttfrom(s, s1, r, a);
        _Ismomentregistredzc_39.Calculate_ismomentregistredzc_39(s, s1, r, a);
        _Vernalizationprogress.Calculate_vernalizationprogress(s, s1, r, a);
        _Phylsowingdatecorrection.Calculate_phylsowingdatecorrection(s, s1, r, a);
        _Updatephase.Calculate_updatephase(s, s1, r, a);
        _Leafnumber.Calculate_leafnumber(s, s1, r, a);
        _Shootnumber.Calculate_shootnumber(s, s1, r, a);
        _Updateleafflag.Calculate_updateleafflag(s, s1, r, a);
        _Registerzadok.Calculate_registerzadok(s, s1, r, a);
        _Updatecalendar.Calculate_updatecalendar(s, s1, r, a);
        _Phyllochron.Calculate_phyllochron(s, s1, r, a);
    }
    private double aMXLFNO;
    private double pNini;
    private double sDsa_sh;
    private double latitude;
    private double kl;
    private double lincr;
    private double ldecr;
    private double pincr;
    private double pTQhf;
    private double B;
    private double areaSL;
    private double areaSS;
    private double lARmin;
    private double sowingDensity;
    private double lARmax;
    private double lNeff;
    private double rp;
    private double p;
    private double pdecr;
    private double maxTvern;
    private double tTWindowForPTQ;
    private double vBEE;
    private int isVernalizable;
    private double minTvern;
    private double intTvern;
    private double vAI;
    private double maxDL;
    private String choosePhyllUse;
    private double minDL;
    private double pFLLAnth;
    private double dcd;
    private double dgf;
    private double degfm;
    private boolean ignoreGrainMaturation;
    private double pHEADANTH;
    private double sLDL;
    private int sowingDay;
    private LocalDateTime sowingDate;
    private int sDws;
    private double sDsa_nh;
    private double der;
    private double targetFertileShoot;
    private double dse;
    private double slopeTSFLN;
    private double intTSFLN;
    public PhenologyComponent(PhenologyComponent toCopy) // copy constructor 
    {
        this.aMXLFNO = toCopy.getaMXLFNO();
        this.pNini = toCopy.getpNini();
        this.sDsa_sh = toCopy.getsDsa_sh();
        this.latitude = toCopy.getlatitude();
        this.kl = toCopy.getkl();
        this.lincr = toCopy.getlincr();
        this.ldecr = toCopy.getldecr();
        this.pincr = toCopy.getpincr();
        this.pTQhf = toCopy.getpTQhf();
        this.B = toCopy.getB();
        this.areaSL = toCopy.getareaSL();
        this.areaSS = toCopy.getareaSS();
        this.lARmin = toCopy.getlARmin();
        this.sowingDensity = toCopy.getsowingDensity();
        this.lARmax = toCopy.getlARmax();
        this.lNeff = toCopy.getlNeff();
        this.rp = toCopy.getrp();
        this.p = toCopy.getp();
        this.pdecr = toCopy.getpdecr();
        this.maxTvern = toCopy.getmaxTvern();
        this.tTWindowForPTQ = toCopy.gettTWindowForPTQ();
        this.vBEE = toCopy.getvBEE();
        this.isVernalizable = toCopy.getisVernalizable();
        this.minTvern = toCopy.getminTvern();
        this.intTvern = toCopy.getintTvern();
        this.vAI = toCopy.getvAI();
        this.maxDL = toCopy.getmaxDL();
        this.choosePhyllUse = toCopy.getchoosePhyllUse();
        this.minDL = toCopy.getminDL();
        this.pFLLAnth = toCopy.getpFLLAnth();
        this.dcd = toCopy.getdcd();
        this.dgf = toCopy.getdgf();
        this.degfm = toCopy.getdegfm();
        this.ignoreGrainMaturation = toCopy.getignoreGrainMaturation();
        this.pHEADANTH = toCopy.getpHEADANTH();
        this.sLDL = toCopy.getsLDL();
        this.sowingDay = toCopy.getsowingDay();
        this.sowingDate = toCopy.getsowingDate();
        this.sDws = toCopy.getsDws();
        this.sDsa_nh = toCopy.getsDsa_nh();
        this.der = toCopy.getder();
        this.targetFertileShoot = toCopy.gettargetFertileShoot();
        this.dse = toCopy.getdse();
        this.slopeTSFLN = toCopy.getslopeTSFLN();
        this.intTSFLN = toCopy.getintTSFLN();

    }
    

    

    public void Init(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        calendarMoments.add("Sowing");
        calendarCumuls.add(0.0d);
        calendarDates.add(sowingDate);
        minFinalNumber = 5.5d;
    }
    
}
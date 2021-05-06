using System;
using System.Collections.Generic;
using System.Linq;
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

    public double aMXLFNO
    {
        get
        { return _Vernalizationprogress.aMXLFNO; }
        set
        { _Vernalizationprogress.aMXLFNO = value; } 
    }
    
    public double pNini
    {
        get
        { return _Vernalizationprogress.pNini; }
        set
        { _Vernalizationprogress.pNini = value; } 
    }
    
    public double sDsa_sh
    {
        get
        { return _Phylsowingdatecorrection.sDsa_sh; }
        set
        { _Phylsowingdatecorrection.sDsa_sh = value; } 
    }
    
    public double latitude
    {
        get
        { return _Phylsowingdatecorrection.latitude; }
        set
        { _Phylsowingdatecorrection.latitude = value; } 
    }
    
    public double kl
    {
        get
        { return _Phyllochron.kl; }
        set
        { _Phyllochron.kl = value;
            _Ptq.kl = value; } 
    }
    
    public double lincr
    {
        get
        { return _Phyllochron.lincr; }
        set
        { _Phyllochron.lincr = value; } 
    }
    
    public double ldecr
    {
        get
        { return _Phyllochron.ldecr; }
        set
        { _Phyllochron.ldecr = value; } 
    }
    
    public double pincr
    {
        get
        { return _Phyllochron.pincr; }
        set
        { _Phyllochron.pincr = value; } 
    }
    
    public double pTQhf
    {
        get
        { return _Phyllochron.pTQhf; }
        set
        { _Phyllochron.pTQhf = value; } 
    }
    
    public double B
    {
        get
        { return _Phyllochron.B; }
        set
        { _Phyllochron.B = value; } 
    }
    
    public double areaSL
    {
        get
        { return _Phyllochron.areaSL; }
        set
        { _Phyllochron.areaSL = value; } 
    }
    
    public double areaSS
    {
        get
        { return _Phyllochron.areaSS; }
        set
        { _Phyllochron.areaSS = value; } 
    }
    
    public double lARmin
    {
        get
        { return _Phyllochron.lARmin; }
        set
        { _Phyllochron.lARmin = value; } 
    }
    
    public double sowingDensity
    {
        get
        { return _Phyllochron.sowingDensity; }
        set
        { _Phyllochron.sowingDensity = value;
            _Shootnumber.sowingDensity = value; } 
    }
    
    public double lARmax
    {
        get
        { return _Phyllochron.lARmax; }
        set
        { _Phyllochron.lARmax = value; } 
    }
    
    public double lNeff
    {
        get
        { return _Phyllochron.lNeff; }
        set
        { _Phyllochron.lNeff = value; } 
    }
    
    public double rp
    {
        get
        { return _Phylsowingdatecorrection.rp; }
        set
        { _Phylsowingdatecorrection.rp = value; } 
    }
    
    public double p
    {
        get
        { return _Phyllochron.p; }
        set
        { _Phyllochron.p = value;
            _Phylsowingdatecorrection.p = value;
            _Updatephase.p = value; } 
    }
    
    public double pdecr
    {
        get
        { return _Phyllochron.pdecr; }
        set
        { _Phyllochron.pdecr = value; } 
    }
    
    public double maxTvern
    {
        get
        { return _Vernalizationprogress.maxTvern; }
        set
        { _Vernalizationprogress.maxTvern = value; } 
    }
    
    public double tTWindowForPTQ
    {
        get
        { return _Gaimean.tTWindowForPTQ; }
        set
        { _Gaimean.tTWindowForPTQ = value;
            _Ptq.tTWindowForPTQ = value; } 
    }
    
    public double vBEE
    {
        get
        { return _Vernalizationprogress.vBEE; }
        set
        { _Vernalizationprogress.vBEE = value; } 
    }
    
    public int isVernalizable
    {
        get
        { return _Vernalizationprogress.isVernalizable; }
        set
        { _Vernalizationprogress.isVernalizable = value;
            _Updatephase.isVernalizable = value; } 
    }
    
    public double minTvern
    {
        get
        { return _Vernalizationprogress.minTvern; }
        set
        { _Vernalizationprogress.minTvern = value; } 
    }
    
    public double intTvern
    {
        get
        { return _Vernalizationprogress.intTvern; }
        set
        { _Vernalizationprogress.intTvern = value; } 
    }
    
    public double vAI
    {
        get
        { return _Vernalizationprogress.vAI; }
        set
        { _Vernalizationprogress.vAI = value; } 
    }
    
    public double maxDL
    {
        get
        { return _Vernalizationprogress.maxDL; }
        set
        { _Vernalizationprogress.maxDL = value;
            _Updatephase.maxDL = value; } 
    }
    
    public string choosePhyllUse
    {
        get
        { return _Phyllochron.choosePhyllUse; }
        set
        { _Phyllochron.choosePhyllUse = value;
            _Updatephase.choosePhyllUse = value; } 
    }
    
    public double minDL
    {
        get
        { return _Vernalizationprogress.minDL; }
        set
        { _Vernalizationprogress.minDL = value; } 
    }
    
    public double pFLLAnth
    {
        get
        { return _Updatephase.pFLLAnth; }
        set
        { _Updatephase.pFLLAnth = value; } 
    }
    
    public double dcd
    {
        get
        { return _Updatephase.dcd; }
        set
        { _Updatephase.dcd = value; } 
    }
    
    public double dgf
    {
        get
        { return _Updatephase.dgf; }
        set
        { _Updatephase.dgf = value; } 
    }
    
    public double degfm
    {
        get
        { return _Updatephase.degfm; }
        set
        { _Updatephase.degfm = value; } 
    }
    
    public bool ignoreGrainMaturation
    {
        get
        { return _Updatephase.ignoreGrainMaturation; }
        set
        { _Updatephase.ignoreGrainMaturation = value; } 
    }
    
    public double pHEADANTH
    {
        get
        { return _Updatephase.pHEADANTH; }
        set
        { _Updatephase.pHEADANTH = value; } 
    }
    
    public double sLDL
    {
        get
        { return _Updatephase.sLDL; }
        set
        { _Updatephase.sLDL = value; } 
    }
    
    public int sowingDay
    {
        get
        { return _Phylsowingdatecorrection.sowingDay; }
        set
        { _Phylsowingdatecorrection.sowingDay = value; } 
    }
    
    public DateTime sowingDate
    {
        get
        { return _Registerzadok.sowingDate; }
        set
        { _Registerzadok.sowingDate = value; } 
    }
    
    public int sDws
    {
        get
        { return _Phylsowingdatecorrection.sDws; }
        set
        { _Phylsowingdatecorrection.sDws = value; } 
    }
    
    public double sDsa_nh
    {
        get
        { return _Phylsowingdatecorrection.sDsa_nh; }
        set
        { _Phylsowingdatecorrection.sDsa_nh = value; } 
    }
    
    public double der
    {
        get
        { return _Registerzadok.der; }
        set
        { _Registerzadok.der = value; } 
    }
    
    public double targetFertileShoot
    {
        get
        { return _Shootnumber.targetFertileShoot; }
        set
        { _Shootnumber.targetFertileShoot = value; } 
    }
    
    public double dse
    {
        get
        { return _Updatephase.dse; }
        set
        { _Updatephase.dse = value; } 
    }
    
    public double slopeTSFLN
    {
        get
        { return _Registerzadok.slopeTSFLN; }
        set
        { _Registerzadok.slopeTSFLN = value; } 
    }
    
    public double intTSFLN
    {
        get
        { return _Registerzadok.intTSFLN; }
        set
        { _Registerzadok.intTSFLN = value; } 
    }
    
    public void  Calculate_phenology(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        _Gaimean.Calculate_gaimean(s,s1, r, a);
        _Ptq.Calculate_ptq(s,s1, r, a);
        _Cumulttfrom.Calculate_cumulttfrom(s,s1, r, a);
        _Ismomentregistredzc_39.Calculate_ismomentregistredzc_39(s,s1, r, a);
        _Vernalizationprogress.Calculate_vernalizationprogress(s,s1, r, a);
        _Phylsowingdatecorrection.Calculate_phylsowingdatecorrection(s,s1, r, a);
        _Updatephase.Calculate_updatephase(s,s1, r, a);
        _Leafnumber.Calculate_leafnumber(s,s1, r, a);
        _Shootnumber.Calculate_shootnumber(s,s1, r, a);
        _Updateleafflag.Calculate_updateleafflag(s,s1, r, a);
        _Registerzadok.Calculate_registerzadok(s,s1, r, a);
        _Updatecalendar.Calculate_updatecalendar(s,s1, r, a);
        _Phyllochron.Calculate_phyllochron(s,s1, r, a);
    }
    
    public PhenologyComponent(PhenologyComponent toCopy): this() // copy constructor 
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
    

    

    public void Init(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        s.calendarMoments.Add("Sowing");
        s.calendarCumuls.Add(0.0d);
        s.calendarDates.Add(sowingDate);
        s.minFinalNumber = 5.5d;
    }
    
}
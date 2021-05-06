public class PhenologyComponent
{
    
    public PhenologyComponent() { }
    

    //Declaration of the associated strategies
    Phyllochron _Phyllochron = new Phyllochron();
    PhylSowingDateCorrection _PhylSowingDateCorrection = new PhylSowingDateCorrection();
    ShootNumber _ShootNumber = new ShootNumber();
    UpdateLeafFlag _UpdateLeafFlag = new UpdateLeafFlag();
    UpdatePhase _UpdatePhase = new UpdatePhase();
    LeafNumber _LeafNumber = new LeafNumber();
    VernalizationProgress _VernalizationProgress = new VernalizationProgress();
    IsMomentRegistredZC_39 _IsMomentRegistredZC_39 = new IsMomentRegistredZC_39();
    CumulTTFrom _CumulTTFrom = new CumulTTFrom();
    UpdateCalendar _UpdateCalendar = new UpdateCalendar();
    RegisterZadok _RegisterZadok = new RegisterZadok();
    PTQ _PTQ = new PTQ();
    GAImean _GAImean = new GAImean();

    public double aMXLFNO
    {
        get
        {
             return _VernalizationProgress.aMXLFNO; 
        }
        set
        {
            _VernalizationProgress.aMXLFNO = value;
        }
    }
    public double pNini
    {
        get
        {
             return _VernalizationProgress.pNini; 
        }
        set
        {
            _VernalizationProgress.pNini = value;
        }
    }
    public double sDsa_sh
    {
        get
        {
             return _PhylSowingDateCorrection.sDsa_sh; 
        }
        set
        {
            _PhylSowingDateCorrection.sDsa_sh = value;
        }
    }
    public double latitude
    {
        get
        {
             return _PhylSowingDateCorrection.latitude; 
        }
        set
        {
            _PhylSowingDateCorrection.latitude = value;
        }
    }
    public double kl
    {
        get
        {
             return _Phyllochron.kl; 
        }
        set
        {
            _Phyllochron.kl = value;
            _PTQ.kl = value;
        }
    }
    public double lincr
    {
        get
        {
             return _Phyllochron.lincr; 
        }
        set
        {
            _Phyllochron.lincr = value;
        }
    }
    public double ldecr
    {
        get
        {
             return _Phyllochron.ldecr; 
        }
        set
        {
            _Phyllochron.ldecr = value;
        }
    }
    public double pincr
    {
        get
        {
             return _Phyllochron.pincr; 
        }
        set
        {
            _Phyllochron.pincr = value;
        }
    }
    public double pTQhf
    {
        get
        {
             return _Phyllochron.pTQhf; 
        }
        set
        {
            _Phyllochron.pTQhf = value;
        }
    }
    public double B
    {
        get
        {
             return _Phyllochron.B; 
        }
        set
        {
            _Phyllochron.B = value;
        }
    }
    public double areaSL
    {
        get
        {
             return _Phyllochron.areaSL; 
        }
        set
        {
            _Phyllochron.areaSL = value;
        }
    }
    public double areaSS
    {
        get
        {
             return _Phyllochron.areaSS; 
        }
        set
        {
            _Phyllochron.areaSS = value;
        }
    }
    public double lARmin
    {
        get
        {
             return _Phyllochron.lARmin; 
        }
        set
        {
            _Phyllochron.lARmin = value;
        }
    }
    public double sowingDensity
    {
        get
        {
             return _Phyllochron.sowingDensity; 
        }
        set
        {
            _Phyllochron.sowingDensity = value;
            _ShootNumber.sowingDensity = value;
        }
    }
    public double lARmax
    {
        get
        {
             return _Phyllochron.lARmax; 
        }
        set
        {
            _Phyllochron.lARmax = value;
        }
    }
    public double lNeff
    {
        get
        {
             return _Phyllochron.lNeff; 
        }
        set
        {
            _Phyllochron.lNeff = value;
        }
    }
    public double rp
    {
        get
        {
             return _PhylSowingDateCorrection.rp; 
        }
        set
        {
            _PhylSowingDateCorrection.rp = value;
        }
    }
    public double p
    {
        get
        {
             return _Phyllochron.p; 
        }
        set
        {
            _Phyllochron.p = value;
            _PhylSowingDateCorrection.p = value;
            _UpdatePhase.p = value;
        }
    }
    public double pdecr
    {
        get
        {
             return _Phyllochron.pdecr; 
        }
        set
        {
            _Phyllochron.pdecr = value;
        }
    }
    public double maxTvern
    {
        get
        {
             return _VernalizationProgress.maxTvern; 
        }
        set
        {
            _VernalizationProgress.maxTvern = value;
        }
    }
    public double tTWindowForPTQ
    {
        get
        {
             return _GAImean.tTWindowForPTQ; 
        }
        set
        {
            _GAImean.tTWindowForPTQ = value;
            _PTQ.tTWindowForPTQ = value;
        }
    }
    public double vBEE
    {
        get
        {
             return _VernalizationProgress.vBEE; 
        }
        set
        {
            _VernalizationProgress.vBEE = value;
        }
    }
    public int isVernalizable
    {
        get
        {
             return _VernalizationProgress.isVernalizable; 
        }
        set
        {
            _VernalizationProgress.isVernalizable = value;
            _UpdatePhase.isVernalizable = value;
        }
    }
    public double minTvern
    {
        get
        {
             return _VernalizationProgress.minTvern; 
        }
        set
        {
            _VernalizationProgress.minTvern = value;
        }
    }
    public double intTvern
    {
        get
        {
             return _VernalizationProgress.intTvern; 
        }
        set
        {
            _VernalizationProgress.intTvern = value;
        }
    }
    public double vAI
    {
        get
        {
             return _VernalizationProgress.vAI; 
        }
        set
        {
            _VernalizationProgress.vAI = value;
        }
    }
    public double maxDL
    {
        get
        {
             return _VernalizationProgress.maxDL; 
        }
        set
        {
            _VernalizationProgress.maxDL = value;
            _UpdatePhase.maxDL = value;
        }
    }
    public string choosePhyllUse
    {
        get
        {
             return _Phyllochron.choosePhyllUse; 
        }
        set
        {
            _Phyllochron.choosePhyllUse = value;
            _UpdatePhase.choosePhyllUse = value;
        }
    }
    public double minDL
    {
        get
        {
             return _VernalizationProgress.minDL; 
        }
        set
        {
            _VernalizationProgress.minDL = value;
        }
    }
    public double pFLLAnth
    {
        get
        {
             return _UpdatePhase.pFLLAnth; 
        }
        set
        {
            _UpdatePhase.pFLLAnth = value;
        }
    }
    public double dcd
    {
        get
        {
             return _UpdatePhase.dcd; 
        }
        set
        {
            _UpdatePhase.dcd = value;
        }
    }
    public double dgf
    {
        get
        {
             return _UpdatePhase.dgf; 
        }
        set
        {
            _UpdatePhase.dgf = value;
        }
    }
    public double degfm
    {
        get
        {
             return _UpdatePhase.degfm; 
        }
        set
        {
            _UpdatePhase.degfm = value;
        }
    }
    public bool ignoreGrainMaturation
    {
        get
        {
             return _UpdatePhase.ignoreGrainMaturation; 
        }
        set
        {
            _UpdatePhase.ignoreGrainMaturation = value;
        }
    }
    public double pHEADANTH
    {
        get
        {
             return _UpdatePhase.pHEADANTH; 
        }
        set
        {
            _UpdatePhase.pHEADANTH = value;
        }
    }
    public double sLDL
    {
        get
        {
             return _UpdatePhase.sLDL; 
        }
        set
        {
            _UpdatePhase.sLDL = value;
        }
    }
    public int sowingDay
    {
        get
        {
             return _PhylSowingDateCorrection.sowingDay; 
        }
        set
        {
            _PhylSowingDateCorrection.sowingDay = value;
        }
    }
    public int sDws
    {
        get
        {
             return _PhylSowingDateCorrection.sDws; 
        }
        set
        {
            _PhylSowingDateCorrection.sDws = value;
        }
    }
    public double sDsa_nh
    {
        get
        {
             return _PhylSowingDateCorrection.sDsa_nh; 
        }
        set
        {
            _PhylSowingDateCorrection.sDsa_nh = value;
        }
    }
    public double der
    {
        get
        {
             return _RegisterZadok.der; 
        }
        set
        {
            _RegisterZadok.der = value;
        }
    }
    public double targetFertileShoot
    {
        get
        {
             return _ShootNumber.targetFertileShoot; 
        }
        set
        {
            _ShootNumber.targetFertileShoot = value;
        }
    }
    public double dse
    {
        get
        {
             return _UpdatePhase.dse; 
        }
        set
        {
            _UpdatePhase.dse = value;
        }
    }
    public double slopeTSFLN
    {
        get
        {
             return _RegisterZadok.slopeTSFLN; 
        }
        set
        {
            _RegisterZadok.slopeTSFLN = value;
        }
    }
    public double intTSFLN
    {
        get
        {
             return _RegisterZadok.intTSFLN; 
        }
        set
        {
            _RegisterZadok.intTSFLN = value;
        }
    }

    public void  CalculateModel(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        _GAImean.CalculateModel(s,s1, r, a);
        _PTQ.CalculateModel(s,s1, r, a);
        _CumulTTFrom.CalculateModel(s,s1, r, a);
        _IsMomentRegistredZC_39.CalculateModel(s,s1, r, a);
        _VernalizationProgress.CalculateModel(s,s1, r, a);
        _PhylSowingDateCorrection.CalculateModel(s,s1, r, a);
        _UpdatePhase.CalculateModel(s,s1, r, a);
        _LeafNumber.CalculateModel(s,s1, r, a);
        _ShootNumber.CalculateModel(s,s1, r, a);
        _UpdateLeafFlag.CalculateModel(s,s1, r, a);
        _RegisterZadok.CalculateModel(s,s1, r, a);
        _UpdateCalendar.CalculateModel(s,s1, r, a);
        _Phyllochron.CalculateModel(s,s1, r, a);
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
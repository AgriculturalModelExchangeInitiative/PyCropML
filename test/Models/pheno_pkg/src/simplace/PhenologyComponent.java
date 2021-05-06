import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import javafx.util.*;
import java.time.LocalDateTime;
public class Phenology
{
    private double aMXLFNO;
    public double getaMXLFNO()
    { return aMXLFNO; }

    public void setaMXLFNO(double _aMXLFNO)
    { this.aMXLFNO= _aMXLFNO; } 
    
    private double pNini;
    public double getpNini()
    { return pNini; }

    public void setpNini(double _pNini)
    { this.pNini= _pNini; } 
    
    private double sDsa_sh;
    public double getsDsa_sh()
    { return sDsa_sh; }

    public void setsDsa_sh(double _sDsa_sh)
    { this.sDsa_sh= _sDsa_sh; } 
    
    private double latitude;
    public double getlatitude()
    { return latitude; }

    public void setlatitude(double _latitude)
    { this.latitude= _latitude; } 
    
    private double kl;
    public double getkl()
    { return kl; }

    public void setkl(double _kl)
    { this.kl= _kl; } 
    
    private double lincr;
    public double getlincr()
    { return lincr; }

    public void setlincr(double _lincr)
    { this.lincr= _lincr; } 
    
    private double ldecr;
    public double getldecr()
    { return ldecr; }

    public void setldecr(double _ldecr)
    { this.ldecr= _ldecr; } 
    
    private double pincr;
    public double getpincr()
    { return pincr; }

    public void setpincr(double _pincr)
    { this.pincr= _pincr; } 
    
    private double pTQhf;
    public double getpTQhf()
    { return pTQhf; }

    public void setpTQhf(double _pTQhf)
    { this.pTQhf= _pTQhf; } 
    
    private double B;
    public double getB()
    { return B; }

    public void setB(double _B)
    { this.B= _B; } 
    
    private double areaSL;
    public double getareaSL()
    { return areaSL; }

    public void setareaSL(double _areaSL)
    { this.areaSL= _areaSL; } 
    
    private double areaSS;
    public double getareaSS()
    { return areaSS; }

    public void setareaSS(double _areaSS)
    { this.areaSS= _areaSS; } 
    
    private double lARmin;
    public double getlARmin()
    { return lARmin; }

    public void setlARmin(double _lARmin)
    { this.lARmin= _lARmin; } 
    
    private double sowingDensity;
    public double getsowingDensity()
    { return sowingDensity; }

    public void setsowingDensity(double _sowingDensity)
    { this.sowingDensity= _sowingDensity; } 
    
    private double lARmax;
    public double getlARmax()
    { return lARmax; }

    public void setlARmax(double _lARmax)
    { this.lARmax= _lARmax; } 
    
    private double lNeff;
    public double getlNeff()
    { return lNeff; }

    public void setlNeff(double _lNeff)
    { this.lNeff= _lNeff; } 
    
    private double rp;
    public double getrp()
    { return rp; }

    public void setrp(double _rp)
    { this.rp= _rp; } 
    
    private double p;
    public double getp()
    { return p; }

    public void setp(double _p)
    { this.p= _p; } 
    
    private double pdecr;
    public double getpdecr()
    { return pdecr; }

    public void setpdecr(double _pdecr)
    { this.pdecr= _pdecr; } 
    
    private double maxTvern;
    public double getmaxTvern()
    { return maxTvern; }

    public void setmaxTvern(double _maxTvern)
    { this.maxTvern= _maxTvern; } 
    
    private double tTWindowForPTQ;
    public double gettTWindowForPTQ()
    { return tTWindowForPTQ; }

    public void settTWindowForPTQ(double _tTWindowForPTQ)
    { this.tTWindowForPTQ= _tTWindowForPTQ; } 
    
    private double vBEE;
    public double getvBEE()
    { return vBEE; }

    public void setvBEE(double _vBEE)
    { this.vBEE= _vBEE; } 
    
    private int isVernalizable;
    public int getisVernalizable()
    { return isVernalizable; }

    public void setisVernalizable(int _isVernalizable)
    { this.isVernalizable= _isVernalizable; } 
    
    private double minTvern;
    public double getminTvern()
    { return minTvern; }

    public void setminTvern(double _minTvern)
    { this.minTvern= _minTvern; } 
    
    private double intTvern;
    public double getintTvern()
    { return intTvern; }

    public void setintTvern(double _intTvern)
    { this.intTvern= _intTvern; } 
    
    private double vAI;
    public double getvAI()
    { return vAI; }

    public void setvAI(double _vAI)
    { this.vAI= _vAI; } 
    
    private double maxDL;
    public double getmaxDL()
    { return maxDL; }

    public void setmaxDL(double _maxDL)
    { this.maxDL= _maxDL; } 
    
    private String choosePhyllUse;
    public String getchoosePhyllUse()
    { return choosePhyllUse; }

    public void setchoosePhyllUse(String _choosePhyllUse)
    { this.choosePhyllUse= _choosePhyllUse; } 
    
    private double minDL;
    public double getminDL()
    { return minDL; }

    public void setminDL(double _minDL)
    { this.minDL= _minDL; } 
    
    private double pFLLAnth;
    public double getpFLLAnth()
    { return pFLLAnth; }

    public void setpFLLAnth(double _pFLLAnth)
    { this.pFLLAnth= _pFLLAnth; } 
    
    private double dcd;
    public double getdcd()
    { return dcd; }

    public void setdcd(double _dcd)
    { this.dcd= _dcd; } 
    
    private double dgf;
    public double getdgf()
    { return dgf; }

    public void setdgf(double _dgf)
    { this.dgf= _dgf; } 
    
    private double degfm;
    public double getdegfm()
    { return degfm; }

    public void setdegfm(double _degfm)
    { this.degfm= _degfm; } 
    
    private boolean ignoreGrainMaturation;
    public boolean getignoreGrainMaturation()
    { return ignoreGrainMaturation; }

    public void setignoreGrainMaturation(boolean _ignoreGrainMaturation)
    { this.ignoreGrainMaturation= _ignoreGrainMaturation; } 
    
    private double pHEADANTH;
    public double getpHEADANTH()
    { return pHEADANTH; }

    public void setpHEADANTH(double _pHEADANTH)
    { this.pHEADANTH= _pHEADANTH; } 
    
    private double sLDL;
    public double getsLDL()
    { return sLDL; }

    public void setsLDL(double _sLDL)
    { this.sLDL= _sLDL; } 
    
    private int sowingDay;
    public int getsowingDay()
    { return sowingDay; }

    public void setsowingDay(int _sowingDay)
    { this.sowingDay= _sowingDay; } 
    
    private LocalDateTime sowingDate;
    public LocalDateTime getsowingDate()
    { return sowingDate; }

    public void setsowingDate(LocalDateTime _sowingDate)
    { this.sowingDate= _sowingDate; } 
    
    private int sDws;
    public int getsDws()
    { return sDws; }

    public void setsDws(int _sDws)
    { this.sDws= _sDws; } 
    
    private double sDsa_nh;
    public double getsDsa_nh()
    { return sDsa_nh; }

    public void setsDsa_nh(double _sDsa_nh)
    { this.sDsa_nh= _sDsa_nh; } 
    
    private double der;
    public double getder()
    { return der; }

    public void setder(double _der)
    { this.der= _der; } 
    
    private double targetFertileShoot;
    public double gettargetFertileShoot()
    { return targetFertileShoot; }

    public void settargetFertileShoot(double _targetFertileShoot)
    { this.targetFertileShoot= _targetFertileShoot; } 
    
    private double dse;
    public double getdse()
    { return dse; }

    public void setdse(double _dse)
    { this.dse= _dse; } 
    
    private double slopeTSFLN;
    public double getslopeTSFLN()
    { return slopeTSFLN; }

    public void setslopeTSFLN(double _slopeTSFLN)
    { this.slopeTSFLN= _slopeTSFLN; } 
    
    private double intTSFLN;
    public double getintTSFLN()
    { return intTSFLN; }

    public void setintTSFLN(double _intTSFLN)
    { this.intTSFLN= _intTSFLN; } 
    
    public Phenology() { }
    public void  Calculate_phenology(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: Phenology -Version: 001, -Time step: 1
        //- Description:
    //            * Title: Phenology
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA/LEPSE
    //            * Abstract: see documentation
        //- inputs:
    //            * name: phyllochron_t1
    //                          ** description : phyllochron
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 0
    //                          ** unit : °C d leaf-1
    //            * name: minFinalNumber_t1
    //                          ** description : minimum final leaf number
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 5.5
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //            * name: aMXLFNO
    //                          ** description : Absolute maximum leaf number
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 24.0
    //                          ** unit : leaf
    //                          ** inputtype : parameter
    //            * name: currentdate
    //                          ** description : current date 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DATE
    //                          ** default : 2007/3/27
    //                          ** inputtype : variable
    //                          ** unit : 
    //            * name: cumulTT
    //                          ** description : cumul thermal times at currentdate
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 112.330110409888
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: pNini
    //                          ** description : Number of primorida in the apex at emergence
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 24
    //                          ** default : 4.0
    //                          ** unit : primordia
    //                          ** inputtype : parameter
    //            * name: sDsa_sh
    //                          ** description : Sowing date at which Phyllochrone is maximum in southern hemispher
    //                          ** parametercategory : species
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 1
    //                          ** max : 365
    //                          ** default : 1.0
    //                          ** unit : d
    //                          ** uri : some url
    //            * name: latitude
    //                          ** description : Latitude
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLE
    //                          ** min : -90
    //                          ** max : 90
    //                          ** default : 0.0
    //                          ** unit : °
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: kl
    //                          ** description : Exctinction Coefficient
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 0.45
    //                          ** min : 0.0
    //                          ** max : 50.0
    //                          ** unit : -
    //                          ** uri : some url
    //            * name: calendarDates_t1
    //                          ** description : List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** default : ['2007/3/21']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarMoments_t1
    //                          ** description : List containing appearance of each stage at previous day
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** default : ['Sowing']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: lincr
    //                          ** description : Leaf number above which the phyllochron is increased by Pincr
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 8.0
    //                          ** min : 0.0
    //                          ** max : 30.0
    //                          ** unit : leaf
    //                          ** uri : some url
    //            * name: ldecr
    //                          ** description : Leaf number up to which the phyllochron is decreased by Pdecr
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 100.0
    //                          ** unit : leaf
    //                          ** uri : some url
    //            * name: pincr
    //                          ** description : Factor increasing the phyllochron for leaf number higher than Lincr
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 1.5
    //                          ** min : 0.0
    //                          ** max : 10.0
    //                          ** unit : -
    //                          ** uri : some url
    //            * name: ptq
    //                          ** description : Photothermal quotient 
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 10000.0
    //                          ** unit : MJ °C-1 d-1 m-2)
    //                          ** uri : some url
    //            * name: pTQhf
    //                          ** description : Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : °C d leaf-1
    //                          ** uri : some url
    //            * name: B
    //                          ** description : Phyllochron at PTQ equal 1
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 20.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : °C d leaf-1
    //                          ** uri : some url
    //            * name: areaSL
    //                          ** description :  Area Leaf
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : cm2
    //                          ** uri : some url
    //            * name: areaSS
    //                          ** description : Area Sheath
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : cm2
    //                          ** uri : some url
    //            * name: lARmin
    //                          ** description : LAR minimum
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : leaf-1 °C
    //                          ** uri : some url
    //            * name: sowingDensity
    //                          ** description : Sowing Density
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : plant m-2
    //                          ** uri : some url
    //            * name: lARmax
    //                          ** description : LAR maximum
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : leaf-1 °C
    //                          ** uri : some url
    //            * name: lNeff
    //                          ** description : Leaf Number efficace
    //                          ** inputtype : parameter
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : leaf
    //                          ** uri : some url
    //            * name: rp
    //                          ** description : Rate of change of Phyllochrone with sowing date
    //                          ** parametercategory : species
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 365
    //                          ** default : 0
    //                          ** unit : d-1
    //                          ** uri : some url
    //            * name: p
    //                          ** description : Phyllochron (Varietal parameter)
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 120.0
    //                          ** min : 0.0
    //                          ** max : 1000.0
    //                          ** unit : °C d leaf-1
    //                          ** uri : some url
    //            * name: pdecr
    //                          ** description : Factor decreasing the phyllochron for leaf number less than Ldecr
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 0.4
    //                          ** min : 0.0
    //                          ** max : 10.0
    //                          ** unit : -
    //                          ** uri : some url
    //            * name: leafNumber_t1
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 0
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //            * name: maxTvern
    //                          ** description : Maximum temperature for vernalization to occur
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 60
    //                          ** default :  23.0
    //                          ** unit : °C
    //                          ** inputtype : parameter
    //            * name: dayLength
    //                          ** description : day length
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 12.3037621834005
    //                          ** unit : mm2 m-2
    //                          ** inputtype : variable
    //            * name: deltaTT
    //                          ** description : Thermal time increase of the day
    //                          ** inputtype : variable
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 100.0
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: pastMaxAI_t1
    //                          ** description : Maximum Leaf Area Index reached the current day
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 5000.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: tTWindowForPTQ
    //                          ** description : Thermal Time window for average
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 5000.0
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: listGAITTWindowForPTQ_t1
    //                          ** description : List of daily Green Area Index in the window dedicated to average
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: gAI
    //                          ** description : Green Area Index of the day
    //                          ** inputtype : variable
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 500.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: pAR
    //                          ** description : Daily Photosyntetically Active Radiation
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 10000.0
    //                          ** unit : MJ m² d
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: listPARTTWindowForPTQ_t1
    //                          ** description : List of Daily PAR during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** default : [0.0]
    //                          ** unit : MJ m2 d
    //                          ** uri : some url
    //            * name: listTTShootWindowForPTQ1_t1
    //                          ** description : List of daily shoot thermal time in the window dedicated to average
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: listTTShootWindowForPTQ_t1
    //                          ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** default : [0.0]
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: vBEE
    //                          ** description : Vernalization rate at 0°C
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.01
    //                          ** unit : d-1
    //                          ** inputtype : parameter
    //            * name: calendarCumuls_t1
    //                          ** description : list containing for each stage occured its cumulated thermal times at previous day
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: isVernalizable
    //                          ** description : true if the plant is vernalizable
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : parameter
    //            * name: vernaprog_t1
    //                          ** description : progression on a 0  to 1 scale of the vernalization
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default :  0.5517254187376879
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: minTvern
    //                          ** description : Minimum temperature for vernalization to occur
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 60
    //                          ** default : 0.0
    //                          ** unit : °C
    //                          ** inputtype : parameter
    //            * name: intTvern
    //                          ** description : Intermediate temperature for vernalization to occur
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 60
    //                          ** default :  11.0
    //                          ** unit : °C
    //                          ** inputtype : parameter
    //            * name: vAI
    //                          ** description : Response of vernalization rate to temperature
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default :  0.015
    //                          ** unit : d-1 °C-1
    //                          ** inputtype : parameter
    //            * name: maxDL
    //                          ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 24
    //                          ** default : 15.0
    //                          ** unit : h
    //                          ** inputtype : parameter
    //            * name: choosePhyllUse
    //                          ** description : Switch to choose the type of phyllochron calculation to be used
    //                          ** inputtype : parameter
    //                          ** parametercategory : species
    //                          ** datatype : STRING
    //                          ** default : Default
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : -
    //                          ** uri : some url
    //            * name: minDL
    //                          ** description : Threshold daylength below which it does influence vernalization rate
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 12
    //                          ** max : 24
    //                          ** default : 8.0
    //                          ** unit : h
    //                          ** inputtype : parameter
    //            * name: hasLastPrimordiumAppeared_t1
    //                          ** description : if Last Primordium has Appeared
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: phase_t1
    //                          ** description :  the name of the phase
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: pFLLAnth
    //                          ** description : Phyllochronic duration of the period between flag leaf ligule appearance and anthesis
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : 
    //                          ** default : 2.22
    //                          ** inputtype : parameter
    //            * name: dcd
    //                          ** description : Duration of the endosperm cell division phase
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 100
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: dgf
    //                          ** description : Grain filling duration (from anthesis to physiological maturity)
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 450
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: degfm
    //                          ** description : Grain maturation duration (from physiological maturity to harvest ripeness)
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 50
    //                          ** default : 0
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: ignoreGrainMaturation
    //                          ** description : true to ignore grain maturation
    //                          ** parametercategory : species
    //                          ** datatype : BOOLEAN
    //                          ** default : FALSE
    //                          ** unit : 
    //                          ** inputtype : parameter
    //            * name: pHEADANTH
    //                          ** description : Number of phyllochron between heading and anthesiss
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : parameter
    //            * name: finalLeafNumber_t1
    //                          ** description : final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 0
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //            * name: sLDL
    //                          ** description : Daylength response of leaf production
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.85
    //                          ** unit : leaf h-1
    //                          ** inputtype : parameter
    //            * name: grainCumulTT
    //                          ** description : cumulTT used for the grain developpment
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: sowingDay
    //                          ** description : Day of Year at sowing
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** min : 1
    //                          ** max : 365
    //                          ** default : 1
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: hasZadokStageChanged_t1
    //                          ** description : true if the zadok stage has changed this time step
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: currentZadokStage
    //                          ** description : current zadok stage
    //                          ** variablecategory : state
    //                          ** datatype : STRING
    //                          ** min : 
    //                          ** max : 
    //                          ** default : MainShootPlus1Tiller
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: sowingDate
    //                          ** description :  Date of Sowing
    //                          ** parametercategory : constant
    //                          ** datatype : DATE
    //                          ** min : 
    //                          ** max : 
    //                          ** default : 2007/3/21
    //                          ** unit : 
    //                          ** inputtype : parameter
    //            * name: sDws
    //                          ** description : Sowing date at which Phyllochrone is minimum
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** default : 1
    //                          ** min : 1
    //                          ** max : 365
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: sDsa_nh
    //                          ** description : Sowing date at which Phyllochrone is maximum in northern hemispher
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 1.0
    //                          ** min : 1
    //                          ** max : 365
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: hasFlagLeafLiguleAppeared
    //                          ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: der
    //                          ** description : Duration of the endosperm endoreduplication phase
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 300.0
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: hasFlagLeafLiguleAppeared_t1
    //                          ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 1
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: tilleringProfile_t1
    //                          ** description :  store the amount of new tiller created at each time a new tiller appears
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [288.0]
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: targetFertileShoot
    //                          ** description : max value of shoot number for the canopy
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 280
    //                          ** max : 1000
    //                          ** default : 600.0
    //                          ** unit : shoot
    //                          ** inputtype : variable
    //            * name: leafTillerNumberArray_t1
    //                          ** description : store the number of tiller for each leaf layer
    //                          ** variablecategory : state
    //                          ** datatype : INTLIST
    //                          ** unit : leaf
    //                          ** default : [1, 1, 1]
    //                          ** inputtype : variable
    //            * name: dse
    //                          ** description : Thermal time from sowing to emergence
    //                          ** parametercategory : genotypic
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 105
    //                          ** unit : °C d
    //                          ** inputtype : parameter
    //            * name: slopeTSFLN
    //                          ** description : used to calculate Terminal spikelet
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0.9
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: intTSFLN
    //                          ** description : used to calculate Terminal spikelet
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0.9
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: canopyShootNumber_t1
    //                          ** description : shoot number for the whole canopy
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 288.0
    //                          ** unit : shoot m-2
    //                          ** inputtype : variable
        //- outputs:
    //            * name: currentZadokStage
    //                          ** description : current zadok stage
    //                          ** variablecategory : state
    //                          ** datatype : STRING
    //                          ** unit :  
    //                          ** uri : some url
    //            * name: hasZadokStageChanged
    //                          ** description : true if the zadok stage has changed this time step
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    //                          ** uri : some url
    //            * name: hasFlagLeafLiguleAppeared
    //                          ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    //                          ** uri : some url
    //            * name: listPARTTWindowForPTQ
    //                          ** description :  List of Daily PAR during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : MJ m2 d
    //            * name: hasLastPrimordiumAppeared
    //                          ** description : if Last Primordium has Appeared
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    //            * name: listTTShootWindowForPTQ
    //                          ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : °C d
    //            * name: listTTShootWindowForPTQ1
    //                          ** description : List of daily shoot thermal time in the window dedicated to average
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: ptq
    //                          ** description : Photothermal Quotient
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : MJ °C-1 d m-2)
    //            * name: calendarMoments
    //                          ** description :  List containing apparition of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** unit : 
    //            * name: canopyShootNumber
    //                          ** description : shoot number for the whole canopy
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : shoot m-2
    //            * name: calendarDates
    //                          ** description :  List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** unit : 
    //            * name: leafTillerNumberArray
    //                          ** description : store the number of tiller for each leaf layer
    //                          ** variablecategory : state
    //                          ** datatype : INTLIST
    //                          ** unit : leaf
    //            * name: vernaprog
    //                          ** description : progression on a 0  to 1 scale of the vernalization
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : 
    //            * name: phyllochron
    //                          ** description :  the rate of leaf appearance 
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit :  °C d leaf-1
    //                          ** uri : some url
    //            * name: leafNumber
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : leaf
    //                          ** uri : some url
    //            * name: numberTillerCohort
    //                          ** description : Number of tiller which appears
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : dimensionless
    //            * name: tilleringProfile
    //                          ** description :  store the amount of new tiller created at each time a new tiller appears
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** unit : dimensionless
    //            * name: averageShootNumberPerPlant
    //                          ** description : average shoot number per plant in the canopy
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : shoot m-2
    //            * name: minFinalNumber
    //                          ** description : minimum final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : leaf
    //            * name: finalLeafNumber
    //                          ** description : final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** unit : leaf
    //            * name: phase
    //                          ** description : the name of the phase
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** unit : 
    //            * name: listGAITTWindowForPTQ
    //                          ** description : List of daily Green Area Index in the window dedicated to average
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: calendarCumuls
    //                          ** description :  list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** unit : °C d
    //            * name: gAImean
    //                          ** description : Mean Green Area Index
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 500.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: pastMaxAI
    //                          ** description : Maximum Leaf Area Index reached the current day
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 5000.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
        double phyllochron_t1 = s1.getphyllochron();
        double minFinalNumber_t1 = s1.getminFinalNumber();
        LocalDateTime currentdate = a.getcurrentdate();
        double cumulTT = a.getcumulTT();
        List<LocalDateTime> calendarDates_t1 = s1.getcalendarDates();
        List<String> calendarMoments_t1 = s1.getcalendarMoments();
        double ptq = s.getptq();
        double leafNumber_t1 = s1.getleafNumber();
        double dayLength = a.getdayLength();
        double deltaTT = a.getdeltaTT();
        double pastMaxAI_t1 = s1.getpastMaxAI();
        List<Double> listGAITTWindowForPTQ_t1 = s1.getlistGAITTWindowForPTQ();
        double gAI = a.getgAI();
        double pAR = a.getpAR();
        List<Double> listPARTTWindowForPTQ_t1 = s1.getlistPARTTWindowForPTQ();
        List<Double> listTTShootWindowForPTQ1_t1 = s1.getlistTTShootWindowForPTQ1();
        List<Double> listTTShootWindowForPTQ_t1 = s1.getlistTTShootWindowForPTQ();
        List<Double> calendarCumuls_t1 = s1.getcalendarCumuls();
        double vernaprog_t1 = s1.getvernaprog();
        int hasLastPrimordiumAppeared_t1 = s1.gethasLastPrimordiumAppeared();
        double phase_t1 = s1.getphase();
        double finalLeafNumber_t1 = s1.getfinalLeafNumber();
        double grainCumulTT = a.getgrainCumulTT();
        int hasZadokStageChanged_t1 = s1.gethasZadokStageChanged();
        String currentZadokStage = s.getcurrentZadokStage();
        int hasFlagLeafLiguleAppeared = s.gethasFlagLeafLiguleAppeared();
        int hasFlagLeafLiguleAppeared_t1 = s1.gethasFlagLeafLiguleAppeared();
        List<Double> tilleringProfile_t1 = s1.gettilleringProfile();
        List<Integer> leafTillerNumberArray_t1 = s1.getleafTillerNumberArray();
        double canopyShootNumber_t1 = s1.getcanopyShootNumber();
        double fixPhyll;
        double leafNumber;
        double gAImean;
        double phyllochron;
        int numberTillerCohort_t1;
        double averageShootNumberPerPlant;
        double canopyShootNumber;
        List<Integer> leafTillerNumberArray = new ArrayList<>(Arrays.asList());
        List<Double> tilleringProfile = new ArrayList<>(Arrays.asList());
        int numberTillerCohort;
        List<String> calendarMoments = new ArrayList<>(Arrays.asList());
        List<LocalDateTime> calendarDates = new ArrayList<>(Arrays.asList());
        List<Double> calendarCumuls = new ArrayList<>(Arrays.asList());
        double finalLeafNumber;
        double phase;
        double cumulTTFromZC_39;
        int isMomentRegistredZC_39;
        double vernaprog;
        double minFinalNumber;
        double cumulTTFromZC_91;
        int hasLastPrimordiumAppeared;
        double cumulTTFromZC_65;
        int hasZadokStageChanged;
        List<Double> listGAITTWindowForPTQ = new ArrayList<>(Arrays.asList());
        List<Double> listPARTTWindowForPTQ = new ArrayList<>(Arrays.asList());
        List<Double> listTTShootWindowForPTQ = new ArrayList<>(Arrays.asList());
        double pastMaxAI;
        List<Double> listTTShootWindowForPTQ1 = new ArrayList<>(Arrays.asList());
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
        s.setptq(ptq);
        s.setcurrentZadokStage(currentZadokStage);
        s.sethasFlagLeafLiguleAppeared(hasFlagLeafLiguleAppeared);
        s.setleafNumber(leafNumber);
        s.setgAImean(gAImean);
        s.setphyllochron(phyllochron);
        s.setaverageShootNumberPerPlant(averageShootNumberPerPlant);
        s.setcanopyShootNumber(canopyShootNumber);
        s.setleafTillerNumberArray(leafTillerNumberArray);
        s.settilleringProfile(tilleringProfile);
        s.setnumberTillerCohort(numberTillerCohort);
        s.setcalendarMoments(calendarMoments);
        s.setcalendarDates(calendarDates);
        s.setcalendarCumuls(calendarCumuls);
        s.setfinalLeafNumber(finalLeafNumber);
        s.setphase(phase);
        s.setvernaprog(vernaprog);
        s.setminFinalNumber(minFinalNumber);
        s.sethasLastPrimordiumAppeared(hasLastPrimordiumAppeared);
        s.sethasZadokStageChanged(hasZadokStageChanged);
        s.setlistGAITTWindowForPTQ(listGAITTWindowForPTQ);
        s.setlistPARTTWindowForPTQ(listPARTTWindowForPTQ);
        s.setlistTTShootWindowForPTQ(listTTShootWindowForPTQ);
        s.setpastMaxAI(pastMaxAI);
        s.setlistTTShootWindowForPTQ1(listTTShootWindowForPTQ1);
    }
    public void Init(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        LocalDateTime currentdate;
        double cumulTT;
        double dayLength;
        double deltaTT;
        double gAI;
        double pAR;
        double grainCumulTT;
        String currentZadokStage = "";
        int hasZadokStageChanged = 0;
        int hasFlagLeafLiguleAppeared = 0;
        List<Double> listPARTTWindowForPTQ = new ArrayList<>(Arrays.asList());
        int hasLastPrimordiumAppeared = 0;
        List<Double> listTTShootWindowForPTQ = new ArrayList<>(Arrays.asList());
        List<Double> listTTShootWindowForPTQ1 = new ArrayList<>(Arrays.asList());
        double ptq = 0.0d;
        List<String> calendarMoments = new ArrayList<>(Arrays.asList());
        double canopyShootNumber = 0.0d;
        List<LocalDateTime> calendarDates = new ArrayList<>(Arrays.asList());
        List<Integer> leafTillerNumberArray = new ArrayList<>(Arrays.asList());
        double vernaprog = 0.0d;
        double phyllochron = 0.0d;
        double leafNumber = 0.0d;
        int numberTillerCohort = 0;
        List<Double> tilleringProfile = new ArrayList<>(Arrays.asList());
        double averageShootNumberPerPlant = 0.0d;
        double minFinalNumber = 0.0d;
        double finalLeafNumber = 0.0d;
        double phase = 0.0d;
        List<Double> listGAITTWindowForPTQ = new ArrayList<>(Arrays.asList());
        List<Double> calendarCumuls = new ArrayList<>(Arrays.asList());
        double gAImean = 0.0d;
        double pastMaxAI = 0.0d;
        calendarMoments.add("Sowing");
        calendarCumuls.add(0.0d);
        calendarDates.add(sowingDate);
        minFinalNumber = 5.5d;
        s.setcurrentZadokStage(currentZadokStage);
        s.sethasZadokStageChanged(hasZadokStageChanged);
        s.sethasFlagLeafLiguleAppeared(hasFlagLeafLiguleAppeared);
        s.setlistPARTTWindowForPTQ(listPARTTWindowForPTQ);
        s.sethasLastPrimordiumAppeared(hasLastPrimordiumAppeared);
        s.setlistTTShootWindowForPTQ(listTTShootWindowForPTQ);
        s.setlistTTShootWindowForPTQ1(listTTShootWindowForPTQ1);
        s.setptq(ptq);
        s.setcalendarMoments(calendarMoments);
        s.setcanopyShootNumber(canopyShootNumber);
        s.setcalendarDates(calendarDates);
        s.setleafTillerNumberArray(leafTillerNumberArray);
        s.setvernaprog(vernaprog);
        s.setphyllochron(phyllochron);
        s.setleafNumber(leafNumber);
        s.setnumberTillerCohort(numberTillerCohort);
        s.settilleringProfile(tilleringProfile);
        s.setaverageShootNumberPerPlant(averageShootNumberPerPlant);
        s.setminFinalNumber(minFinalNumber);
        s.setfinalLeafNumber(finalLeafNumber);
        s.setphase(phase);
        s.setlistGAITTWindowForPTQ(listGAITTWindowForPTQ);
        s.setcalendarCumuls(calendarCumuls);
        s.setgAImean(gAImean);
        s.setpastMaxAI(pastMaxAI);
    }
}
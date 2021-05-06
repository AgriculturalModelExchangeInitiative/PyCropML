import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import javafx.util.*;
import java.time.LocalDateTime;
public class Vernalizationprogress
{
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
    
    private double vBEE;
    public double getvBEE()
    { return vBEE; }

    public void setvBEE(double _vBEE)
    { this.vBEE= _vBEE; } 
    
    private double minDL;
    public double getminDL()
    { return minDL; }

    public void setminDL(double _minDL)
    { this.minDL= _minDL; } 
    
    private double maxDL;
    public double getmaxDL()
    { return maxDL; }

    public void setmaxDL(double _maxDL)
    { this.maxDL= _maxDL; } 
    
    private double maxTvern;
    public double getmaxTvern()
    { return maxTvern; }

    public void setmaxTvern(double _maxTvern)
    { this.maxTvern= _maxTvern; } 
    
    private double pNini;
    public double getpNini()
    { return pNini; }

    public void setpNini(double _pNini)
    { this.pNini= _pNini; } 
    
    private double aMXLFNO;
    public double getaMXLFNO()
    { return aMXLFNO; }

    public void setaMXLFNO(double _aMXLFNO)
    { this.aMXLFNO= _aMXLFNO; } 
    
    private int isVernalizable;
    public int getisVernalizable()
    { return isVernalizable; }

    public void setisVernalizable(int _isVernalizable)
    { this.isVernalizable= _isVernalizable; } 
    
    public Vernalizationprogress() { }
    public void  Calculate_vernalizationprogress(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: VernalizationProgress -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: VernalizationProgress Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Calculate progress (VernaProg) towards vernalization, but there 
    //        			is no vernalization below minTvern 
    //        			and above maxTvern . The maximum value of VernaProg is 1.
    //        			Progress towards full vernalization is a linear function of shoot 
    //        			temperature (soil temperature until leaf # reach MaxLeafSoil and then
    //        			 canopy temperature)
    //    	
        //- inputs:
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
    //                          ** description : difference cumul TT between j and j-1 day 
    //                          ** variablecategory : auxiliary
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 100
    //                          ** default : 20.3429985011972
    //                          ** unit : °C d
    //            * name: cumulTT
    //                          ** description : cumul thermal times at currentdate
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 112.330110409888
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: leafNumber_t1
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 0
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //            * name: calendarMoments_t1
    //                          ** description : List containing appearance of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** default : ['Sowing']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarDates_t1
    //                          ** description : List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** default : ['2007/3/21']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarCumuls_t1
    //                          ** description : list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
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
    //            * name: vBEE
    //                          ** description : Vernalization rate at 0°C
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.01
    //                          ** unit : d-1
    //                          ** inputtype : parameter
    //            * name: minDL
    //                          ** description : Threshold daylength below which it does influence vernalization rate
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 12
    //                          ** max : 24
    //                          ** default : 8.0
    //                          ** unit : h
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
    //            * name: maxTvern
    //                          ** description : Maximum temperature for vernalization to occur
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 60
    //                          ** default :  23.0
    //                          ** unit : °C
    //                          ** inputtype : parameter
    //            * name: pNini
    //                          ** description : Number of primorida in the apex at emergence
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 24
    //                          ** default : 4.0
    //                          ** unit : primordia
    //                          ** inputtype : parameter
    //            * name: aMXLFNO
    //                          ** description : Absolute maximum leaf number
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 24.0
    //                          ** unit : leaf
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
    //            * name: currentdate
    //                          ** description : current date 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DATE
    //                          ** default : 2007/3/27
    //                          ** inputtype : variable
    //                          ** unit : 
    //            * name: isVernalizable
    //                          ** description : true if the plant is vernalizable
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : parameter
    //            * name: minFinalNumber_t1
    //                          ** description : minimum final leaf number
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 5.5
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //                          ** variablecategory : state
        //- outputs:
    //            * name: vernaprog
    //                          ** description : progression on a 0  to 1 scale of the vernalization
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : 
    //            * name: minFinalNumber
    //                          ** description : minimum final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : leaf
    //            * name: calendarMoments
    //                          ** description : List containing appearance of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** unit : 
    //            * name: calendarDates
    //                          ** description : List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** unit : 
    //            * name: calendarCumuls
    //                          ** description : list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** unit : 
        double dayLength = a.getdayLength();
        double deltaTT = a.getdeltaTT();
        double cumulTT = a.getcumulTT();
        double leafNumber_t1 = s1.getleafNumber();
        List<String> calendarMoments_t1 = s1.getcalendarMoments();
        List<LocalDateTime> calendarDates_t1 = s1.getcalendarDates();
        List<Double> calendarCumuls_t1 = s1.getcalendarCumuls();
        double vernaprog_t1 = s1.getvernaprog();
        LocalDateTime currentdate = a.getcurrentdate();
        double minFinalNumber_t1 = s1.getminFinalNumber();
        double vernaprog;
        double minFinalNumber;
        List<String> calendarMoments = new ArrayList<>(Arrays.asList());
        List<LocalDateTime> calendarDates = new ArrayList<>(Arrays.asList());
        List<Double> calendarCumuls = new ArrayList<>(Arrays.asList());
        double maxVernaProg;
        double dLverna;
        double primordno;
        double minLeafNumber;
        double potlfno;
        double tt;
        calendarMoments = new ArrayList<>(calendarMoments_t1);
        calendarCumuls = new ArrayList<>(calendarCumuls_t1);
        calendarDates = new ArrayList<>(calendarDates_t1);
        minFinalNumber = minFinalNumber_t1;
        vernaprog = vernaprog_t1;
        if (isVernalizable == 1 && vernaprog_t1 < 1.0d)
        {
            tt = deltaTT;
            if (tt >= minTvern && tt <= intTvern)
            {
                vernaprog = vernaprog_t1 + (vAI * tt) + vBEE;
            }
            else
            {
                vernaprog = vernaprog_t1;
            }
            if (tt > intTvern)
            {
                maxVernaProg = vAI * intTvern + vBEE;
                dLverna = Math.max(minDL, Math.min(maxDL, dayLength));
                vernaprog = vernaprog + Math.max(0.0d, maxVernaProg * (1.0d + ((intTvern - tt) / (maxTvern - intTvern) * ((dLverna - minDL) / (maxDL - minDL)))));
            }
            primordno = 2.0d * leafNumber_t1 + pNini;
            minLeafNumber = minFinalNumber_t1;
            if (vernaprog >= 1.0d || primordno >= aMXLFNO)
            {
                minFinalNumber = Math.max(primordno, minFinalNumber_t1);
                calendarMoments.add("EndVernalisation");
                calendarCumuls.add(cumulTT);
                calendarDates.add(currentdate);
                vernaprog = Math.max(1.0d, vernaprog);
            }
            else
            {
                potlfno = aMXLFNO - ((aMXLFNO - minLeafNumber) * vernaprog);
                if (primordno >= potlfno)
                {
                    minFinalNumber = Math.max((potlfno + primordno) / 2.0d, minFinalNumber_t1);
                    vernaprog = Math.max(1.0d, vernaprog);
                    calendarMoments.add("EndVernalisation");
                    calendarCumuls.add(cumulTT);
                    calendarDates.add(currentdate);
                }
            }
        }
        s.setvernaprog(vernaprog);
        s.setminFinalNumber(minFinalNumber);
        s.setcalendarMoments(calendarMoments);
        s.setcalendarDates(calendarDates);
        s.setcalendarCumuls(calendarCumuls);
    }
}
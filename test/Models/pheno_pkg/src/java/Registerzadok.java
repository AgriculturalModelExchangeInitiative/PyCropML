import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import javafx.util.*;
import java.time.LocalDateTime;
public class Registerzadok
{
    private double der;
    public double getder()
    { return der; }

    public void setder(double _der)
    { this.der= _der; } 
    
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
    
    private LocalDateTime sowingDate;
    public LocalDateTime getsowingDate()
    { return sowingDate; }

    public void setsowingDate(LocalDateTime _sowingDate)
    { this.sowingDate= _sowingDate; } 
    
    public Registerzadok() { }
    public void  Calculate_registerzadok(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: RegisterZadok -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: RegisterZadok Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA/LEPSE Montpellier
    //            * Abstract: Record the zadok stage in the calendar
    //    	
        //- inputs:
    //            * name: cumulTT
    //                          ** description : 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 354.582294511779
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: phase
    //                          ** description : instance of the phase class . You can get the name of the phase using phase.getPhaseAsString(PhaseValue) 
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** default : 2
    //                          ** unit : 
    //                          ** uri : some url
    //            * name: leafNumber
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 4.8854219661087575
    //                          ** unit : leaf
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: calendarMoments
    //                          ** description : List containing apparition of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** default : ['Sowing']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarDates
    //                          ** description : List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** default : ['2007/3/21']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarCumuls
    //                          ** description : list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: cumulTTFromZC_65
    //                          ** description : cumul of the thermal time (DeltaTT) since the moment ZC_65
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 0
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: currentdate
    //                          ** description : current date
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DATE
    //                          ** min : 
    //                          ** max : 
    //                          ** default : 2007/4/9
    //                          ** unit : 
    //                          ** uri : some url
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
    //            * name: finalLeafNumber
    //                          ** description : final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 8.797582013199484
    //                          ** unit : leaf
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
    //            * name: sowingDate
    //                          ** description :  Date of Sowing
    //                          ** parametercategory : constant
    //                          ** datatype : DATE
    //                          ** min : 
    //                          ** max : 
    //                          ** default : 2007/3/21
    //                          ** unit : 
    //                          ** inputtype : parameter
        //- outputs:
    //            * name: hasZadokStageChanged
    //                          ** description : true if the zadok stage has changed this time step
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    //                          ** uri : some url
    //            * name: currentZadokStage
    //                          ** description : current zadok stage
    //                          ** variablecategory : state
    //                          ** datatype : STRING
    //                          ** unit :  
    //                          ** uri : some url
    //            * name: calendarMoments
    //                          ** description :  List containing apparition of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** unit : 
    //            * name: calendarDates
    //                          ** description :  List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** unit : 
    //            * name: calendarCumuls
    //                          ** description :  list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** unit : °C d
        double cumulTT = a.getcumulTT();
        double phase = s.getphase();
        double leafNumber = s.getleafNumber();
        List<String> calendarMoments = s.getcalendarMoments();
        List<LocalDateTime> calendarDates = s.getcalendarDates();
        List<Double> calendarCumuls = s.getcalendarCumuls();
        double cumulTTFromZC_65 = a.getcumulTTFromZC_65();
        LocalDateTime currentdate = a.getcurrentdate();
        double finalLeafNumber = s.getfinalLeafNumber();
        String currentZadokStage = s.getcurrentZadokStage();
        int hasZadokStageChanged_t1 = s1.gethasZadokStageChanged();
        int hasZadokStageChanged;
        int roundedFinalLeafNumber;
        roundedFinalLeafNumber = (int)(finalLeafNumber + 0.5d);
        if (leafNumber >= 4.0d && !calendarMoments.contains("MainShootPlus1Tiller"))
        {
            calendarMoments.add("MainShootPlus1Tiller");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus1Tiller";
        }
        else if ( leafNumber >= 5.0d && !calendarMoments.contains("MainShootPlus2Tiller"))
        {
            calendarMoments.add("MainShootPlus2Tiller");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus2Tiller";
        }
        else if ( leafNumber >= 6.0d && !calendarMoments.contains("MainShootPlus3Tiller"))
        {
            calendarMoments.add("MainShootPlus3Tiller");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus3Tiller";
        }
        else if ( finalLeafNumber > 0.0d && (leafNumber >= slopeTSFLN * finalLeafNumber - intTSFLN && !calendarMoments.contains("TerminalSpikelet")))
        {
            calendarMoments.add("TerminalSpikelet");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "TerminalSpikelet";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 4.0d && roundedFinalLeafNumber - 4 > 0 && !calendarMoments.contains("PseudoStemErection"))
        {
            calendarMoments.add("PseudoStemErection");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "PseudoStemErection";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 3.0d && roundedFinalLeafNumber - 3 > 0 && !calendarMoments.contains("1stNodeDetectable"))
        {
            calendarMoments.add("1stNodeDetectable");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "1stNodeDetectable";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 2.0d && roundedFinalLeafNumber - 2 > 0 && !calendarMoments.contains("2ndNodeDetectable"))
        {
            calendarMoments.add("2ndNodeDetectable");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "2ndNodeDetectable";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 1.0d && roundedFinalLeafNumber - 1 > 0 && !calendarMoments.contains("FlagLeafJustVisible"))
        {
            calendarMoments.add("FlagLeafJustVisible");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "FlagLeafJustVisible";
        }
        else if ( !calendarMoments.contains("MidGrainFilling") && (phase == 4.5d && cumulTTFromZC_65 >= der))
        {
            calendarMoments.add("MidGrainFilling");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MidGrainFilling";
        }
        else
        {
            hasZadokStageChanged = 0;
        }
        s.setcalendarMoments(calendarMoments);
        s.setcalendarDates(calendarDates);
        s.setcalendarCumuls(calendarCumuls);
        s.setcurrentZadokStage(currentZadokStage);
        s.sethasZadokStageChanged(hasZadokStageChanged);
    }
}
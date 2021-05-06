using System;
using System.Collections.Generic;
using System.Linq;
public class RegisterZadok
{
    private double _der;
    public double der
        {
            get { return this._der; }
            set { this._der= value; } 
        }
    private double _slopeTSFLN;
    public double slopeTSFLN
        {
            get { return this._slopeTSFLN; }
            set { this._slopeTSFLN= value; } 
        }
    private double _intTSFLN;
    public double intTSFLN
        {
            get { return this._intTSFLN; }
            set { this._intTSFLN= value; } 
        }
    public RegisterZadok() { }
    
    public void  CalculateModel(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
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
    //                          ** description : Slope of the relationship between Haun stage at terminal spikelet and final leaf number
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0.9
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: intTSFLN
    //                          ** description : Intercept of the relationship between Haun stage at terminal spikelet and final leaf number
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 2.6
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
    //            * name: currentZadokStage_t1
    //                          ** description : precedent zadok stage
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
    //                          ** min : 
    //                          ** max : 
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
        double cumulTT = a.cumulTT;
        double phase = s.phase;
        double leafNumber = s.leafNumber;
        List<string> calendarMoments = s.calendarMoments;
        List<DateTime> calendarDates = s.calendarDates;
        List<double> calendarCumuls = s.calendarCumuls;
        double cumulTTFromZC_65 = a.cumulTTFromZC_65;
        DateTime currentdate = a.currentdate;
        double finalLeafNumber = s.finalLeafNumber;
        string currentZadokStage_t1 = s1.currentZadokStage;
        int hasZadokStageChanged_t1 = s1.hasZadokStageChanged;
        int hasZadokStageChanged;
        string currentZadokStage;
        int roundedFinalLeafNumber;
        currentZadokStage = currentZadokStage_t1;
        roundedFinalLeafNumber = (int)(finalLeafNumber + 0.5d);
        if (leafNumber >= 4.0d && !calendarMoments.Contains("MainShootPlus1Tiller"))
        {
            calendarMoments.Add("MainShootPlus1Tiller");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus1Tiller";
        }
        else if ( leafNumber >= 5.0d && !calendarMoments.Contains("MainShootPlus2Tiller"))
        {
            calendarMoments.Add("MainShootPlus2Tiller");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus2Tiller";
        }
        else if ( leafNumber >= 6.0d && !calendarMoments.Contains("MainShootPlus3Tiller"))
        {
            calendarMoments.Add("MainShootPlus3Tiller");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus3Tiller";
        }
        else if ( finalLeafNumber > 0.0d && (leafNumber >= slopeTSFLN * finalLeafNumber - intTSFLN && !calendarMoments.Contains("TerminalSpikelet")))
        {
            calendarMoments.Add("TerminalSpikelet");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "TerminalSpikelet";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 4.0d && roundedFinalLeafNumber - 4 > 0 && !calendarMoments.Contains("PseudoStemErection"))
        {
            calendarMoments.Add("PseudoStemErection");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "PseudoStemErection";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 3.0d && roundedFinalLeafNumber - 3 > 0 && !calendarMoments.Contains("1stNodeDetectable"))
        {
            calendarMoments.Add("1stNodeDetectable");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "1stNodeDetectable";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 2.0d && roundedFinalLeafNumber - 2 > 0 && !calendarMoments.Contains("2ndNodeDetectable"))
        {
            calendarMoments.Add("2ndNodeDetectable");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "2ndNodeDetectable";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 1.0d && roundedFinalLeafNumber - 1 > 0 && !calendarMoments.Contains("FlagLeafJustVisible"))
        {
            calendarMoments.Add("FlagLeafJustVisible");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "FlagLeafJustVisible";
        }
        else if ( !calendarMoments.Contains("MidGrainFilling") && (phase == 4.5d && cumulTTFromZC_65 >= der))
        {
            calendarMoments.Add("MidGrainFilling");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MidGrainFilling";
        }
        else
        {
            hasZadokStageChanged = 0;
        }
        s.calendarMoments= calendarMoments;
        s.calendarDates= calendarDates;
        s.calendarCumuls= calendarCumuls;
        s.hasZadokStageChanged= hasZadokStageChanged;
        s.currentZadokStage= currentZadokStage;
    }
}
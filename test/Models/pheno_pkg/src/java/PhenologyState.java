import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;
public class PhenologyState
{
    private double ptq;
    private String currentZadokStage;
    private int hasFlagLeafLiguleAppeared;
    private int hasZadokStageChanged;
    private List<Double> listPARTTWindowForPTQ;
    private int hasLastPrimordiumAppeared;
    private List<Double> listTTShootWindowForPTQ;
    private List<Double> listTTShootWindowForPTQ1;
    private List<String> calendarMoments;
    private double canopyShootNumber;
    private List<LocalDateTime> calendarDates;
    private List<Integer> leafTillerNumberArray;
    private double vernaprog;
    private double phyllochron;
    private double leafNumber;
    private int numberTillerCohort;
    private List<Double> tilleringProfile;
    private double averageShootNumberPerPlant;
    private double minFinalNumber;
    private double finalLeafNumber;
    private double phase;
    private List<Double> listGAITTWindowForPTQ;
    private List<Double> calendarCumuls;
    private double gAImean;
    private double pastMaxAI;
    private int isMomentRegistredZC_39;
    
    public PhenologyState() { }
    
    public PhenologyState(PhenologyState toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.ptq = toCopy.ptq;
            this.currentZadokStage = toCopy.currentZadokStage;
            this.hasFlagLeafLiguleAppeared = toCopy.hasFlagLeafLiguleAppeared;
            this.hasZadokStageChanged = toCopy.hasZadokStageChanged;
            List <Double> _listPARTTWindowForPTQ = new ArrayList<>();
            for (Double c : toCopy.listPARTTWindowForPTQ)
            {
                _listPARTTWindowForPTQ.add(c);
            }
            this.listPARTTWindowForPTQ = _listPARTTWindowForPTQ;
            this.hasLastPrimordiumAppeared = toCopy.hasLastPrimordiumAppeared;
            List <Double> _listTTShootWindowForPTQ = new ArrayList<>();
            for (Double c : toCopy.listTTShootWindowForPTQ)
            {
                _listTTShootWindowForPTQ.add(c);
            }
            this.listTTShootWindowForPTQ = _listTTShootWindowForPTQ;
            List <Double> _listTTShootWindowForPTQ1 = new ArrayList<>();
            for (Double c : toCopy.listTTShootWindowForPTQ1)
            {
                _listTTShootWindowForPTQ1.add(c);
            }
            this.listTTShootWindowForPTQ1 = _listTTShootWindowForPTQ1;
            List <String> _calendarMoments = new ArrayList<>();
            for (String c : toCopy.calendarMoments)
            {
                _calendarMoments.add(c);
            }
            this.calendarMoments = _calendarMoments;
            this.canopyShootNumber = toCopy.canopyShootNumber;
            List <LocalDateTime> _calendarDates = new ArrayList<>();
            for (LocalDateTime c : toCopy.calendarDates)
            {
                _calendarDates.add(c);
            }
            this.calendarDates = _calendarDates;
            List <Integer> _leafTillerNumberArray = new ArrayList<>();
            for (Integer c : toCopy.leafTillerNumberArray)
            {
                _leafTillerNumberArray.add(c);
            }
            this.leafTillerNumberArray = _leafTillerNumberArray;
            this.vernaprog = toCopy.vernaprog;
            this.phyllochron = toCopy.phyllochron;
            this.leafNumber = toCopy.leafNumber;
            this.numberTillerCohort = toCopy.numberTillerCohort;
            List <Double> _tilleringProfile = new ArrayList<>();
            for (Double c : toCopy.tilleringProfile)
            {
                _tilleringProfile.add(c);
            }
            this.tilleringProfile = _tilleringProfile;
            this.averageShootNumberPerPlant = toCopy.averageShootNumberPerPlant;
            this.minFinalNumber = toCopy.minFinalNumber;
            this.finalLeafNumber = toCopy.finalLeafNumber;
            this.phase = toCopy.phase;
            List <Double> _listGAITTWindowForPTQ = new ArrayList<>();
            for (Double c : toCopy.listGAITTWindowForPTQ)
            {
                _listGAITTWindowForPTQ.add(c);
            }
            this.listGAITTWindowForPTQ = _listGAITTWindowForPTQ;
            List <Double> _calendarCumuls = new ArrayList<>();
            for (Double c : toCopy.calendarCumuls)
            {
                _calendarCumuls.add(c);
            }
            this.calendarCumuls = _calendarCumuls;
            this.gAImean = toCopy.gAImean;
            this.pastMaxAI = toCopy.pastMaxAI;
            this.isMomentRegistredZC_39 = toCopy.isMomentRegistredZC_39;
        }
    }
    public double getptq()
    { return ptq; }

    public void setptq(double _ptq)
    { this.ptq= _ptq; } 
    
    public String getcurrentZadokStage()
    { return currentZadokStage; }

    public void setcurrentZadokStage(String _currentZadokStage)
    { this.currentZadokStage= _currentZadokStage; } 
    
    public int gethasFlagLeafLiguleAppeared()
    { return hasFlagLeafLiguleAppeared; }

    public void sethasFlagLeafLiguleAppeared(int _hasFlagLeafLiguleAppeared)
    { this.hasFlagLeafLiguleAppeared= _hasFlagLeafLiguleAppeared; } 
    
    public int gethasZadokStageChanged()
    { return hasZadokStageChanged; }

    public void sethasZadokStageChanged(int _hasZadokStageChanged)
    { this.hasZadokStageChanged= _hasZadokStageChanged; } 
    
    public List<Double> getlistPARTTWindowForPTQ()
    { return listPARTTWindowForPTQ; }

    public void setlistPARTTWindowForPTQ(List<Double> _listPARTTWindowForPTQ)
    { this.listPARTTWindowForPTQ= _listPARTTWindowForPTQ; } 
    
    public int gethasLastPrimordiumAppeared()
    { return hasLastPrimordiumAppeared; }

    public void sethasLastPrimordiumAppeared(int _hasLastPrimordiumAppeared)
    { this.hasLastPrimordiumAppeared= _hasLastPrimordiumAppeared; } 
    
    public List<Double> getlistTTShootWindowForPTQ()
    { return listTTShootWindowForPTQ; }

    public void setlistTTShootWindowForPTQ(List<Double> _listTTShootWindowForPTQ)
    { this.listTTShootWindowForPTQ= _listTTShootWindowForPTQ; } 
    
    public List<Double> getlistTTShootWindowForPTQ1()
    { return listTTShootWindowForPTQ1; }

    public void setlistTTShootWindowForPTQ1(List<Double> _listTTShootWindowForPTQ1)
    { this.listTTShootWindowForPTQ1= _listTTShootWindowForPTQ1; } 
    
    public List<String> getcalendarMoments()
    { return calendarMoments; }

    public void setcalendarMoments(List<String> _calendarMoments)
    { this.calendarMoments= _calendarMoments; } 
    
    public double getcanopyShootNumber()
    { return canopyShootNumber; }

    public void setcanopyShootNumber(double _canopyShootNumber)
    { this.canopyShootNumber= _canopyShootNumber; } 
    
    public List<LocalDateTime> getcalendarDates()
    { return calendarDates; }

    public void setcalendarDates(List<LocalDateTime> _calendarDates)
    { this.calendarDates= _calendarDates; } 
    
    public List<Integer> getleafTillerNumberArray()
    { return leafTillerNumberArray; }

    public void setleafTillerNumberArray(List<Integer> _leafTillerNumberArray)
    { this.leafTillerNumberArray= _leafTillerNumberArray; } 
    
    public double getvernaprog()
    { return vernaprog; }

    public void setvernaprog(double _vernaprog)
    { this.vernaprog= _vernaprog; } 
    
    public double getphyllochron()
    { return phyllochron; }

    public void setphyllochron(double _phyllochron)
    { this.phyllochron= _phyllochron; } 
    
    public double getleafNumber()
    { return leafNumber; }

    public void setleafNumber(double _leafNumber)
    { this.leafNumber= _leafNumber; } 
    
    public int getnumberTillerCohort()
    { return numberTillerCohort; }

    public void setnumberTillerCohort(int _numberTillerCohort)
    { this.numberTillerCohort= _numberTillerCohort; } 
    
    public List<Double> gettilleringProfile()
    { return tilleringProfile; }

    public void settilleringProfile(List<Double> _tilleringProfile)
    { this.tilleringProfile= _tilleringProfile; } 
    
    public double getaverageShootNumberPerPlant()
    { return averageShootNumberPerPlant; }

    public void setaverageShootNumberPerPlant(double _averageShootNumberPerPlant)
    { this.averageShootNumberPerPlant= _averageShootNumberPerPlant; } 
    
    public double getminFinalNumber()
    { return minFinalNumber; }

    public void setminFinalNumber(double _minFinalNumber)
    { this.minFinalNumber= _minFinalNumber; } 
    
    public double getfinalLeafNumber()
    { return finalLeafNumber; }

    public void setfinalLeafNumber(double _finalLeafNumber)
    { this.finalLeafNumber= _finalLeafNumber; } 
    
    public double getphase()
    { return phase; }

    public void setphase(double _phase)
    { this.phase= _phase; } 
    
    public List<Double> getlistGAITTWindowForPTQ()
    { return listGAITTWindowForPTQ; }

    public void setlistGAITTWindowForPTQ(List<Double> _listGAITTWindowForPTQ)
    { this.listGAITTWindowForPTQ= _listGAITTWindowForPTQ; } 
    
    public List<Double> getcalendarCumuls()
    { return calendarCumuls; }

    public void setcalendarCumuls(List<Double> _calendarCumuls)
    { this.calendarCumuls= _calendarCumuls; } 
    
    public double getgAImean()
    { return gAImean; }

    public void setgAImean(double _gAImean)
    { this.gAImean= _gAImean; } 
    
    public double getpastMaxAI()
    { return pastMaxAI; }

    public void setpastMaxAI(double _pastMaxAI)
    { this.pastMaxAI= _pastMaxAI; } 
    
    public int getisMomentRegistredZC_39()
    { return isMomentRegistredZC_39; }

    public void setisMomentRegistredZC_39(int _isMomentRegistredZC_39)
    { this.isMomentRegistredZC_39= _isMomentRegistredZC_39; } 
    
}
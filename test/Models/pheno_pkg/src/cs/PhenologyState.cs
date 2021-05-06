using System;
using System.Collections.Generic;
public class PhenologyState
{
    private double _ptq;
    private string _currentZadokStage;
    private int _hasFlagLeafLiguleAppeared;
    private int _hasZadokStageChanged;
    private List<double> _listPARTTWindowForPTQ = new List<double>();
    private int _hasLastPrimordiumAppeared;
    private List<double> _listTTShootWindowForPTQ = new List<double>();
    private List<double> _listTTShootWindowForPTQ1 = new List<double>();
    private List<string> _calendarMoments = new List<string>();
    private double _canopyShootNumber;
    private List<DateTime> _calendarDates = new List<DateTime>();
    private List<int> _leafTillerNumberArray = new List<int>();
    private double _vernaprog;
    private double _phyllochron;
    private double _leafNumber;
    private int _numberTillerCohort;
    private List<double> _tilleringProfile = new List<double>();
    private double _averageShootNumberPerPlant;
    private double _minFinalNumber;
    private double _finalLeafNumber;
    private double _phase;
    private List<double> _listGAITTWindowForPTQ = new List<double>();
    private List<double> _calendarCumuls = new List<double>();
    private double _gAImean;
    private double _pastMaxAI;
    private int _isMomentRegistredZC_39;
    
    public PhenologyState() { }
    
    
    public PhenologyState(PhenologyState toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    _ptq = toCopy._ptq;
    _currentZadokStage = toCopy._currentZadokStage;
    _hasFlagLeafLiguleAppeared = toCopy._hasFlagLeafLiguleAppeared;
    _hasZadokStageChanged = toCopy._hasZadokStageChanged;
    listPARTTWindowForPTQ = new List<double>();
        for (int i = 0; i < toCopy.listPARTTWindowForPTQ.Count; i++)
        { listPARTTWindowForPTQ.Add(toCopy.listPARTTWindowForPTQ[i]); }
    
    _hasLastPrimordiumAppeared = toCopy._hasLastPrimordiumAppeared;
    listTTShootWindowForPTQ = new List<double>();
        for (int i = 0; i < toCopy.listTTShootWindowForPTQ.Count; i++)
        { listTTShootWindowForPTQ.Add(toCopy.listTTShootWindowForPTQ[i]); }
    
    listTTShootWindowForPTQ1 = new List<double>();
        for (int i = 0; i < toCopy.listTTShootWindowForPTQ1.Count; i++)
        { listTTShootWindowForPTQ1.Add(toCopy.listTTShootWindowForPTQ1[i]); }
    
    calendarMoments = new List<string>();
        for (int i = 0; i < toCopy.calendarMoments.Count; i++)
        { calendarMoments.Add(toCopy.calendarMoments[i]); }
    
    _canopyShootNumber = toCopy._canopyShootNumber;
    calendarDates = new List<DateTime>();
        for (int i = 0; i < toCopy.calendarDates.Count; i++)
        { calendarDates.Add(toCopy.calendarDates[i]); }
    
    leafTillerNumberArray = new List<int>();
        for (int i = 0; i < toCopy.leafTillerNumberArray.Count; i++)
        { leafTillerNumberArray.Add(toCopy.leafTillerNumberArray[i]); }
    
    _vernaprog = toCopy._vernaprog;
    _phyllochron = toCopy._phyllochron;
    _leafNumber = toCopy._leafNumber;
    _numberTillerCohort = toCopy._numberTillerCohort;
    tilleringProfile = new List<double>();
        for (int i = 0; i < toCopy.tilleringProfile.Count; i++)
        { tilleringProfile.Add(toCopy.tilleringProfile[i]); }
    
    _averageShootNumberPerPlant = toCopy._averageShootNumberPerPlant;
    _minFinalNumber = toCopy._minFinalNumber;
    _finalLeafNumber = toCopy._finalLeafNumber;
    _phase = toCopy._phase;
    listGAITTWindowForPTQ = new List<double>();
        for (int i = 0; i < toCopy.listGAITTWindowForPTQ.Count; i++)
        { listGAITTWindowForPTQ.Add(toCopy.listGAITTWindowForPTQ[i]); }
    
    calendarCumuls = new List<double>();
        for (int i = 0; i < toCopy.calendarCumuls.Count; i++)
        { calendarCumuls.Add(toCopy.calendarCumuls[i]); }
    
    _gAImean = toCopy._gAImean;
    _pastMaxAI = toCopy._pastMaxAI;
    _isMomentRegistredZC_39 = toCopy._isMomentRegistredZC_39;
    }
    }
    public double ptq
    {
        get { return this._ptq; }
        set { this._ptq= value; } 
    }
    public string currentZadokStage
    {
        get { return this._currentZadokStage; }
        set { this._currentZadokStage= value; } 
    }
    public int hasFlagLeafLiguleAppeared
    {
        get { return this._hasFlagLeafLiguleAppeared; }
        set { this._hasFlagLeafLiguleAppeared= value; } 
    }
    public int hasZadokStageChanged
    {
        get { return this._hasZadokStageChanged; }
        set { this._hasZadokStageChanged= value; } 
    }
    public List<double> listPARTTWindowForPTQ
    {
        get { return this._listPARTTWindowForPTQ; }
        set { this._listPARTTWindowForPTQ= value; } 
    }
    public int hasLastPrimordiumAppeared
    {
        get { return this._hasLastPrimordiumAppeared; }
        set { this._hasLastPrimordiumAppeared= value; } 
    }
    public List<double> listTTShootWindowForPTQ
    {
        get { return this._listTTShootWindowForPTQ; }
        set { this._listTTShootWindowForPTQ= value; } 
    }
    public List<double> listTTShootWindowForPTQ1
    {
        get { return this._listTTShootWindowForPTQ1; }
        set { this._listTTShootWindowForPTQ1= value; } 
    }
    public List<string> calendarMoments
    {
        get { return this._calendarMoments; }
        set { this._calendarMoments= value; } 
    }
    public double canopyShootNumber
    {
        get { return this._canopyShootNumber; }
        set { this._canopyShootNumber= value; } 
    }
    public List<DateTime> calendarDates
    {
        get { return this._calendarDates; }
        set { this._calendarDates= value; } 
    }
    public List<int> leafTillerNumberArray
    {
        get { return this._leafTillerNumberArray; }
        set { this._leafTillerNumberArray= value; } 
    }
    public double vernaprog
    {
        get { return this._vernaprog; }
        set { this._vernaprog= value; } 
    }
    public double phyllochron
    {
        get { return this._phyllochron; }
        set { this._phyllochron= value; } 
    }
    public double leafNumber
    {
        get { return this._leafNumber; }
        set { this._leafNumber= value; } 
    }
    public int numberTillerCohort
    {
        get { return this._numberTillerCohort; }
        set { this._numberTillerCohort= value; } 
    }
    public List<double> tilleringProfile
    {
        get { return this._tilleringProfile; }
        set { this._tilleringProfile= value; } 
    }
    public double averageShootNumberPerPlant
    {
        get { return this._averageShootNumberPerPlant; }
        set { this._averageShootNumberPerPlant= value; } 
    }
    public double minFinalNumber
    {
        get { return this._minFinalNumber; }
        set { this._minFinalNumber= value; } 
    }
    public double finalLeafNumber
    {
        get { return this._finalLeafNumber; }
        set { this._finalLeafNumber= value; } 
    }
    public double phase
    {
        get { return this._phase; }
        set { this._phase= value; } 
    }
    public List<double> listGAITTWindowForPTQ
    {
        get { return this._listGAITTWindowForPTQ; }
        set { this._listGAITTWindowForPTQ= value; } 
    }
    public List<double> calendarCumuls
    {
        get { return this._calendarCumuls; }
        set { this._calendarCumuls= value; } 
    }
    public double gAImean
    {
        get { return this._gAImean; }
        set { this._gAImean= value; } 
    }
    public double pastMaxAI
    {
        get { return this._pastMaxAI; }
        set { this._pastMaxAI= value; } 
    }
    public int isMomentRegistredZC_39
    {
        get { return this._isMomentRegistredZC_39; }
        set { this._isMomentRegistredZC_39= value; } 
    }
}
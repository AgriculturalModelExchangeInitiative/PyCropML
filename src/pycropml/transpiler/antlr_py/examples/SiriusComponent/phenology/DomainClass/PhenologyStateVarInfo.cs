
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualityPhenology.DomainClass
{
    public class PhenologyStateVarInfo : IVarInfoClass
    {
        static VarInfo _phyllochron = new VarInfo();
        static VarInfo _minFinalNumber = new VarInfo();
        static VarInfo _calendarDates = new VarInfo();
        static VarInfo _calendarMoments = new VarInfo();
        static VarInfo _ptq = new VarInfo();
        static VarInfo _leafNumber = new VarInfo();
        static VarInfo _pastMaxAI = new VarInfo();
        static VarInfo _listGAITTWindowForPTQ = new VarInfo();
        static VarInfo _listPARTTWindowForPTQ = new VarInfo();
        static VarInfo _listTTShootWindowForPTQ1 = new VarInfo();
        static VarInfo _listTTShootWindowForPTQ = new VarInfo();
        static VarInfo _calendarCumuls = new VarInfo();
        static VarInfo _vernaprog = new VarInfo();
        static VarInfo _hasLastPrimordiumAppeared = new VarInfo();
        static VarInfo _phase = new VarInfo();
        static VarInfo _finalLeafNumber = new VarInfo();
        static VarInfo _hasZadokStageChanged = new VarInfo();
        static VarInfo _currentZadokStage = new VarInfo();
        static VarInfo _hasFlagLeafLiguleAppeared = new VarInfo();
        static VarInfo _tilleringProfile = new VarInfo();
        static VarInfo _leafTillerNumberArray = new VarInfo();
        static VarInfo _canopyShootNumber = new VarInfo();
        static VarInfo _numberTillerCohort = new VarInfo();
        static VarInfo _averageShootNumberPerPlant = new VarInfo();
        static VarInfo _gAImean = new VarInfo();
        static VarInfo _isMomentRegistredZC_39 = new VarInfo();

        static PhenologyStateVarInfo()
        {
            PhenologyStateVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "PhenologyState Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "PhenologyState";}
        }

        public static  VarInfo phyllochron
        {
            get { return _phyllochron;}
        }

        public static  VarInfo minFinalNumber
        {
            get { return _minFinalNumber;}
        }

        public static  VarInfo calendarDates
        {
            get { return _calendarDates;}
        }

        public static  VarInfo calendarMoments
        {
            get { return _calendarMoments;}
        }

        public static  VarInfo ptq
        {
            get { return _ptq;}
        }

        public static  VarInfo leafNumber
        {
            get { return _leafNumber;}
        }

        public static  VarInfo pastMaxAI
        {
            get { return _pastMaxAI;}
        }

        public static  VarInfo listGAITTWindowForPTQ
        {
            get { return _listGAITTWindowForPTQ;}
        }

        public static  VarInfo listPARTTWindowForPTQ
        {
            get { return _listPARTTWindowForPTQ;}
        }

        public static  VarInfo listTTShootWindowForPTQ1
        {
            get { return _listTTShootWindowForPTQ1;}
        }

        public static  VarInfo listTTShootWindowForPTQ
        {
            get { return _listTTShootWindowForPTQ;}
        }

        public static  VarInfo calendarCumuls
        {
            get { return _calendarCumuls;}
        }

        public static  VarInfo vernaprog
        {
            get { return _vernaprog;}
        }

        public static  VarInfo hasLastPrimordiumAppeared
        {
            get { return _hasLastPrimordiumAppeared;}
        }

        public static  VarInfo phase
        {
            get { return _phase;}
        }

        public static  VarInfo finalLeafNumber
        {
            get { return _finalLeafNumber;}
        }

        public static  VarInfo hasZadokStageChanged
        {
            get { return _hasZadokStageChanged;}
        }

        public static  VarInfo currentZadokStage
        {
            get { return _currentZadokStage;}
        }

        public static  VarInfo hasFlagLeafLiguleAppeared
        {
            get { return _hasFlagLeafLiguleAppeared;}
        }

        public static  VarInfo tilleringProfile
        {
            get { return _tilleringProfile;}
        }

        public static  VarInfo leafTillerNumberArray
        {
            get { return _leafTillerNumberArray;}
        }

        public static  VarInfo canopyShootNumber
        {
            get { return _canopyShootNumber;}
        }

        public static  VarInfo numberTillerCohort
        {
            get { return _numberTillerCohort;}
        }

        public static  VarInfo averageShootNumberPerPlant
        {
            get { return _averageShootNumberPerPlant;}
        }

        public static  VarInfo gAImean
        {
            get { return _gAImean;}
        }

        public static  VarInfo isMomentRegistredZC_39
        {
            get { return _isMomentRegistredZC_39;}
        }

        static void DescribeVariables()
        {
            _phyllochron.Name = "phyllochron";
            _phyllochron.Description = "phyllochron";
            _phyllochron.MaxValue = 1000;
            _phyllochron.MinValue = 0;
            _phyllochron.DefaultValue = 0;
            _phyllochron.Units = "°C d leaf-1";
            _phyllochron.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _minFinalNumber.Name = "minFinalNumber";
            _minFinalNumber.Description = "minimum final leaf number";
            _minFinalNumber.MaxValue = 25;
            _minFinalNumber.MinValue = 0;
            _minFinalNumber.DefaultValue = 5.5;
            _minFinalNumber.Units = "leaf";
            _minFinalNumber.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _calendarDates.Name = "calendarDates";
            _calendarDates.Description = "List containing  the dates of the wheat developmental phases";
            _calendarDates.MaxValue = -1D;
            _calendarDates.MinValue = -1D;
            _calendarDates.DefaultValue = -1D;
            _calendarDates.Units = "";
            _calendarDates.ValueType = VarInfoValueTypes.GetInstanceForName("ListDate");

            _calendarMoments.Name = "calendarMoments";
            _calendarMoments.Description = "List containing appearance of each stage";
            _calendarMoments.MaxValue = -1D;
            _calendarMoments.MinValue = -1D;
            _calendarMoments.DefaultValue = -1D;
            _calendarMoments.Units = "";
            _calendarMoments.ValueType = VarInfoValueTypes.GetInstanceForName("ListString");

            _ptq.Name = "ptq";
            _ptq.Description = "Photothermal quotient ";
            _ptq.MaxValue = 10000.0;
            _ptq.MinValue = 0.0;
            _ptq.DefaultValue = 0.0;
            _ptq.Units = "MJ °C-1 d-1 m-2)";
            _ptq.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _leafNumber.Name = "leafNumber";
            _leafNumber.Description = "Actual number of phytomers";
            _leafNumber.MaxValue = 25;
            _leafNumber.MinValue = 0;
            _leafNumber.DefaultValue = 0;
            _leafNumber.Units = "leaf";
            _leafNumber.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _pastMaxAI.Name = "pastMaxAI";
            _pastMaxAI.Description = "Maximum Leaf Area Index reached the current day";
            _pastMaxAI.MaxValue = 5000.0;
            _pastMaxAI.MinValue = 0.0;
            _pastMaxAI.DefaultValue = 0.0;
            _pastMaxAI.Units = "m2 leaf m-2 ground";
            _pastMaxAI.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _listGAITTWindowForPTQ.Name = "listGAITTWindowForPTQ";
            _listGAITTWindowForPTQ.Description = "List of daily Green Area Index in the window dedicated to average";
            _listGAITTWindowForPTQ.MaxValue = -1D;
            _listGAITTWindowForPTQ.MinValue = -1D;
            _listGAITTWindowForPTQ.DefaultValue = -1D;
            _listGAITTWindowForPTQ.Units = "m2 leaf m-2 ground";
            _listGAITTWindowForPTQ.ValueType = VarInfoValueTypes.GetInstanceForName("ListDouble");

            _listPARTTWindowForPTQ.Name = "listPARTTWindowForPTQ";
            _listPARTTWindowForPTQ.Description = "List of Daily PAR during TTWindowForPTQ thermal time period";
            _listPARTTWindowForPTQ.MaxValue = -1D;
            _listPARTTWindowForPTQ.MinValue = -1D;
            _listPARTTWindowForPTQ.DefaultValue = -1D;
            _listPARTTWindowForPTQ.Units = "MJ m2 d";
            _listPARTTWindowForPTQ.ValueType = VarInfoValueTypes.GetInstanceForName("ListDouble");

            _listTTShootWindowForPTQ1.Name = "listTTShootWindowForPTQ1";
            _listTTShootWindowForPTQ1.Description = "List of daily shoot thermal time in the window dedicated to average";
            _listTTShootWindowForPTQ1.MaxValue = -1D;
            _listTTShootWindowForPTQ1.MinValue = -1D;
            _listTTShootWindowForPTQ1.DefaultValue = -1D;
            _listTTShootWindowForPTQ1.Units = "°C d";
            _listTTShootWindowForPTQ1.ValueType = VarInfoValueTypes.GetInstanceForName("ListDouble");

            _listTTShootWindowForPTQ.Name = "listTTShootWindowForPTQ";
            _listTTShootWindowForPTQ.Description = "List of Daily Shoot thermal time during TTWindowForPTQ thermal time period";
            _listTTShootWindowForPTQ.MaxValue = -1D;
            _listTTShootWindowForPTQ.MinValue = -1D;
            _listTTShootWindowForPTQ.DefaultValue = -1D;
            _listTTShootWindowForPTQ.Units = "°C d";
            _listTTShootWindowForPTQ.ValueType = VarInfoValueTypes.GetInstanceForName("ListDouble");

            _calendarCumuls.Name = "calendarCumuls";
            _calendarCumuls.Description = "list containing for each stage occured its cumulated thermal times";
            _calendarCumuls.MaxValue = -1D;
            _calendarCumuls.MinValue = -1D;
            _calendarCumuls.DefaultValue = -1D;
            _calendarCumuls.Units = "°C d";
            _calendarCumuls.ValueType = VarInfoValueTypes.GetInstanceForName("ListDouble");

            _vernaprog.Name = "vernaprog";
            _vernaprog.Description = "progression on a 0  to 1 scale of the vernalization";
            _vernaprog.MaxValue = 1;
            _vernaprog.MinValue = 0;
            _vernaprog.DefaultValue =  0.5517254187376879;
            _vernaprog.Units = "";
            _vernaprog.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _hasLastPrimordiumAppeared.Name = "hasLastPrimordiumAppeared";
            _hasLastPrimordiumAppeared.Description = "if Last Primordium has Appeared";
            _hasLastPrimordiumAppeared.MaxValue = 1;
            _hasLastPrimordiumAppeared.MinValue = 0;
            _hasLastPrimordiumAppeared.DefaultValue = 0;
            _hasLastPrimordiumAppeared.Units = "";
            _hasLastPrimordiumAppeared.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            _phase.Name = "phase";
            _phase.Description = " the name of the phase";
            _phase.MaxValue = 7;
            _phase.MinValue = 0;
            _phase.DefaultValue = 1;
            _phase.Units = "";
            _phase.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _finalLeafNumber.Name = "finalLeafNumber";
            _finalLeafNumber.Description = "final leaf number";
            _finalLeafNumber.MaxValue = 25;
            _finalLeafNumber.MinValue = 0;
            _finalLeafNumber.DefaultValue = 0;
            _finalLeafNumber.Units = "leaf";
            _finalLeafNumber.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _hasZadokStageChanged.Name = "hasZadokStageChanged";
            _hasZadokStageChanged.Description = "true if the zadok stage has changed this time step";
            _hasZadokStageChanged.MaxValue = 1;
            _hasZadokStageChanged.MinValue = 0;
            _hasZadokStageChanged.DefaultValue = 0;
            _hasZadokStageChanged.Units = "";
            _hasZadokStageChanged.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            _currentZadokStage.Name = "currentZadokStage";
            _currentZadokStage.Description = "zadok stage";
            _currentZadokStage.MaxValue = -1D;
            _currentZadokStage.MinValue = -1D;
            _currentZadokStage.DefaultValue = -1D;
            _currentZadokStage.Units = "";
            _currentZadokStage.ValueType = VarInfoValueTypes.GetInstanceForName("String");

            _hasFlagLeafLiguleAppeared.Name = "hasFlagLeafLiguleAppeared";
            _hasFlagLeafLiguleAppeared.Description = "true if flag leaf has appeared (leafnumber reached finalLeafNumber)";
            _hasFlagLeafLiguleAppeared.MaxValue = 1;
            _hasFlagLeafLiguleAppeared.MinValue = 0;
            _hasFlagLeafLiguleAppeared.DefaultValue = 1;
            _hasFlagLeafLiguleAppeared.Units = "";
            _hasFlagLeafLiguleAppeared.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            _tilleringProfile.Name = "tilleringProfile";
            _tilleringProfile.Description = " store the amount of new tiller created at each time a new tiller appears";
            _tilleringProfile.MaxValue = -1D;
            _tilleringProfile.MinValue = -1D;
            _tilleringProfile.DefaultValue = -1D;
            _tilleringProfile.Units = "";
            _tilleringProfile.ValueType = VarInfoValueTypes.GetInstanceForName("ListDouble");

            _leafTillerNumberArray.Name = "leafTillerNumberArray";
            _leafTillerNumberArray.Description = "store the number of tiller for each leaf layer";
            _leafTillerNumberArray.MaxValue = -1D;
            _leafTillerNumberArray.MinValue = -1D;
            _leafTillerNumberArray.DefaultValue = -1D;
            _leafTillerNumberArray.Units = "leaf";
            _leafTillerNumberArray.ValueType = VarInfoValueTypes.GetInstanceForName("ListInteger");

            _canopyShootNumber.Name = "canopyShootNumber";
            _canopyShootNumber.Description = "shoot number for the whole canopy";
            _canopyShootNumber.MaxValue = 10000;
            _canopyShootNumber.MinValue = 0;
            _canopyShootNumber.DefaultValue = 288.0;
            _canopyShootNumber.Units = "shoot m-2";
            _canopyShootNumber.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _numberTillerCohort.Name = "numberTillerCohort";
            _numberTillerCohort.Description = "Number of tiller which appears";
            _numberTillerCohort.MaxValue = 10000;
            _numberTillerCohort.MinValue = 0;
            _numberTillerCohort.DefaultValue = -1D;
            _numberTillerCohort.Units = "dimensionless";
            _numberTillerCohort.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            _averageShootNumberPerPlant.Name = "averageShootNumberPerPlant";
            _averageShootNumberPerPlant.Description = "average shoot number per plant in the canopy";
            _averageShootNumberPerPlant.MaxValue = 10000;
            _averageShootNumberPerPlant.MinValue = 0;
            _averageShootNumberPerPlant.DefaultValue = -1D;
            _averageShootNumberPerPlant.Units = "shoot m-2";
            _averageShootNumberPerPlant.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _gAImean.Name = "gAImean";
            _gAImean.Description = "Mean Green Area Index";
            _gAImean.MaxValue = 500.0;
            _gAImean.MinValue = 0.0;
            _gAImean.DefaultValue = -1D;
            _gAImean.Units = "m2 leaf m-2 ground";
            _gAImean.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _isMomentRegistredZC_39.Name = "isMomentRegistredZC_39";
            _isMomentRegistredZC_39.Description = " if Flag leaf ligule has already appeared ";
            _isMomentRegistredZC_39.MaxValue = 1;
            _isMomentRegistredZC_39.MinValue = 0;
            _isMomentRegistredZC_39.DefaultValue = -1D;
            _isMomentRegistredZC_39.Units = "";
            _isMomentRegistredZC_39.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

        }

    }
}
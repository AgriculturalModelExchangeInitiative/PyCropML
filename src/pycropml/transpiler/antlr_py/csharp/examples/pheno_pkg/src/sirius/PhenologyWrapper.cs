using System;
using System.Collections.Generic;
using System.Linq;
using SQCrop2ML_Phenology.DomainClass;
using SQCrop2ML_Phenology.Strategies;

namespace SiriusModel.Model.Phenology
{
    class PhenologyWrapper :  UniverseLink
    {
        private PhenologyState s;
        private PhenologyRate r;
        private PhenologyAuxiliary a;
        private PhenologyComponent phenologyComponent;

        public PhenologyWrapper(Universe universe) : base(universe)
        {
            s = new PhenologyState();
            r = new PhenologyRate();
            a = new PhenologyAuxiliary();
            phenologyComponent = new Phenology();
            loadParameters();
        }

        public double phyllochron{ get { return s.phyllochron;}} 
     
        public double minFinalNumber{ get { return s.minFinalNumber;}} 
     
        public List<DateTime> calendarDates{ get { return s.calendarDates;}} 
     
        public List<string> calendarMoments{ get { return s.calendarMoments;}} 
     
        public double ptq{ get { return s.ptq;}} 
     
        public double leafNumber{ get { return s.leafNumber;}} 
     
        public double pastMaxAI{ get { return s.pastMaxAI;}} 
     
        public List<double> listGAITTWindowForPTQ{ get { return s.listGAITTWindowForPTQ;}} 
     
        public List<double> listPARTTWindowForPTQ{ get { return s.listPARTTWindowForPTQ;}} 
     
        public List<double> listTTShootWindowForPTQ1{ get { return s.listTTShootWindowForPTQ1;}} 
     
        public List<double> listTTShootWindowForPTQ{ get { return s.listTTShootWindowForPTQ;}} 
     
        public List<double> calendarCumuls{ get { return s.calendarCumuls;}} 
     
        public double vernaprog{ get { return s.vernaprog;}} 
     
        public int hasLastPrimordiumAppeared{ get { return s.hasLastPrimordiumAppeared;}} 
     
        public double phase{ get { return s.phase;}} 
     
        public double finalLeafNumber{ get { return s.finalLeafNumber;}} 
     
        public int hasZadokStageChanged{ get { return s.hasZadokStageChanged;}} 
     
        public string currentZadokStage{ get { return s.currentZadokStage;}} 
     
        public List<double> tilleringProfile{ get { return s.tilleringProfile;}} 
     
        public List<int> leafTillerNumberArray{ get { return s.leafTillerNumberArray;}} 
     
        public double canopyShootNumber{ get { return s.canopyShootNumber;}} 
     
        public int numberTillerCohort{ get { return s.numberTillerCohort;}} 
     
        public double averageShootNumberPerPlant{ get { return s.averageShootNumberPerPlant;}} 
     
        public double gAImean{ get { return s.gAImean;}} 
     
        public int hasFlagLeafLiguleAppeared{ get { return s.hasFlagLeafLiguleAppeared;}} 
     

        public PhenologyWrapper(Universe universe, PhenologyWrapper toCopy, bool copyAll) : base(universe)
        {
            s = (toCopy.s != null) ? new PhenologyState(toCopy.s, copyAll) : null;
            r = (toCopy.r != null) ? new PhenologyRate(toCopy.r, copyAll) : null;
            a = (toCopy.a != null) ? new PhenologyAuxiliary(toCopy.a, copyAll) : null;
            if (copyAll)
            {
                phenologyComponent = (toCopy.phenologyComponent != null) ? new Phenology(toCopy.phenologyComponent) : null;
            }
        }

        public void Init(){
            phenologyComponent.Init(s, r, a);
            loadParameters();
        }

        private void loadParameters()
        {
            phenologyComponent.aMXLFNO = aMXLFNO;
            phenologyComponent.pNini = pNini;
            phenologyComponent.sDsa_sh = sDsa_sh;
            phenologyComponent.latitude = latitude;
            phenologyComponent.kl = kl;
            phenologyComponent.lincr = lincr;
            phenologyComponent.ldecr = ldecr;
            phenologyComponent.pincr = pincr;
            phenologyComponent.pTQhf = pTQhf;
            phenologyComponent.B = B;
            phenologyComponent.areaSL = areaSL;
            phenologyComponent.areaSS = areaSS;
            phenologyComponent.lARmin = lARmin;
            phenologyComponent.sowingDensity = sowingDensity;
            phenologyComponent.lARmax = lARmax;
            phenologyComponent.lNeff = lNeff;
            phenologyComponent.rp = rp;
            phenologyComponent.p = p;
            phenologyComponent.pdecr = pdecr;
            phenologyComponent.maxTvern = maxTvern;
            phenologyComponent.tTWindowForPTQ = tTWindowForPTQ;
            phenologyComponent.vBEE = vBEE;
            phenologyComponent.isVernalizable = isVernalizable;
            phenologyComponent.minTvern = minTvern;
            phenologyComponent.intTvern = intTvern;
            phenologyComponent.vAI = vAI;
            phenologyComponent.maxDL = maxDL;
            phenologyComponent.choosePhyllUse = choosePhyllUse;
            phenologyComponent.minDL = minDL;
            phenologyComponent.pFLLAnth = pFLLAnth;
            phenologyComponent.dcd = dcd;
            phenologyComponent.dgf = dgf;
            phenologyComponent.degfm = degfm;
            phenologyComponent.ignoreGrainMaturation = ignoreGrainMaturation;
            phenologyComponent.pHEADANTH = pHEADANTH;
            phenologyComponent.sLDL = sLDL;
            phenologyComponent.sowingDay = sowingDay;
            phenologyComponent.sDws = sDws;
            phenologyComponent.sDsa_nh = sDsa_nh;
            phenologyComponent.der = der;
            phenologyComponent.targetFertileShoot = targetFertileShoot;
            phenologyComponent.dse = dse;
            phenologyComponent.slopeTSFLN = slopeTSFLN;
            phenologyComponent.intTSFLN = intTSFLN;
        }

        public void EstimatePhenology(DateTime currentdate, double cumulTT, double dayLength, double deltaTT, double gAI, double pAR, double grainCumulTT)
        {
            a.currentdate = currentdate;
            a.cumulTT = cumulTT;
            a.dayLength = dayLength;
            a.deltaTT = deltaTT;
            a.gAI = gAI;
            a.pAR = pAR;
            a.grainCumulTT = grainCumulTT;
            phenologyComponent.CalculateModel(s,s1, r, a);
        }

    }

}
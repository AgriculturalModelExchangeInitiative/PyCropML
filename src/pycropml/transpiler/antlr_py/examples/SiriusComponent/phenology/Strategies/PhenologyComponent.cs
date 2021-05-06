
using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml;
using CRA.ModelLayer.MetadataTypes;
using CRA.ModelLayer.Core;
using CRA.ModelLayer.Strategy;
using System.Reflection;
using VarInfo=CRA.ModelLayer.Core.VarInfo;
using Preconditions=CRA.ModelLayer.Core.Preconditions;
using CRA.AgroManagement;       

using SiriusQualityPhenology.DomainClass;
namespace SiriusQualityPhenology.Strategies
{
    public class PhenologyComponent : IStrategySiriusQualityPhenology
    {
        public PhenologyComponent()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new CompositeStrategyVarInfo(_VernalizationProgress, "aMXLFNO");
            _parameters0_0.Add(v1);
            VarInfo v2 = new CompositeStrategyVarInfo(_VernalizationProgress, "pNini");
            _parameters0_0.Add(v2);
            VarInfo v3 = new CompositeStrategyVarInfo(_PhylSowingDateCorrection, "sDsa_sh");
            _parameters0_0.Add(v3);
            VarInfo v4 = new CompositeStrategyVarInfo(_PhylSowingDateCorrection, "latitude");
            _parameters0_0.Add(v4);
            VarInfo v5 = new CompositeStrategyVarInfo(_Phyllochron, "kl");
            _parameters0_0.Add(v5);
            VarInfo v6 = new CompositeStrategyVarInfo(_PTQ, "kl");
            _parameters0_0.Add(v6);
            VarInfo v7 = new CompositeStrategyVarInfo(_Phyllochron, "lincr");
            _parameters0_0.Add(v7);
            VarInfo v8 = new CompositeStrategyVarInfo(_Phyllochron, "ldecr");
            _parameters0_0.Add(v8);
            VarInfo v9 = new CompositeStrategyVarInfo(_Phyllochron, "pincr");
            _parameters0_0.Add(v9);
            VarInfo v10 = new CompositeStrategyVarInfo(_Phyllochron, "pTQhf");
            _parameters0_0.Add(v10);
            VarInfo v11 = new CompositeStrategyVarInfo(_Phyllochron, "B");
            _parameters0_0.Add(v11);
            VarInfo v12 = new CompositeStrategyVarInfo(_Phyllochron, "areaSL");
            _parameters0_0.Add(v12);
            VarInfo v13 = new CompositeStrategyVarInfo(_Phyllochron, "areaSS");
            _parameters0_0.Add(v13);
            VarInfo v14 = new CompositeStrategyVarInfo(_Phyllochron, "lARmin");
            _parameters0_0.Add(v14);
            VarInfo v15 = new CompositeStrategyVarInfo(_Phyllochron, "sowingDensity");
            _parameters0_0.Add(v15);
            VarInfo v16 = new CompositeStrategyVarInfo(_ShootNumber, "sowingDensity");
            _parameters0_0.Add(v16);
            VarInfo v17 = new CompositeStrategyVarInfo(_Phyllochron, "lARmax");
            _parameters0_0.Add(v17);
            VarInfo v18 = new CompositeStrategyVarInfo(_Phyllochron, "lNeff");
            _parameters0_0.Add(v18);
            VarInfo v19 = new CompositeStrategyVarInfo(_PhylSowingDateCorrection, "rp");
            _parameters0_0.Add(v19);
            VarInfo v20 = new CompositeStrategyVarInfo(_Phyllochron, "p");
            _parameters0_0.Add(v20);
            VarInfo v21 = new CompositeStrategyVarInfo(_PhylSowingDateCorrection, "p");
            _parameters0_0.Add(v21);
            VarInfo v22 = new CompositeStrategyVarInfo(_UpdatePhase, "p");
            _parameters0_0.Add(v22);
            VarInfo v23 = new CompositeStrategyVarInfo(_Phyllochron, "pdecr");
            _parameters0_0.Add(v23);
            VarInfo v24 = new CompositeStrategyVarInfo(_VernalizationProgress, "maxTvern");
            _parameters0_0.Add(v24);
            VarInfo v25 = new CompositeStrategyVarInfo(_GAImean, "tTWindowForPTQ");
            _parameters0_0.Add(v25);
            VarInfo v26 = new CompositeStrategyVarInfo(_PTQ, "tTWindowForPTQ");
            _parameters0_0.Add(v26);
            VarInfo v27 = new CompositeStrategyVarInfo(_VernalizationProgress, "vBEE");
            _parameters0_0.Add(v27);
            VarInfo v28 = new CompositeStrategyVarInfo(_VernalizationProgress, "isVernalizable");
            _parameters0_0.Add(v28);
            VarInfo v29 = new CompositeStrategyVarInfo(_UpdatePhase, "isVernalizable");
            _parameters0_0.Add(v29);
            VarInfo v30 = new CompositeStrategyVarInfo(_VernalizationProgress, "minTvern");
            _parameters0_0.Add(v30);
            VarInfo v31 = new CompositeStrategyVarInfo(_VernalizationProgress, "intTvern");
            _parameters0_0.Add(v31);
            VarInfo v32 = new CompositeStrategyVarInfo(_VernalizationProgress, "vAI");
            _parameters0_0.Add(v32);
            VarInfo v33 = new CompositeStrategyVarInfo(_VernalizationProgress, "maxDL");
            _parameters0_0.Add(v33);
            VarInfo v34 = new CompositeStrategyVarInfo(_UpdatePhase, "maxDL");
            _parameters0_0.Add(v34);
            VarInfo v35 = new CompositeStrategyVarInfo(_Phyllochron, "choosePhyllUse");
            _parameters0_0.Add(v35);
            VarInfo v36 = new CompositeStrategyVarInfo(_UpdatePhase, "choosePhyllUse");
            _parameters0_0.Add(v36);
            VarInfo v37 = new CompositeStrategyVarInfo(_VernalizationProgress, "minDL");
            _parameters0_0.Add(v37);
            VarInfo v38 = new CompositeStrategyVarInfo(_UpdatePhase, "pFLLAnth");
            _parameters0_0.Add(v38);
            VarInfo v39 = new CompositeStrategyVarInfo(_UpdatePhase, "dcd");
            _parameters0_0.Add(v39);
            VarInfo v40 = new CompositeStrategyVarInfo(_UpdatePhase, "dgf");
            _parameters0_0.Add(v40);
            VarInfo v41 = new CompositeStrategyVarInfo(_UpdatePhase, "degfm");
            _parameters0_0.Add(v41);
            VarInfo v42 = new CompositeStrategyVarInfo(_UpdatePhase, "ignoreGrainMaturation");
            _parameters0_0.Add(v42);
            VarInfo v43 = new CompositeStrategyVarInfo(_UpdatePhase, "pHEADANTH");
            _parameters0_0.Add(v43);
            VarInfo v44 = new CompositeStrategyVarInfo(_UpdatePhase, "sLDL");
            _parameters0_0.Add(v44);
            VarInfo v45 = new CompositeStrategyVarInfo(_PhylSowingDateCorrection, "sowingDay");
            _parameters0_0.Add(v45);
            VarInfo v46 = new CompositeStrategyVarInfo(_PhylSowingDateCorrection, "sDws");
            _parameters0_0.Add(v46);
            VarInfo v47 = new CompositeStrategyVarInfo(_PhylSowingDateCorrection, "sDsa_nh");
            _parameters0_0.Add(v47);
            VarInfo v48 = new CompositeStrategyVarInfo(_RegisterZadok, "der");
            _parameters0_0.Add(v48);
            VarInfo v49 = new CompositeStrategyVarInfo(_ShootNumber, "targetFertileShoot");
            _parameters0_0.Add(v49);
            VarInfo v50 = new CompositeStrategyVarInfo(_UpdatePhase, "dse");
            _parameters0_0.Add(v50);
            VarInfo v51 = new CompositeStrategyVarInfo(_RegisterZadok, "slopeTSFLN");
            _parameters0_0.Add(v51);
            VarInfo v52 = new CompositeStrategyVarInfo(_RegisterZadok, "intTSFLN");
            _parameters0_0.Add(v52);
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd1.PropertyName = "phyllochron";
            pd1.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd2.PropertyName = "minFinalNumber";
            pd2.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd3.PropertyName = "currentdate";
            pd3.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd4.PropertyName = "cumulTT";
            pd4.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd5.PropertyName = "calendarDates";
            pd5.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
            _inputs0_0.Add(pd5);
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd6.PropertyName = "calendarMoments";
            pd6.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
            _inputs0_0.Add(pd6);
            PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd7.PropertyName = "ptq";
            pd7.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq);
            _inputs0_0.Add(pd7);
            PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd8.PropertyName = "leafNumber";
            pd8.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
            _inputs0_0.Add(pd8);
            PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd9.PropertyName = "dayLength";
            pd9.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength);
            _inputs0_0.Add(pd9);
            PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd10.PropertyName = "deltaTT";
            pd10.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT);
            _inputs0_0.Add(pd10);
            PropertyDescription pd11 = new PropertyDescription();
            pd11.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd11.PropertyName = "pastMaxAI";
            pd11.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI).ValueType.TypeForCurrentValue;
            pd11.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI);
            _inputs0_0.Add(pd11);
            PropertyDescription pd12 = new PropertyDescription();
            pd12.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd12.PropertyName = "listGAITTWindowForPTQ";
            pd12.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ).ValueType.TypeForCurrentValue;
            pd12.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ);
            _inputs0_0.Add(pd12);
            PropertyDescription pd13 = new PropertyDescription();
            pd13.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd13.PropertyName = "gAI";
            pd13.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI).ValueType.TypeForCurrentValue;
            pd13.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI);
            _inputs0_0.Add(pd13);
            PropertyDescription pd14 = new PropertyDescription();
            pd14.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd14.PropertyName = "pAR";
            pd14.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.pAR).ValueType.TypeForCurrentValue;
            pd14.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.pAR);
            _inputs0_0.Add(pd14);
            PropertyDescription pd15 = new PropertyDescription();
            pd15.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd15.PropertyName = "listPARTTWindowForPTQ";
            pd15.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ).ValueType.TypeForCurrentValue;
            pd15.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ);
            _inputs0_0.Add(pd15);
            PropertyDescription pd16 = new PropertyDescription();
            pd16.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd16.PropertyName = "listTTShootWindowForPTQ1";
            pd16.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1).ValueType.TypeForCurrentValue;
            pd16.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1);
            _inputs0_0.Add(pd16);
            PropertyDescription pd17 = new PropertyDescription();
            pd17.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd17.PropertyName = "listTTShootWindowForPTQ";
            pd17.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ).ValueType.TypeForCurrentValue;
            pd17.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ);
            _inputs0_0.Add(pd17);
            PropertyDescription pd18 = new PropertyDescription();
            pd18.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd18.PropertyName = "calendarCumuls";
            pd18.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls).ValueType.TypeForCurrentValue;
            pd18.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
            _inputs0_0.Add(pd18);
            PropertyDescription pd19 = new PropertyDescription();
            pd19.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd19.PropertyName = "vernaprog";
            pd19.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog).ValueType.TypeForCurrentValue;
            pd19.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog);
            _inputs0_0.Add(pd19);
            PropertyDescription pd20 = new PropertyDescription();
            pd20.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd20.PropertyName = "hasLastPrimordiumAppeared";
            pd20.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared).ValueType.TypeForCurrentValue;
            pd20.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared);
            _inputs0_0.Add(pd20);
            PropertyDescription pd21 = new PropertyDescription();
            pd21.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd21.PropertyName = "phase";
            pd21.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase).ValueType.TypeForCurrentValue;
            pd21.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase);
            _inputs0_0.Add(pd21);
            PropertyDescription pd22 = new PropertyDescription();
            pd22.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd22.PropertyName = "finalLeafNumber";
            pd22.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber).ValueType.TypeForCurrentValue;
            pd22.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber);
            _inputs0_0.Add(pd22);
            PropertyDescription pd23 = new PropertyDescription();
            pd23.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd23.PropertyName = "grainCumulTT";
            pd23.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.grainCumulTT).ValueType.TypeForCurrentValue;
            pd23.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.grainCumulTT);
            _inputs0_0.Add(pd23);
            PropertyDescription pd24 = new PropertyDescription();
            pd24.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd24.PropertyName = "hasZadokStageChanged";
            pd24.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged).ValueType.TypeForCurrentValue;
            pd24.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged);
            _inputs0_0.Add(pd24);
            PropertyDescription pd25 = new PropertyDescription();
            pd25.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd25.PropertyName = "currentZadokStage";
            pd25.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage).ValueType.TypeForCurrentValue;
            pd25.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage);
            _inputs0_0.Add(pd25);
            PropertyDescription pd26 = new PropertyDescription();
            pd26.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd26.PropertyName = "hasFlagLeafLiguleAppeared";
            pd26.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared).ValueType.TypeForCurrentValue;
            pd26.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared);
            _inputs0_0.Add(pd26);
            PropertyDescription pd27 = new PropertyDescription();
            pd27.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd27.PropertyName = "hasFlagLeafLiguleAppeared";
            pd27.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared).ValueType.TypeForCurrentValue;
            pd27.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared);
            _inputs0_0.Add(pd27);
            PropertyDescription pd28 = new PropertyDescription();
            pd28.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd28.PropertyName = "tilleringProfile";
            pd28.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile).ValueType.TypeForCurrentValue;
            pd28.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile);
            _inputs0_0.Add(pd28);
            PropertyDescription pd29 = new PropertyDescription();
            pd29.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd29.PropertyName = "leafTillerNumberArray";
            pd29.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray).ValueType.TypeForCurrentValue;
            pd29.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray);
            _inputs0_0.Add(pd29);
            PropertyDescription pd30 = new PropertyDescription();
            pd30.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd30.PropertyName = "canopyShootNumber";
            pd30.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber).ValueType.TypeForCurrentValue;
            pd30.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber);
            _inputs0_0.Add(pd30);
            mo0_0.Inputs=_inputs0_0;
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd31 = new PropertyDescription();
            pd31.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd31.PropertyName = "currentZadokStage";
            pd31.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage).ValueType.TypeForCurrentValue;
            pd31.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage);
            _outputs0_0.Add(pd31);
            PropertyDescription pd32 = new PropertyDescription();
            pd32.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd32.PropertyName = "hasZadokStageChanged";
            pd32.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged).ValueType.TypeForCurrentValue;
            pd32.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged);
            _outputs0_0.Add(pd32);
            PropertyDescription pd33 = new PropertyDescription();
            pd33.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd33.PropertyName = "hasFlagLeafLiguleAppeared";
            pd33.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared).ValueType.TypeForCurrentValue;
            pd33.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared);
            _outputs0_0.Add(pd33);
            PropertyDescription pd34 = new PropertyDescription();
            pd34.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd34.PropertyName = "listPARTTWindowForPTQ";
            pd34.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ).ValueType.TypeForCurrentValue;
            pd34.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ);
            _outputs0_0.Add(pd34);
            PropertyDescription pd35 = new PropertyDescription();
            pd35.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd35.PropertyName = "hasLastPrimordiumAppeared";
            pd35.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared).ValueType.TypeForCurrentValue;
            pd35.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared);
            _outputs0_0.Add(pd35);
            PropertyDescription pd36 = new PropertyDescription();
            pd36.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd36.PropertyName = "listTTShootWindowForPTQ";
            pd36.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ).ValueType.TypeForCurrentValue;
            pd36.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ);
            _outputs0_0.Add(pd36);
            PropertyDescription pd37 = new PropertyDescription();
            pd37.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd37.PropertyName = "listTTShootWindowForPTQ1";
            pd37.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1).ValueType.TypeForCurrentValue;
            pd37.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1);
            _outputs0_0.Add(pd37);
            PropertyDescription pd38 = new PropertyDescription();
            pd38.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd38.PropertyName = "ptq";
            pd38.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq).ValueType.TypeForCurrentValue;
            pd38.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq);
            _outputs0_0.Add(pd38);
            PropertyDescription pd39 = new PropertyDescription();
            pd39.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd39.PropertyName = "calendarMoments";
            pd39.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments).ValueType.TypeForCurrentValue;
            pd39.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
            _outputs0_0.Add(pd39);
            PropertyDescription pd40 = new PropertyDescription();
            pd40.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd40.PropertyName = "canopyShootNumber";
            pd40.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber).ValueType.TypeForCurrentValue;
            pd40.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber);
            _outputs0_0.Add(pd40);
            PropertyDescription pd41 = new PropertyDescription();
            pd41.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd41.PropertyName = "calendarDates";
            pd41.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates).ValueType.TypeForCurrentValue;
            pd41.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
            _outputs0_0.Add(pd41);
            PropertyDescription pd42 = new PropertyDescription();
            pd42.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd42.PropertyName = "leafTillerNumberArray";
            pd42.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray).ValueType.TypeForCurrentValue;
            pd42.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray);
            _outputs0_0.Add(pd42);
            PropertyDescription pd43 = new PropertyDescription();
            pd43.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd43.PropertyName = "vernaprog";
            pd43.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog).ValueType.TypeForCurrentValue;
            pd43.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog);
            _outputs0_0.Add(pd43);
            PropertyDescription pd44 = new PropertyDescription();
            pd44.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd44.PropertyName = "phyllochron";
            pd44.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron).ValueType.TypeForCurrentValue;
            pd44.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron);
            _outputs0_0.Add(pd44);
            PropertyDescription pd45 = new PropertyDescription();
            pd45.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd45.PropertyName = "leafNumber";
            pd45.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber).ValueType.TypeForCurrentValue;
            pd45.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
            _outputs0_0.Add(pd45);
            PropertyDescription pd46 = new PropertyDescription();
            pd46.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd46.PropertyName = "numberTillerCohort";
            pd46.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort).ValueType.TypeForCurrentValue;
            pd46.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort);
            _outputs0_0.Add(pd46);
            PropertyDescription pd47 = new PropertyDescription();
            pd47.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd47.PropertyName = "tilleringProfile";
            pd47.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile).ValueType.TypeForCurrentValue;
            pd47.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile);
            _outputs0_0.Add(pd47);
            PropertyDescription pd48 = new PropertyDescription();
            pd48.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd48.PropertyName = "averageShootNumberPerPlant";
            pd48.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.averageShootNumberPerPlant).ValueType.TypeForCurrentValue;
            pd48.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.averageShootNumberPerPlant);
            _outputs0_0.Add(pd48);
            PropertyDescription pd49 = new PropertyDescription();
            pd49.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd49.PropertyName = "minFinalNumber";
            pd49.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber).ValueType.TypeForCurrentValue;
            pd49.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber);
            _outputs0_0.Add(pd49);
            PropertyDescription pd50 = new PropertyDescription();
            pd50.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd50.PropertyName = "finalLeafNumber";
            pd50.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber).ValueType.TypeForCurrentValue;
            pd50.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber);
            _outputs0_0.Add(pd50);
            PropertyDescription pd51 = new PropertyDescription();
            pd51.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd51.PropertyName = "phase";
            pd51.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase).ValueType.TypeForCurrentValue;
            pd51.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase);
            _outputs0_0.Add(pd51);
            PropertyDescription pd52 = new PropertyDescription();
            pd52.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd52.PropertyName = "listGAITTWindowForPTQ";
            pd52.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ).ValueType.TypeForCurrentValue;
            pd52.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ);
            _outputs0_0.Add(pd52);
            PropertyDescription pd53 = new PropertyDescription();
            pd53.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd53.PropertyName = "calendarCumuls";
            pd53.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls).ValueType.TypeForCurrentValue;
            pd53.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
            _outputs0_0.Add(pd53);
            PropertyDescription pd54 = new PropertyDescription();
            pd54.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd54.PropertyName = "gAImean";
            pd54.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean).ValueType.TypeForCurrentValue;
            pd54.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean);
            _outputs0_0.Add(pd54);
            PropertyDescription pd55 = new PropertyDescription();
            pd55.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd55.PropertyName = "pastMaxAI";
            pd55.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI).ValueType.TypeForCurrentValue;
            pd55.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI);
            _outputs0_0.Add(pd55);
            mo0_0.Outputs=_outputs0_0;
            List<string> lAssStrat0_0 = new List<string>();
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.Phyllochron).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.PhylSowingDateCorrection).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.ShootNumber).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.UpdateLeafFlag).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.UpdatePhase).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.LeafNumber).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.VernalizationProgress).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.IsMomentRegistredZC_39).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.CumulTTFrom).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.UpdateCalendar).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.RegisterZadok).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.PTQ).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityPhenology.Strategies.GAImean).FullName);
            mo0_0.AssociatedStrategies = lAssStrat0_0;
            _modellingOptionsManager = new ModellingOptionsManager(mo0_0);
            SetStaticParametersVarInfoDefinitions();
            SetPublisherData();
        }

        public string Description
        {
            get { return "see documentation" ;}
        }

        public string URL
        {
            get { return "" ;}
        }

        public string Domain
        {
            get { return "";}
        }

        public string ModelType
        {
            get { return "";}
        }

        public bool IsContext
        {
            get { return false;}
        }

        public IList<int> TimeStep
        {
            get
            {
                IList<int> ts = new List<int>();
                return ts;
            }
        }

        private  PublisherData _pd;
        public PublisherData PublisherData
        {
            get { return _pd;} 
        }

        private  void SetPublisherData()
        {
            _pd = new CRA.ModelLayer.MetadataTypes.PublisherData();
            _pd.Add("Creator", "Pierre MARTRE");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "INRA/LEPSE");
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        public IEnumerable<Type> GetStrategyDomainClassesTypes()
        {
            return new List<Type>() {  typeof(SiriusQualityPhenology.DomainClass.PhenologyState), typeof(SiriusQualityPhenology.DomainClass.PhenologyState), typeof(SiriusQualityPhenology.DomainClass.PhenologyRate), typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary), typeof(SiriusQualityPhenology.DomainClass.PhenologyExogenous)};
        }

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

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
            _Phyllochron.SetParametersDefaultValue();
            _PhylSowingDateCorrection.SetParametersDefaultValue();
            _ShootNumber.SetParametersDefaultValue();
            _UpdateLeafFlag.SetParametersDefaultValue();
            _UpdatePhase.SetParametersDefaultValue();
            _LeafNumber.SetParametersDefaultValue();
            _VernalizationProgress.SetParametersDefaultValue();
            _IsMomentRegistredZC_39.SetParametersDefaultValue();
            _CumulTTFrom.SetParametersDefaultValue();
            _UpdateCalendar.SetParametersDefaultValue();
            _RegisterZadok.SetParametersDefaultValue();
            _PTQ.SetParametersDefaultValue();
            _GAImean.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            aMXLFNOVarInfo.Name = "aMXLFNO";
            aMXLFNOVarInfo.Description = "Absolute maximum leaf number";
            aMXLFNOVarInfo.MaxValue = 25;
            aMXLFNOVarInfo.MinValue = 0;
            aMXLFNOVarInfo.DefaultValue = 24.0;
            aMXLFNOVarInfo.Units = "leaf";
            aMXLFNOVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pNiniVarInfo.Name = "pNini";
            pNiniVarInfo.Description = "Number of primorida in the apex at emergence";
            pNiniVarInfo.MaxValue = 24;
            pNiniVarInfo.MinValue = 0;
            pNiniVarInfo.DefaultValue = 4.0;
            pNiniVarInfo.Units = "primordia";
            pNiniVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            sDsa_shVarInfo.Name = "sDsa_sh";
            sDsa_shVarInfo.Description = "Sowing date at which Phyllochrone is maximum in southern hemispher";
            sDsa_shVarInfo.MaxValue = 365;
            sDsa_shVarInfo.MinValue = 1;
            sDsa_shVarInfo.DefaultValue = 1.0;
            sDsa_shVarInfo.Units = "d";
            sDsa_shVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            latitudeVarInfo.Name = "latitude";
            latitudeVarInfo.Description = "Latitude";
            latitudeVarInfo.MaxValue = 90;
            latitudeVarInfo.MinValue = -90;
            latitudeVarInfo.DefaultValue = 0.0;
            latitudeVarInfo.Units = "°";
            latitudeVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            klVarInfo.Name = "kl";
            klVarInfo.Description = "Exctinction Coefficient";
            klVarInfo.MaxValue = 50.0;
            klVarInfo.MinValue = 0.0;
            klVarInfo.DefaultValue = 0.45;
            klVarInfo.Units = "-";
            klVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            lincrVarInfo.Name = "lincr";
            lincrVarInfo.Description = "Leaf number above which the phyllochron is increased by Pincr";
            lincrVarInfo.MaxValue = 30.0;
            lincrVarInfo.MinValue = 0.0;
            lincrVarInfo.DefaultValue = 8.0;
            lincrVarInfo.Units = "leaf";
            lincrVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            ldecrVarInfo.Name = "ldecr";
            ldecrVarInfo.Description = "Leaf number up to which the phyllochron is decreased by Pdecr";
            ldecrVarInfo.MaxValue = 100.0;
            ldecrVarInfo.MinValue = 0.0;
            ldecrVarInfo.DefaultValue = 0.0;
            ldecrVarInfo.Units = "leaf";
            ldecrVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pincrVarInfo.Name = "pincr";
            pincrVarInfo.Description = "Factor increasing the phyllochron for leaf number higher than Lincr";
            pincrVarInfo.MaxValue = 10.0;
            pincrVarInfo.MinValue = 0.0;
            pincrVarInfo.DefaultValue = 1.5;
            pincrVarInfo.Units = "-";
            pincrVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pTQhfVarInfo.Name = "pTQhf";
            pTQhfVarInfo.Description = "Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient";
            pTQhfVarInfo.MaxValue = 1000.0;
            pTQhfVarInfo.MinValue = 0.0;
            pTQhfVarInfo.DefaultValue = 0.0;
            pTQhfVarInfo.Units = "°C d leaf-1";
            pTQhfVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            BVarInfo.Name = "B";
            BVarInfo.Description = "Phyllochron at PTQ equal 1";
            BVarInfo.MaxValue = 1000.0;
            BVarInfo.MinValue = 0.0;
            BVarInfo.DefaultValue = 20.0;
            BVarInfo.Units = "°C d leaf-1";
            BVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            areaSLVarInfo.Name = "areaSL";
            areaSLVarInfo.Description = " Area Leaf";
            areaSLVarInfo.MaxValue = 1000.0;
            areaSLVarInfo.MinValue = 0.0;
            areaSLVarInfo.DefaultValue = 0.0;
            areaSLVarInfo.Units = "cm2";
            areaSLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            areaSSVarInfo.Name = "areaSS";
            areaSSVarInfo.Description = "Area Sheath";
            areaSSVarInfo.MaxValue = 1000.0;
            areaSSVarInfo.MinValue = 0.0;
            areaSSVarInfo.DefaultValue = 0.0;
            areaSSVarInfo.Units = "cm2";
            areaSSVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            lARminVarInfo.Name = "lARmin";
            lARminVarInfo.Description = "LAR minimum";
            lARminVarInfo.MaxValue = 1000.0;
            lARminVarInfo.MinValue = 0.0;
            lARminVarInfo.DefaultValue = 0.0;
            lARminVarInfo.Units = "leaf-1 °C";
            lARminVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            sowingDensityVarInfo.Name = "sowingDensity";
            sowingDensityVarInfo.Description = "Sowing Density";
            sowingDensityVarInfo.MaxValue = 1000.0;
            sowingDensityVarInfo.MinValue = 0.0;
            sowingDensityVarInfo.DefaultValue = 0.0;
            sowingDensityVarInfo.Units = "plant m-2";
            sowingDensityVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            lARmaxVarInfo.Name = "lARmax";
            lARmaxVarInfo.Description = "LAR maximum";
            lARmaxVarInfo.MaxValue = 1000.0;
            lARmaxVarInfo.MinValue = 0.0;
            lARmaxVarInfo.DefaultValue = 0.0;
            lARmaxVarInfo.Units = "leaf-1 °C";
            lARmaxVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            lNeffVarInfo.Name = "lNeff";
            lNeffVarInfo.Description = "Leaf Number efficace";
            lNeffVarInfo.MaxValue = 1000.0;
            lNeffVarInfo.MinValue = 0.0;
            lNeffVarInfo.DefaultValue = 0.0;
            lNeffVarInfo.Units = "leaf";
            lNeffVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            rpVarInfo.Name = "rp";
            rpVarInfo.Description = "Rate of change of Phyllochrone with sowing date";
            rpVarInfo.MaxValue = 365;
            rpVarInfo.MinValue = 0;
            rpVarInfo.DefaultValue = 0;
            rpVarInfo.Units = "d-1";
            rpVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pVarInfo.Name = "p";
            pVarInfo.Description = "Phyllochron (Varietal parameter)";
            pVarInfo.MaxValue = 1000.0;
            pVarInfo.MinValue = 0.0;
            pVarInfo.DefaultValue = 120.0;
            pVarInfo.Units = "°C d leaf-1";
            pVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pdecrVarInfo.Name = "pdecr";
            pdecrVarInfo.Description = "Factor decreasing the phyllochron for leaf number less than Ldecr";
            pdecrVarInfo.MaxValue = 10.0;
            pdecrVarInfo.MinValue = 0.0;
            pdecrVarInfo.DefaultValue = 0.4;
            pdecrVarInfo.Units = "-";
            pdecrVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            maxTvernVarInfo.Name = "maxTvern";
            maxTvernVarInfo.Description = "Maximum temperature for vernalization to occur";
            maxTvernVarInfo.MaxValue = 60;
            maxTvernVarInfo.MinValue = -20;
            maxTvernVarInfo.DefaultValue =  23.0;
            maxTvernVarInfo.Units = "°C";
            maxTvernVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            tTWindowForPTQVarInfo.Name = "tTWindowForPTQ";
            tTWindowForPTQVarInfo.Description = "Thermal Time window for average";
            tTWindowForPTQVarInfo.MaxValue = 5000.0;
            tTWindowForPTQVarInfo.MinValue = 0.0;
            tTWindowForPTQVarInfo.DefaultValue = 0.0;
            tTWindowForPTQVarInfo.Units = "°C d";
            tTWindowForPTQVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            vBEEVarInfo.Name = "vBEE";
            vBEEVarInfo.Description = "Vernalization rate at 0°C";
            vBEEVarInfo.MaxValue = 1;
            vBEEVarInfo.MinValue = 0;
            vBEEVarInfo.DefaultValue = 0.01;
            vBEEVarInfo.Units = "d-1";
            vBEEVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            isVernalizableVarInfo.Name = "isVernalizable";
            isVernalizableVarInfo.Description = "true if the plant is vernalizable";
            isVernalizableVarInfo.MaxValue = 1;
            isVernalizableVarInfo.MinValue = 0;
            isVernalizableVarInfo.DefaultValue = 1;
            isVernalizableVarInfo.Units = "";
            isVernalizableVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            minTvernVarInfo.Name = "minTvern";
            minTvernVarInfo.Description = "Minimum temperature for vernalization to occur";
            minTvernVarInfo.MaxValue = 60;
            minTvernVarInfo.MinValue = -20;
            minTvernVarInfo.DefaultValue = 0.0;
            minTvernVarInfo.Units = "°C";
            minTvernVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            intTvernVarInfo.Name = "intTvern";
            intTvernVarInfo.Description = "Intermediate temperature for vernalization to occur";
            intTvernVarInfo.MaxValue = 60;
            intTvernVarInfo.MinValue = -20;
            intTvernVarInfo.DefaultValue =  11.0;
            intTvernVarInfo.Units = "°C";
            intTvernVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            vAIVarInfo.Name = "vAI";
            vAIVarInfo.Description = "Response of vernalization rate to temperature";
            vAIVarInfo.MaxValue = 1;
            vAIVarInfo.MinValue = 0;
            vAIVarInfo.DefaultValue =  0.015;
            vAIVarInfo.Units = "d-1 °C-1";
            vAIVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            maxDLVarInfo.Name = "maxDL";
            maxDLVarInfo.Description = "Saturating photoperiod above which final leaf number is not influenced by daylength";
            maxDLVarInfo.MaxValue = 24;
            maxDLVarInfo.MinValue = 0;
            maxDLVarInfo.DefaultValue = 15.0;
            maxDLVarInfo.Units = "h";
            maxDLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            choosePhyllUseVarInfo.Name = "choosePhyllUse";
            choosePhyllUseVarInfo.Description = "Switch to choose the type of phyllochron calculation to be used";
            choosePhyllUseVarInfo.MaxValue = -1D;
            choosePhyllUseVarInfo.MinValue = -1D;
            choosePhyllUseVarInfo.DefaultValue = -1D;
            choosePhyllUseVarInfo.Units = "-";
            choosePhyllUseVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("String");

            minDLVarInfo.Name = "minDL";
            minDLVarInfo.Description = "Threshold daylength below which it does influence vernalization rate";
            minDLVarInfo.MaxValue = 24;
            minDLVarInfo.MinValue = 12;
            minDLVarInfo.DefaultValue = 8.0;
            minDLVarInfo.Units = "h";
            minDLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pFLLAnthVarInfo.Name = "pFLLAnth";
            pFLLAnthVarInfo.Description = "Phyllochronic duration of the period between flag leaf ligule appearance and anthesis";
            pFLLAnthVarInfo.MaxValue = 1000;
            pFLLAnthVarInfo.MinValue = 0;
            pFLLAnthVarInfo.DefaultValue = 2.22;
            pFLLAnthVarInfo.Units = "";
            pFLLAnthVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            dcdVarInfo.Name = "dcd";
            dcdVarInfo.Description = "Duration of the endosperm cell division phase";
            dcdVarInfo.MaxValue = 10000;
            dcdVarInfo.MinValue = 0;
            dcdVarInfo.DefaultValue = 100;
            dcdVarInfo.Units = "°C d";
            dcdVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            dgfVarInfo.Name = "dgf";
            dgfVarInfo.Description = "Grain filling duration (from anthesis to physiological maturity)";
            dgfVarInfo.MaxValue = 10000;
            dgfVarInfo.MinValue = 0;
            dgfVarInfo.DefaultValue = 450;
            dgfVarInfo.Units = "°C d";
            dgfVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            degfmVarInfo.Name = "degfm";
            degfmVarInfo.Description = "Grain maturation duration (from physiological maturity to harvest ripeness)";
            degfmVarInfo.MaxValue = 50;
            degfmVarInfo.MinValue = 0;
            degfmVarInfo.DefaultValue = 0;
            degfmVarInfo.Units = "°C d";
            degfmVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            ignoreGrainMaturationVarInfo.Name = "ignoreGrainMaturation";
            ignoreGrainMaturationVarInfo.Description = "true to ignore grain maturation";
            ignoreGrainMaturationVarInfo.MaxValue = -1D;
            ignoreGrainMaturationVarInfo.MinValue = -1D;
            ignoreGrainMaturationVarInfo.DefaultValue = -1D;
            ignoreGrainMaturationVarInfo.Units = "";
            ignoreGrainMaturationVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            pHEADANTHVarInfo.Name = "pHEADANTH";
            pHEADANTHVarInfo.Description = "Number of phyllochron between heading and anthesiss";
            pHEADANTHVarInfo.MaxValue = 1000;
            pHEADANTHVarInfo.MinValue = 0;
            pHEADANTHVarInfo.DefaultValue = 1;
            pHEADANTHVarInfo.Units = "";
            pHEADANTHVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            sLDLVarInfo.Name = "sLDL";
            sLDLVarInfo.Description = "Daylength response of leaf production";
            sLDLVarInfo.MaxValue = 1;
            sLDLVarInfo.MinValue = 0;
            sLDLVarInfo.DefaultValue = 0.85;
            sLDLVarInfo.Units = "leaf h-1";
            sLDLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            sowingDayVarInfo.Name = "sowingDay";
            sowingDayVarInfo.Description = "Day of Year at sowing";
            sowingDayVarInfo.MaxValue = 365;
            sowingDayVarInfo.MinValue = 1;
            sowingDayVarInfo.DefaultValue = 1;
            sowingDayVarInfo.Units = "d";
            sowingDayVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            sDwsVarInfo.Name = "sDws";
            sDwsVarInfo.Description = "Sowing date at which Phyllochrone is minimum";
            sDwsVarInfo.MaxValue = 365;
            sDwsVarInfo.MinValue = 1;
            sDwsVarInfo.DefaultValue = 1;
            sDwsVarInfo.Units = "d";
            sDwsVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            sDsa_nhVarInfo.Name = "sDsa_nh";
            sDsa_nhVarInfo.Description = "Sowing date at which Phyllochrone is maximum in northern hemispher";
            sDsa_nhVarInfo.MaxValue = 365;
            sDsa_nhVarInfo.MinValue = 1;
            sDsa_nhVarInfo.DefaultValue = 1.0;
            sDsa_nhVarInfo.Units = "d";
            sDsa_nhVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            derVarInfo.Name = "der";
            derVarInfo.Description = "Duration of the endosperm endoreduplication phase";
            derVarInfo.MaxValue = 10000;
            derVarInfo.MinValue = 0;
            derVarInfo.DefaultValue = 300.0;
            derVarInfo.Units = "°C d";
            derVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            targetFertileShootVarInfo.Name = "targetFertileShoot";
            targetFertileShootVarInfo.Description = "max value of shoot number for the canopy";
            targetFertileShootVarInfo.MaxValue = 1000;
            targetFertileShootVarInfo.MinValue = 280;
            targetFertileShootVarInfo.DefaultValue = 600.0;
            targetFertileShootVarInfo.Units = "shoot";
            targetFertileShootVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            dseVarInfo.Name = "dse";
            dseVarInfo.Description = "Thermal time from sowing to emergence";
            dseVarInfo.MaxValue = 1000;
            dseVarInfo.MinValue = 0;
            dseVarInfo.DefaultValue = 105;
            dseVarInfo.Units = "°C d";
            dseVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            slopeTSFLNVarInfo.Name = "slopeTSFLN";
            slopeTSFLNVarInfo.Description = "Slope of the relationship between Haun stage at terminal spikelet and final leaf number";
            slopeTSFLNVarInfo.MaxValue = 10000;
            slopeTSFLNVarInfo.MinValue = 0;
            slopeTSFLNVarInfo.DefaultValue = 0.9;
            slopeTSFLNVarInfo.Units = "";
            slopeTSFLNVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            intTSFLNVarInfo.Name = "intTSFLN";
            intTSFLNVarInfo.Description = "Intercept of the relationship between Haun stage at terminal spikelet and final leaf number";
            intTSFLNVarInfo.MaxValue = 10000;
            intTSFLNVarInfo.MinValue = 0;
            intTSFLNVarInfo.DefaultValue = 2.6;
            intTSFLNVarInfo.Units = "";
            intTSFLNVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        public static VarInfo aMXLFNOVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.VernalizationProgress.aMXLFNOVarInfo;} 
        }

        public static VarInfo pNiniVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.VernalizationProgress.pNiniVarInfo;} 
        }

        public static VarInfo sDsa_shVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.PhylSowingDateCorrection.sDsa_shVarInfo;} 
        }

        public static VarInfo latitudeVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.PhylSowingDateCorrection.latitudeVarInfo;} 
        }

        public static VarInfo klVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.klVarInfo;} 
        }

        public static VarInfo lincrVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.lincrVarInfo;} 
        }

        public static VarInfo ldecrVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.ldecrVarInfo;} 
        }

        public static VarInfo pincrVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.pincrVarInfo;} 
        }

        public static VarInfo pTQhfVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.pTQhfVarInfo;} 
        }

        public static VarInfo BVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.BVarInfo;} 
        }

        public static VarInfo areaSLVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.areaSLVarInfo;} 
        }

        public static VarInfo areaSSVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.areaSSVarInfo;} 
        }

        public static VarInfo lARminVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.lARminVarInfo;} 
        }

        public static VarInfo sowingDensityVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.sowingDensityVarInfo;} 
        }

        public static VarInfo lARmaxVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.lARmaxVarInfo;} 
        }

        public static VarInfo lNeffVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.lNeffVarInfo;} 
        }

        public static VarInfo rpVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.PhylSowingDateCorrection.rpVarInfo;} 
        }

        public static VarInfo pVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.pVarInfo;} 
        }

        public static VarInfo pdecrVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.pdecrVarInfo;} 
        }

        public static VarInfo maxTvernVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.VernalizationProgress.maxTvernVarInfo;} 
        }

        public static VarInfo tTWindowForPTQVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.GAImean.tTWindowForPTQVarInfo;} 
        }

        public static VarInfo vBEEVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.VernalizationProgress.vBEEVarInfo;} 
        }

        public static VarInfo isVernalizableVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.VernalizationProgress.isVernalizableVarInfo;} 
        }

        public static VarInfo minTvernVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.VernalizationProgress.minTvernVarInfo;} 
        }

        public static VarInfo intTvernVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.VernalizationProgress.intTvernVarInfo;} 
        }

        public static VarInfo vAIVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.VernalizationProgress.vAIVarInfo;} 
        }

        public static VarInfo maxDLVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.VernalizationProgress.maxDLVarInfo;} 
        }

        public static VarInfo choosePhyllUseVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.Phyllochron.choosePhyllUseVarInfo;} 
        }

        public static VarInfo minDLVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.VernalizationProgress.minDLVarInfo;} 
        }

        public static VarInfo pFLLAnthVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.UpdatePhase.pFLLAnthVarInfo;} 
        }

        public static VarInfo dcdVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.UpdatePhase.dcdVarInfo;} 
        }

        public static VarInfo dgfVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.UpdatePhase.dgfVarInfo;} 
        }

        public static VarInfo degfmVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.UpdatePhase.degfmVarInfo;} 
        }

        public static VarInfo ignoreGrainMaturationVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.UpdatePhase.ignoreGrainMaturationVarInfo;} 
        }

        public static VarInfo pHEADANTHVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.UpdatePhase.pHEADANTHVarInfo;} 
        }

        public static VarInfo sLDLVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.UpdatePhase.sLDLVarInfo;} 
        }

        public static VarInfo sowingDayVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.PhylSowingDateCorrection.sowingDayVarInfo;} 
        }

        public static VarInfo sDwsVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.PhylSowingDateCorrection.sDwsVarInfo;} 
        }

        public static VarInfo sDsa_nhVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.PhylSowingDateCorrection.sDsa_nhVarInfo;} 
        }

        public static VarInfo derVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.RegisterZadok.derVarInfo;} 
        }

        public static VarInfo targetFertileShootVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.ShootNumber.targetFertileShootVarInfo;} 
        }

        public static VarInfo dseVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.UpdatePhase.dseVarInfo;} 
        }

        public static VarInfo slopeTSFLNVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.RegisterZadok.slopeTSFLNVarInfo;} 
        }

        public static VarInfo intTSFLNVarInfo
        {
            get { return SiriusQualityPhenology.Strategies.RegisterZadok.intTSFLNVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage.CurrentValue=s.currentZadokStage;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged.CurrentValue=s.hasZadokStageChanged;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared.CurrentValue=s.hasFlagLeafLiguleAppeared;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ.CurrentValue=s.listPARTTWindowForPTQ;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared.CurrentValue=s.hasLastPrimordiumAppeared;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ.CurrentValue=s.listTTShootWindowForPTQ;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1.CurrentValue=s.listTTShootWindowForPTQ1;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq.CurrentValue=s.ptq;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.CurrentValue=s.calendarMoments;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber.CurrentValue=s.canopyShootNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.CurrentValue=s.calendarDates;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray.CurrentValue=s.leafTillerNumberArray;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog.CurrentValue=s.vernaprog;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron.CurrentValue=s.phyllochron;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.CurrentValue=s.leafNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort.CurrentValue=s.numberTillerCohort;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile.CurrentValue=s.tilleringProfile;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.averageShootNumberPerPlant.CurrentValue=s.averageShootNumberPerPlant;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber.CurrentValue=s.minFinalNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber.CurrentValue=s.finalLeafNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase.CurrentValue=s.phase;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ.CurrentValue=s.listGAITTWindowForPTQ;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.CurrentValue=s.calendarCumuls;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean.CurrentValue=s.gAImean;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI.CurrentValue=s.pastMaxAI;

                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 

                RangeBasedCondition r75 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage);
                if(r75.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage.ValueType)){prc.AddCondition(r75);}
                RangeBasedCondition r76 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged);
                if(r76.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged.ValueType)){prc.AddCondition(r76);}
                RangeBasedCondition r77 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared);
                if(r77.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared.ValueType)){prc.AddCondition(r77);}
                RangeBasedCondition r78 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ);
                if(r78.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ.ValueType)){prc.AddCondition(r78);}
                RangeBasedCondition r79 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared);
                if(r79.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared.ValueType)){prc.AddCondition(r79);}
                RangeBasedCondition r80 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ);
                if(r80.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ.ValueType)){prc.AddCondition(r80);}
                RangeBasedCondition r81 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1);
                if(r81.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1.ValueType)){prc.AddCondition(r81);}
                RangeBasedCondition r82 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq);
                if(r82.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq.ValueType)){prc.AddCondition(r82);}
                RangeBasedCondition r83 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
                if(r83.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.ValueType)){prc.AddCondition(r83);}
                RangeBasedCondition r84 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber);
                if(r84.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber.ValueType)){prc.AddCondition(r84);}
                RangeBasedCondition r85 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
                if(r85.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.ValueType)){prc.AddCondition(r85);}
                RangeBasedCondition r86 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray);
                if(r86.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray.ValueType)){prc.AddCondition(r86);}
                RangeBasedCondition r87 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog);
                if(r87.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog.ValueType)){prc.AddCondition(r87);}
                RangeBasedCondition r88 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron);
                if(r88.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron.ValueType)){prc.AddCondition(r88);}
                RangeBasedCondition r89 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
                if(r89.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.ValueType)){prc.AddCondition(r89);}
                RangeBasedCondition r90 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort);
                if(r90.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort.ValueType)){prc.AddCondition(r90);}
                RangeBasedCondition r91 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile);
                if(r91.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile.ValueType)){prc.AddCondition(r91);}
                RangeBasedCondition r92 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.averageShootNumberPerPlant);
                if(r92.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.averageShootNumberPerPlant.ValueType)){prc.AddCondition(r92);}
                RangeBasedCondition r93 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber);
                if(r93.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber.ValueType)){prc.AddCondition(r93);}
                RangeBasedCondition r94 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber);
                if(r94.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber.ValueType)){prc.AddCondition(r94);}
                RangeBasedCondition r95 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase);
                if(r95.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase.ValueType)){prc.AddCondition(r95);}
                RangeBasedCondition r96 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ);
                if(r96.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ.ValueType)){prc.AddCondition(r96);}
                RangeBasedCondition r97 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
                if(r97.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.ValueType)){prc.AddCondition(r97);}
                RangeBasedCondition r98 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean);
                if(r98.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean.ValueType)){prc.AddCondition(r98);}
                RangeBasedCondition r99 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI);
                if(r99.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI.ValueType)){prc.AddCondition(r99);}

                string ret = "";
                ret += _Phyllochron.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _PhylSowingDateCorrection.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _ShootNumber.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _UpdateLeafFlag.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _UpdatePhase.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _LeafNumber.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _VernalizationProgress.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _IsMomentRegistredZC_39.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _CumulTTFrom.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _UpdateCalendar.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _RegisterZadok.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _PTQ.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _GAImean.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                if (ret != "") { pre.TestsOut(ret, true, "   postconditions tests of associated classes"); }

                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component SiriusQuality.Phenology, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron.CurrentValue=s.phyllochron;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber.CurrentValue=s.minFinalNumber;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate.CurrentValue=a.currentdate;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT.CurrentValue=a.cumulTT;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.CurrentValue=s.calendarDates;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.CurrentValue=s.calendarMoments;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq.CurrentValue=s.ptq;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.CurrentValue=s.leafNumber;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength.CurrentValue=a.dayLength;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT.CurrentValue=a.deltaTT;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI.CurrentValue=s.pastMaxAI;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ.CurrentValue=s.listGAITTWindowForPTQ;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI.CurrentValue=a.gAI;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.pAR.CurrentValue=a.pAR;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ.CurrentValue=s.listPARTTWindowForPTQ;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1.CurrentValue=s.listTTShootWindowForPTQ1;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ.CurrentValue=s.listTTShootWindowForPTQ;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.CurrentValue=s.calendarCumuls;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog.CurrentValue=s.vernaprog;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared.CurrentValue=s.hasLastPrimordiumAppeared;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase.CurrentValue=s.phase;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber.CurrentValue=s.finalLeafNumber;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.grainCumulTT.CurrentValue=a.grainCumulTT;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged.CurrentValue=s.hasZadokStageChanged;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage.CurrentValue=s.currentZadokStage;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared.CurrentValue=s.hasFlagLeafLiguleAppeared;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared.CurrentValue=s.hasFlagLeafLiguleAppeared;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile.CurrentValue=s.tilleringProfile;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray.CurrentValue=s.leafTillerNumberArray;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber.CurrentValue=s.canopyShootNumber;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.minFinalNumber.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.ValueType)){prc.AddCondition(r5);}
                RangeBasedCondition r6 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
                if(r6.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.ValueType)){prc.AddCondition(r6);}
                RangeBasedCondition r7 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq);
                if(r7.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.dayLength.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT.ValueType)){prc.AddCondition(r10);}
                RangeBasedCondition r11 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI);
                if(r11.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI.ValueType)){prc.AddCondition(r11);}
                RangeBasedCondition r12 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ);
                if(r12.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ.ValueType)){prc.AddCondition(r12);}
                RangeBasedCondition r13 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI);
                if(r13.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI.ValueType)){prc.AddCondition(r13);}
                RangeBasedCondition r14 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.pAR);
                if(r14.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.pAR.ValueType)){prc.AddCondition(r14);}
                RangeBasedCondition r15 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ);
                if(r15.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ.ValueType)){prc.AddCondition(r15);}
                RangeBasedCondition r16 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1);
                if(r16.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1.ValueType)){prc.AddCondition(r16);}
                RangeBasedCondition r17 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ);
                if(r17.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ.ValueType)){prc.AddCondition(r17);}
                RangeBasedCondition r18 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
                if(r18.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.ValueType)){prc.AddCondition(r18);}
                RangeBasedCondition r19 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog);
                if(r19.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.vernaprog.ValueType)){prc.AddCondition(r19);}
                RangeBasedCondition r20 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared);
                if(r20.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasLastPrimordiumAppeared.ValueType)){prc.AddCondition(r20);}
                RangeBasedCondition r21 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase);
                if(r21.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase.ValueType)){prc.AddCondition(r21);}
                RangeBasedCondition r22 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber);
                if(r22.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber.ValueType)){prc.AddCondition(r22);}
                RangeBasedCondition r23 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.grainCumulTT);
                if(r23.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.grainCumulTT.ValueType)){prc.AddCondition(r23);}
                RangeBasedCondition r24 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged);
                if(r24.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged.ValueType)){prc.AddCondition(r24);}
                RangeBasedCondition r25 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage);
                if(r25.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage.ValueType)){prc.AddCondition(r25);}
                RangeBasedCondition r26 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared);
                if(r26.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared.ValueType)){prc.AddCondition(r26);}
                RangeBasedCondition r27 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared);
                if(r27.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasFlagLeafLiguleAppeared.ValueType)){prc.AddCondition(r27);}
                RangeBasedCondition r28 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile);
                if(r28.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile.ValueType)){prc.AddCondition(r28);}
                RangeBasedCondition r29 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray);
                if(r29.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray.ValueType)){prc.AddCondition(r29);}
                RangeBasedCondition r30 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber);
                if(r30.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber.ValueType)){prc.AddCondition(r30);}

                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("aMXLFNO")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pNini")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sDsa_sh")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("latitude")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("kl")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("lincr")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("ldecr")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pincr")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pTQhf")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("B")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("areaSL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("areaSS")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("lARmin")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sowingDensity")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("lARmax")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("lNeff")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("rp")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("p")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pdecr")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("maxTvern")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("tTWindowForPTQ")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("vBEE")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("isVernalizable")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("minTvern")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("intTvern")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("vAI")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("maxDL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("choosePhyllUse")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("minDL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pFLLAnth")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("dcd")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("dgf")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("degfm")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("ignoreGrainMaturation")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pHEADANTH")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sLDL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sowingDay")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sDws")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sDsa_nh")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("der")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("targetFertileShoot")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("dse")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("slopeTSFLN")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("intTSFLN")));
                string ret = "";
                ret += _Phyllochron.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _PhylSowingDateCorrection.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _ShootNumber.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _UpdateLeafFlag.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _UpdatePhase.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _LeafNumber.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _VernalizationProgress.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _IsMomentRegistredZC_39.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _CumulTTFrom.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _UpdateCalendar.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _RegisterZadok.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _PTQ.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                ret += _GAImean.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityPhenology.Strategies.Phenology");
                if (ret != "") { pre.TestsOut(ret, true, "   preconditions tests of associated classes"); }

                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in component " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component SiriusQuality.Phenology, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SiriusQualityPhenology, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        private void CalculateModel(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            EstimateOfAssociatedClasses(s, s1, r, a, ex);
        }

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

        private void EstimateOfAssociatedClasses(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            _GAImean.Estimate(s,s1, r, a, ex);
            _PTQ.Estimate(s,s1, r, a, ex);
            _CumulTTFrom.Estimate(s,s1, r, a, ex);
            _IsMomentRegistredZC_39.Estimate(s,s1, r, a, ex);
            _VernalizationProgress.Estimate(s,s1, r, a, ex);
            _PhylSowingDateCorrection.Estimate(s,s1, r, a, ex);
            _UpdatePhase.Estimate(s,s1, r, a, ex);
            _LeafNumber.Estimate(s,s1, r, a, ex);
            _ShootNumber.Estimate(s,s1, r, a, ex);
            _UpdateLeafFlag.Estimate(s,s1, r, a, ex);
            _RegisterZadok.Estimate(s,s1, r, a, ex);
            _UpdateCalendar.Estimate(s,s1, r, a, ex);
            _Phyllochron.Estimate(s,s1, r, a, ex);
        }

        public void Init(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            DateTime sowingDate = new DateTime(2007, 3, 21);
            s.calendarMoments.Add("Sowing");
            s.calendarCumuls.Add(0.0d);
            s.calendarDates.Add(sowingDate);
            s.minFinalNumber = 5.5d;
            _ShootNumber.Init(s, s1, r, a, ex);
        
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
    }
}
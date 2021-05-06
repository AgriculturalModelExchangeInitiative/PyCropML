from datetime import datetime
from math import *
from Phyllochron import model_Phyllochron
from PhylSowingDateCorrection import model_PhylSowingDateCorrection
from ShootNumber import model_ShootNumber
from UpdateLeafFlag import model_UpdateLeafFlag
from UpdatePhase import model_UpdatePhase
from LeafNumber import model_LeafNumber
from VernalizationProgress import model_VernalizationProgress
from IsMomentRegistredZC_39 import model_IsMomentRegistredZC_39
from CumulTTFrom import model_CumulTTFrom
from UpdateCalendar import model_UpdateCalendar
from RegisterZadok import model_RegisterZadok
from PTQ import model_PTQ
from GAImean import model_GAImean
def model_Phenology(float phyllochron_t1=0.0,
      float minFinalNumber_t1=5.5,
      float aMXLFNO=24.0,
      datetime currentdate=datetime(2007, 3, 27) ,
      float cumulTT=112.330110409888,
      float pNini=4.0,
      float sDsa_sh=1.0,
      float latitude=0.0,
      float kl=0.45,
      list calendarDates_t1=[datetime(2007, 3, 21) ,],
      list calendarMoments_t1=['Sowing'],
      float lincr=8.0,
      float ldecr=0.0,
      float pincr=1.5,
      float ptq=0.0,
      float pTQhf=0.0,
      float B=20.0,
      float areaSL=0.0,
      float areaSS=0.0,
      float lARmin=0.0,
      float sowingDensity=0.0,
      float lARmax=0.0,
      float lNeff=0.0,
      float rp=0.0,
      float p=120.0,
      float pdecr=0.4,
      float leafNumber_t1=0.0,
      float maxTvern=23.0,
      float dayLength=12.3037621834005,
      float deltaTT=0.0,
      float pastMaxAI_t1=0.0,
      float tTWindowForPTQ=0.0,
      list listGAITTWindowForPTQ_t1=[0.0],
      float gAI=0.0,
      float pAR=0.0,
      list listPARTTWindowForPTQ_t1=[0.0],
      list listTTShootWindowForPTQ1_t1=[0.0],
      list listTTShootWindowForPTQ_t1=[0.0],
      float vBEE=0.01,
      list calendarCumuls_t1=[0.0],
      int isVernalizable=1,
      float vernaprog_t1=0.5517254187376879,
      float minTvern=0.0,
      float intTvern=11.0,
      float vAI=0.015,
      float maxDL=15.0,
      str choosePhyllUse='Default',
      float minDL=8.0,
      int hasLastPrimordiumAppeared_t1=0,
      float phase_t1=1.0,
      float pFLLAnth=2.22,
      float dcd=100.0,
      float dgf=450.0,
      float degfm=0.0,
      bool ignoreGrainMaturation=False,
      float pHEADANTH=1.0,
      float finalLeafNumber_t1=0.0,
      float sLDL=0.85,
      float grainCumulTT=0.0,
      int sowingDay=1,
      int hasZadokStageChanged_t1=0,
      str currentZadokStage_t1='MainShootPlus1Tiller',
      int sDws=1,
      float sDsa_nh=1.0,
      int hasFlagLeafLiguleAppeared=0,
      float der=300.0,
      int hasFlagLeafLiguleAppeared_t1=1,
      list tilleringProfile_t1=[288.0],
      float targetFertileShoot=600.0,
      list leafTillerNumberArray_t1=[1, 1, 1],
      float dse=105.0,
      float slopeTSFLN=0.9,
      float intTSFLN=2.6,
      float canopyShootNumber_t1=288.0):
    cdef float fixPhyll
    cdef float leafNumber
    cdef float gAImean
    cdef float phyllochron
    cdef int numberTillerCohort_t1
    cdef float averageShootNumberPerPlant
    cdef float canopyShootNumber
    cdef intlist leafTillerNumberArray
    cdef floatlist tilleringProfile
    cdef int numberTillerCohort
    cdef stringlist calendarMoments
    cdef datelist calendarDates
    cdef floatlist calendarCumuls
    cdef float finalLeafNumber
    cdef float phase
    cdef float cumulTTFromZC_39
    cdef int isMomentRegistredZC_39
    cdef float vernaprog
    cdef float minFinalNumber
    cdef float cumulTTFromZC_91
    cdef int hasLastPrimordiumAppeared
    cdef float cumulTTFromZC_65
    cdef int hasZadokStageChanged
    cdef str currentZadokStage
    cdef floatlist listGAITTWindowForPTQ
    cdef floatlist listPARTTWindowForPTQ
    cdef floatlist listTTShootWindowForPTQ
    cdef float pastMaxAI
    cdef floatlist listTTShootWindowForPTQ1
    gAImean, pastMaxAI, listTTShootWindowForPTQ1, listGAITTWindowForPTQ = model_GAImean( gAI,tTWindowForPTQ,deltaTT,pastMaxAI_t1,listTTShootWindowForPTQ1_t1,listGAITTWindowForPTQ_t1)
    listPARTTWindowForPTQ, listTTShootWindowForPTQ, ptq = model_PTQ( tTWindowForPTQ,kl,listTTShootWindowForPTQ_t1,listPARTTWindowForPTQ_t1,listGAITTWindowForPTQ,pAR,deltaTT)
    cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91 = model_CumulTTFrom( calendarMoments_t1,calendarCumuls_t1,cumulTT)
    isMomentRegistredZC_39 = model_IsMomentRegistredZC_39( calendarMoments_t1)
    vernaprog, minFinalNumber, calendarMoments, calendarDates, calendarCumuls = model_VernalizationProgress( dayLength,deltaTT,cumulTT,leafNumber_t1,calendarMoments_t1,calendarDates_t1,calendarCumuls_t1,minTvern,intTvern,vAI,vBEE,minDL,maxDL,maxTvern,pNini,aMXLFNO,vernaprog_t1,currentdate,isVernalizable,minFinalNumber_t1)
    fixPhyll = model_PhylSowingDateCorrection( sowingDay,latitude,sDsa_sh,rp,sDws,sDsa_nh,p)
    finalLeafNumber, phase, hasLastPrimordiumAppeared = model_UpdatePhase( cumulTT,leafNumber_t1,cumulTTFromZC_39,isMomentRegistredZC_39,gAI,grainCumulTT,dayLength,vernaprog,minFinalNumber,fixPhyll,isVernalizable,dse,pFLLAnth,dcd,dgf,degfm,maxDL,sLDL,ignoreGrainMaturation,pHEADANTH,choosePhyllUse,p,phase_t1,cumulTTFromZC_91,phyllochron,hasLastPrimordiumAppeared_t1,finalLeafNumber_t1)
    leafNumber = model_LeafNumber( deltaTT,phyllochron_t1,hasFlagLeafLiguleAppeared,leafNumber_t1,phase)
    averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, numberTillerCohort = model_ShootNumber( canopyShootNumber_t1,leafNumber,sowingDensity,targetFertileShoot,tilleringProfile_t1,leafTillerNumberArray_t1,numberTillerCohort_t1)
    hasFlagLeafLiguleAppeared, calendarMoments, calendarDates, calendarCumuls = model_UpdateLeafFlag( cumulTT,leafNumber,calendarMoments,calendarDates,calendarCumuls,currentdate,finalLeafNumber,hasFlagLeafLiguleAppeared_t1,phase)
    hasZadokStageChanged, currentZadokStage, calendarMoments, calendarDates, calendarCumuls = model_RegisterZadok( cumulTT,phase,leafNumber,calendarMoments,calendarDates,calendarCumuls,cumulTTFromZC_65,currentdate,der,slopeTSFLN,intTSFLN,finalLeafNumber,currentZadokStage_t1,hasZadokStageChanged_t1)
    calendarMoments, calendarDates, calendarCumuls = model_UpdateCalendar( cumulTT,calendarMoments,calendarDates,calendarCumuls,currentdate,phase)
    phyllochron = model_Phyllochron( fixPhyll,leafNumber,lincr,ldecr,pdecr,pincr,ptq,gAImean,kl,pTQhf,B,p,choosePhyllUse,areaSL,areaSS,lARmin,lARmax,sowingDensity,lNeff)
    return currentZadokStage, hasZadokStageChanged, hasFlagLeafLiguleAppeared, listPARTTWindowForPTQ, hasLastPrimordiumAppeared, listTTShootWindowForPTQ, listTTShootWindowForPTQ1, ptq, calendarMoments, canopyShootNumber, calendarDates, leafTillerNumberArray, vernaprog, phyllochron, leafNumber, numberTillerCohort, tilleringProfile, averageShootNumberPerPlant, minFinalNumber, finalLeafNumber, phase, listGAITTWindowForPTQ, calendarCumuls, gAImean, pastMaxAI

def init_Phenology(float aMXLFNO=24.0,
                     datetime currentdate=datetime(2007, 3, 27) ,
                     float cumulTT=112.330110409888,
                     float pNini=4.0,
                     float sDsa_sh=1.0,
                     float latitude=0.0,
                     float kl=0.45,
                     float lincr=8.0,
                     float ldecr=0.0,
                     float pincr=1.5,
                     float pTQhf=0.0,
                     float B=20.0,
                     float areaSL=0.0,
                     float areaSS=0.0,
                     float lARmin=0.0,
                     float sowingDensity=0.0,
                     float lARmax=0.0,
                     float lNeff=0.0,
                     float rp=0.0,
                     float p=120.0,
                     float pdecr=0.4,
                     float maxTvern=23.0,
                     float dayLength=12.3037621834005,
                     float deltaTT=0.0,
                     float tTWindowForPTQ=0.0,
                     float gAI=0.0,
                     float pAR=0.0,
                     float vBEE=0.01,
                     int isVernalizable=1,
                     float minTvern=0.0,
                     float intTvern=11.0,
                     float vAI=0.015,
                     float maxDL=15.0,
                     str choosePhyllUse='Default',
                     float minDL=8.0,
                     float pFLLAnth=2.22,
                     float dcd=100.0,
                     float dgf=450.0,
                     float degfm=0.0,
                     bool ignoreGrainMaturation=False,
                     float pHEADANTH=1.0,
                     float sLDL=0.85,
                     float grainCumulTT=0.0,
                     int sowingDay=1,
                     int sDws=1,
                     float sDsa_nh=1.0,
                     float der=300.0,
                     float targetFertileShoot=600.0,
                     float dse=105.0,
                     float slopeTSFLN=0.9,
                     float intTSFLN=2.6):

    cdef str currentZadokStage ='' 
    cdef int hasZadokStageChanged = 0
    cdef int hasFlagLeafLiguleAppeared = 0
    cdef floatlist listPARTTWindowForPTQ
    cdef int hasLastPrimordiumAppeared = 0
    cdef floatlist listTTShootWindowForPTQ
    cdef floatlist listTTShootWindowForPTQ1
    cdef float ptq = 0.0
    cdef stringlist calendarMoments
    cdef float canopyShootNumber = 0.0
    cdef datelist calendarDates 
    cdef intlist leafTillerNumberArray
    cdef float vernaprog = 0.0
    cdef float phyllochron = 0.0
    cdef float leafNumber = 0.0
    cdef int numberTillerCohort = 0
    cdef floatlist tilleringProfile
    cdef float averageShootNumberPerPlant = 0.0
    cdef float minFinalNumber = 0.0
    cdef float finalLeafNumber = 0.0
    cdef float phase = 0.0
    cdef floatlist listGAITTWindowForPTQ
    cdef floatlist calendarCumuls
    cdef float gAImean = 0.0
    cdef float pastMaxAI = 0.0
    cdef datetime sowingDate = datetime(2017,12,3)
    calendarMoments.append("Sowing");
    calendarCumuls.append(0.0);
    calendarDates.append(sowingDate);
    minFinalNumber = 5.5;        
    #model_ShootNumber.Init();
    return  currentZadokStage, hasZadokStageChanged, hasFlagLeafLiguleAppeared, listPARTTWindowForPTQ, hasLastPrimordiumAppeared, listTTShootWindowForPTQ, listTTShootWindowForPTQ1, ptq, calendarMoments, canopyShootNumber, calendarDates, leafTillerNumberArray, vernaprog, phyllochron, leafNumber, numberTillerCohort, tilleringProfile, averageShootNumberPerPlant, minFinalNumber, finalLeafNumber, phase, listGAITTWindowForPTQ, calendarCumuls, gAImean, pastMaxAI

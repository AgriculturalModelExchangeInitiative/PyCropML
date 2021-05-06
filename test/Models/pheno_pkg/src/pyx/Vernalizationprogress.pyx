import numpy 
from math import *
from datetime import datetime

def model_vernalizationprogress(float dayLength=12.3037621834005,
                                float deltaTT=20.3429985011972,
                                float cumulTT=112.330110409888,
                                float leafNumber_t1=0.0,
                                list calendarMoments_t1=['Sowing'],
                                list calendarDates_t1=[datetime(2007, 3, 21) ,],
                                list calendarCumuls_t1=[0.0],
                                float minTvern=0.0,
                                float intTvern=11.0,
                                float vAI=0.015,
                                float vBEE=0.01,
                                float minDL=8.0,
                                float maxDL=15.0,
                                float maxTvern=23.0,
                                float pNini=4.0,
                                float aMXLFNO=24.0,
                                float vernaprog_t1=0.5517254187376879,
                                datetime currentdate=datetime(2007, 3, 27) ,
                                int isVernalizable=1,
                                float minFinalNumber_t1=5.5):
    """

    VernalizationProgress Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: Calculate progress (VernaProg) towards vernalization, but there 
        			is no vernalization below minTvern 
        			and above maxTvern . The maximum value of VernaProg is 1.
        			Progress towards full vernalization is a linear function of shoot 
        			temperature (soil temperature until leaf # reach MaxLeafSoil and then
        			 canopy temperature)
    	

    """
    cdef float vernaprog
    cdef float minFinalNumber
    cdef stringlist calendarMoments
    cdef datelist calendarDates
    cdef floatlist calendarCumuls
    cdef float maxVernaProg, dLverna, primordno, minLeafNumber, potlfno, tt
    calendarMoments = copy(calendarMoments_t1)
    calendarCumuls = copy(calendarCumuls_t1)
    calendarDates = copy(calendarDates_t1) 
    minFinalNumber = minFinalNumber_t1
    vernaprog = vernaprog_t1
    if (isVernalizable==1 and vernaprog_t1 < 1.0):
        tt = deltaTT       
        if (tt >= minTvern and tt <= intTvern):
            vernaprog = vernaprog_t1 + vAI * tt + vBEE  
        else:
            vernaprog = vernaprog_t1
        if (tt > intTvern):
            maxVernaProg = vAI * intTvern + vBEE
            dLverna = max(minDL, min(maxDL, dayLength))
            vernaprog += max(0.0, maxVernaProg * (1.0 + ((intTvern - tt) / (maxTvern - intTvern)) * ((dLverna - minDL) / (maxDL - minDL))))      
        primordno = 2.0 * leafNumber_t1 + pNini     
        minLeafNumber = minFinalNumber_t1
        if (vernaprog >= 1.0 or primordno >= aMXLFNO):      
            minFinalNumber = max(primordno, minFinalNumber_t1)
            calendarMoments.append("EndVernalisation")
            calendarCumuls.append(cumulTT)
            calendarDates.append(currentdate)        
            vernaprog = max(1.0, vernaprog)      
        else:    
            potlfno = aMXLFNO - (aMXLFNO - minLeafNumber) * vernaprog
            if (primordno >= potlfno):    
                minFinalNumber = max((potlfno + primordno) / 2.0, minFinalNumber_t1)
                vernaprog = max(1.0, vernaprog)
                calendarMoments.append("EndVernalisation")
                calendarCumuls.append(cumulTT) 
                calendarDates.append(currentdate)
    return  vernaprog, minFinalNumber, calendarMoments, calendarDates, calendarCumuls


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

             


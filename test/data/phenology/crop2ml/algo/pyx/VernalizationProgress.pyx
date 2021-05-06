
cdef float maxVernaProg, dLverna, primordno, minLeafNumber, potlfno, tt
if (isVernalizable==1 and vernaprog < 1.0):
    tt = deltaTT       
    if (tt >= minTvern and tt <= intTvern):
        vernaprog = vernaprog + vAI * tt + vBEE      
    if (tt > intTvern):
        maxVernaProg = vAI * intTvern + vBEE
        dLverna = max(minDL, min(maxDL, dayLength))
        vernaprog += max(0.0, maxVernaProg * (1.0 + ((intTvern - tt) / (maxTvern - intTvern)) * ((dLverna - minDL) / (maxDL - minDL))))      
    primordno = 2.0 * leafNumber + pNini     
    minLeafNumber = minFinalNumber
    if (vernaprog >= 1.0 or primordno >= aMXLFNO):      
        minFinalNumber = max(primordno, minFinalNumber)
        calendarMoments.append("EndVernalisation")
        calendarCumuls.append(cumulTT) 
        calendarDates.append(currentdate)        
        vernaprog = max(1.0, vernaprog)      
    else:    
        potlfno = aMXLFNO - (aMXLFNO - minLeafNumber) * vernaprog
        if (primordno >= potlfno):    
            minFinalNumber = max((potlfno + primordno) / 2.0, minFinalNumber)
            vernaprog = max(1.0, vernaprog)
            calendarMoments.append("EndVernalisation")
            calendarCumuls.append(cumulTT) 
            calendarDates.append(currentdate)

             


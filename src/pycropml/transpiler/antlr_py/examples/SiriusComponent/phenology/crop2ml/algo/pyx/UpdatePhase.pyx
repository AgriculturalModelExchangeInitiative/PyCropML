cdef float ttFromLastLeafToHeading 
cdef float appFLN 
cdef float localDegfm 
cdef float ttFromLastLeafToAnthesis 
hasLastPrimordiumAppeared = hasLastPrimordiumAppeared_t1
finalLeafNumber = finalLeafNumber_t1
phase = phase_t1
if phase_t1 >= 0.0 and phase_t1 < 1.0:
    if cumulTT >= dse:
        phase = 1.0
    else:
        phase = phase_t1
elif phase_t1 >= 1.0 and phase_t1 < 2.0:
    if isVernalizable == 1 and vernaprog >= 1.0 or isVernalizable == 0:
        if dayLength > maxDL:
            finalLeafNumber = minFinalNumber
            hasLastPrimordiumAppeared = 1
        else:
            appFLN = minFinalNumber + (sLDL * (maxDL - dayLength))
            if appFLN / 2.0 <= leafNumber_t1:
                finalLeafNumber = appFLN
                hasLastPrimordiumAppeared = 1
            else:
                phase = phase_t1
        if hasLastPrimordiumAppeared == 1:
            phase = 2.0
    else:
        phase = phase_t1
elif phase_t1 >= 2.0 and phase_t1 < 4.0:
    if isMomentRegistredZC_39 == 1:
        if phase_t1 < 3.0:
            ttFromLastLeafToHeading = 0.0
            if choosePhyllUse == "Default":
                ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * fixPhyll
            elif choosePhyllUse == "PTQ":
                ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron
            elif choosePhyllUse == "Test":
                ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p
            if cumulTTFromZC_39 >= ttFromLastLeafToHeading:
                phase = 3.0
            else:
                phase = phase_t1
        else:
            phase = phase_t1
        ttFromLastLeafToAnthesis = 0.0
        if choosePhyllUse == "Default":
            ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll
        elif choosePhyllUse == "PTQ":
            ttFromLastLeafToAnthesis = pFLLAnth * phyllochron
        elif choosePhyllUse == "Test":
            ttFromLastLeafToAnthesis = pFLLAnth * p
        if cumulTTFromZC_39 >= ttFromLastLeafToAnthesis:
            phase = 4.0
    else:
        phase = phase_t1
elif phase_t1 == 4.0:
    if grainCumulTT >= dcd:
        phase = 4.5
    else:
        phase = phase_t1
elif phase_t1 == 4.5:
    if grainCumulTT >= dgf or gAI <= 0.0:
        phase = 5.0
    else:
        phase = phase_t1
elif phase_t1 >= 5.0 and phase_t1 < 6.0:
    localDegfm = degfm
    if ignoreGrainMaturation:
        localDegfm = -1.0
    if cumulTTFromZC_91 >= localDegfm:
        phase = 6.0
    else:
        phase = phase_t1
elif phase_t1 >= 6.0 and phase_t1 < 7.0:
    phase = phase_t1
cdef float ttFromLastLeafToHeading, appFLN, localDegfm, ttFromLastLeafToAnthesis
if (phase >= 0.0 and phase < 1.0):
    if (cumulTT >= dse):
        phase = 1.0  #Emergence            
elif (phase >= 1.0 and phase < 2.0):  #EmergenceToFloralInitiation
    if ((isVernalizable==1 and vernaprog >= 1.0) or (isVernalizable==0)):
        if (dayLength > maxDL):
            finalLeafNumber = minFinalNumber
            hasLastPrimordiumAppeared = 1
        else:
            appFLN = minFinalNumber + sLDL * (maxDL - dayLength)                    
                # calculation of final leaf number from daylength at inflexion plus 2 leaves
            if (appFLN / 2.0 <= leafNumber):
                finalLeafNumber = appFLN
                hasLastPrimordiumAppeared =1
            #CheckFloralInitiation
        if (hasLastPrimordiumAppeared==1):              
                phase = 2.0#Floralinitiation              
elif (phase >= 2.0 and phase < 4.0):#FloralInitiationToAnthesis
    if (isMomentRegistredZC_39==1):
                  #calculate the heading date
        if (phase < 3.0):
            ttFromLastLeafToHeading = 0.0
            if(choosePhyllUse=="Default"): ttFromLastLeafToHeading =(pFLLAnth - pHEADANTH) * fixPhyll
            elif (choosePhyllUse == "PTQ"): ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron
            elif (choosePhyllUse == "Test"): ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p
            if (cumulTTFromZC_39 >= ttFromLastLeafToHeading):
                phase = 3.0                       
                #CheckAnthesis;
        ttFromLastLeafToAnthesis =0.0
        if (choosePhyllUse == "Default"): ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll
        elif (choosePhyllUse == "PTQ"): ttFromLastLeafToAnthesis = pFLLAnth * phyllochron
        elif (choosePhyllUse == "Test"): ttFromLastLeafToAnthesis = pFLLAnth * p      
        if (cumulTTFromZC_39 >= ttFromLastLeafToAnthesis):
            phase = 4.0#Anthesis                     
elif (phase == 4.0):#AnthesisToEndCellDivision          
                #CheckEndCellDivision
    if (grainCumulTT >= dcd):             
        phase = 4.5#EndCellDivision                            
elif (phase == 4.5):#EndCellDivisionToEndGrainFill    
                # CheckEndGrainFilling
    if (grainCumulTT >= dgf or gai <= 0.0):          
        phase = 5.0#End of grain filling              
elif (phase >= 5.0 and phase < 6.0):#EndGrainFillToMaturity
                #CheckMaturity
                #/<Comment>To enable ignoring grain maturation duration</Comment>
    localDegfm = degfm
    if ignoreGrainMaturation: localDegfm = -1.0       
    if (cumulTTFromZC_91 >= localDegfm ):        
        phase = 6.0 #maturity               
    
    
    
    
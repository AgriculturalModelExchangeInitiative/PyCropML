cdef float gai_
if choosePhyllUse =="Default":
    if (leafNumber < ldecr): phyllochron = fixPhyll * pdecr
    elif (leafNumber >= ldecr and leafNumber < lincr): phyllochron = fixPhyll
    else: phyllochron = fixPhyll * pincr
if choosePhyllUse =="PTQ":
    gai_ = max(pastMaxAI,gai)
    pastMaxAI = gai_
    if (gai_ > 0.0): phyllochron = phylPTQ1 * ((gai_ * kl) / (1 - exp(-kl * gai_))) / (ptq + aPTQ)
    else: phyllochron = phylPTQ1      
if choosePhyllUse == "Test":
    if (leafNumber < ldecr): phyllochron = p * pdecr
    elif (leafNumber >= ldecr and leafNumber < lincr): phyllochron = p
    else: phyllochron = p * pincr
        

    
 


if choosePhyllUse =="Default":
    if (leafNumber < ldecr): phyllochron = fixPhyll * pdecr
    elif (leafNumber >= ldecr and leafNumber < lincr): phyllochron = fixPhyll
    else: phyllochron = fixPhyll * pincr
if choosePhyllUse =="PTQ":
    pastMaxAI1 = pastMaxAI
    gai = max(pastMaxAI1,gai)
    pastMaxAI = gai
    if (gai > 0.0): phyllochron = phylPTQ1 * ((gai * kl) / (1 - exp(-kl * gai))) / (ptq + aPTQ)
    else: phyllochron = phylPTQ1      
if choosePhyllUse == "Test":
    if (leafNumber < ldecr): phyllochron = p * pdecr
    elif (leafNumber >= ldecr and leafNumber < lincr): phyllochron = p
    else: phyllochron = p * pincr
        

    
 

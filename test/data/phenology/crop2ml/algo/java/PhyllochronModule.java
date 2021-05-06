
phyllochron=0;
if (choosePhyllUse =="Default")
{
	if (leafNumber < ldecr) phyllochron = fixPhyll * pdecr;
	else if (leafNumber >= ldecr && leafNumber < lincr) phyllochron = fixPhyll;
	else phyllochron = fixPhyll * pincr;
}        
if (choosePhyllUse =="PTQ")
{
    gai = Math.max(pastMaxAI,gai);
    pastMaxAI = gai;
    if (gai > 0.0) phyllochron = phylPTQ1 * ((gai * kl) / (1 - Math.exp(-kl * gai))) / (ptq + aPTQ);
    else phyllochron = phylPTQ1;    
}        
if (choosePhyllUse == "Test")
{
    if (leafNumber < ldecr) phyllochron = p * pdecr;
    else if (leafNumber >= ldecr && leafNumber < lincr)  phyllochron = p;
    else phyllochron = p * pincr;
}       

    
 

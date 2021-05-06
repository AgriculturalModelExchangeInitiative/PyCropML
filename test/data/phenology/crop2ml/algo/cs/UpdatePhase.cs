	
 double ttFromLastLeafToHeading, appFLN, localDegfm, ttFromLastLeafToAnthesis;				
if (phase >= 0.0 && phase < 1.0)//SowingToEmergence
{
			//CheckEmergence

	if (cumulTT>= dse)
	{
		phase = 1.0;//Emergence
	}

}
else if (phase >= 1.0 && phase < 2.0)//EmergenceToFloralInitiation
{
	if ((isVernalizable==1 && vernaprog >= 1.0) || (isVernalizable==0))
	{
		if (dayLength > maxDL)
		{
			finalLeafNumber = minFinalNumber;
			hasLastPrimordiumAppeared = 1;						
		}
		else
		{
			appFLN = minFinalNumber + sLDL * (maxDL - dayLength);
						// calculation of final leaf number from dayLength at inflexion plus 2 leaves
			if (appFLN / 2.0 <= leafNumber)
			{
				finalLeafNumber = appFLN;
				hasLastPrimordiumAppeared =1;
			}
		}
			//for Maize phenologystate.hasLastPrimordiumAppeared = true;
				//CheckFloralInitiation
		if (hasLastPrimordiumAppeared==1)
		{
			phase = 2.0;//Floralinitiation
		}			
	}
}
else if (phase >= 2.0 && phase < 4.0)//FloralInitiationToAnthesis
{
	if (isMomentRegistredZC_39==1)
	{
				//calculate the heading date
		if (phase < 3.0)
		{
			ttFromLastLeafToHeading = 0.0;
			if(choosePhyllUse=="Default")ttFromLastLeafToHeading =(pFLLAnth - pHEADANTH) * fixPhyll;
			else if (choosePhyllUse == "PTQ") ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron;
			else if (choosePhyllUse == "Test") ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p;
			if (cumulTTFromZC_39 >= ttFromLastLeafToHeading)
			{
				phase = 3.0;
			}
		}					
				//CheckAnthesis;
		ttFromLastLeafToAnthesis =0.0;
		if (choosePhyllUse == "Default") ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll;
		else if (choosePhyllUse == "PTQ") ttFromLastLeafToAnthesis = pFLLAnth * phyllochron;
		else if (choosePhyllUse == "Test") ttFromLastLeafToAnthesis = pFLLAnth * p;

		if (cumulTTFromZC_39 >= ttFromLastLeafToAnthesis)
		{
				phase = 4.0;//Anthesis
		}
	}		
}
else if (phase == 4.0)//AnthesisToEndCellDivision
{
			//CheckEndCellDivision
	if (grainCumulTT >= dcd)
	{
		phase = 4.5;//EndCellDivision
	}
}
else if (phase == 4.5)//EndCellDivisionToEndGrainFill
{
			// CheckEndGrainFilling
	if (grainCumulTT >= dgf || gai <= 0.0)
	{
		phase = 5.0;//End of grain filling
	}
}
else if (phase >= 5.0 && phase < 6.0)//EndGrainFillToMaturity
{
			//CheckMaturity
			///<Comment>To enable ignoring grain maturation duration</Comment>
	localDegfm = degfm;
	if (ignoreGrainMaturation==true) localDegfm = -1;			
	if (cumulTTFromZC_91 >= localDegfm)
	{
		phase = 6.0; //maturity
	}
}

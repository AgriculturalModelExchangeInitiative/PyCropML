
if (IsVernalizable==1 && vernaprog < 1.0)
{
	tt = deltaTT; // other sirius versions use previous temperature value
	if (tt >= minTvern && tt <= intTvern)
	{
		vernaprog = vernaprog + vAI * tt + vBEE;
	}
	if (tt > intTvern)
	{
		double maxVernaProg = vAI * intTvern + vBEE;
		double DLverna = Math.Max(minDL, Math.Min(maxDL, dayLength));
		vernaprog += Math.Max(0.0, maxVernaProg * (1 + ((intTvern - tt) / (maxTvern - intTvern)) * ((dLverna - minDL) / (maxDL - minDL))));
	}			
	double primordno = 2.0 * leafNumber + pNini;
	double minLeafNumber = minFinalNumber;
	if (vernaprog >= 1.0 || primordno >= aMXLFNO)
	{
		MinFinalNumber = Math.Max(primordno, minFinalNumber);
		calendarMoments.Add("EndVernalisation");
        calendarCumuls.Add(cumulTT) ;
        calendarDates.Add(currentdate);  
	}
	else
	{
		double potlfno = aMXLFNO - (aMXLFNO - minLeafNumber) * vernaprog;
		if (primordno >= potlfno)
		{
			MinFinalNumber = Math.Max((potlfno + primordno) / 2.0, minFinalNumber);	
			calendarMoments.Add("EndVernalisation");
        	calendarCumuls.Add(cumulTT);
        	calendarDates.Add(currentdate);  					
			vernaprog = Math.Max(1.0, vernaprog);
		}

	}
}

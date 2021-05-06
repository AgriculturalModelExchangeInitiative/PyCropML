
if (isVernalizable==1 && vernaprog < 1)
{
	double tt = deltaTT; // other sirius versions use previous temperature value
	if (tt >= minTvern && tt <= intTvern)
	{
		vernaprog = vernaprog + vAI * tt + vBEE;
	}
	if (tt > intTvern)
	{
		double maxVernaProg = vAI * intTvern + vBEE;
		double dLverna = Math.max(minDL, Math.min(maxDL, dayLength));
		vernaprog += Math.max(0, maxVernaProg * (1 + ((intTvern - tt) / (maxTvern - intTvern)) * ((dLverna - minDL) / (maxDL - minDL))));
	}			
	double primordno = 2.0 * leafNumber + pNini;
	double minLeafNumber = minFinalNumber;
	if (vernaprog >= 1.0 || primordno >= aMXLFNO)
	{
		minFinalNumber = Math.max(primordno, minFinalNumber);
		calendarMoments.add("EndVernalisation");
        calendarCumuls.add(cumulTT) ;
        calendarDates.add(currentdate);  
	}
	else
	{
		double potlfno = aMXLFNO - (aMXLFNO - minLeafNumber) * vernaprog;
		if (primordno >= potlfno)
		{
			minFinalNumber = Math.max((potlfno + primordno) / 2.0, minFinalNumber);	
			calendarMoments.add("EndVernalisation");
        	calendarCumuls.add(cumulTT);
        	calendarDates.add(currentdate);  					
			vernaprog = Math.max(1, vernaprog);
		}
	}
}

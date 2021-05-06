

double maxVernaProg, dLverna, primordno, minLeafNumber, tt, potlfno;
if (isVernalizable == 1 && vernaprog < 1)
{
	tt = deltaTT; // other sirius versions use previous temperature value
	if (tt >= minTvern && tt <= intTvern)
	{
		vernaprog = vernaprog + vAI * tt + vBEE;
	}
	if (tt > intTvern)
	{
		maxVernaProg = VAI * intTvern + vBEE;
		dLverna = fmax(minDL, fmin(maxDL, dayLength));
		vernaprog += fmax(0, maxVernaProg * (1 + ((intTvern - tt) / (maxTvern - intTvern)) * ((DLverna - minDL) / (maxDL - minDL))));
	}
	primordno = 2.0 * leafNumber + pNini;
	minLeafNumber = minFinalNumber;
	if (vernaprog >= 1.0 || primordno >= aMXLFNO)
	{
		minFinalNumber = fmax(primordno, minFinalNumber);
		calendarMoments.push_back("EndVernalisation");
		calendarCumuls.push_back(cumulTT);
		calendarDates.push_back(currentdate);
	}
	else
	{
		potlfno = aMXLFNO - (aMXLFNO - minLeafNumber) * vernaprog;
		if (primordno >= potlfno)
		{
			minFinalNumber = fmax((potlfno + primordno) / 2.0, minFinalNumber);
			calendarMoments.push_back("EndVernalisation");
			calendarCumuls.push_back(cumulTT);
			calendarDates.push_back(currentdate);
			vernaprog = fmax(1, vernaprog);
		}
	}
}

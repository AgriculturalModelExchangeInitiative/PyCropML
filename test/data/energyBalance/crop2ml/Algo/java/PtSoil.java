double AlphaE;
if (tau < tauAlpha)
{
	AlphaE = 1 ;
}
else
{
AlphaE = Alpha - ((Alpha - 1) * (1 - tau) / (1 - tauAlpha));
}
energyLimitedEvaporation= (evapoTranspirationPriestlyTaylor / Alpha) * AlphaE * tau


		
if (phase >= 1.0 && phase< 4.0)
{
	if (hasFlagLeafLiguleAppeared==0)//sowingToAnthesis
	{
		if (phyllochron == 0.0)
		{
			phyllochron = 0.0000001;		
		}
		leafNumber = leafNumber + Math.Min(deltaTT / phyllochron, 0.999);	
	}
}
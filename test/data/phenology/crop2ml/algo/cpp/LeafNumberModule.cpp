
if (phase >= 1 && phase < 4)
{
	if (hasFlagLeafLiguleAppeared == 0) //sowingToAnthesis
	{
		if (phyllochron == 0.0)
		{
			phyllochron = 0.0000001;
		}
		leafNumber = leafNumber + fmin(deltaTT / phyllochron, 0.999);
	}
}

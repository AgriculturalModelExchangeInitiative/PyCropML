
if (latitude < 0.0)
{
	if (sowingDay > sDsa_sh)
	{
		fixPhyll = p * (1 - rp * Math.min(sowingDay - sDsa_sh, sDws));
	}
	else fixPhyll = p;
}
else
{
	if (sowingDay < sDsa_nh)
	{
		fixPhyll = p * (1 - rp * Math.min(sowingDay, sDws));
	}
	else fixPhyll = p;
}
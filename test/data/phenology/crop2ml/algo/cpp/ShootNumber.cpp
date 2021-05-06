
int emergedLeaves, shoots;
double oldCanopyShootNumber;
oldCanopyShootNumber = canopyShootNumber;
emergedLeaves = (int)fmax(1, ceil(leafNumber - 1));
shoots = Calculate_Fibonacci(emergedLeaves).value;
canopyShootNumber = fmin(shoots * sowingDensity, targetFertileShoot);
averageShootNumberPerPlant = canopyShootNumber / sowingDensity;
if (canopyShootNumber != oldCanopyShootNumber)
{
	tilleringProfile.push_back(canopyShootNumber - oldCanopyShootNumber);
}
tillerNumber = tilleringProfile.size();
for (int i = leafTillerNumberArray.size(); i < ceil(leafNumber); i++)
{
	leafTillerNumberArray.push_back(tillerNumber);
}

int emergedLeaves, shoots;
double oldCanopyShootNumber;
oldCanopyShootNumber = canopyShootNumber;
emergedLeaves = (int)Math.max(1, Math.ceil(leafNumber - 1));
shoots = fibonacci(emergedLeaves);
canopyShootNumber = Math.min(shoots * sowingDensity, targetFertileShoot);
averageShootNumberPerPlant = canopyShootNumber / sowingDensity;
if (canopyShootNumber != oldCanopyShootNumber)
{
	tilleringProfile.add(canopyShootNumber - oldCanopyShootNumber);
}		
tillerNumber = tilleringProfile.size();		
for (int i = leafTillerNumberArray.size(); i < Math.ceil(leafNumber); i++)
{
	leafTillerNumberArray.add(tillerNumber);
}

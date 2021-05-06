
double oldCanopyShootNumber;
int emergedLeaves, shoots, i;
oldCanopyShootNumber = canopyShootNumber;
emergedLeaves = (int)Math.Max(1.0, Math.Ceiling(leafNumber - 1));
shoots = fibonacci(emergedLeaves);
canopyShootNumber = Math.Min(Shoots * sowingDensity, targetFertileShoot);
AverageShootNumberPerPlant = canopyShootNumber / sowingDensity;
if (canopyShootNumber != oldCanopyShootNumber)
{
	tilleringProfile.Add(canopyShootNumber - oldCanopyShootNumber);
}		
tillerNumber = tilleringProfile.Count;		
for (i = leafTillerNumberArray.Count; i < Math.Ceiling(leafNumber); i++)
{
	leafTillerNumberArray.Add(tillerNumber);
}

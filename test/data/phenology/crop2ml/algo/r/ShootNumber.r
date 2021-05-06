
oldCanopyShootNumber = canopyShootNumber
emergedLeaves = int(max(1, ceil(leafNumber - 1)))
shoots = fibonacci(emergedLeaves)
canopyShootNumber = min(shoots * sowingDensity, targetFertileShoot)
averageShootNumberPerPlant = canopyShootNumber / sowingDensity       
if (canopyShootNumber != oldCanopyShootNumber):
    tilleringProfile.append(canopyShootNumber - oldCanopyShootNumber)         
tillerNumber = len(tilleringProfile)     
for i in range(len(leafTillerNumberArray),int(ceil(leafNumber))):
    leafTillerNumberArray.append(tillerNumber)
    




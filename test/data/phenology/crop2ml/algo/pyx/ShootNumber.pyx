
cdef float oldCanopyShootNumber
cdef int emergedLeaves, shoots, i
oldCanopyShootNumber = canopyShootNumber
emergedLeaves = int(max(1.0, ceil(leafNumber - 1)))
shoots = fibonacci_(emergedLeaves)
canopyShootNumber = min(float(shoots * sowingDensity), targetFertileShoot)
averageShootNumberPerPlant = canopyShootNumber / sowingDensity       
if (canopyShootNumber != oldCanopyShootNumber):
    tilleringProfile.append(canopyShootNumber - oldCanopyShootNumber)         
tillerNumber = len(tilleringProfile)     
for i in range(len(leafTillerNumberArray),int(ceil(leafNumber)),1):
    leafTillerNumberArray.append(tillerNumber)
    




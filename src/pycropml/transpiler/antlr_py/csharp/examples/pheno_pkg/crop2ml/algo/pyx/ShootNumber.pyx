
cdef int emergedLeaves, shoots, i
cdef intlist lNumberArray_rate
emergedLeaves = max(1, ceil(leafNumber - 1.0))
shoots = fibonacci(emergedLeaves)
canopyShootNumber = min(shoots * sowingDensity, targetFertileShoot)
averageShootNumberPerPlant = canopyShootNumber / sowingDensity
tilleringProfile = copy(tilleringProfile_t1)
if (canopyShootNumber != canopyShootNumber_t1):
    tilleringProfile.append(canopyShootNumber - canopyShootNumber_t1)
numberTillerCohort = len(tilleringProfile)
for i in range(len(leafTillerNumberArray_t1),ceil(leafNumber),1):
    lNumberArray_rate.append(numberTillerCohort)
leafTillerNumberArray = integr(leafTillerNumberArray_t1, lNumberArray_rate)
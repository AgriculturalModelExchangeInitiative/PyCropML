import numpy 
from math import *
def model_ShootNumber(float canopyShootNumber_t1=288.0,
                      float leafNumber=3.34,
                      float sowingDensity=288.0,
                      float targetFertileShoot=600.0,
                      list tilleringProfile_t1=[288.0],
                      list leafTillerNumberArray_t1=[1, 1, 1],
                      int numberTillerCohort_t1=1):
    """

    CalculateShootNumber Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA/LEPSE Montpellier
    Abstract: calculate the shoot number and update the related variables if needed

    """
    cdef float averageShootNumberPerPlant
    cdef float canopyShootNumber
    cdef intlist leafTillerNumberArray
    cdef floatlist tilleringProfile
    cdef int numberTillerCohort
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
    return  averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, numberTillerCohort
def fibonacci(int n):
    if n<=1: return n
    else: return fibonacci(n-1)+fibonacci(n-2)
def init_ShootNumber(float sowingDensity=288.0,
                     float targetFertileShoot=600.0):
    cdef float canopyShootNumber_t1
    cdef float leafNumber
    cdef floatlist tilleringProfile_t1
    cdef intlist leafTillerNumberArray_t1
    cdef int numberTillerCohort_t1
    cdef float averageShootNumberPerPlant
    cdef float canopyShootNumber
    cdef intlist leafTillerNumberArray
    cdef floatlist tilleringProfile
    cdef int numberTillerCohort
    canopyShootNumber = sowingDensity
    averageShootNumberPerPlant = 1.0
    tilleringProfile.append(sowingDensity)
    numberTillerCohort = 1
    return  averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, numberTillerCohort

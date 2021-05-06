# coding: utf8
from copy import copy

import numpy
from math import *

def model_shootnumber(canopyShootNumber_t1 = 288.0,
         leafNumber = 3.34,
         sowingDensity = 288.0,
         targetFertileShoot = 600.0,
         tilleringProfile_t1 = [288.0],
         leafTillerNumberArray_t1 = [1, 1, 1],
         numberTillerCohort_t1 = 1):
    """
     - Name: ShootNumber -Version: 1.0, -Time step: 1
     - Description:
                 * Title: CalculateShootNumber Model
                 * Author: Pierre MARTRE
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA/LEPSE Montpellier
                 * Abstract: calculate the shoot number and update the related variables if needed
     - inputs:
                 * name: canopyShootNumber_t1
                               ** min : 0
                               ** default : 288.0
                               ** max : 10000
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : shoot m-2
                               ** description : shoot number for the whole canopy
                 * name: leafNumber
                               ** min : 0
                               ** default : 3.34
                               ** max : 10000
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : Leaf number 
                 * name: sowingDensity
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 500
                               ** default : 288.0
                               ** inputtype : parameter
                               ** unit : plant m-2
                               ** description : number of plant /m²
                 * name: targetFertileShoot
                               ** parametercategory : species
                               ** min : 280
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** default : 600.0
                               ** inputtype : variable
                               ** unit : shoot
                               ** description : max value of shoot number for the canopy
                 * name: tilleringProfile_t1
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** default : [288.0]
                               ** inputtype : variable
                               ** unit : 
                               ** description :  store the amount of new tiller created at each time a new tiller appears
                 * name: leafTillerNumberArray_t1
                               ** variablecategory : state
                               ** datatype : INTLIST
                               ** default : [1, 1, 1]
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : store the number of tiller for each leaf layer
                 * name: numberTillerCohort_t1
                               ** min : 0
                               ** default : 1
                               ** max : 10000
                               ** variablecategory : state
                               ** datatype : INT
                               ** inputtype : variable
                               ** unit : 
                               ** description :  Number of tiller which appears
     - outputs:
                 * name: averageShootNumberPerPlant
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : shoot m-2
                               ** description : average shoot number per plant in the canopy
                 * name: canopyShootNumber
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : shoot m-2
                               ** description : shoot number for the whole canopy
                 * name: leafTillerNumberArray
                               ** variablecategory : state
                               ** datatype : INTLIST
                               ** unit : leaf
                               ** description : store the number of tiller for each leaf layer
                 * name: tilleringProfile
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** unit : dimensionless
                               ** description :  store the amount of new tiller created at each time a new tiller appears
                 * name: numberTillerCohort
                               ** datatype : INT
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : dimensionless
                               ** description : Number of tiller which appears
    """

    leafTillerNumberArray = []
    tilleringProfile = []
    lNumberArray_rate = []
    emergedLeaves = max(1, ceil(leafNumber - 1.0))
    shoots = fibonacci(emergedLeaves)
    canopyShootNumber = min(shoots * sowingDensity, targetFertileShoot)
    averageShootNumberPerPlant = canopyShootNumber / sowingDensity
    if canopyShootNumber != canopyShootNumber_t1:
        tilleringProfile = copy(tilleringProfile_t1)
        tilleringProfile.append(canopyShootNumber - canopyShootNumber_t1)
    numberTillerCohort = len(tilleringProfile)
    for i in range(len(leafTillerNumberArray_t1) , ceil(leafNumber) , 1):
        lNumberArray_rate.append(numberTillerCohort)
    leafTillerNumberArray = copy(leafTillerNumberArray_t1)
    leafTillerNumberArray.extend(lNumberArray_rate)
    return (averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, numberTillerCohort)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def init_shootnumber(sowingDensity = 288.0,
         targetFertileShoot = 600.0):
    tilleringProfile_t1 = []
    leafTillerNumberArray_t1 = []
    leafTillerNumberArray = []
    tilleringProfile = []
    canopyShootNumber = sowingDensity
    averageShootNumberPerPlant = 1.0
    tilleringProfile.append(sowingDensity)
    numberTillerCohort = 1
    leafTillerNumberArray = []
    return (averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, numberTillerCohort)
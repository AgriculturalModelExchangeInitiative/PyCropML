#'Test generation'

from VernalizationProgress import *
from math import *
import numpy 



def test_test_wheat1():
    params= VernalizationProgress(
    isVernalizable = 1,
    minTvern = 0.0,
    intTvern = 11.0,
    vAI = 0.015,
    vBEE = 0.01,
    minDL = 8.0,
    maxDL = 15.0,
    maxTvern = 23.0,
    pNini = 4.0,
    aMXLFNO = 24.0,
    cumulTT =  112.330110409888,
     )
    vernaprog_estimated = round(params[0], 2)
    vernaprog_computed = 0.64
    assert (vernaprog_estimated == vernaprog_computed)
    minFinalNumber_estimated = round(params[1], 2)
    minFinalNumber_computed = 5.5
    assert (minFinalNumber_estimated == minFinalNumber_computed)
    calendarMoments_estimated = params[2]
    calendarMoments_computed = ["Sowing"]
    assert np.all(calendarMoments_estimated == calendarMoments_computed)
    calendarDates_estimated = params[3]
    calendarDates_computed = ["2007/3/21"]
    assert np.all(calendarDates_estimated == calendarDates_computed)
    calendarCumuls_estimated = np.around(params[4], 2)
    calendarCumuls_computed = [0.0]
    assert np.all(calendarCumuls_estimated == calendarCumuls_computed)
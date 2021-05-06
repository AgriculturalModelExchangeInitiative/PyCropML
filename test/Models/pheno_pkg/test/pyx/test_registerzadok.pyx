#'Test generation'

from RegisterZadok import *
from math import *
import numpy 



def test_test_wheat1():
    params= RegisterZadok(
    slopeTSFLN = 0.9,
    intTSFLN = 2.6,
    der = 300.0,
    calendarMoments = ["Sowing","Emergence","EndVernalisation","MainShootPlus1Tiller"],
    calendarDates = ["2007/3/21","2007/3/27","2007/3/30","2007/4/5"],
    calendarCumuls = [ 0.0, 112.330110409888,157.969706915664, 280.570678654207],
    phase = 2,
     )
    hasZadokStageChanged_estimated = params[0]
    hasZadokStageChanged_computed = 0
    assert (hasZadokStageChanged_estimated == hasZadokStageChanged_computed)
    currentZadokStage_estimated = params[1]
    currentZadokStage_computed = "MainShootPlus1Tiller"
    assert (currentZadokStage_estimated == currentZadokStage_computed)
    calendarMoments_estimated = params[2]
    calendarMoments_computed = ["Sowing","Emergence","EndVernalisation","MainShootPlus1Tiller"]
    assert np.all(calendarMoments_estimated == calendarMoments_computed)
    calendarDates_estimated = params[3]
    calendarDates_computed = ["2007/3/21", "2007/3/27","2007/3/30","2007/4/5"]
    assert np.all(calendarDates_estimated == calendarDates_computed)
    calendarCumuls_estimated = np.around(params[4], 2)
    calendarCumuls_computed = [ 0.0, 112.33,157.97, 280.57]
    assert np.all(calendarCumuls_estimated == calendarCumuls_computed)
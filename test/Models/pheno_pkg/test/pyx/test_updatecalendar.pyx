#'Test generation'

from UpdateCalendar import *
from math import *
import numpy 



def test_test_wheat1():
    params= UpdateCalendar(
    cumulTT =  112.330110409888,
    calendarMoments = ["Sowing"],
    calendarDates = ["2007/3/21"],
    calendarCumuls = [0.0],
    phase = 1,
     )
    calendarMoments_estimated = params[0]
    calendarMoments_computed = ["Sowing", "Emergence"]
    assert np.all(calendarMoments_estimated == calendarMoments_computed)
    calendarDates_estimated = params[1]
    calendarDates_computed = ["2007/3/21", "2007/3/27"]
    assert np.all(calendarDates_estimated == calendarDates_computed)
    calendarCumuls_estimated = np.around(params[2], 2)
    calendarCumuls_computed = [ 0.0 ,112.33]
    assert np.all(calendarCumuls_estimated == calendarCumuls_computed)
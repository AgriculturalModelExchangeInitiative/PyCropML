#'Test generation'

from UpdateLeafFlag import *
from math import *
import numpy 



def test_test_wheat1():
    params= UpdateLeafFlag(
    hasFlagLeafLiguleAppeared_t1 = 0,
    phase = 3,
    calendarMoments = ["Sowing", "Emergence", "EndVernalisation", "MainShootPlus1Tiller", "FloralInitiation", "MainShootPlus2Tiller", "TerminalSpikelet", "PseudoStemErection", "MainShootPlus3Tiller", "1stNodeDetectable", "2ndNodeDetectable", "FlagLeafJustVisible"],
    calendarDates = ["2007/3/21", "2007/3/27", "2007/3/30", "2007/4/5", "2007/4/9", "2007/4/10", "2007/4/11", "2007/4/12", "2007/4/14", "2007/4/15", "2007/4/19", "2007/4/24"],
    calendarCumuls = [0.0, 112.330110409888, 157.969706915664, 280.570678654207, 354.582294511779, 378.453152853726, 402.042720581446, 424.98704708663, 467.23305195298, 487.544313430698, 560.665248444002, 646.389617338974],
     )
    hasFlagLeafLiguleAppeared_estimated = params[0]
    hasFlagLeafLiguleAppeared_computed = 1
    assert (hasFlagLeafLiguleAppeared_estimated == hasFlagLeafLiguleAppeared_computed)
    calendarMoments_estimated = params[1]
    calendarMoments_computed = ["Sowing", "Emergence", "EndVernalisation", "MainShootPlus1Tiller", "FloralInitiation", "MainShootPlus2Tiller", "TerminalSpikelet", "PseudoStemErection", "MainShootPlus3Tiller", "1stNodeDetectable", "2ndNodeDetectable", "FlagLeafJustVisible", "FlagLeafLiguleJustVisible"]
    assert np.all(calendarMoments_estimated == calendarMoments_computed)
    calendarDates_estimated = params[2]
    calendarDates_computed = ["2007/3/21", "2007/3/27", "2007/3/30", "2007/4/5", "2007/4/9", "2007/4/10", "2007/4/11", "2007/4/12", "2007/4/14", "2007/4/15", "2007/4/19", "2007/4/24","2007/4/29"]
    assert np.all(calendarDates_estimated == calendarDates_computed)
    calendarCumuls_estimated = np.around(params[3], 2)
    calendarCumuls_computed = [0.0, 112.33, 157.97, 280.57, 354.58, 378.45, 402.04, 424.99, 467.23, 487.54, 560.67, 646.39, 741.51]
    assert np.all(calendarCumuls_estimated == calendarCumuls_computed)
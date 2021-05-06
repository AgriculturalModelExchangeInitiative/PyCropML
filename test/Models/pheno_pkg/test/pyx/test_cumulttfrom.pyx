#'Test generation'

from CumulTTFrom import *
from math import *
import numpy 



def test_test_wheat1():
    params= CumulTTFrom(
    calendarMoments_t1 = ["Sowing", "Emergence", "FloralInitiation", "FlagLeafLiguleJustVisible", "Heading", "Anthesis"],
    calendarCumuls_t1 = [0.0, 112.330110409888, 354.582294511779, 741.510096671757, 853.999637026622, 954.59002776961],
    cumulTT = 972.970888983105,
     )
    cumulTTFromZC_65_estimated = round(params[0], 2)
    cumulTTFromZC_65_computed = 18.38
    assert (cumulTTFromZC_65_estimated == cumulTTFromZC_65_computed)
    cumulTTFromZC_39_estimated = round(params[1], 2)
    cumulTTFromZC_39_computed = 231.46
    assert (cumulTTFromZC_39_estimated == cumulTTFromZC_39_computed)
    cumulTTFromZC_91_estimated = round(params[2], 2)
    cumulTTFromZC_91_computed = 0
    assert (cumulTTFromZC_91_estimated == cumulTTFromZC_91_computed)
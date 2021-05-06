#'Test generation'

from IsMomentRegistredZC_39 import *
from math import *
import numpy 



def test_test_wheat1():
    params= IsMomentRegistredZC_39(
    calendarMoments_t1 = ["Sowing", "Emergence", "FloralInitiation", "FlagLeafLiguleJustVisible", "Heading", "Anthesis"],
     )
    isMomentRegistredZC_39_estimated = params
    isMomentRegistredZC_39_computed = 1
    assert (isMomentRegistredZC_39_estimated == isMomentRegistredZC_39_computed)
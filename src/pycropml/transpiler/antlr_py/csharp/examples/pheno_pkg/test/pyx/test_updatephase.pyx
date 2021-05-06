#'Test generation'

from UpdatePhase import *
from math import *
import numpy 



def test_test_wheat1():
    params= UpdatePhase(
    choosePhyllUse = "Default",
    isVernalizable = 1,
    dse = 105.0,
    dcd = 100.0,
    degfm = 0.0,
    maxDL = 15.0,
    sLDL = 0.85,
    ignoreGrainMaturation = TRUE,
    pHEADANTH = 1.0,
    p = 120,
    phase_t1 = 1,
    hasLastPrimordiumAppeared_t1 = 0,
     )
    finalLeafNumber_estimated = round(params[0], 2)
    finalLeafNumber_computed = 8.80
    assert (finalLeafNumber_estimated == finalLeafNumber_computed)
    phase_estimated = round(params[1], 1)
    phase_computed = 2
    assert (phase_estimated == phase_computed)
    hasLastPrimordiumAppeared_estimated = params[2]
    hasLastPrimordiumAppeared_computed = 1
    assert (hasLastPrimordiumAppeared_estimated == hasLastPrimordiumAppeared_computed)
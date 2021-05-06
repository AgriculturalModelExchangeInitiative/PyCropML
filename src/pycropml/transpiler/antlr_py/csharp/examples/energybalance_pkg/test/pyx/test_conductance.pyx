#'Test generation'

from conductance import *
from math import *
import numpy 



def test_test1():
    params= conductance(
    d = 0.67,
    zh = 0.013,
    zm = 0.13,
    wind = 124000,
    plantHeight = 0,
     )
    conductance_estimated = round(params, 3)
    conductance_computed = 598.685
    assert (conductance_estimated == conductance_computed)
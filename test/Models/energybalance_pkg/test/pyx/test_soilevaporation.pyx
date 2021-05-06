#'Test generation'

from soilevaporation import *
from math import *
import numpy 



def test_test1():
    params= soilevaporation(
    diffusionLimitedEvaporation = 6605.505,
    energyLimitedEvaporation = 448.240,
     )
    soilEvaporation_estimated = round(params, 3)
    soilEvaporation_computed = 448.240
    assert (soilEvaporation_estimated == soilEvaporation_computed)
#'Test generation'

from diffusionlimitedevaporation import *
from math import *
import numpy 



def test_test1():
    params= diffusionlimitedevaporation(
    soilDiffusionConstant = 4.2,
    deficitOnTopLayers = 5341,
     )
    diffusionLimitedEvaporation_estimated = round(params, 3)
    diffusionLimitedEvaporation_computed = 6605.505
    assert (diffusionLimitedEvaporation_estimated == diffusionLimitedEvaporation_computed)
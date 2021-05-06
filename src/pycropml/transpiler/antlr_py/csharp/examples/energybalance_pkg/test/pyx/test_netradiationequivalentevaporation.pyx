#'Test generation'

from netradiationequivalentevaporation import *
from math import *
import numpy 



def test_test1():
    params= netradiationequivalentevaporation(
    netRadiation = 1.566,
     )
    netRadiationEquivalentEvaporation_estimated = round(params, 3)
    netRadiationEquivalentEvaporation_computed = 638.142
    assert (netRadiationEquivalentEvaporation_estimated == netRadiationEquivalentEvaporation_computed)
#'Test generation'

from netradiation import *
from math import *
import numpy 



def test_test1():
    params= netradiation(
    elevation = 0,
    solarRadiation = 3,
    vaporPressure = 6.1,
     )
    netRadiation_estimated = round(params[0], 3)
    netRadiation_computed = 1.566
    assert (netRadiation_estimated == netRadiation_computed)
    netOutGoingLongWaveRadiation_estimated = round(params[1], 3)
    netOutGoingLongWaveRadiation_computed = 0.744
    assert (netOutGoingLongWaveRadiation_estimated == netOutGoingLongWaveRadiation_computed)
#'Test generation'

from soilheatflux import *
from math import *
import numpy 



def test_test1():
    params= soilheatflux(
    tau = 0.9983,
    netRadiationEquivalentEvaporation = 638.142,
    soilEvaporation = 448.240,
     )
    soilHeatFlux_estimated = round(params, 3)
    soilHeatFlux_computed = 188.817
    assert (soilHeatFlux_estimated == soilHeatFlux_computed)
#'Test generation'

from canopytemperature import *
from math import *
import numpy 



def test_test1():
    params= canopytemperature(
    rhoDensityAir = 1.225,
    minTair = 0.7,
    maxTair = 7.2,
     )
    minCanopyTemperature_estimated = round(params[0], 3)
    minCanopyTemperature_computed = 2.184
    assert (minCanopyTemperature_estimated == minCanopyTemperature_computed)
    maxCanopyTemperature_estimated = round(params[1], 3)
    maxCanopyTemperature_computed = 8.684
    assert (maxCanopyTemperature_estimated == maxCanopyTemperature_computed)
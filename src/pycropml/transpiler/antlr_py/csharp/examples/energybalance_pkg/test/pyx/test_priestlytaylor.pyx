#'Test generation'

from priestlytaylor import *
from math import *
import numpy 



def test_test1():
    params= priestlytaylor(
    Alpha = 1.5,
    netRadiationEquivalentEvaporation = 638.142,
     )
    evapoTranspirationPriestlyTaylor_estimated = round(params, 3)
    evapoTranspirationPriestlyTaylor_computed = 449.367
    assert (evapoTranspirationPriestlyTaylor_estimated == evapoTranspirationPriestlyTaylor_computed)
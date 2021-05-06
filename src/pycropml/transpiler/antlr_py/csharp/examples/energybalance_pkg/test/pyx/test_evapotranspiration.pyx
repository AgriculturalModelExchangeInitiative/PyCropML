#'Test generation'

from evapotranspiration import *
from math import *
import numpy 



def test_test1():
    params= evapotranspiration(
    isWindVpDefined = 1,
    evapoTranspirationPriestlyTaylor = 449.367,
    evapoTranspirationPenman = 830.957,
     )
    evapoTranspiration_estimated = round(params, 3)
    evapoTranspiration_computed = 830.957
    assert (evapoTranspiration_estimated == evapoTranspiration_computed)
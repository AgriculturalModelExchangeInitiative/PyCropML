#'Test generation'

from penman import *
from math import *
import numpy 



def test_test1():
    params= penman(
    Alpha = 1.5,
    lambdaV = 2.454,
    evapoTranspirationPriestlyTaylor = 449.367,
    hslope = 0.584,
    VPDair = 2.19,
     )
    evapoTranspirationPenman_estimated = round(params, 3)
    evapoTranspirationPenman_computed = 830.958
    assert (evapoTranspirationPenman_estimated == evapoTranspirationPenman_computed)
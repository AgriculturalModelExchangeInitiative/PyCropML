#'Test generation'

from PhylSowingDateCorrection import *
from math import *
import numpy 



def test_test_wheat1():
    params= PhylSowingDateCorrection(
    sowingDay = 80,
    latitude = 33.069,
    sDsa_sh = 151,
    rp = 0.003,
    sDws = 90,
    sDsa_nh = 200,
    p = 120,
     )
    fixPhyll_estimated = round(params, 2)
    fixPhyll_computed = 91.2
    assert (fixPhyll_estimated == fixPhyll_computed)
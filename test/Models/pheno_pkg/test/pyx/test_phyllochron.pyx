#'Test generation'

from Phyllochron import *
from math import *
import numpy 



def test_test_wheat1():
    params= Phyllochron(
    lincr = 8.0,
    ldecr = 3.0,
    pdecr = 0.4,
    pincr = 1.25,
    ptq = 0.97,
    kl = 0.45,
    p = 120.0,
    choosePhyllUse = "Default",
    fixPhyll = 91.2,
     )
    phyllochron_estimated = round(params, 2)
    phyllochron_computed = 36.48
    assert (phyllochron_estimated == phyllochron_computed)
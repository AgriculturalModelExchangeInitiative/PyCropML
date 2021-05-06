#'Test generation'

from LeafNumber import *
from math import *
import numpy 



def test_test_wheat1():
    params= LeafNumber(
    leafNumber_t1 = 5.147163833893262,
    phase = 3,
    phyllochron_t1 = 91.2,
     )
    leafNumber_estimated = round(params, 2)
    leafNumber_computed = 5.41
    assert (leafNumber_estimated == leafNumber_computed)
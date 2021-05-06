#'Test generation'

from PTQ import *
from math import *
import numpy 



def test_test_wheat1():
    params= PTQ(
    tTWindowForPTQ = 70.0,
    kl = 0.45,
    listTTShootWindowForPTQ_t1 = [0.0],
    listPARTTWindowForPTQ_t1 = [0.0],
    listGAITTWindowForPTQ = [0.0, 5.2],
    pAR = 0.0,
    deltaTT = 21.3,
     )
    listPARTTWindowForPTQ_estimated = np.around(params[0], 2)
    listPARTTWindowForPTQ_computed = [0.00, 0.0]
    assert np.all(listPARTTWindowForPTQ_estimated == listPARTTWindowForPTQ_computed)
    listTTShootWindowForPTQ_estimated = np.around(params[1], 2)
    listTTShootWindowForPTQ_computed = [0.0, 21.3]
    assert np.all(listTTShootWindowForPTQ_estimated == listTTShootWindowForPTQ_computed)
    ptq_estimated = round(params[2], 2)
    ptq_computed = 0.0
    assert (ptq_estimated == ptq_computed)
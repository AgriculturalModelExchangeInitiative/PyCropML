#'Test generation'

from GAImean import *
from math import *
import numpy 



def test_test_wheat1():
    params= GAImean(
    tTWindowForPTQ = 70.0,
    gAI = 91.2,
    deltaTT = 0.279,
    pastMaxAI_t1 = 0.279,
    listTTShootWindowForPTQ1_t1 = [0.0],
    listGAITTWindowForPTQ_t1 = [0.0],
     )
    gAImean_estimated = round(params[0], 2)
    gAImean_computed = 45.6
    assert (gAImean_estimated == gAImean_computed)
    pastMaxAI_estimated = round(params[1], 2)
    pastMaxAI_computed = 45.6
    assert (pastMaxAI_estimated == pastMaxAI_computed)
    listTTShootWindowForPTQ1_estimated = np.around(params[2], 2)
    listTTShootWindowForPTQ1_computed = [0.0, 0.28]
    assert np.all(listTTShootWindowForPTQ1_estimated == listTTShootWindowForPTQ1_computed)
    listGAITTWindowForPTQ_estimated = np.around(params[3], 2)
    listGAITTWindowForPTQ_computed = [0.0, 91.2]
    assert np.all(listGAITTWindowForPTQ_estimated == listGAITTWindowForPTQ_computed)
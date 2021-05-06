#'Test generation'

from potentialtranspiration import *
from math import *
import numpy 



def test_test1():
    params= potentialtranspiration(
    tau = 0.9983,
    evapoTranspiration = 830.958,
     )
    potentialTranspiration_estimated = round(params, 3)
    potentialTranspiration_computed = 1.413
    assert (potentialTranspiration_estimated == potentialTranspiration_computed)
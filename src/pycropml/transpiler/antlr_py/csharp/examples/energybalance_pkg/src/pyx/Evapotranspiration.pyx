import numpy 
from math import *
def model_evapotranspiration(int isWindVpDefined=1,
                             float evapoTranspirationPriestlyTaylor=449.367,
                             float evapoTranspirationPenman=830.958):
    """

    Evapotranspiration Model
    Author: Pierre Martre
    Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
            Evapotranspiration and canopy and soil temperature calculations
    Institution: INRA Montpellier
    Abstract: According to the availability of wind and/or vapor pressure daily data, the
            SiriusQuality2 model calculates the evapotranspiration rate using the Penman (if wind
            and vapor pressure data are available) (Penman 1948) or the Priestly-Taylor
            (Priestley and Taylor 1972) method 

    """
    cdef float evapoTranspiration
    if (isWindVpDefined == 1):
        evapoTranspiration = evapoTranspirationPenman
    else:
        evapoTranspiration = evapoTranspirationPriestlyTaylor
    return  evapoTranspiration

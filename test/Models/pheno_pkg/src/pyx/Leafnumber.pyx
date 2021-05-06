import numpy 
from math import *
def model_leafnumber(float deltaTT=23.5895677277199,
                     float phyllochron_t1=0.0,
                     int hasFlagLeafLiguleAppeared=0,
                     float leafNumber_t1=0.0,
                     float phase=1.0):
    """

    CalculateLeafNumber Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day

    """
    cdef float leafNumber
    leafNumber = leafNumber_t1
    cdef float phyllochron_
    if (phase >= 1.0 and phase< 4.0):
        if (hasFlagLeafLiguleAppeared==0):
            if (phyllochron_t1 == 0.0):
                phyllochron_ = 0.0000001
            else: phyllochron_ = phyllochron_t1
            leafNumber = leafNumber_t1 + min(deltaTT / phyllochron_, 0.999)
    return  leafNumber

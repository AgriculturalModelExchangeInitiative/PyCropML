import numpy 
from math import *
def model_IsMomentRegistredZC_39(list calendarMoments_t1=['Sowing']):
    """

    Is FlagLeafLiguleJustVisible Model
    Author: Pierre Martre
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: if FlagLeafLiguleJustVisible is already Registred 

    """
    cdef int isMomentRegistredZC_39
    isMomentRegistredZC_39 = 1 if "FlagLeafLiguleJustVisible" in calendarMoments_t1 else 0
    return  isMomentRegistredZC_39

import numpy 
from math import *
def model_cumulttfrom(list calendarMoments_t1=['Sowing'],
                      list calendarCumuls_t1=[0.0],
                      float cumulTT=8.0):
    """

    CumulTTFrom Model
    Author: Pierre Martre
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: Calculate CumulTT 

    """
    cdef float cumulTTFromZC_65
    cdef float cumulTTFromZC_39
    cdef float cumulTTFromZC_91
    # initialisation 
    cumulTTFromZC_65 = 0.0
    cumulTTFromZC_39 = 0.0
    cumulTTFromZC_91 = 0.0     
    if "Anthesis" in calendarMoments_t1:
        cumulTTFromZC_65 = cumulTT-calendarCumuls_t1[calendarMoments_t1.index("Anthesis")]    
    if "FlagLeafLiguleJustVisible" in calendarMoments_t1:
        cumulTTFromZC_39 = cumulTT-calendarCumuls_t1[calendarMoments_t1.index("FlagLeafLiguleJustVisible")]  
    if "EndGrainFilling"in calendarMoments_t1:
        cumulTTFromZC_91 = cumulTT-calendarCumuls_t1[calendarMoments_t1.index("EndGrainFilling")]
    return  cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91

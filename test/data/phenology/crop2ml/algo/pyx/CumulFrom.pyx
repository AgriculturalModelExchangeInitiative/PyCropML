   
cumulTTFromZC_65 = 0.0
cumulTTFromZC_39 = 0.0
cumulTTFromZC_91 = 0.0     
if "Anthesis" in calendarMoments:
    cumulTTFromZC_65 = cumulTT-calendarCumuls[calendarMoments.index("Anthesis")]    
if "FlagLeafLiguleJustVisible" in calendarMoments:
    cumulTTFromZC_39 = cumulTT-calendarCumuls[calendarMoments.index("FlagLeafLiguleJustVisible")]  
if "EndGrainFilling"in calendarMoments:
    cumulTTFromZC_91 = cumulTT-calendarCumuls[calendarMoments.index("EndGrainFilling")]

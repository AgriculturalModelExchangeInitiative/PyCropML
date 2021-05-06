cumulTTFromZC_65 = 0
cumulTTFromZC_39 = 0
cumulTTFromZC_91 = 0     
if (any(calendarMoments=="Anthesis"))
    if (switchMaize == 0) cumulTTFromZC_65 = cumulTT-calendarCumuls[which(calendarMoments=="Anthesis")]  
if (any(calendarMoments=="FlagLeafLiguleJustVisible"))
    if (switchMaize == 0) cumulTTFromZC_39 = cumulTT-calendarCumuls[which(calendarMoments=="FlagLeafLiguleJustVisible")]
if (any(calendarMoments=="EndGrainFilling"))
    if (switchMaize == 0) cumulTTFromZC_91 = cumulTT-calendarCumuls[which(calendarMoments=="EndGrainFilling")]

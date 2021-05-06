
cumulTTFromZC_65 = 0.0D;
cumulTTFromZC_39 = 0.0D;
cumulTTFromZC_91 = 0.0D;  
if (calendarMoments.Contains("Anthesis")){
    cumulTTFromZC_65 = cumulTT-calendarCumuls[calendarMoments.IndexOf("Anthesis")];
}    
if (calendarMoments.Contains("FlagLeafLiguleJustVisible")){
    cumulTTFromZC_39 = cumulTT-calendarCumuls[calendarMoments.IndexOf("FlagLeafLiguleJustVisible")];
}   
if (calendarMoments.Contains("EndGrainFilling")){
    cumulTTFromZC_91 = cumulTT-calendarCumuls[calendarMoments.IndexOf("EndGrainFilling")];
}

cumulTTFromZC_65 = 0;
cumulTTFromZC_39 = 0;
cumulTTFromZC_91 =0;

size_t posAnthesis = find(calendarMoments.begin(), calendarMoments.end(), "Anthesis")- calendarMoments.begin() ;

if(posAnthesis<calendarMoments.size()){
    cumulTTFromZC_65 = cumulTT - calendarCumuls[posAnthesis];
}
size_t posFlag = find(calendarMoments.begin(), calendarMoments.end(), "FlagLeafLiguleJustVisible")-calendarMoments.begin();

if(posFlag<calendarMoments.size()){
    cumulTTFromZC_39 = cumulTT - calendarCumuls[posFlag];
}
size_t posFill= find(calendarMoments.begin(), calendarMoments.end(), "EndGrainFilling")-calendarMoments.begin();

if(posFill<calendarMoments.size()){
    cumulTTFromZC_91 = cumulTT- calendarCumuls[posFill];
}




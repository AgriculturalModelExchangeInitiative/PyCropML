
int roundedFinalLeafNumber = (int)(finalLeafNumber+0.5);
if (leafNumber>=4.0 && calendarMoments.Contains("MainShootPlus1Tiller")==false)
{
    calendarMoments.Add("MainShootPlus1Tiller");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "MainShootPlus1Tiller";
}
else if (leafNumber>=5.0 && calendarMoments.Contains("MainShootPlus2Tiller")==false)
{
    calendarMoments.Add("MainShootPlus2Tiller");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "MainShootPlus2Tiller";
}
else if (leafNumber>=6.0 && calendarMoments.Contains("MainShootPlus3Tiller")==false)
{
    calendarMoments.Add("MainShootPlus3Tiller");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "MainShootPlus3Tiller";
}        
else if (finalLeafNumber > 0.0 && leafNumber>=(slopeTSFLN * finalLeafNumber - intTSFLN) &&  calendarMoments.Contains("TerminalSpikelet")==false)
{
    calendarMoments.Add("TerminalSpikelet");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "TerminalSpikelet";
}        
        
else if ((leafNumber >= (roundedFinalLeafNumber-4) && (roundedFinalLeafNumber-4) > 0) && calendarMoments.Contains("PseudoStemErection")==false)
{
    calendarMoments.Add("PseudoStemErection");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "PseudoStemErection";
}
else if ((leafNumber >= (roundedFinalLeafNumber-3) && (roundedFinalLeafNumber-3) > 0) && calendarMoments.Contains("1stNodeDetectable")==false)
{
    calendarMoments.Add("1stNodeDetectable");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "1stNodeDetectable";
}

else if ((leafNumber >= (roundedFinalLeafNumber-2) && (roundedFinalLeafNumber-2) > 0) &&  calendarMoments.Contains("2ndNodeDetectable")==false)
{
    calendarMoments.Add("2ndNodeDetectable");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "2ndNodeDetectable";
}    
else if ((leafNumber >= (roundedFinalLeafNumber-1) && (roundedFinalLeafNumber-1) > 0) && calendarMoments.Contains("FlagLeafJustVisible")==false)
{
    calendarMoments.Add("FlagLeafJustVisible");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "FlagLeafJustVisible";
}
     
else if ((calendarMoments.Contains("MidGrainFilling")==false) && phase == 4.5 && cumulTTFromZC_65 >= der)
{
    calendarMoments.Add("MidGrainFilling");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "MidGrainFilling" ;                
}
else
    hasZadokStageChanged = 0;



int roundedFinalLeafNumber = (int)(finalLeafNumber + 0.5);
size_t pos = find(calendarMoments.begin(), calendarMoments.end(), "MainShootPlus1Tiller") - calendarMoments.begin();
if (leafNumber >= 4 && pos >= calendarMoments.size())
{
    calendarMoments.push_back("MainShootPlus1Tiller");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "MainShootPlus1Tiller";
}
else if (leafNumber >= 5 && (size_t(find(calendarMoments.begin(), calendarMoments.end(), "MainShootPlus2Tiller") - calendarMoments.begin())) >= calendarMoments.size())
{
    calendarMoments.push_back("MainShootPlus2Tiller");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "MainShootPlus2Tiller";
}
else if (leafNumber >= 6 && (size_t(find(calendarMoments.begin(), calendarMoments.end(), "MainShootPlus3Tiller") - calendarMoments.begin())) >= calendarMoments.size())
{
    calendarMoments.push_back("MainShootPlus3Tiller");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "MainShootPlus3Tiller";
}
else if (finalLeafNumber > 0 && leafNumber >= (slopeTSFLN * finalLeafNumber - intTSFLN) && (size_t(find(calendarMoments.begin(), calendarMoments.end(), "TerminalSpikelet") - calendarMoments.begin())) >= calendarMoments.size())
{
    calendarMoments.push_back("TerminalSpikelet");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "TerminalSpikelet";
}
else if ((leafNumber >= (roundedFinalLeafNumber - 4) && (roundedFinalLeafNumber - 4) > 0) && (size_t(find(calendarMoments.begin(), calendarMoments.end(), "PseudoStemErection") - calendarMoments.begin())) >= calendarMoments.size())
{
    calendarMoments.push_back("PseudoStemErection");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "PseudoStemErection";
}
else if ((leafNumber >= (roundedFinalLeafNumber - 3) && (roundedFinalLeafNumber - 3) > 0) && (size_t(find(calendarMoments.begin(), calendarMoments.end(), "1stNodeDetectable") - calendarMoments.begin())) >= calendarMoments.size())
{
    calendarMoments.push_back("1stNodeDetectable");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "1stNodeDetectable";
}
else if ((leafNumber >= (roundedFinalLeafNumber - 2) && (roundedFinalLeafNumber - 2) > 0) && (size_t(find(calendarMoments.begin(), calendarMoments.end(), "2ndNodeDetectable") - calendarMoments.begin())) >= calendarMoments.size())
{
    calendarMoments.push_back("2ndNodeDetectable");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "2ndNodeDetectable";
}
else if ((leafNumber >= (roundedFinalLeafNumber - 1) && (roundedFinalLeafNumber - 1) > 0) && (size_t(find(calendarMoments.begin(), calendarMoments.end(), "FlagLeafJustVisible") - calendarMoments.begin())) >= calendarMoments.size())
{
    calendarMoments.push_back("FlagLeafJustVisible");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "FlagLeafJustVisible";
}
else if ((size_t(find(calendarMoments.begin(), calendarMoments.end(), "MidGrainFilling") - calendarMoments.begin())) >= calendarMoments.size() && phase == 4.5 && cumulTTFromZC_65 >= der)
{
    calendarMoments.push_back("MidGrainFilling");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "MidGrainFilling";
}
else
    hasZadokStageChanged = 0;

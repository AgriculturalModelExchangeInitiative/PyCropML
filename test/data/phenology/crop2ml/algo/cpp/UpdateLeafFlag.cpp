
if (phase >= 1 && phase < 4)
{
    if (leafNumber > 0)
    {
        if (hasFlagLeafLiguleAppeared == 0 && (finalLeafNumber > 0 && leafNumber >= finalLeafNumber))
        {
            hasFlagLeafLiguleAppeared = 1;
            size_t pos = find(calendarMoments.begin(), calendarMoments.end(), "FlagLeafLiguleJustVisible") - calendarMoments.begin();

            if (pos >= calendarMoments.size())
            {
                calendarMoments.push_back("FlagLeafLiguleJustVisible");
                calendarCumuls.push_back(cumulTT);
                calendarDates.push_back(currentdate);
            }
        }
    }
    else
        hasFlagLeafLiguleAppeared = 0;
}

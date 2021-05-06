if (phase >= 1.0 && phase< 4.0)
{
    if (leafNumber > 0.0)
    {
        if (hasFlagLeafLiguleAppeared == 0 && (finalLeafNumber > 0.0 && leafNumber >= finalLeafNumber))
        {
            hasFlagLeafLiguleAppeared = 1;
            if  (calendarMoments.Contains("FlagLeafLiguleJustVisible")==false)
            {
                calendarMoments.Add("FlagLeafLiguleJustVisible");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
            }
        }
    }
    else
        hasFlagLeafLiguleAppeared = 0;
}


    

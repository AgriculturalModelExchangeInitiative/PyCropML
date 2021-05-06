
if (phase >= 1.0 and phase< 4.0):
    if (leafNumber > 0.0):
        if (hasFlagLeafLiguleAppeared == 0 and (finalLeafNumber > 0.0 and leafNumber >= finalLeafNumber)):
            hasFlagLeafLiguleAppeared = 1
            if  "FlagLeafLiguleJustVisible" not in calendarMoments:
                calendarMoments.append("FlagLeafLiguleJustVisible")
                calendarCumuls.append(cumulTT)
                calendarDates.append(currentdate)
    else:
        hasFlagLeafLiguleAppeared = 0


    

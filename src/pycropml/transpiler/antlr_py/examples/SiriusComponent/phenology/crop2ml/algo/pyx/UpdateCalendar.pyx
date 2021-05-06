if phase >= 1.0 and phase < 2.0 and "Emergence" not in calendarMoments:
    calendarMoments.append("Emergence")
    calendarCumuls.append(cumulTT)
    calendarDates.append(currentdate)
elif phase >= 2.0 and phase < 3.0 and "FloralInitiation" not in calendarMoments:
    calendarMoments.append("FloralInitiation")
    calendarCumuls.append(cumulTT)
    calendarDates.append(currentdate)
elif phase >= 3.0 and phase < 4.0 and "Heading" not in calendarMoments:
    calendarMoments.append("Heading")
    calendarCumuls.append(cumulTT)
    calendarDates.append(currentdate)
elif phase == 4.0 and "Anthesis" not in calendarMoments:
    calendarMoments.append("Anthesis")
    calendarCumuls.append(cumulTT)
    calendarDates.append(currentdate)
elif phase == 4.5 and "EndCellDivision" not in calendarMoments:
    calendarMoments.append("EndCellDivision")
    calendarCumuls.append(cumulTT)
    calendarDates.append(currentdate)
elif phase >= 5.0 and phase < 6.0 and "EndGrainFilling" not in calendarMoments:
    calendarMoments.append("EndGrainFilling")
    calendarCumuls.append(cumulTT)
    calendarDates.append(currentdate)
elif phase >= 6.0 and phase < 7.0 and "Maturity" not in calendarMoments:
    calendarMoments.append("Maturity")
    calendarCumuls.append(cumulTT)
    calendarDates.append(currentdate)
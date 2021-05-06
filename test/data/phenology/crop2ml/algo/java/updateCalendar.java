
if ((phase >= 1 && phase < 2) && (calendarMoments.contains("Emergence")==false ))
{
    calendarMoments.add("Emergence");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
}
else if ((phase >= 2 && phase < 3)  && ( calendarMoments.contains("FloralInitiation")==false  ))
{
    calendarMoments.add("FloralInitiation") ;
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
}
else if ((phase >= 3 && phase < 4)  && (calendarMoments.contains("Heading")==false  ))
{
    calendarMoments.add("Heading");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
}
else if ((phase == 4)  && (calendarMoments.contains("Anthesis" )==false  ))
{
    calendarMoments.add("Anthesis");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
}
else if ((phase == 4.5)  && (calendarMoments.contains("EndCellDivision" )==false  ))
{
    calendarMoments.add("EndCellDivision");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
}
else if ((phase >= 5 && phase < 6) && ( calendarMoments.contains("EndGrainFilling")==false  ))
{
    calendarMoments.add("EndGrainFilling");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
}
else if ((phase >= 6 && phase < 7)  && (calendarMoments.contains("Maturity" )==false ))
{
    calendarMoments.add("Maturity");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
}





if ((phase >= 1.0 && phase < 2.0) && (calendarMoments.Contains("Emergence")==false ))
{
    calendarMoments.Add("Emergence");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
}
else if ((phase >= 2.0 && phase < 3.0)  && ( calendarMoments.Contains("FloralInitiation")==false  ))
{
    calendarMoments.Add("FloralInitiation") ;
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
}
else if ((phase >= 3.0 && phase < 4.0)  && (calendarMoments.Contains("Heading")==false  ))
{
    calendarMoments.Add("Heading");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
}
else if ((phase == 4.0)  && (calendarMoments.Contains("Anthesis" )==false  ))
{
    calendarMoments.Add("Anthesis");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
}
else if ((phase == 4.5)  && (calendarMoments.Contains("EndCellDivision" )==false  ))
{
    calendarMoments.Add("EndCellDivision");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
}
else if ((phase >= 5.0 && phase < 6.0) && ( calendarMoments.Contains("EndGrainFilling")==false  ))
{
    calendarMoments.Add("EndGrainFilling");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
}
else if ((phase >= 6.0 && phase < 7.0)  && (calendarMoments.Contains("Maturity" )==false ))
{
    calendarMoments.Add("Maturity");
    calendarCumuls.Add(cumulTT);
    calendarDates.Add(currentdate);
}




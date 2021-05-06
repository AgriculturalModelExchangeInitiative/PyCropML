
size_t pos = find(calendarMoments.begin(), calendarMoments.end(),"Emergence" ) - calendarMoments.begin();
if ((phase >= 1 && phase < 2) && (pos>=calendarMoments.size()))
{
    calendarMoments.push_back("Emergence");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
}
else if ((phase >= 2 && phase < 3)  && (size_t(find(calendarMoments.begin(), calendarMoments.end(),"FloralInitiation" ) - calendarMoments.begin()))>=calendarMoments.size())
{
    calendarMoments.push_back("FloralInitiation") ;
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
}
else if ((phase >= 3 && phase < 4)  && (size_t(find(calendarMoments.begin(), calendarMoments.end(),"Heading" ) - calendarMoments.begin()))>=calendarMoments.size())
{
    calendarMoments.push_back("Heading");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
}
else if ((phase == 4)  && (size_t(find(calendarMoments.begin(), calendarMoments.end(),"Anthesis" ) - calendarMoments.begin()))>=calendarMoments.size())
{
    calendarMoments.push_back("Anthesis");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
}
else if ((phase == 4.5)  &&(size_t(find(calendarMoments.begin(), calendarMoments.end(),"EndCellDivision" ) - calendarMoments.begin()))>=calendarMoments.size())
{
    calendarMoments.push_back("EndCellDivision");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
}
else if ((phase >= 5 && phase < 6) && (size_t(find(calendarMoments.begin(), calendarMoments.end(),"EndGrainFilling" ) - calendarMoments.begin()))>=calendarMoments.size())
{
    calendarMoments.push_back("EndGrainFilling");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
}
else if ((phase >= 6 && phase < 7)  && (size_t(find(calendarMoments.begin(), calendarMoments.end(),"Maturity" ) - calendarMoments.begin()))>=calendarMoments.size())
{
    calendarMoments.push_back("Maturity");
    calendarCumuls.push_back(cumulTT);
    calendarDates.push_back(currentdate);
}





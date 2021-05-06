import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import javafx.util.*;
import java.time.LocalDateTime;
public class Updatecalendar
{
    
    public Updatecalendar() { }
    public void  Calculate_updatecalendar(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: UpdateCalendar -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: Calendar Model
    //            * Author: Pierre Martre
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Lists containing for each stage the date it occurs as well as a copy of all types of cumulated thermal times 
        //- inputs:
    //            * name: cumulTT
    //                          ** description : cumul thermal times at current date
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 741.510096671757
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: calendarMoments
    //                          ** description : List containing apparition of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** default : ['Sowing']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarDates
    //                          ** description : List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** default : ['2007/3/21']
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: calendarCumuls
    //                          ** description : list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: currentdate
    //                          ** description : current date
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DATE
    //                          ** default : 2007/3/27
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: phase
    //                          ** description :  the name of the phase
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : variable
        //- outputs:
    //            * name: calendarMoments
    //                          ** description :  List containing apparition of each stage
    //                          ** variablecategory : state
    //                          ** datatype : STRINGLIST
    //                          ** unit : 
    //            * name: calendarDates
    //                          ** description :  List containing  the dates of the wheat developmental phases
    //                          ** variablecategory : state
    //                          ** datatype : DATELIST
    //                          ** unit : 
    //            * name: calendarCumuls
    //                          ** description :  list containing for each stage occured its cumulated thermal times
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** unit : °C d
        double cumulTT = a.getcumulTT();
        List<String> calendarMoments = s.getcalendarMoments();
        List<LocalDateTime> calendarDates = s.getcalendarDates();
        List<Double> calendarCumuls = s.getcalendarCumuls();
        LocalDateTime currentdate = a.getcurrentdate();
        double phase = s.getphase();
        if (phase >= 1.0d && phase < 2.0d && !calendarMoments.contains("Emergence"))
        {
            calendarMoments.add("Emergence");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
        }
        else if ( phase >= 2.0d && phase < 3.0d && !calendarMoments.contains("FloralInitiation"))
        {
            calendarMoments.add("FloralInitiation");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
        }
        else if ( phase >= 3.0d && phase < 4.0d && !calendarMoments.contains("Heading"))
        {
            calendarMoments.add("Heading");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
        }
        else if ( phase == 4.0d && !calendarMoments.contains("Anthesis"))
        {
            calendarMoments.add("Anthesis");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
        }
        else if ( phase == 4.5d && !calendarMoments.contains("EndCellDivision"))
        {
            calendarMoments.add("EndCellDivision");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
        }
        else if ( phase >= 5.0d && phase < 6.0d && !calendarMoments.contains("EndGrainFilling"))
        {
            calendarMoments.add("EndGrainFilling");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
        }
        else if ( phase >= 6.0d && phase < 7.0d && !calendarMoments.contains("Maturity"))
        {
            calendarMoments.add("Maturity");
            calendarCumuls.add(cumulTT);
            calendarDates.add(currentdate);
        }
        s.setcalendarMoments(calendarMoments);
        s.setcalendarDates(calendarDates);
        s.setcalendarCumuls(calendarCumuls);
    }
}
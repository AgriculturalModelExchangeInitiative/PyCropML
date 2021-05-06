model_updatecalendar <- function (cumulTT = 741.510096671757,
         calendarMoments = c('Sowing'),
         calendarDates = c('2007/3/21'),
         calendarCumuls = c(0.0),
         currentdate = '2007/3/27',
         phase = 1.0){
    #'- Name: UpdateCalendar -Version: 1.0, -Time step: 1
    #'- Description:
    #'            * Title: Calendar Model
    #'            * Author: Pierre Martre
    #'            * Reference: Modeling development phase in the 
    #'                Wheat Simulation Model SiriusQuality.
    #'                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    #'            * Institution: INRA Montpellier
    #'            * Abstract: Lists containing for each stage the date it occurs as well as a copy of all types of cumulated thermal times 
    #'- inputs:
    #'            * name: cumulTT
    #'                          ** description : cumul thermal times at current date
    #'                          ** variablecategory : auxiliary
    #'                          ** datatype : DOUBLE
    #'                          ** min : -200
    #'                          ** max : 10000
    #'                          ** default : 741.510096671757
    #'                          ** unit : °C d
    #'                          ** inputtype : variable
    #'            * name: calendarMoments
    #'                          ** description : List containing apparition of each stage
    #'                          ** variablecategory : state
    #'                          ** datatype : STRINGLIST
    #'                          ** default : ['Sowing']
    #'                          ** unit : 
    #'                          ** inputtype : variable
    #'            * name: calendarDates
    #'                          ** description : List containing  the dates of the wheat developmental phases
    #'                          ** variablecategory : state
    #'                          ** datatype : DATELIST
    #'                          ** default : ['2007/3/21']
    #'                          ** unit : 
    #'                          ** inputtype : variable
    #'            * name: calendarCumuls
    #'                          ** description : list containing for each stage occured its cumulated thermal times
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLELIST
    #'                          ** default : [0.0]
    #'                          ** unit : °C d
    #'                          ** inputtype : variable
    #'            * name: currentdate
    #'                          ** description : current date
    #'                          ** variablecategory : auxiliary
    #'                          ** datatype : DATE
    #'                          ** default : 2007/3/27
    #'                          ** unit : 
    #'                          ** inputtype : variable
    #'            * name: phase
    #'                          ** description :  the name of the phase
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 7
    #'                          ** default : 1
    #'                          ** unit : 
    #'                          ** inputtype : variable
    #'- outputs:
    #'            * name: calendarMoments
    #'                          ** description :  List containing apparition of each stage
    #'                          ** variablecategory : state
    #'                          ** datatype : STRINGLIST
    #'                          ** unit : 
    #'            * name: calendarDates
    #'                          ** description :  List containing  the dates of the wheat developmental phases
    #'                          ** variablecategory : state
    #'                          ** datatype : DATELIST
    #'                          ** unit : 
    #'            * name: calendarCumuls
    #'                          ** description :  list containing for each stage occured its cumulated thermal times
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLELIST
    #'                          ** unit : °C d
    if (phase >= 1.0 && phase < 2.0 && !('Emergence' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'Emergence')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
    }
    else if ( phase >= 2.0 && phase < 3.0 && !('FloralInitiation' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'FloralInitiation')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
    }
    else if ( phase >= 3.0 && phase < 4.0 && !('Heading' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'Heading')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
    }
    else if ( phase == 4.0 && !('Anthesis' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'Anthesis')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
    }
    else if ( phase == 4.5 && !('EndCellDivision' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'EndCellDivision')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
    }
    else if ( phase >= 5.0 && phase < 6.0 && !('EndGrainFilling' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'EndGrainFilling')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
    }
    else if ( phase >= 6.0 && phase < 7.0 && !('Maturity' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'Maturity')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
    }
    return (list ("calendarMoments" = calendarMoments,"calendarDates" = calendarDates,"calendarCumuls" = calendarCumuls))
}
model_registerzadok <- function (cumulTT = 354.582294511779,
         phase = 2.0,
         leafNumber = 4.8854219661087575,
         calendarMoments = c('Sowing'),
         calendarDates = c('2007/3/21'),
         calendarCumuls = c(0.0),
         cumulTTFromZC_65 = 0.0,
         currentdate = '2007/4/9',
         der = 300.0,
         slopeTSFLN = 0.9,
         intTSFLN = 0.9,
         finalLeafNumber = 8.797582013199484,
         currentZadokStage = 'MainShootPlus1Tiller',
         hasZadokStageChanged_t1 = 0,
         sowingDate = '2007/3/21'){
    #'- Name: RegisterZadok -Version: 1.0, -Time step: 1
    #'- Description:
    #'            * Title: RegisterZadok Model
    #'            * Author: Pierre MARTRE
    #'            * Reference: Modeling development phase in the 
    #'                Wheat Simulation Model SiriusQuality.
    #'                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    #'            * Institution: INRA/LEPSE Montpellier
    #'            * Abstract: Record the zadok stage in the calendar
    #'    	
    #'- inputs:
    #'            * name: cumulTT
    #'                          ** description : 
    #'                          ** variablecategory : auxiliary
    #'                          ** datatype : DOUBLE
    #'                          ** min : -200
    #'                          ** max : 10000
    #'                          ** default : 354.582294511779
    #'                          ** unit : °C d
    #'                          ** uri : some url
    #'                          ** inputtype : variable
    #'            * name: phase
    #'                          ** description : instance of the phase class . You can get the name of the phase using phase.getPhaseAsString(PhaseValue) 
    #'                          ** variablecategory : state
    #'                          ** inputtype : variable
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 7
    #'                          ** default : 2
    #'                          ** unit : 
    #'                          ** uri : some url
    #'            * name: leafNumber
    #'                          ** description : Actual number of phytomers
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 25
    #'                          ** default : 4.8854219661087575
    #'                          ** unit : leaf
    #'                          ** uri : some url
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
    #'            * name: cumulTTFromZC_65
    #'                          ** description : cumul of the thermal time (DeltaTT) since the moment ZC_65
    #'                          ** variablecategory : auxiliary
    #'                          ** datatype : DOUBLE
    #'                          ** min : -200
    #'                          ** max : 10000
    #'                          ** default : 0
    #'                          ** unit : °C d
    #'                          ** uri : some url
    #'                          ** inputtype : variable
    #'            * name: currentdate
    #'                          ** description : current date
    #'                          ** variablecategory : auxiliary
    #'                          ** datatype : DATE
    #'                          ** min : 
    #'                          ** max : 
    #'                          ** default : 2007/4/9
    #'                          ** unit : 
    #'                          ** uri : some url
    #'                          ** inputtype : variable
    #'            * name: der
    #'                          ** description : Duration of the endosperm endoreduplication phase
    #'                          ** parametercategory : species
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** default : 300.0
    #'                          ** unit : °C d
    #'                          ** uri : some url
    #'                          ** inputtype : parameter
    #'            * name: slopeTSFLN
    #'                          ** description : used to calculate Terminal spikelet
    #'                          ** parametercategory : species
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** default : 0.9
    #'                          ** unit : 
    #'                          ** uri : some url
    #'                          ** inputtype : parameter
    #'            * name: intTSFLN
    #'                          ** description : used to calculate Terminal spikelet
    #'                          ** parametercategory : species
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** default : 0.9
    #'                          ** unit : 
    #'                          ** uri : some url
    #'                          ** inputtype : parameter
    #'            * name: finalLeafNumber
    #'                          ** description : final leaf number
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** min : 0
    #'                          ** max : 10000
    #'                          ** default : 8.797582013199484
    #'                          ** unit : leaf
    #'                          ** uri : some url
    #'                          ** inputtype : variable
    #'            * name: currentZadokStage
    #'                          ** description : current zadok stage
    #'                          ** variablecategory : state
    #'                          ** datatype : STRING
    #'                          ** min : 
    #'                          ** max : 
    #'                          ** default : MainShootPlus1Tiller
    #'                          ** unit : 
    #'                          ** uri : some url
    #'                          ** inputtype : variable
    #'            * name: hasZadokStageChanged_t1
    #'                          ** description : true if the zadok stage has changed this time step
    #'                          ** variablecategory : state
    #'                          ** datatype : INT
    #'                          ** min : 0
    #'                          ** max : 1
    #'                          ** default : 0
    #'                          ** unit : 
    #'                          ** uri : some url
    #'                          ** inputtype : variable
    #'            * name: sowingDate
    #'                          ** description :  Date of Sowing
    #'                          ** parametercategory : constant
    #'                          ** datatype : DATE
    #'                          ** min : 
    #'                          ** max : 
    #'                          ** default : 2007/3/21
    #'                          ** unit : 
    #'                          ** inputtype : parameter
    #'- outputs:
    #'            * name: hasZadokStageChanged
    #'                          ** description : true if the zadok stage has changed this time step
    #'                          ** variablecategory : state
    #'                          ** datatype : INT
    #'                          ** min : 0
    #'                          ** max : 1
    #'                          ** unit : 
    #'                          ** uri : some url
    #'            * name: currentZadokStage
    #'                          ** description : current zadok stage
    #'                          ** variablecategory : state
    #'                          ** datatype : STRING
    #'                          ** unit :  
    #'                          ** uri : some url
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
    roundedFinalLeafNumber <- as.integer(finalLeafNumber + 0.5)
    if (leafNumber >= 4.0 && !('MainShootPlus1Tiller' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'MainShootPlus1Tiller')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
        hasZadokStageChanged <- 1
        currentZadokStage <- 'MainShootPlus1Tiller'
    }
    else if ( leafNumber >= 5.0 && !('MainShootPlus2Tiller' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'MainShootPlus2Tiller')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
        hasZadokStageChanged <- 1
        currentZadokStage <- 'MainShootPlus2Tiller'
    }
    else if ( leafNumber >= 6.0 && !('MainShootPlus3Tiller' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'MainShootPlus3Tiller')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
        hasZadokStageChanged <- 1
        currentZadokStage <- 'MainShootPlus3Tiller'
    }
    else if ( finalLeafNumber > 0.0 && (leafNumber >= slopeTSFLN * finalLeafNumber - intTSFLN && !('TerminalSpikelet' %in% calendarMoments)))
    {
        calendarMoments <- c(calendarMoments, 'TerminalSpikelet')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
        hasZadokStageChanged <- 1
        currentZadokStage <- 'TerminalSpikelet'
    }
    else if ( leafNumber >= roundedFinalLeafNumber - 4.0 && roundedFinalLeafNumber - 4 > 0 && !('PseudoStemErection' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'PseudoStemErection')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
        hasZadokStageChanged <- 1
        currentZadokStage <- 'PseudoStemErection'
    }
    else if ( leafNumber >= roundedFinalLeafNumber - 3.0 && roundedFinalLeafNumber - 3 > 0 && !('1stNodeDetectable' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, '1stNodeDetectable')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
        hasZadokStageChanged <- 1
        currentZadokStage <- '1stNodeDetectable'
    }
    else if ( leafNumber >= roundedFinalLeafNumber - 2.0 && roundedFinalLeafNumber - 2 > 0 && !('2ndNodeDetectable' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, '2ndNodeDetectable')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
        hasZadokStageChanged <- 1
        currentZadokStage <- '2ndNodeDetectable'
    }
    else if ( leafNumber >= roundedFinalLeafNumber - 1.0 && roundedFinalLeafNumber - 1 > 0 && !('FlagLeafJustVisible' %in% calendarMoments))
    {
        calendarMoments <- c(calendarMoments, 'FlagLeafJustVisible')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
        hasZadokStageChanged <- 1
        currentZadokStage <- 'FlagLeafJustVisible'
    }
    else if ( !('MidGrainFilling' %in% calendarMoments) && (phase == 4.5 && cumulTTFromZC_65 >= der))
    {
        calendarMoments <- c(calendarMoments, 'MidGrainFilling')
        calendarCumuls <- c(calendarCumuls, cumulTT)
        calendarDates <- c(calendarDates, currentdate)
        hasZadokStageChanged <- 1
        currentZadokStage <- 'MidGrainFilling'
    }
    else
    {
        hasZadokStageChanged <- 0
    }
    return (list ("hasZadokStageChanged" = hasZadokStageChanged,"currentZadokStage" = currentZadokStage,"calendarMoments" = calendarMoments,"calendarDates" = calendarDates,"calendarCumuls" = calendarCumuls))
}
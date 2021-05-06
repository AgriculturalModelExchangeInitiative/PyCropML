#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
# include<numeric>
# include<algorithm>
# include<array>
#include <map>
# include <tuple>
#include "Registerzadok.h"
using namespace std;

Registerzadok::Registerzadok() { }
float Registerzadok::getder() {return this-> der; }
float Registerzadok::getslopeTSFLN() {return this-> slopeTSFLN; }
float Registerzadok::getintTSFLN() {return this-> intTSFLN; }
string Registerzadok::getsowingDate() {return this-> sowingDate; }
void Registerzadok::setder(float _der) { this->der = _der; }
void Registerzadok::setslopeTSFLN(float _slopeTSFLN) { this->slopeTSFLN = _slopeTSFLN; }
void Registerzadok::setintTSFLN(float _intTSFLN) { this->intTSFLN = _intTSFLN; }
void Registerzadok::setsowingDate(string _sowingDate) { this->sowingDate = _sowingDate; }
void Registerzadok::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
{
    //- Name: RegisterZadok -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: RegisterZadok Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA/LEPSE Montpellier
    //            * Abstract: Record the zadok stage in the calendar
    //    	
    //- inputs:
    //            * name: cumulTT
    //                          ** description : 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 354.582294511779
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: phase
    //                          ** description : instance of the phase class . You can get the name of the phase using phase.getPhaseAsString(PhaseValue) 
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** default : 2
    //                          ** unit : 
    //                          ** uri : some url
    //            * name: leafNumber
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 4.8854219661087575
    //                          ** unit : leaf
    //                          ** uri : some url
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
    //            * name: cumulTTFromZC_65
    //                          ** description : cumul of the thermal time (DeltaTT) since the moment ZC_65
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -200
    //                          ** max : 10000
    //                          ** default : 0
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: currentdate
    //                          ** description : current date
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DATE
    //                          ** min : 
    //                          ** max : 
    //                          ** default : 2007/4/9
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: der
    //                          ** description : Duration of the endosperm endoreduplication phase
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 300.0
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: slopeTSFLN
    //                          ** description : used to calculate Terminal spikelet
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0.9
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: intTSFLN
    //                          ** description : used to calculate Terminal spikelet
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 0.9
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: finalLeafNumber
    //                          ** description : final leaf number
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 8.797582013199484
    //                          ** unit : leaf
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: currentZadokStage
    //                          ** description : current zadok stage
    //                          ** variablecategory : state
    //                          ** datatype : STRING
    //                          ** min : 
    //                          ** max : 
    //                          ** default : MainShootPlus1Tiller
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: hasZadokStageChanged_t1
    //                          ** description : true if the zadok stage has changed this time step
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: sowingDate
    //                          ** description :  Date of Sowing
    //                          ** parametercategory : constant
    //                          ** datatype : DATE
    //                          ** min : 
    //                          ** max : 
    //                          ** default : 2007/3/21
    //                          ** unit : 
    //                          ** inputtype : parameter
    //- outputs:
    //            * name: hasZadokStageChanged
    //                          ** description : true if the zadok stage has changed this time step
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : 
    //                          ** uri : some url
    //            * name: currentZadokStage
    //                          ** description : current zadok stage
    //                          ** variablecategory : state
    //                          ** datatype : STRING
    //                          ** unit :  
    //                          ** uri : some url
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
    float cumulTT = a.getcumulTT();
    float phase = s.getphase();
    float leafNumber = s.getleafNumber();
    vector<string> calendarMoments = s.getcalendarMoments();
    vector<string> calendarDates = s.getcalendarDates();
    vector<float> calendarCumuls = s.getcalendarCumuls();
    float cumulTTFromZC_65 = a.getcumulTTFromZC_65();
    string currentdate = a.getcurrentdate();
    float finalLeafNumber = s.getfinalLeafNumber();
    string currentZadokStage = s.getcurrentZadokStage();
    int hasZadokStageChanged_t1 = s1.gethasZadokStageChanged();
    int hasZadokStageChanged;
    int roundedFinalLeafNumber;
    roundedFinalLeafNumber = int(finalLeafNumber + 0.5f);
    if (leafNumber >= 4.0f && !(find(calendarMoments.begin(), calendarMoments.end(), "MainShootPlus1Tiller") != calendarMoments.end()))
    {
        calendarMoments.push_back("MainShootPlus1Tiller");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
        hasZadokStageChanged = 1;
        currentZadokStage = "MainShootPlus1Tiller";
    }
    else if ( leafNumber >= 5.0f && !(find(calendarMoments.begin(), calendarMoments.end(), "MainShootPlus2Tiller") != calendarMoments.end()))
    {
        calendarMoments.push_back("MainShootPlus2Tiller");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
        hasZadokStageChanged = 1;
        currentZadokStage = "MainShootPlus2Tiller";
    }
    else if ( leafNumber >= 6.0f && !(find(calendarMoments.begin(), calendarMoments.end(), "MainShootPlus3Tiller") != calendarMoments.end()))
    {
        calendarMoments.push_back("MainShootPlus3Tiller");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
        hasZadokStageChanged = 1;
        currentZadokStage = "MainShootPlus3Tiller";
    }
    else if ( finalLeafNumber > 0.0f && (leafNumber >= slopeTSFLN * finalLeafNumber - intTSFLN && !(find(calendarMoments.begin(), calendarMoments.end(), "TerminalSpikelet") != calendarMoments.end())))
    {
        calendarMoments.push_back("TerminalSpikelet");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
        hasZadokStageChanged = 1;
        currentZadokStage = "TerminalSpikelet";
    }
    else if ( leafNumber >= roundedFinalLeafNumber - 4.0f && roundedFinalLeafNumber - 4 > 0 && !(find(calendarMoments.begin(), calendarMoments.end(), "PseudoStemErection") != calendarMoments.end()))
    {
        calendarMoments.push_back("PseudoStemErection");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
        hasZadokStageChanged = 1;
        currentZadokStage = "PseudoStemErection";
    }
    else if ( leafNumber >= roundedFinalLeafNumber - 3.0f && roundedFinalLeafNumber - 3 > 0 && !(find(calendarMoments.begin(), calendarMoments.end(), "1stNodeDetectable") != calendarMoments.end()))
    {
        calendarMoments.push_back("1stNodeDetectable");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
        hasZadokStageChanged = 1;
        currentZadokStage = "1stNodeDetectable";
    }
    else if ( leafNumber >= roundedFinalLeafNumber - 2.0f && roundedFinalLeafNumber - 2 > 0 && !(find(calendarMoments.begin(), calendarMoments.end(), "2ndNodeDetectable") != calendarMoments.end()))
    {
        calendarMoments.push_back("2ndNodeDetectable");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
        hasZadokStageChanged = 1;
        currentZadokStage = "2ndNodeDetectable";
    }
    else if ( leafNumber >= roundedFinalLeafNumber - 1.0f && roundedFinalLeafNumber - 1 > 0 && !(find(calendarMoments.begin(), calendarMoments.end(), "FlagLeafJustVisible") != calendarMoments.end()))
    {
        calendarMoments.push_back("FlagLeafJustVisible");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
        hasZadokStageChanged = 1;
        currentZadokStage = "FlagLeafJustVisible";
    }
    else if ( !(find(calendarMoments.begin(), calendarMoments.end(), "MidGrainFilling") != calendarMoments.end()) && (phase == 4.5f && cumulTTFromZC_65 >= der))
    {
        calendarMoments.push_back("MidGrainFilling");
        calendarCumuls.push_back(cumulTT);
        calendarDates.push_back(currentdate);
        hasZadokStageChanged = 1;
        currentZadokStage = "MidGrainFilling";
    }
    else
    {
        hasZadokStageChanged = 0;
    }
    s.setcalendarMoments(calendarMoments);
    s.setcalendarDates(calendarDates);
    s.setcalendarCumuls(calendarCumuls);
    s.setcurrentZadokStage(currentZadokStage);
    s.sethasZadokStageChanged(hasZadokStageChanged);
}
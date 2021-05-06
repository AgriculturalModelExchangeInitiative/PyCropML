// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Registerzadok: public DiscreteTimeDyn {
public:
    Registerzadok(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        der = (events.exist("der")) ? vv::toDouble(events.get("der")) : 300.0;
        slopeTSFLN = (events.exist("slopeTSFLN")) ? vv::toDouble(events.get("slopeTSFLN")) : 0.9;
        intTSFLN = (events.exist("intTSFLN")) ? vv::toDouble(events.get("intTSFLN")) : 0.9;
        sowingDate = (events.exist("sowingDate")) ? vv::toDateTime(events.get("sowingDate")) : 2007/3/21;
        //  Variables gérées par ce composant
        calendarMoments.init(this,"calendarMoments", events);
        calendarDates.init(this,"calendarDates", events);
        calendarCumuls.init(this,"calendarCumuls", events);
        currentZadokStage.init(this,"currentZadokStage", events);
        hasZadokStageChanged.init(this,"hasZadokStageChanged", events);
        //  Variables gérées par un autre composant
        phase.init(this,"phase", events);
        leafNumber.init(this,"leafNumber", events);
        finalLeafNumber.init(this,"finalLeafNumber", events);
        cumulTT.init(this,"cumulTT", events);
        cumulTTFromZC_65.init(this,"cumulTTFromZC_65", events);
        currentdate.init(this,"currentdate", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Registerzadok() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        int roundedFinalLeafNumber;
        roundedFinalLeafNumber = int(finalLeafNumber() + 0.5d);
        if (leafNumber() >= 4.0d && !(find(calendarMoments.begin(), calendarMoments.end(), "MainShootPlus1Tiller") != calendarMoments.end()))
        {
            calendarMoments().push_back("MainShootPlus1Tiller");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus1Tiller";
        }
        else if ( leafNumber() >= 5.0d && !(find(calendarMoments.begin(), calendarMoments.end(), "MainShootPlus2Tiller") != calendarMoments.end()))
        {
            calendarMoments().push_back("MainShootPlus2Tiller");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus2Tiller";
        }
        else if ( leafNumber() >= 6.0d && !(find(calendarMoments.begin(), calendarMoments.end(), "MainShootPlus3Tiller") != calendarMoments.end()))
        {
            calendarMoments().push_back("MainShootPlus3Tiller");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus3Tiller";
        }
        else if ( finalLeafNumber() > 0.0d && (leafNumber() >= slopeTSFLN * finalLeafNumber() - intTSFLN && !(find(calendarMoments.begin(), calendarMoments.end(), "TerminalSpikelet") != calendarMoments.end())))
        {
            calendarMoments().push_back("TerminalSpikelet");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
            hasZadokStageChanged = 1;
            currentZadokStage = "TerminalSpikelet";
        }
        else if ( leafNumber() >= roundedFinalLeafNumber - 4.0d && roundedFinalLeafNumber - 4 > 0 && !(find(calendarMoments.begin(), calendarMoments.end(), "PseudoStemErection") != calendarMoments.end()))
        {
            calendarMoments().push_back("PseudoStemErection");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
            hasZadokStageChanged = 1;
            currentZadokStage = "PseudoStemErection";
        }
        else if ( leafNumber() >= roundedFinalLeafNumber - 3.0d && roundedFinalLeafNumber - 3 > 0 && !(find(calendarMoments.begin(), calendarMoments.end(), "1stNodeDetectable") != calendarMoments.end()))
        {
            calendarMoments().push_back("1stNodeDetectable");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
            hasZadokStageChanged = 1;
            currentZadokStage = "1stNodeDetectable";
        }
        else if ( leafNumber() >= roundedFinalLeafNumber - 2.0d && roundedFinalLeafNumber - 2 > 0 && !(find(calendarMoments.begin(), calendarMoments.end(), "2ndNodeDetectable") != calendarMoments.end()))
        {
            calendarMoments().push_back("2ndNodeDetectable");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
            hasZadokStageChanged = 1;
            currentZadokStage = "2ndNodeDetectable";
        }
        else if ( leafNumber() >= roundedFinalLeafNumber - 1.0d && roundedFinalLeafNumber - 1 > 0 && !(find(calendarMoments.begin(), calendarMoments.end(), "FlagLeafJustVisible") != calendarMoments.end()))
        {
            calendarMoments().push_back("FlagLeafJustVisible");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
            hasZadokStageChanged = 1;
            currentZadokStage = "FlagLeafJustVisible";
        }
        else if ( !(find(calendarMoments.begin(), calendarMoments.end(), "MidGrainFilling") != calendarMoments.end()) && (phase() == 4.5d && cumulTTFromZC_65() >= der))
        {
            calendarMoments().push_back("MidGrainFilling");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
            hasZadokStageChanged = 1;
            currentZadokStage = "MidGrainFilling";
        }
        else
        {
            hasZadokStageChanged = 0;
        }
    }
private:
    //Variables d'etat
    /**
    * @brief List containing apparition of each stage ()
    */
    Vect calendarMoments/**
    * @brief List containing  the dates of the wheat developmental phases ()
    */
    Vect calendarDates/**
    * @brief list containing for each stage occured its cumulated thermal times (°C d)
    */
    Vect calendarCumuls/**
    * @brief current zadok stage ()
    */
    Var currentZadokStage/**
    * @brief true if the zadok stage has changed this time step ()
    */
    Var hasZadokStageChanged

    //Entrées
    /**
        * @brief instance of the phase class . You can get the name of the phase using phase.getPhaseAsString(PhaseValue)  ()
        */
    Var phase/**
        * @brief Actual number of phytomers (leaf)
        */
    Var leafNumber/**
        * @brief final leaf number (leaf)
        */
    Var finalLeafNumber/**
        * @brief  (°C d)
        */
    Var cumulTT/**
        * @brief cumul of the thermal time (DeltaTT) since the moment ZC_65 (°C d)
        */
    Var cumulTTFromZC_65/**
        * @brief current date ()
        */
    Var currentdate

    //Paramètres du modele
    /**
    * @brief Duration of the endosperm endoreduplication phase (°C d)
    */
    double der;
    /**
    * @brief used to calculate Terminal spikelet ()
    */
    double slopeTSFLN;
    /**
    * @brief used to calculate Terminal spikelet ()
    */
    double intTSFLN;
    /**
    * @brief  Date of Sowing ()
    */
    string sowingDate;
};
}
}
DECLARE_DYNAMICS(record::Phenology::Registerzadok); // balise specifique VLE
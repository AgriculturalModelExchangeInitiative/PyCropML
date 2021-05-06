// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Updateleafflag: public DiscreteTimeDyn {
public:
    Updateleafflag(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        //  Variables gérées par ce composant
        calendarMoments.init(this,"calendarMoments", events);
        calendarDates.init(this,"calendarDates", events);
        calendarCumuls.init(this,"calendarCumuls", events);
        hasFlagLeafLiguleAppeared.init(this,"hasFlagLeafLiguleAppeared", events);
        //  Variables gérées par un autre composant
        leafNumber.init(this,"leafNumber", events);
        finalLeafNumber.init(this,"finalLeafNumber", events);
        phase.init(this,"phase", events);
        cumulTT.init(this,"cumulTT", events);
        currentdate.init(this,"currentdate", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Updateleafflag() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        hasFlagLeafLiguleAppeared = 0;
        if (phase() >= 1.0d && phase() < 4.0d)
        {
            if (leafNumber() > 0.0d)
            {
                if (hasFlagLeafLiguleAppeared() == 0 && (finalLeafNumber() > 0.0d && leafNumber() >= finalLeafNumber()))
                {
                    hasFlagLeafLiguleAppeared = 1;
                    if (!(find(calendarMoments.begin(), calendarMoments.end(), "FlagLeafLiguleJustVisible") != calendarMoments.end()))
                    {
                        calendarMoments().push_back("FlagLeafLiguleJustVisible");
                        calendarCumuls().push_back(cumulTT());
                        calendarDates().push_back(currentdate());
                    }
                }
            }
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
    * @brief true if flag leaf has appeared (leafnumber reached finalLeafNumber) ()
    */
    Var hasFlagLeafLiguleAppeared

    //Entrées
    /**
        * @brief Actual number of phytomers (leaf)
        */
    Var leafNumber/**
        * @brief final leaf number (leaf)
        */
    Var finalLeafNumber/**
        * @brief  the name of the phase ()
        */
    Var phase/**
        * @brief cumul thermal times at current date (°C d)
        */
    Var cumulTT/**
        * @brief  current date ()
        */
    Var currentdate

    //Paramètres du modele
};
}
}
DECLARE_DYNAMICS(record::Phenology::Updateleafflag); // balise specifique VLE
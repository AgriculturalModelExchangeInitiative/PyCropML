// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Updatecalendar: public DiscreteTimeDyn {
public:
    Updatecalendar(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        //  Variables gérées par ce composant
        calendarMoments.init(this,"calendarMoments", events);
        calendarDates.init(this,"calendarDates", events);
        calendarCumuls.init(this,"calendarCumuls", events);
        //  Variables gérées par un autre composant
        phase.init(this,"phase", events);
        cumulTT.init(this,"cumulTT", events);
        currentdate.init(this,"currentdate", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Updatecalendar() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        if (phase() >= 1.0d && phase() < 2.0d && !(find(calendarMoments.begin(), calendarMoments.end(), "Emergence") != calendarMoments.end()))
        {
            calendarMoments().push_back("Emergence");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
        }
        else if ( phase() >= 2.0d && phase() < 3.0d && !(find(calendarMoments.begin(), calendarMoments.end(), "FloralInitiation") != calendarMoments.end()))
        {
            calendarMoments().push_back("FloralInitiation");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
        }
        else if ( phase() >= 3.0d && phase() < 4.0d && !(find(calendarMoments.begin(), calendarMoments.end(), "Heading") != calendarMoments.end()))
        {
            calendarMoments().push_back("Heading");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
        }
        else if ( phase() == 4.0d && !(find(calendarMoments.begin(), calendarMoments.end(), "Anthesis") != calendarMoments.end()))
        {
            calendarMoments().push_back("Anthesis");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
        }
        else if ( phase() == 4.5d && !(find(calendarMoments.begin(), calendarMoments.end(), "EndCellDivision") != calendarMoments.end()))
        {
            calendarMoments().push_back("EndCellDivision");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
        }
        else if ( phase() >= 5.0d && phase() < 6.0d && !(find(calendarMoments.begin(), calendarMoments.end(), "EndGrainFilling") != calendarMoments.end()))
        {
            calendarMoments().push_back("EndGrainFilling");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
        }
        else if ( phase() >= 6.0d && phase() < 7.0d && !(find(calendarMoments.begin(), calendarMoments.end(), "Maturity") != calendarMoments.end()))
        {
            calendarMoments().push_back("Maturity");
            calendarCumuls().push_back(cumulTT());
            calendarDates().push_back(currentdate());
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
    Vect calendarCumuls

    //Entrées
    /**
        * @brief  the name of the phase ()
        */
    Var phase/**
        * @brief cumul thermal times at current date (°C d)
        */
    Var cumulTT/**
        * @brief current date ()
        */
    Var currentdate

    //Paramètres du modele
};
}
}
DECLARE_DYNAMICS(record::Phenology::Updatecalendar); // balise specifique VLE
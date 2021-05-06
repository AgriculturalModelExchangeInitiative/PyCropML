// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Cumulttfrom: public DiscreteTimeDyn {
public:
    Cumulttfrom(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        //  Variables gérées par ce composant
        cumulTTFromZC_65.init(this,"cumulTTFromZC_65", events);
        cumulTTFromZC_39.init(this,"cumulTTFromZC_39", events);
        cumulTTFromZC_91.init(this,"cumulTTFromZC_91", events);
        //  Variables gérées par un autre composant
        calendarMoments.init(this,"calendarMoments", events);
        calendarCumuls.init(this,"calendarCumuls", events);
        cumulTT.init(this,"cumulTT", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Cumulttfrom() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        cumulTTFromZC_65 = 0.0d;
        cumulTTFromZC_39 = 0.0d;
        cumulTTFromZC_91 = 0.0d;
        if (find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "Anthesis") != calendarMoments_t1.end())
        {
            cumulTTFromZC_65 = cumulTT() - calendarCumuls(-1)[find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "Anthesis") - calendarMoments_t1.begin()];
        }
        if (find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "FlagLeafLiguleJustVisible") != calendarMoments_t1.end())
        {
            cumulTTFromZC_39 = cumulTT() - calendarCumuls(-1)[find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "FlagLeafLiguleJustVisible") - calendarMoments_t1.begin()];
        }
        if (find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "EndGrainFilling") != calendarMoments_t1.end())
        {
            cumulTTFromZC_91 = cumulTT() - calendarCumuls(-1)[find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "EndGrainFilling") - calendarMoments_t1.begin()];
        }
    }
private:
    //Variables d'etat
    /**
    * @brief  cumul TT from Anthesis to current date  (°C d)
    */
    Var cumulTTFromZC_65/**
    * @brief  cumul TT from FlagLeafLiguleJustVisible to current date  (°C d)
    */
    Var cumulTTFromZC_39/**
    * @brief  cumul TT from EndGrainFilling to current date  (°C d)
    */
    Var cumulTTFromZC_91

    //Entrées
    /**
        * @brief List containing appearance of each stage at previous day ()
        */
    Vect calendarMoments/**
        * @brief list containing for each stage occured its cumulated thermal times at previous day (°C d)
        */
    Vect calendarCumuls/**
        * @brief cumul TT at current date (°C d)
        */
    Var cumulTT

    //Paramètres du modele
};
}
}
DECLARE_DYNAMICS(record::Phenology::Cumulttfrom); // balise specifique VLE
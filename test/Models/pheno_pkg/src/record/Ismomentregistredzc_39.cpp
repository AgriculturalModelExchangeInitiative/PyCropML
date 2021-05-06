// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Ismomentregistredzc_39: public DiscreteTimeDyn {
public:
    Ismomentregistredzc_39(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        //  Variables gérées par ce composant
        isMomentRegistredZC_39.init(this,"isMomentRegistredZC_39", events);
        //  Variables gérées par un autre composant
        calendarMoments.init(this,"calendarMoments", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Ismomentregistredzc_39() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        isMomentRegistredZC_39 = find(calendarMoments_t1.begin(), calendarMoments_t1.end(), "FlagLeafLiguleJustVisible") != calendarMoments_t1.end() ? 1 : 0;
    }
private:
    //Variables d'etat
    /**
    * @brief  if Flag leaf ligule has already appeared  ()
    */
    Var isMomentRegistredZC_39

    //Entrées
    /**
        * @brief List containing appearance of each stage at previous time ()
        */
    Vect calendarMoments

    //Paramètres du modele
};
}
}
DECLARE_DYNAMICS(record::Phenology::Ismomentregistredzc_39); // balise specifique VLE
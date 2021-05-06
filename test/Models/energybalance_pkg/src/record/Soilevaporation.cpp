// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Soilevaporation: public DiscreteTimeDyn {
public:
    Soilevaporation(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        //  Variables gérées par ce composant
        soilEvaporation.init(this,"soilEvaporation", events);
        //  Variables gérées par un autre composant
        diffusionLimitedEvaporation.init(this,"diffusionLimitedEvaporation", events);
        energyLimitedEvaporation.init(this,"energyLimitedEvaporation", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Soilevaporation() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        soilEvaporation = min(diffusionLimitedEvaporation(), energyLimitedEvaporation());
    }
private:
    //Variables d'etat
    /**
    * @brief soil Evaporation (g m-2 d-1)
    */
    Var soilEvaporation

    //Entrées
    /**
        * @brief diffusion Limited Evaporation (g m-2 d-1)
        */
    Var diffusionLimitedEvaporation/**
        * @brief energy Limited Evaporation (g m-2 d-1)
        */
    Var energyLimitedEvaporation

    //Paramètres du modele
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Soilevaporation); // balise specifique VLE
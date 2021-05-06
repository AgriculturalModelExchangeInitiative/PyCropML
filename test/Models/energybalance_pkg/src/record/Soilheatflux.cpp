// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Soilheatflux: public DiscreteTimeDyn {
public:
    Soilheatflux(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        tau = (events.exist("tau")) ? vv::toDouble(events.get("tau")) : 0.9983;
        //  Variables gérées par ce composant
        soilHeatFlux.init(this,"soilHeatFlux", events);
        //  Variables gérées par un autre composant
        netRadiationEquivalentEvaporation.init(this,"netRadiationEquivalentEvaporation", events);
        soilEvaporation.init(this,"soilEvaporation", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Soilheatflux() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        soilHeatFlux = tau * netRadiationEquivalentEvaporation() - soilEvaporation();
    }
private:
    //Variables d'etat
    /**
    * @brief soil Heat Flux  (g m-2 d-1)
    */
    Var soilHeatFlux

    //Entrées
    /**
        * @brief net Radiation Equivalent Evaporation (g m-2 d-1)
        */
    Var netRadiationEquivalentEvaporation/**
        * @brief soil Evaporation (g m-2 d-1)
        */
    Var soilEvaporation

    //Paramètres du modele
    /**
    * @brief plant cover factor ()
    */
    double tau;
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Soilheatflux); // balise specifique VLE
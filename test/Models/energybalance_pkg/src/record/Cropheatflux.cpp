// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Cropheatflux: public DiscreteTimeDyn {
public:
    Cropheatflux(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        //  Variables gérées par ce composant
        cropHeatFlux.init(this,"cropHeatFlux", events);
        //  Variables gérées par un autre composant
        soilHeatFlux.init(this,"soilHeatFlux", events);
        potentialTranspiration.init(this,"potentialTranspiration", events);
        netRadiationEquivalentEvaporation.init(this,"netRadiationEquivalentEvaporation", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Cropheatflux() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        cropHeatFlux = netRadiationEquivalentEvaporation() - soilHeatFlux() - potentialTranspiration();
    }
private:
    //Variables d'etat
    /**
    * @brief  crop Heat Flux (g m-2 d-1)
    */
    Var cropHeatFlux

    //Entrées
    /**
        * @brief soil Heat Flux (g m-2 d-1)
        */
    Var soilHeatFlux/**
        * @brief potential Transpiration (g m-2 d-1)
        */
    Var potentialTranspiration/**
        * @brief net Radiation Equivalent Evaporation (g m-2 d-1)
        */
    Var netRadiationEquivalentEvaporation

    //Paramètres du modele
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Cropheatflux); // balise specifique VLE
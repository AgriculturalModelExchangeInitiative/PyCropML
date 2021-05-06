// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Netradiationequivalentevaporation: public DiscreteTimeDyn {
public:
    Netradiationequivalentevaporation(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        lambdaV = (events.exist("lambdaV")) ? vv::toDouble(events.get("lambdaV")) : 2.454;
        //  Variables gérées par ce composant
        netRadiationEquivalentEvaporation.init(this,"netRadiationEquivalentEvaporation", events);
        //  Variables gérées par un autre composant
        netRadiation.init(this,"netRadiation", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Netradiationequivalentevaporation() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        netRadiationEquivalentEvaporation = netRadiation() / lambdaV * 1000.0d;
    }
private:
    //Variables d'etat
    /**
    * @brief net Radiation in Equivalent Evaporation  (g m-2 d-1)
    */
    Var netRadiationEquivalentEvaporation

    //Entrées
    /**
        * @brief net radiation (MJ m-2 d-1)
        */
    Var netRadiation

    //Paramètres du modele
    /**
    * @brief latent heat of vaporization of water (MJ kg-1)
    */
    double lambdaV;
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Netradiationequivalentevaporation); // balise specifique VLE
// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Priestlytaylor: public DiscreteTimeDyn {
public:
    Priestlytaylor(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        psychrometricConstant = (events.exist("psychrometricConstant")) ? vv::toDouble(events.get("psychrometricConstant")) : 0.66;
        Alpha = (events.exist("Alpha")) ? vv::toDouble(events.get("Alpha")) : 1.5;
        //  Variables gérées par ce composant
        evapoTranspirationPriestlyTaylor.init(this,"evapoTranspirationPriestlyTaylor", events);
        //  Variables gérées par un autre composant
        netRadiationEquivalentEvaporation.init(this,"netRadiationEquivalentEvaporation", events);
        hslope.init(this,"hslope", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Priestlytaylor() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        evapoTranspirationPriestlyTaylor = max(Alpha * hslope() * netRadiationEquivalentEvaporation() / (hslope() + psychrometricConstant), 0.0d);
    }
private:
    //Variables d'etat
    /**
    * @brief evapoTranspiration of Priestly Taylor  (g m-2 d-1)
    */
    Var evapoTranspirationPriestlyTaylor

    //Entrées
    /**
        * @brief net Radiation in Equivalent Evaporation (g m-2 d-1)
        */
    Var netRadiationEquivalentEvaporation/**
        * @brief the slope of saturated vapor pressure temperature curve at a given temperature  (hPa °C-1)
        */
    Var hslope

    //Paramètres du modele
    /**
    * @brief psychrometric constant ()
    */
    double psychrometricConstant;
    /**
    * @brief Priestley-Taylor evapotranspiration proportionality constant ()
    */
    double Alpha;
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Priestlytaylor); // balise specifique VLE
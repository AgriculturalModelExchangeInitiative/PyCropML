// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Ptsoil: public DiscreteTimeDyn {
public:
    Ptsoil(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        Alpha = (events.exist("Alpha")) ? vv::toDouble(events.get("Alpha")) : 1.5;
        tau = (events.exist("tau")) ? vv::toDouble(events.get("tau")) : 0.9983;
        tauAlpha = (events.exist("tauAlpha")) ? vv::toDouble(events.get("tauAlpha")) : 0.3;
        //  Variables gérées par ce composant
        energyLimitedEvaporation.init(this,"energyLimitedEvaporation", events);
        //  Variables gérées par un autre composant
        evapoTranspirationPriestlyTaylor.init(this,"evapoTranspirationPriestlyTaylor", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Ptsoil() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        double AlphaE;
        if (tau < tauAlpha)
        {
            AlphaE = 1.0d;
        }
        else
        {
            AlphaE = Alpha - ((Alpha - 1.0d) * (1.0d - tau) / (1.0d - tauAlpha));
        }
        energyLimitedEvaporation = evapoTranspirationPriestlyTaylor() / Alpha * AlphaE * tau;
    }
private:
    //Variables d'etat
    /**
    * @brief energy Limited Evaporation  (g m-2 d-1)
    */
    Var energyLimitedEvaporation

    //Entrées
    /**
        * @brief evapoTranspiration Priestly Taylor (g m-2 d-1)
        */
    Var evapoTranspirationPriestlyTaylor

    //Paramètres du modele
    /**
    * @brief Priestley-Taylor evapotranspiration proportionality constant ()
    */
    double Alpha;
    /**
    * @brief plant cover factor ()
    */
    double tau;
    /**
    * @brief Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1 ()
    */
    double tauAlpha;
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Ptsoil); // balise specifique VLE
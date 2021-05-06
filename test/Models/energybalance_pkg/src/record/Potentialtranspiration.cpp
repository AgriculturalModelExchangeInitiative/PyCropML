// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Potentialtranspiration: public DiscreteTimeDyn {
public:
    Potentialtranspiration(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        tau = (events.exist("tau")) ? vv::toDouble(events.get("tau")) : 0.9983;
        //  Variables gérées par ce composant
        potentialTranspiration.init(this,"potentialTranspiration", events);
        //  Variables gérées par un autre composant
        evapoTranspiration.init(this,"evapoTranspiration", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Potentialtranspiration() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        potentialTranspiration = evapoTranspiration() * (1.0d - tau);
    }
private:
    //Variables d'etat
    /**
    * @brief potential Transpiration  (g m-2 d-1)
    */
    Var potentialTranspiration

    //Entrées
    /**
        * @brief evapoTranspiration (mm)
        */
    Var evapoTranspiration

    //Paramètres du modele
    /**
    * @brief plant cover factor ()
    */
    double tau;
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Potentialtranspiration); // balise specifique VLE
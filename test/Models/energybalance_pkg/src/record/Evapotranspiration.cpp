// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Evapotranspiration: public DiscreteTimeDyn {
public:
    Evapotranspiration(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        isWindVpDefined = (events.exist("isWindVpDefined")) ? vv::toInteger(events.get("isWindVpDefined")) : 1;
        //  Variables gérées par ce composant
        evapoTranspiration.init(this,"evapoTranspiration", events);
        //  Variables gérées par un autre composant
        evapoTranspirationPriestlyTaylor.init(this,"evapoTranspirationPriestlyTaylor", events);
        evapoTranspirationPenman.init(this,"evapoTranspirationPenman", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Evapotranspiration() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        if (isWindVpDefined == 1)
        {
            evapoTranspiration = evapoTranspirationPenman();
        }
        else
        {
            evapoTranspiration = evapoTranspirationPriestlyTaylor();
        }
    }
private:
    //Variables d'etat
    /**
    * @brief evapoTranspiration (mm)
    */
    Var evapoTranspiration

    //Entrées
    /**
        * @brief evapoTranspiration of Priestly Taylor  (mm)
        */
    Var evapoTranspirationPriestlyTaylor/**
        * @brief evapoTranspiration of Penman  (mm)
        */
    Var evapoTranspirationPenman

    //Paramètres du modele
    /**
    * @brief if wind and vapour pressure are defined ()
    */
    int isWindVpDefined;
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Evapotranspiration); // balise specifique VLE
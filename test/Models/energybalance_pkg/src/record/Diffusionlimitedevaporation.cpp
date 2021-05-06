// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Diffusionlimitedevaporation: public DiscreteTimeDyn {
public:
    Diffusionlimitedevaporation(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        soilDiffusionConstant = (events.exist("soilDiffusionConstant")) ? vv::toDouble(events.get("soilDiffusionConstant")) : 4.2;
        //  Variables gérées par ce composant
        diffusionLimitedEvaporation.init(this,"diffusionLimitedEvaporation", events);
        //  Variables gérées par un autre composant
        deficitOnTopLayers.init(this,"deficitOnTopLayers", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Diffusionlimitedevaporation() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        if (deficitOnTopLayers() / 1000.0d <= 0.0d)
        {
            diffusionLimitedEvaporation = 8.3d * 1000.0d;
        }
        else
        {
            if (deficitOnTopLayers() / 1000.0d < 25.0d)
            {
                diffusionLimitedEvaporation = 2.0d * soilDiffusionConstant * soilDiffusionConstant / (deficitOnTopLayers() / 1000.0d) * 1000.0d;
            }
            else
            {
                diffusionLimitedEvaporation = 0.0d;
            }
        }
    }
private:
    //Variables d'etat
    /**
    * @brief the evaporation from the diffusion limited soil  (g m-2 d-1)
    */
    Var diffusionLimitedEvaporation

    //Entrées
    /**
        * @brief deficit On TopLayers (g m-2 d-1)
        */
    Var deficitOnTopLayers

    //Paramètres du modele
    /**
    * @brief soil Diffusion Constant ()
    */
    double soilDiffusionConstant;
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Diffusionlimitedevaporation); // balise specifique VLE
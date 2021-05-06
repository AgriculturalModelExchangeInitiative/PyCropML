// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Penman: public DiscreteTimeDyn {
public:
    Penman(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilisee si la condition n'est pas definie
        //...
        rhoDensityAir = (events.exist("rhoDensityAir")) ? vv::toDouble(events.get("rhoDensityAir")) : 1.225;

    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Penman() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        evapoTranspirationPenman = evapoTranspirationPriestlyTaylor() / Alpha + (1000.0d * (rhoDensityAir * specificHeatCapacityAir * VPDair() * conductance() / (lambdaV * (hslope() + psychrometricConstant))));
    }
private:
    //Variables d'etat
    /**
    * @brief  evapoTranspiration of Penman Monteith (g/m**2/d)
    */
    Var evapoTranspirationPenman

    //Entrées
    /**
        * @brief conductance (m/d)
        */
    Var conductance/**
        * @brief evapoTranspiration of Priestly Taylor  ((g/m**2)/d)
        */
    Var evapoTranspirationPriestlyTaylor/**
        * @brief the slope of saturated vapor pressure temperature curve at a given temperature  (hPa/degC)
        */
    Var hslope/**
        * @brief  vapour pressure density (hPa)
        */
    Var VPDair

    //Paramètres du modele
    /**
    * @brief psychrometric constant (hPa/degC)
    */
    double psychrometricConstant;
    /**
    * @brief Priestley-Taylor evapotranspiration proportionality constant ()
    */
    double Alpha;
    /**
    * @brief latent heat of vaporization of water (MJ/kg)
    */
    double lambdaV;
    /**
    * @brief Density of air (kg/m**3)
    */
    double rhoDensityAir;
    /**
    * @brief Specific heat capacity of dry air ((MJ/kg)/degC)
    */
    double specificHeatCapacityAir;
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Penman); // balise specifique VLE
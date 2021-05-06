// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Canopytemperature: public DiscreteTimeDyn {
public:
    Canopytemperature(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        lambdaV = (events.exist("lambdaV")) ? vv::toDouble(events.get("lambdaV")) : 2.454;
        rhoDensityAir = (events.exist("rhoDensityAir")) ? vv::toDouble(events.get("rhoDensityAir")) : 1.225;
        specificHeatCapacityAir = (events.exist("specificHeatCapacityAir")) ? vv::toDouble(events.get("specificHeatCapacityAir")) : 0.00101;
        //  Variables gérées par ce composant
        minCanopyTemperature.init(this,"minCanopyTemperature", events);
        maxCanopyTemperature.init(this,"maxCanopyTemperature", events);
        //  Variables gérées par un autre composant
        conductance.init(this,"conductance", events);
        cropHeatFlux.init(this,"cropHeatFlux", events);
        minTair.init(this,"minTair", events);
        maxTair.init(this,"maxTair", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Canopytemperature() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        minCanopyTemperature = minTair() + (cropHeatFlux() / (rhoDensityAir * specificHeatCapacityAir * conductance() / lambdaV * 1000.0d));
        maxCanopyTemperature = maxTair() + (cropHeatFlux() / (rhoDensityAir * specificHeatCapacityAir * conductance() / lambdaV * 1000.0d));
    }
private:
    //Variables d'etat
    /**
    * @brief minimal Canopy Temperature   (degC)
    */
    Var minCanopyTemperature/**
    * @brief maximal Canopy Temperature  (degC)
    */
    Var maxCanopyTemperature

    //Entrées
    /**
        * @brief the boundary layer conductance (m/d)
        */
    Var conductance/**
        * @brief Crop heat flux (g/m**2/d)
        */
    Var cropHeatFlux/**
        * @brief minimum air temperature (degC)
        */
    Var minTair/**
        * @brief maximum air Temperature (degC)
        */
    Var maxTair

    //Paramètres du modele
    /**
    * @brief latent heat of vaporization of water (MJ/kg)
    */
    double lambdaV;
    /**
    * @brief Density of air (kg/m**3)
    */
    double rhoDensityAir;
    /**
    * @brief Specific heat capacity of dry air (MJ/kg/degC)
    */
    double specificHeatCapacityAir;
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Canopytemperature); // balise specifique VLE
// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Netradiation: public DiscreteTimeDyn {
public:
    Netradiation(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        albedoCoefficient = (events.exist("albedoCoefficient")) ? vv::toDouble(events.get("albedoCoefficient")) : 0.23;
        stefanBoltzman = (events.exist("stefanBoltzman")) ? vv::toDouble(events.get("stefanBoltzman")) : 4.903E-09;
        elevation = (events.exist("elevation")) ? vv::toDouble(events.get("elevation")) : 0;
        //  Variables gérées par ce composant
        netRadiation.init(this,"netRadiation", events);
        netOutGoingLongWaveRadiation.init(this,"netOutGoingLongWaveRadiation", events);
        //  Variables gérées par un autre composant
        minTair.init(this,"minTair", events);
        maxTair.init(this,"maxTair", events);
        solarRadiation.init(this,"solarRadiation", events);
        vaporPressure.init(this,"vaporPressure", events);
        extraSolarRadiation.init(this,"extraSolarRadiation", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Netradiation() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        double Nsr;
        double clearSkySolarRadiation;
        double averageT;
        double surfaceEmissivity;
        double cloudCoverFactor;
        double Nolr;
        Nsr = (1.0d - albedoCoefficient) * solarRadiation();
        clearSkySolarRadiation = (0.75d + (2 * pow(10.0d, -5) * elevation)) * extraSolarRadiation();
        averageT = (pow(maxTair() + 273.16d, 4) + pow(minTair() + 273.16d, 4)) / 2.0d;
        surfaceEmissivity = 0.34d - (0.14d * sqrt(vaporPressure() / 10.0d));
        cloudCoverFactor = 1.35d * (solarRadiation() / clearSkySolarRadiation) - 0.35d;
        Nolr = stefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor;
        netRadiation = Nsr - Nolr;
        netOutGoingLongWaveRadiation = Nolr;
    }
private:
    //Variables d'etat
    /**
    * @brief  net radiation  (MJ m-2 d-1)
    */
    Var netRadiation/**
    * @brief net OutGoing Long Wave Radiation  (g m-2 d-1)
    */
    Var netOutGoingLongWaveRadiation

    //Entrées
    /**
        * @brief minimum air temperature (°C)
        */
    Var minTair/**
        * @brief maximum air Temperature (°C)
        */
    Var maxTair/**
        * @brief solar Radiation (MJ m-2 d-1)
        */
    Var solarRadiation/**
        * @brief vapor Pressure (hPa)
        */
    Var vaporPressure/**
        * @brief extra Solar Radiation (MJ m2 d-1)
        */
    Var extraSolarRadiation

    //Paramètres du modele
    /**
    * @brief albedo Coefficient ()
    */
    double albedoCoefficient;
    /**
    * @brief stefan Boltzman constant ()
    */
    double stefanBoltzman;
    /**
    * @brief elevation (m)
    */
    double elevation;
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Netradiation); // balise specifique VLE
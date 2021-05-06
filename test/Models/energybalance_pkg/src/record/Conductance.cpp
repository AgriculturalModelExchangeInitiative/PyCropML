// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Energybalance {
using namespace vle::discrete_time;
class Conductance: public DiscreteTimeDyn {
public:
    Conductance(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        vonKarman = (events.exist("vonKarman")) ? vv::toDouble(events.get("vonKarman")) : 0.42;
        heightWeatherMeasurements = (events.exist("heightWeatherMeasurements")) ? vv::toDouble(events.get("heightWeatherMeasurements")) : 2;
        zm = (events.exist("zm")) ? vv::toDouble(events.get("zm")) : 0.13;
        zh = (events.exist("zh")) ? vv::toDouble(events.get("zh")) : 0.013;
        d = (events.exist("d")) ? vv::toDouble(events.get("d")) : 0.67;
        //  Variables gérées par ce composant
        conductance.init(this,"conductance", events);
        //  Variables gérées par un autre composant
        plantHeight.init(this,"plantHeight", events);
        wind.init(this,"wind", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Conductance() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        double h;
        h = max(10.0d, plantHeight()) / 100.0d;
        conductance = wind() * pow(vonKarman, 2) / (log((heightWeatherMeasurements - (d * h)) / (zm * h)) * log((heightWeatherMeasurements - (d * h)) / (zh * h)));
    }
private:
    //Variables d'etat
    /**
    * @brief the boundary layer conductance (m/d)
    */
    Var conductance

    //Entrées
    /**
        * @brief plant Height (mm)
        */
    Var plantHeight/**
        * @brief wind (m/d)
        */
    Var wind

    //Paramètres du modele
    /**
    * @brief von Karman constant (dimensionless)
    */
    double vonKarman;
    /**
    * @brief reference height of wind and humidity measurements (m)
    */
    double heightWeatherMeasurements;
    /**
    * @brief roughness length governing momentum transfer, FAO (m)
    */
    double zm;
    /**
    * @brief roughness length governing transfer of heat and vapour, FAO (m)
    */
    double zh;
    /**
    * @brief corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO (dimensionless)
    */
    double d;
};
}
}
DECLARE_DYNAMICS(record::Energybalance::Conductance); // balise specifique VLE
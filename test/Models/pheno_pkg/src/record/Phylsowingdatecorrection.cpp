// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Phylsowingdatecorrection: public DiscreteTimeDyn {
public:
    Phylsowingdatecorrection(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        sowingDay = (events.exist("sowingDay")) ? vv::toInteger(events.get("sowingDay")) : 1;
        latitude = (events.exist("latitude")) ? vv::toDouble(events.get("latitude")) : 0.0;
        sDsa_sh = (events.exist("sDsa_sh")) ? vv::toDouble(events.get("sDsa_sh")) : 1.0;
        rp = (events.exist("rp")) ? vv::toDouble(events.get("rp")) : 0;
        sDws = (events.exist("sDws")) ? vv::toInteger(events.get("sDws")) : 1;
        sDsa_nh = (events.exist("sDsa_nh")) ? vv::toDouble(events.get("sDsa_nh")) : 1.0;
        p = (events.exist("p")) ? vv::toDouble(events.get("p")) : 120;
        //  Variables gérées par ce composant
        fixPhyll.init(this,"fixPhyll", events);
        //  Variables gérées par un autre composant
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Phylsowingdatecorrection() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        if (latitude < 0.0d)
        {
            if (sowingDay > int(sDsa_sh))
            {
                fixPhyll = p * (1 - (rp * min((sowingDay - sDsa_sh), float(sDws))));
            }
            else
            {
                fixPhyll = p;
            }
        }
        else
        {
            if (sowingDay < int(sDsa_nh))
            {
                fixPhyll = p * (1 - (rp * min(sowingDay, sDws)));
            }
            else
            {
                fixPhyll = p;
            }
        }
    }
private:
    //Variables d'etat
    /**
    * @brief  Phyllochron Varietal parameter  (°C d leaf-1)
    */
    Var fixPhyll

    //Entrées

    //Paramètres du modele
    /**
    * @brief Day of Year at sowing (d)
    */
    int sowingDay;
    /**
    * @brief Latitude (°)
    */
    double latitude;
    /**
    * @brief Sowing date at which Phyllochrone is maximum in southern hemispher (d)
    */
    double sDsa_sh;
    /**
    * @brief Rate of change of Phyllochrone with sowing date (d-1)
    */
    double rp;
    /**
    * @brief Sowing date at which Phyllochrone is minimum (d)
    */
    int sDws;
    /**
    * @brief Sowing date at which Phyllochrone is maximum in northern hemispher (d)
    */
    double sDsa_nh;
    /**
    * @brief Phyllochron (Varietal parameter) (°C d leaf-1)
    */
    double p;
};
}
}
DECLARE_DYNAMICS(record::Phenology::Phylsowingdatecorrection); // balise specifique VLE
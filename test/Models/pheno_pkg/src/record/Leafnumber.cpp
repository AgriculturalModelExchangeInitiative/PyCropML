// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Leafnumber: public DiscreteTimeDyn {
public:
    Leafnumber(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        //  Variables gérées par ce composant
        leafNumber.init(this,"leafNumber", events);
        //  Variables gérées par un autre composant
        phyllochron.init(this,"phyllochron", events);
        hasFlagLeafLiguleAppeared.init(this,"hasFlagLeafLiguleAppeared", events);
        phase.init(this,"phase", events);
        deltaTT.init(this,"deltaTT", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Leafnumber() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        leafNumber = leafNumber(-1);
        double phyllochron_;
        if (phase() >= 1.0d && phase() < 4.0d)
        {
            if (hasFlagLeafLiguleAppeared() == 0)
            {
                if (phyllochron(-1) == 0.0d)
                {
                    phyllochron_ = 0.0000001d;
                }
                else
                {
                    phyllochron_ = phyllochron(-1);
                }
                leafNumber = leafNumber(-1) + min(deltaTT() / phyllochron_, 0.999d);
            }
        }
    }
private:
    //Variables d'etat
    /**
    * @brief Actual number of phytomers (leaf)
    */
    Var leafNumber

    //Entrées
    /**
        * @brief phyllochron (°C d leaf-1)
        */
    Var phyllochron/**
        * @brief true if flag leaf has appeared (leafnumber reached finalLeafNumber) ()
        */
    Var hasFlagLeafLiguleAppeared/**
        * @brief  the name of the phase ( )
        */
    Var phase/**
        * @brief daily delta TT  (°C d)
        */
    Var deltaTT

    //Paramètres du modele
};
}
}
DECLARE_DYNAMICS(record::Phenology::Leafnumber); // balise specifique VLE
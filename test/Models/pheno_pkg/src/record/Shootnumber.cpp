// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Shootnumber: public DiscreteTimeDyn {
public:
    Shootnumber(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        sowingDensity = (events.exist("sowingDensity")) ? vv::toDouble(events.get("sowingDensity")) : 288.0;
        targetFertileShoot = (events.exist("targetFertileShoot")) ? vv::toDouble(events.get("targetFertileShoot")) : 600.0;
        //  Variables gérées par ce composant
        averageShootNumberPerPlant.init(this,"averageShootNumberPerPlant", events);
        canopyShootNumber.init(this,"canopyShootNumber", events);
        leafTillerNumberArray.init(this,"leafTillerNumberArray", events);
        tilleringProfile.init(this,"tilleringProfile", events);
        numberTillerCohort.init(this,"numberTillerCohort", events);
        //  Variables gérées par un autre composant
        leafNumber.init(this,"leafNumber", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Shootnumber() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        int emergedLeaves;
        int shoots;
        int i;
        vector<int> lNumberArray_rate;
        emergedLeaves = max(1, (int) ceil(leafNumber() - 1.0d));
        shoots = fibonacci(emergedLeaves);
        canopyShootNumber = min(shoots * sowingDensity, targetFertileShoot);
        averageShootNumberPerPlant = canopyShootNumber() / sowingDensity;
        if (canopyShootNumber() != canopyShootNumber(-1))
        {
            tilleringProfile = tilleringProfile_t1;
            tilleringProfile.push_back(canopyShootNumber() - canopyShootNumber(-1));
        }
        numberTillerCohort = tilleringProfile().size();
        for (i=leafTillerNumberArray(-1).size() ; i<(int) ceil(leafNumber()) ; i+=1)
        {
            lNumberArray_rate.push_back(numberTillerCohort());
        }
        leafTillerNumberArray = leafTillerNumberArray_t1;
        leafTillerNumberArray.reserve(leafTillerNumberArray.size() + distance(lNumberArray_rate.begin(),lNumberArray_rate.end()));
        leafTillerNumberArray.insert(leafTillerNumberArray.end(),lNumberArray_rate.begin(),lNumberArray_rate.end());
    }
private:
    //Variables d'etat
    /**
    * @brief average shoot number per plant in the canopy (shoot m-2)
    */
    Var averageShootNumberPerPlant/**
    * @brief shoot number for the whole canopy (shoot m-2)
    */
    Var canopyShootNumber/**
    * @brief store the number of tiller for each leaf layer (leaf)
    */
    Vect leafTillerNumberArray/**
    * @brief  store the amount of new tiller created at each time a new tiller appears (dimensionless)
    */
    Vect tilleringProfile/**
    * @brief Number of tiller which appears (dimensionless)
    */
    Var numberTillerCohort

    //Entrées
    /**
        * @brief Leaf number  (leaf)
        */
    Var leafNumber

    //Paramètres du modele
    /**
    * @brief number of plant /m² (plant m-2)
    */
    double sowingDensity;
    /**
    * @brief max value of shoot number for the canopy (shoot)
    */
    double targetFertileShoot;
    int Shootnumber:: fibonacci(int n)
    {
        if (n <= 1)
        {
            return n;
        }
        else
        {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        canopyShootNumber = sowingDensity;
        averageShootNumberPerPlant = 1.0d;
        tilleringProfile().push_back(sowingDensity);
        numberTillerCohort = 1;
        leafTillerNumberArray = vector<int>{};
    }
};
}
}
DECLARE_DYNAMICS(record::Phenology::Shootnumber); // balise specifique VLE
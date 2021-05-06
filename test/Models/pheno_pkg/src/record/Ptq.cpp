// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Ptq: public DiscreteTimeDyn {
public:
    Ptq(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        tTWindowForPTQ = (events.exist("tTWindowForPTQ")) ? vv::toDouble(events.get("tTWindowForPTQ")) : 70.0;
        kl = (events.exist("kl")) ? vv::toDouble(events.get("kl")) : 0.45;
        //  Variables gérées par ce composant
        listPARTTWindowForPTQ.init(this,"listPARTTWindowForPTQ", events);
        listTTShootWindowForPTQ.init(this,"listTTShootWindowForPTQ", events);
        ptq.init(this,"ptq", events);
        //  Variables gérées par un autre composant
        listGAITTWindowForPTQ.init(this,"listGAITTWindowForPTQ", events);
        pAR.init(this,"pAR", events);
        deltaTT.init(this,"deltaTT", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Ptq() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        vector<double> TTList;
        vector<double> PARList;
        int i;
        int count;
        double SumTT;
        double parInt = 0.0d;
        double TTShoot;
        for (i=0 ; i<listTTShootWindowForPTQ(-1).size() ; i+=1)
        {
            TTList.push_back(listTTShootWindowForPTQ(-1)[i]);
            PARList.push_back(listPARTTWindowForPTQ(-1)[i]);
        }
        TTList.push_back(deltaTT());
        PARList.push_back(pAR());
        SumTT = accumulate(TTList.begin(), TTList.end(), decltype(TTList)::value_type(0));
        count = 0;
        while ( SumTT > tTWindowForPTQ)
        {
            SumTT = SumTT - TTList[count];
            count = count + 1;
        }
        for (i=count ; i<TTList.size() ; i+=1)
        {
            listTTShootWindowForPTQ().push_back(TTList[i]);
            listPARTTWindowForPTQ().push_back(PARList[i]);
        }
        for (i=0 ; i<listTTShootWindowForPTQ().size() ; i+=1)
        {
            parInt = parInt + (listPARTTWindowForPTQ()[i] * (1 - exp(-kl * listGAITTWindowForPTQ()[i])));
        }
        TTShoot = accumulate(listTTShootWindowForPTQ.begin(), listTTShootWindowForPTQ.end(), decltype(listTTShootWindowForPTQ)::value_type(0));
        ptq = parInt / TTShoot;
    }
private:
    //Variables d'etat
    /**
    * @brief  List of Daily PAR during TTWindowForPTQ thermal time period (MJ m2 d)
    */
    Vect listPARTTWindowForPTQ/**
    * @brief List of Daily Shoot thermal time during TTWindowForPTQ thermal time period (°C d)
    */
    Vect listTTShootWindowForPTQ/**
    * @brief Photothermal Quotient (MJ °C-1 d m-2))
    */
    Var ptq

    //Entrées
    /**
        * @brief List of daily GAI over TTWindowForPTQ thermal time period (m2 m-2)
        */
    Vect listGAITTWindowForPTQ/**
        * @brief Daily Photosyntetically Active Radiation (MJ m² d)
        */
    Var pAR/**
        * @brief daily delta TT  (°C d)
        */
    Var deltaTT

    //Paramètres du modele
    /**
    * @brief Thermal time window in which averages are computed (°C d)
    */
    double tTWindowForPTQ;
    /**
    * @brief Exctinction Coefficient ()
    */
    double kl;
};
}
}
DECLARE_DYNAMICS(record::Phenology::Ptq); // balise specifique VLE
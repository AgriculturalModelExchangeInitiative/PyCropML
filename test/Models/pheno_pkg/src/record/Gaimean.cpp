// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Gaimean: public DiscreteTimeDyn {
public:
    Gaimean(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        tTWindowForPTQ = (events.exist("tTWindowForPTQ")) ? vv::toDouble(events.get("tTWindowForPTQ")) : 0.0;
        //  Variables gérées par ce composant
        gAImean.init(this,"gAImean", events);
        pastMaxAI.init(this,"pastMaxAI", events);
        listTTShootWindowForPTQ1.init(this,"listTTShootWindowForPTQ1", events);
        listGAITTWindowForPTQ.init(this,"listGAITTWindowForPTQ", events);
        //  Variables gérées par un autre composant
        gAI.init(this,"gAI", events);
        deltaTT.init(this,"deltaTT", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Gaimean() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        vector<double> TTList;
        vector<double> GAIList;
        double SumTT;
        int count = 0;
        double gai_ = 0.0d;
        double gaiMean_ = 0.0d;
        int countGaiMean = 0;
        int i;
        for (i=0 ; i<listTTShootWindowForPTQ1(-1).size() ; i+=1)
        {
            TTList.push_back(listTTShootWindowForPTQ1(-1)[i]);
            GAIList.push_back(listGAITTWindowForPTQ(-1)[i]);
        }
        TTList.push_back(deltaTT());
        GAIList.push_back(gAI());
        SumTT = accumulate(TTList.begin(), TTList.end(), decltype(TTList)::value_type(0));
        while ( SumTT > tTWindowForPTQ)
        {
            SumTT = SumTT - TTList[count];
            count = count + 1;
        }
        for (i=count ; i<TTList.size() ; i+=1)
        {
            listTTShootWindowForPTQ1().push_back(TTList[i]);
            listGAITTWindowForPTQ().push_back(GAIList[i]);
        }
        for (i=0 ; i<listGAITTWindowForPTQ().size() ; i+=1)
        {
            gaiMean_ = gaiMean_ + listGAITTWindowForPTQ()[i];
            countGaiMean = countGaiMean + 1;
        }
        gaiMean_ = gaiMean_ / countGaiMean;
        gai_ = max(pastMaxAI(-1), gaiMean_);
        pastMaxAI = gai_;
        gAImean = gai_;
    }
private:
    //Variables d'etat
    /**
    * @brief Mean Green Area Index (m2 leaf m-2 ground)
    */
    Var gAImean/**
    * @brief Maximum Leaf Area Index reached the current day (m2 leaf m-2 ground)
    */
    Var pastMaxAI/**
    * @brief List of daily shoot thermal time in the window dedicated to average (°C d)
    */
    Vect listTTShootWindowForPTQ1/**
    * @brief List of daily Green Area Index in the window dedicated to average (m2 leaf m-2 ground)
    */
    Vect listGAITTWindowForPTQ

    //Entrées
    /**
        * @brief Green Area Index of the day (m2 leaf m-2 ground)
        */
    Var gAI/**
        * @brief Thermal time increase of the day (°C d)
        */
    Var deltaTT

    //Paramètres du modele
    /**
    * @brief Thermal Time window for average (°C d)
    */
    double tTWindowForPTQ;
};
}
}
DECLARE_DYNAMICS(record::Phenology::Gaimean); // balise specifique VLE
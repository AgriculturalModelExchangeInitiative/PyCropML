// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Phyllochron: public DiscreteTimeDyn {
public:
    Phyllochron(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        lincr = (events.exist("lincr")) ? vv::toDouble(events.get("lincr")) : 8.0;
        ldecr = (events.exist("ldecr")) ? vv::toDouble(events.get("ldecr")) : 0.0;
        pdecr = (events.exist("pdecr")) ? vv::toDouble(events.get("pdecr")) : 0.4;
        pincr = (events.exist("pincr")) ? vv::toDouble(events.get("pincr")) : 1.5;
        kl = (events.exist("kl")) ? vv::toDouble(events.get("kl")) : 0.45;
        pTQhf = (events.exist("pTQhf")) ? vv::toDouble(events.get("pTQhf")) : 0.0;
        B = (events.exist("B")) ? vv::toDouble(events.get("B")) : 20.0;
        p = (events.exist("p")) ? vv::toDouble(events.get("p")) : 120.0;
        choosePhyllUse = (events.exist("choosePhyllUse")) ? vv::toString(events.get("choosePhyllUse")) : Default;
        areaSL = (events.exist("areaSL")) ? vv::toDouble(events.get("areaSL")) : 0.0;
        areaSS = (events.exist("areaSS")) ? vv::toDouble(events.get("areaSS")) : 0.0;
        lARmin = (events.exist("lARmin")) ? vv::toDouble(events.get("lARmin")) : 0.0;
        lARmax = (events.exist("lARmax")) ? vv::toDouble(events.get("lARmax")) : 0.0;
        sowingDensity = (events.exist("sowingDensity")) ? vv::toDouble(events.get("sowingDensity")) : 0.0;
        lNeff = (events.exist("lNeff")) ? vv::toDouble(events.get("lNeff")) : 0.0;
        //  Variables gérées par ce composant
        phyllochron.init(this,"phyllochron", events);
        //  Variables gérées par un autre composant
        leafNumber.init(this,"leafNumber", events);
        ptq.init(this,"ptq", events);
        gAImean.init(this,"gAImean", events);
        fixPhyll.init(this,"fixPhyll", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Phyllochron() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        double gaiLim;
        double LAR;
        phyllochron = 0.0d;
        LAR = 0.0d;
        gaiLim = lNeff * ((areaSL + areaSS) / 10000.0d) * sowingDensity;
        if (choosePhyllUse == "Default")
        {
            if (leafNumber() < ldecr)
            {
                phyllochron = fixPhyll() * pdecr;
            }
            else if ( leafNumber() >= ldecr && leafNumber() < lincr)
            {
                phyllochron = fixPhyll();
            }
            else
            {
                phyllochron = fixPhyll() * pincr;
            }
        }
        if (choosePhyllUse == "PTQ")
        {
            if (gAImean() > gaiLim)
            {
                LAR = (lARmin + ((lARmax - lARmin) * ptq() / (pTQhf + ptq()))) / (B * gAImean());
            }
            else
            {
                LAR = (lARmin + ((lARmax - lARmin) * ptq() / (pTQhf + ptq()))) / (B * gaiLim);
            }
            phyllochron = 1.0d / LAR;
        }
        if (choosePhyllUse == "Test")
        {
            if (leafNumber() < ldecr)
            {
                phyllochron = p * pdecr;
            }
            else if ( leafNumber() >= ldecr && leafNumber() < lincr)
            {
                phyllochron = p;
            }
            else
            {
                phyllochron = p * pincr;
            }
        }
    }
private:
    //Variables d'etat
    /**
    * @brief  the rate of leaf appearance  ( °C d leaf-1)
    */
    Var phyllochron

    //Entrées
    /**
        * @brief Actual number of phytomers (leaf)
        */
    Var leafNumber/**
        * @brief Photothermal quotient  (MJ °C-1 d-1 m-2))
        */
    Var ptq/**
        * @brief Green Area Index (m2 m-2)
        */
    Var gAImean/**
        * @brief Sowing date corrected Phyllochron (°C d leaf-1)
        */
    Var fixPhyll

    //Paramètres du modele
    /**
    * @brief Leaf number above which the phyllochron is increased by Pincr (leaf)
    */
    double lincr;
    /**
    * @brief Leaf number up to which the phyllochron is decreased by Pdecr (leaf)
    */
    double ldecr;
    /**
    * @brief Factor decreasing the phyllochron for leaf number less than Ldecr (-)
    */
    double pdecr;
    /**
    * @brief Factor increasing the phyllochron for leaf number higher than Lincr (-)
    */
    double pincr;
    /**
    * @brief Exctinction Coefficient (-)
    */
    double kl;
    /**
    * @brief Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient (°C d leaf-1)
    */
    double pTQhf;
    /**
    * @brief Phyllochron at PTQ equal 1 (°C d leaf-1)
    */
    double B;
    /**
    * @brief Phyllochron (Varietal parameter) (°C d leaf-1)
    */
    double p;
    /**
    * @brief Switch to choose the type of phyllochron calculation to be used (-)
    */
    string choosePhyllUse;
    /**
    * @brief  Area Leaf (cm2)
    */
    double areaSL;
    /**
    * @brief Area Sheath (cm2)
    */
    double areaSS;
    /**
    * @brief LAR minimum (leaf-1 °C)
    */
    double lARmin;
    /**
    * @brief LAR maximum (leaf-1 °C)
    */
    double lARmax;
    /**
    * @brief Sowing Density (plant m-2)
    */
    double sowingDensity;
    /**
    * @brief Leaf Number efficace (leaf)
    */
    double lNeff;
};
}
}
DECLARE_DYNAMICS(record::Phenology::Phyllochron); // balise specifique VLE
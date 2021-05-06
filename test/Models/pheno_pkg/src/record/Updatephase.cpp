// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Updatephase: public DiscreteTimeDyn {
public:
    Updatephase(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        isVernalizable = (events.exist("isVernalizable")) ? vv::toInteger(events.get("isVernalizable")) : 1;
        dse = (events.exist("dse")) ? vv::toDouble(events.get("dse")) : 105;
        pFLLAnth = (events.exist("pFLLAnth")) ? vv::toDouble(events.get("pFLLAnth")) : 2.22;
        dcd = (events.exist("dcd")) ? vv::toDouble(events.get("dcd")) : 100;
        dgf = (events.exist("dgf")) ? vv::toDouble(events.get("dgf")) : 450;
        degfm = (events.exist("degfm")) ? vv::toDouble(events.get("degfm")) : 0;
        maxDL = (events.exist("maxDL")) ? vv::toDouble(events.get("maxDL")) : 15;
        sLDL = (events.exist("sLDL")) ? vv::toDouble(events.get("sLDL")) : 0.85;
        ignoreGrainMaturation = (events.exist("ignoreGrainMaturation")) ? vv::toBoolean(events.get("ignoreGrainMaturation")) : FALSE;
        pHEADANTH = (events.exist("pHEADANTH")) ? vv::toDouble(events.get("pHEADANTH")) : 1;
        choosePhyllUse = (events.exist("choosePhyllUse")) ? vv::toString(events.get("choosePhyllUse")) : Default;
        p = (events.exist("p")) ? vv::toDouble(events.get("p")) : 120;
        //  Variables gérées par ce composant
        finalLeafNumber.init(this,"finalLeafNumber", events);
        phase.init(this,"phase", events);
        hasLastPrimordiumAppeared.init(this,"hasLastPrimordiumAppeared", events);
        //  Variables gérées par un autre composant
        leafNumber.init(this,"leafNumber", events);
        isMomentRegistredZC_39.init(this,"isMomentRegistredZC_39", events);
        vernaprog.init(this,"vernaprog", events);
        minFinalNumber.init(this,"minFinalNumber", events);
        phyllochron.init(this,"phyllochron", events);
        cumulTT.init(this,"cumulTT", events);
        cumulTTFromZC_39.init(this,"cumulTTFromZC_39", events);
        gAI.init(this,"gAI", events);
        grainCumulTT.init(this,"grainCumulTT", events);
        dayLength.init(this,"dayLength", events);
        fixPhyll.init(this,"fixPhyll", events);
        cumulTTFromZC_91.init(this,"cumulTTFromZC_91", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Updatephase() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        double ttFromLastLeafToHeading;
        double appFLN;
        double localDegfm;
        double ttFromLastLeafToAnthesis;
        hasLastPrimordiumAppeared = hasLastPrimordiumAppeared(-1);
        finalLeafNumber = finalLeafNumber(-1);
        phase = phase(-1);
        if (phase(-1) >= 0.0d && phase(-1) < 1.0d)
        {
            if (cumulTT() >= dse)
            {
                phase = 1.0d;
            }
            else
            {
                phase = phase(-1);
            }
        }
        else if ( phase(-1) >= 1.0d && phase(-1) < 2.0d)
        {
            if (isVernalizable == 1 && vernaprog() >= 1.0d || isVernalizable == 0)
            {
                if (dayLength() > maxDL)
                {
                    finalLeafNumber = minFinalNumber();
                    hasLastPrimordiumAppeared = 1;
                }
                else
                {
                    appFLN = minFinalNumber() + (sLDL * (maxDL - dayLength()));
                    if (appFLN / 2.0d <= leafNumber(-1))
                    {
                        finalLeafNumber = appFLN;
                        hasLastPrimordiumAppeared = 1;
                    }
                    else
                    {
                        phase = phase(-1);
                    }
                }
                if (hasLastPrimordiumAppeared() == 1)
                {
                    phase = 2.0d;
                }
            }
            else
            {
                phase = phase(-1);
            }
        }
        else if ( phase(-1) >= 2.0d && phase(-1) < 4.0d)
        {
            if (isMomentRegistredZC_39() == 1)
            {
                if (phase(-1) < 3.0d)
                {
                    ttFromLastLeafToHeading = 0.0d;
                    if (choosePhyllUse == "Default")
                    {
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * fixPhyll();
                    }
                    else if ( choosePhyllUse == "PTQ")
                    {
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron();
                    }
                    else if ( choosePhyllUse == "Test")
                    {
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p;
                    }
                    if (cumulTTFromZC_39() >= ttFromLastLeafToHeading)
                    {
                        phase = 3.0d;
                    }
                    else
                    {
                        phase = phase(-1);
                    }
                }
                else
                {
                    phase = phase(-1);
                }
                ttFromLastLeafToAnthesis = 0.0d;
                if (choosePhyllUse == "Default")
                {
                    ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll();
                }
                else if ( choosePhyllUse == "PTQ")
                {
                    ttFromLastLeafToAnthesis = pFLLAnth * phyllochron();
                }
                else if ( choosePhyllUse == "Test")
                {
                    ttFromLastLeafToAnthesis = pFLLAnth * p;
                }
                if (cumulTTFromZC_39() >= ttFromLastLeafToAnthesis)
                {
                    phase = 4.0d;
                }
            }
            else
            {
                phase = phase(-1);
            }
        }
        else if ( phase(-1) == 4.0d)
        {
            if (grainCumulTT() >= dcd)
            {
                phase = 4.5d;
            }
            else
            {
                phase = phase(-1);
            }
        }
        else if ( phase(-1) == 4.5d)
        {
            if (grainCumulTT() >= dgf || gAI() <= 0.0d)
            {
                phase = 5.0d;
            }
            else
            {
                phase = phase(-1);
            }
        }
        else if ( phase(-1) >= 5.0d && phase(-1) < 6.0d)
        {
            localDegfm = degfm;
            if (ignoreGrainMaturation)
            {
                localDegfm = -1.0d;
            }
            if (cumulTTFromZC_91() >= localDegfm)
            {
                phase = 6.0d;
            }
            else
            {
                phase = phase(-1);
            }
        }
        else if ( phase(-1) >= 6.0d && phase(-1) < 7.0d)
        {
            phase = phase(-1);
        }
    }
private:
    //Variables d'etat
    /**
    * @brief final leaf number (leaf)
    */
    Var finalLeafNumber/**
    * @brief the name of the phase ()
    */
    Var phase/**
    * @brief if Last Primordium has Appeared ()
    */
    Var hasLastPrimordiumAppeared

    //Entrées
    /**
        * @brief Actual number of phytomers (leaf)
        */
    Var leafNumber/**
        * @brief true if ZC_39 is registered in the calendar ()
        */
    Var isMomentRegistredZC_39/**
        * @brief progression on a 0  to 1 scale of the vernalization ()
        */
    Var vernaprog/**
        * @brief minimum final leaf number (leaf)
        */
    Var minFinalNumber/**
        * @brief Phyllochron (°C d leaf-1)
        */
    Var phyllochron/**
        * @brief cumul thermal times at current date (°C d)
        */
    Var cumulTT/**
        * @brief cumul of the thermal time ( DeltaTT) since the moment ZC_39 (°C d-1)
        */
    Var cumulTTFromZC_39/**
        * @brief used to calculate Terminal spikelet ()
        */
    Var gAI/**
        * @brief cumulTT used for the grain developpment (°C d)
        */
    Var grainCumulTT/**
        * @brief length of the day (h)
        */
    Var dayLength/**
        * @brief Phyllochron with sowing date fix (°C d)
        */
    Var fixPhyll/**
        * @brief cumul of the thermal time (DeltaTT) since the moment ZC_91 (°C d-1)
        */
    Var cumulTTFromZC_91

    //Paramètres du modele
    /**
    * @brief true if the plant is vernalizable ()
    */
    int isVernalizable;
    /**
    * @brief Thermal time from sowing to emergence (°C d)
    */
    double dse;
    /**
    * @brief Phyllochronic duration of the period between flag leaf ligule appearance and anthesis ()
    */
    double pFLLAnth;
    /**
    * @brief Duration of the endosperm cell division phase (°C d)
    */
    double dcd;
    /**
    * @brief Grain filling duration (from anthesis to physiological maturity) (°C d)
    */
    double dgf;
    /**
    * @brief Grain maturation duration (from physiological maturity to harvest ripeness) (°C d)
    */
    double degfm;
    /**
    * @brief Saturating photoperiod above which final leaf number is not influenced by daylength (h)
    */
    double maxDL;
    /**
    * @brief Daylength response of leaf production (leaf h-1)
    */
    double sLDL;
    /**
    * @brief true to ignore grain maturation ()
    */
    bool ignoreGrainMaturation;
    /**
    * @brief Number of phyllochron between heading and anthesiss ()
    */
    double pHEADANTH;
    /**
    * @brief Switch to choose the type of phyllochron calculation to be used ()
    */
    string choosePhyllUse;
    /**
    * @brief Phyllochron (Varietal parameter) (°C d leaf-1)
    */
    double p;
};
}
}
DECLARE_DYNAMICS(record::Phenology::Updatephase); // balise specifique VLE
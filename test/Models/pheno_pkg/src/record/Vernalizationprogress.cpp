// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
namespace Phenology {
using namespace vle::discrete_time;
class Vernalizationprogress: public DiscreteTimeDyn {
public:
    Vernalizationprogress(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie
        minTvern = (events.exist("minTvern")) ? vv::toDouble(events.get("minTvern")) : 0.0;
        intTvern = (events.exist("intTvern")) ? vv::toDouble(events.get("intTvern")) :  11.0;
        vAI = (events.exist("vAI")) ? vv::toDouble(events.get("vAI")) :  0.015;
        vBEE = (events.exist("vBEE")) ? vv::toDouble(events.get("vBEE")) : 0.01;
        minDL = (events.exist("minDL")) ? vv::toDouble(events.get("minDL")) : 8.0;
        maxDL = (events.exist("maxDL")) ? vv::toDouble(events.get("maxDL")) : 15.0;
        maxTvern = (events.exist("maxTvern")) ? vv::toDouble(events.get("maxTvern")) :  23.0;
        pNini = (events.exist("pNini")) ? vv::toDouble(events.get("pNini")) : 4.0;
        aMXLFNO = (events.exist("aMXLFNO")) ? vv::toDouble(events.get("aMXLFNO")) : 24.0;
        isVernalizable = (events.exist("isVernalizable")) ? vv::toInteger(events.get("isVernalizable")) : 1;
        //  Variables gérées par ce composant
        vernaprog.init(this,"vernaprog", events);
        minFinalNumber.init(this,"minFinalNumber", events);
        calendarMoments.init(this,"calendarMoments", events);
        calendarDates.init(this,"calendarDates", events);
        calendarCumuls.init(this,"calendarCumuls", events);
        //  Variables gérées par un autre composant
        leafNumber.init(this,"leafNumber", events);
        dayLength.init(this,"dayLength", events);
        deltaTT.init(this,"deltaTT", events);
        cumulTT.init(this,"cumulTT", events);
        currentdate.init(this,"currentdate", events);
    }
    /**
    * @brief Destructeur de la classe du modèle.
    **/
    virtual ~Vernalizationprogress() {};
    /**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */
    virtual void compute(const vd::Time& /*time*/)
    {
        double maxVernaProg;
        double dLverna;
        double primordno;
        double minLeafNumber;
        double potlfno;
        double tt;
        calendarMoments = calendarMoments_t1;
        calendarCumuls = calendarCumuls_t1;
        calendarDates = calendarDates_t1;
        minFinalNumber = minFinalNumber(-1);
        vernaprog = vernaprog(-1);
        if (isVernalizable == 1 && vernaprog(-1) < 1.0d)
        {
            tt = deltaTT();
            if (tt >= minTvern && tt <= intTvern)
            {
                vernaprog = vernaprog(-1) + (vAI * tt) + vBEE;
            }
            else
            {
                vernaprog = vernaprog(-1);
            }
            if (tt > intTvern)
            {
                maxVernaProg = vAI * intTvern + vBEE;
                dLverna = max(minDL, min(maxDL, dayLength()));
                vernaprog = vernaprog() + max(0.0d, maxVernaProg * (1.0d + ((intTvern - tt) / (maxTvern - intTvern) * ((dLverna - minDL) / (maxDL - minDL)))));
            }
            primordno = 2.0d * leafNumber(-1) + pNini;
            minLeafNumber = minFinalNumber(-1);
            if (vernaprog() >= 1.0d || primordno >= aMXLFNO)
            {
                minFinalNumber = max(primordno, minFinalNumber(-1));
                calendarMoments().push_back("EndVernalisation");
                calendarCumuls().push_back(cumulTT());
                calendarDates().push_back(currentdate());
                vernaprog = max(1.0d, vernaprog());
            }
            else
            {
                potlfno = aMXLFNO - ((aMXLFNO - minLeafNumber) * vernaprog());
                if (primordno >= potlfno)
                {
                    minFinalNumber = max((potlfno + primordno) / 2.0d, minFinalNumber(-1));
                    vernaprog = max(1.0d, vernaprog());
                    calendarMoments().push_back("EndVernalisation");
                    calendarCumuls().push_back(cumulTT());
                    calendarDates().push_back(currentdate());
                }
            }
        }
    }
private:
    //Variables d'etat
    /**
    * @brief progression on a 0  to 1 scale of the vernalization ()
    */
    Var vernaprog/**
    * @brief minimum final leaf number (leaf)
    */
    Var minFinalNumber/**
    * @brief List containing appearance of each stage ()
    */
    Vect calendarMoments/**
    * @brief List containing  the dates of the wheat developmental phases ()
    */
    Vect calendarDates/**
    * @brief list containing for each stage occured its cumulated thermal times ()
    */
    Vect calendarCumuls

    //Entrées
    /**
        * @brief Actual number of phytomers (leaf)
        */
    Var leafNumber/**
        * @brief day length (mm2 m-2)
        */
    Var dayLength/**
        * @brief difference cumul TT between j and j-1 day  (°C d)
        */
    Var deltaTT/**
        * @brief cumul thermal times at currentdate (°C d)
        */
    Var cumulTT/**
        * @brief current date  ()
        */
    Var currentdate

    //Paramètres du modele
    /**
    * @brief Minimum temperature for vernalization to occur (°C)
    */
    double minTvern;
    /**
    * @brief Intermediate temperature for vernalization to occur (°C)
    */
    double intTvern;
    /**
    * @brief Response of vernalization rate to temperature (d-1 °C-1)
    */
    double vAI;
    /**
    * @brief Vernalization rate at 0°C (d-1)
    */
    double vBEE;
    /**
    * @brief Threshold daylength below which it does influence vernalization rate (h)
    */
    double minDL;
    /**
    * @brief Saturating photoperiod above which final leaf number is not influenced by daylength (h)
    */
    double maxDL;
    /**
    * @brief Maximum temperature for vernalization to occur (°C)
    */
    double maxTvern;
    /**
    * @brief Number of primorida in the apex at emergence (primordia)
    */
    double pNini;
    /**
    * @brief Absolute maximum leaf number (leaf)
    */
    double aMXLFNO;
    /**
    * @brief true if the plant is vernalizable ()
    */
    int isVernalizable;
};
}
}
DECLARE_DYNAMICS(record::Phenology::Vernalizationprogress); // balise specifique VLE
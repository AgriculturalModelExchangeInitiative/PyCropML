import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import javafx.util.*;
import java.time.LocalDateTime;
import java.time.LocalDateTime;
import net.simplace.sim.model.FWSimComponent;
import net.simplace.sim.util.FWSimVarMap;
import net.simplace.sim.util.FWSimVariable;
import net.simplace.sim.util.FWSimVariable.CONTENT_TYPE;
import net.simplace.sim.util.FWSimVariable.DATA_TYPE;
import org.jdom.Element;


public class Updatephase extends FWSimComponent
{
    private FWSimVariable<Integer> isVernalizable;
    private FWSimVariable<Double> dse;
    private FWSimVariable<Double> pFLLAnth;
    private FWSimVariable<Double> dcd;
    private FWSimVariable<Double> dgf;
    private FWSimVariable<Double> degfm;
    private FWSimVariable<Double> maxDL;
    private FWSimVariable<Double> sLDL;
    private FWSimVariable<Boolean> ignoreGrainMaturation;
    private FWSimVariable<Double> pHEADANTH;
    private FWSimVariable<String> choosePhyllUse;
    private FWSimVariable<Double> p;
    private FWSimVariable<Double> cumulTT;
    private FWSimVariable<Double> cumulTTFromZC_39;
    private FWSimVariable<Double> gAI;
    private FWSimVariable<Double> grainCumulTT;
    private FWSimVariable<Double> dayLength;
    private FWSimVariable<Double> fixPhyll;
    private FWSimVariable<Double> cumulTTFromZC_91;
    private FWSimVariable<Double> leafNumber_t1;
    private FWSimVariable<Integer> isMomentRegistredZC_39;
    private FWSimVariable<Double> vernaprog;
    private FWSimVariable<Double> minFinalNumber;
    private FWSimVariable<Double> phase_t1;
    private FWSimVariable<Double> phyllochron;
    private FWSimVariable<Integer> hasLastPrimordiumAppeared_t1;
    private FWSimVariable<Double> finalLeafNumber_t1;
    private FWSimVariable<Double> finalLeafNumber;
    private FWSimVariable<Double> phase;
    private FWSimVariable<Integer> hasLastPrimordiumAppeared;

    public Updatephase(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Updatephase(){
        super();
    }
    @Override
    protected void process()
    {
        double tcumulTT = cumulTT.getValue();
        double tleafNumber_t1 = leafNumber_t1.getValue();
        double tcumulTTFromZC_39 = cumulTTFromZC_39.getValue();
        int tisMomentRegistredZC_39 = isMomentRegistredZC_39.getValue();
        double tgAI = gAI.getValue();
        double tgrainCumulTT = grainCumulTT.getValue();
        double tdayLength = dayLength.getValue();
        double tvernaprog = vernaprog.getValue();
        double tminFinalNumber = minFinalNumber.getValue();
        double tfixPhyll = fixPhyll.getValue();
        int tisVernalizable = isVernalizable.getValue();
        double tdse = dse.getValue();
        double tpFLLAnth = pFLLAnth.getValue();
        double tdcd = dcd.getValue();
        double tdgf = dgf.getValue();
        double tdegfm = degfm.getValue();
        double tmaxDL = maxDL.getValue();
        double tsLDL = sLDL.getValue();
        boolean tignoreGrainMaturation = ignoreGrainMaturation.getValue();
        double tpHEADANTH = pHEADANTH.getValue();
        String tchoosePhyllUse = choosePhyllUse.getValue();
        double tp = p.getValue();
        double tphase_t1 = phase_t1.getValue();
        double tcumulTTFromZC_91 = cumulTTFromZC_91.getValue();
        double tphyllochron = phyllochron.getValue();
        int thasLastPrimordiumAppeared_t1 = hasLastPrimordiumAppeared_t1.getValue();
        double tfinalLeafNumber_t1 = finalLeafNumber_t1.getValue();
        double tfinalLeafNumber;
        double tphase;
        int thasLastPrimordiumAppeared;
        double ttFromLastLeafToHeading;
        double appFLN;
        double localDegfm;
        double ttFromLastLeafToAnthesis;
        thasLastPrimordiumAppeared = thasLastPrimordiumAppeared_t1;
        tfinalLeafNumber = tfinalLeafNumber_t1;
        tphase = tphase_t1;
        if (tphase_t1 >= 0.0d && tphase_t1 < 1.0d)
        {
            if (tcumulTT >= tdse)
            {
                tphase = 1.0d;
            }
            else
            {
                tphase = tphase_t1;
            }
        }
        else if ( tphase_t1 >= 1.0d && tphase_t1 < 2.0d)
        {
            if (tisVernalizable == 1 && tvernaprog >= 1.0d || tisVernalizable == 0)
            {
                if (tdayLength > tmaxDL)
                {
                    tfinalLeafNumber = tminFinalNumber;
                    thasLastPrimordiumAppeared = 1;
                }
                else
                {
                    appFLN = tminFinalNumber + (tsLDL * (tmaxDL - tdayLength));
                    if (appFLN / 2.0d <= tleafNumber_t1)
                    {
                        tfinalLeafNumber = appFLN;
                        thasLastPrimordiumAppeared = 1;
                    }
                    else
                    {
                        tphase = tphase_t1;
                    }
                }
                if (thasLastPrimordiumAppeared == 1)
                {
                    tphase = 2.0d;
                }
            }
            else
            {
                tphase = tphase_t1;
            }
        }
        else if ( tphase_t1 >= 2.0d && tphase_t1 < 4.0d)
        {
            if (tisMomentRegistredZC_39 == 1)
            {
                if (tphase_t1 < 3.0d)
                {
                    ttFromLastLeafToHeading = 0.0d;
                    if (tchoosePhyllUse == "Default")
                    {
                        ttFromLastLeafToHeading = (tpFLLAnth - tpHEADANTH) * tfixPhyll;
                    }
                    else if ( tchoosePhyllUse == "PTQ")
                    {
                        ttFromLastLeafToHeading = (tpFLLAnth - tpHEADANTH) * tphyllochron;
                    }
                    else if ( tchoosePhyllUse == "Test")
                    {
                        ttFromLastLeafToHeading = (tpFLLAnth - tpHEADANTH) * tp;
                    }
                    if (tcumulTTFromZC_39 >= ttFromLastLeafToHeading)
                    {
                        tphase = 3.0d;
                    }
                    else
                    {
                        tphase = tphase_t1;
                    }
                }
                else
                {
                    tphase = tphase_t1;
                }
                ttFromLastLeafToAnthesis = 0.0d;
                if (tchoosePhyllUse == "Default")
                {
                    ttFromLastLeafToAnthesis = tpFLLAnth * tfixPhyll;
                }
                else if ( tchoosePhyllUse == "PTQ")
                {
                    ttFromLastLeafToAnthesis = tpFLLAnth * tphyllochron;
                }
                else if ( tchoosePhyllUse == "Test")
                {
                    ttFromLastLeafToAnthesis = tpFLLAnth * tp;
                }
                if (tcumulTTFromZC_39 >= ttFromLastLeafToAnthesis)
                {
                    tphase = 4.0d;
                }
            }
            else
            {
                tphase = tphase_t1;
            }
        }
        else if ( tphase_t1 == 4.0d)
        {
            if (tgrainCumulTT >= tdcd)
            {
                tphase = 4.5d;
            }
            else
            {
                tphase = tphase_t1;
            }
        }
        else if ( tphase_t1 == 4.5d)
        {
            if (tgrainCumulTT >= tdgf || tgAI <= 0.0d)
            {
                tphase = 5.0d;
            }
            else
            {
                tphase = tphase_t1;
            }
        }
        else if ( tphase_t1 >= 5.0d && tphase_t1 < 6.0d)
        {
            localDegfm = tdegfm;
            if (tignoreGrainMaturation)
            {
                localDegfm = -1.0d;
            }
            if (tcumulTTFromZC_91 >= localDegfm)
            {
                tphase = 6.0d;
            }
            else
            {
                tphase = tphase_t1;
            }
        }
        else if ( tphase_t1 >= 6.0d && tphase_t1 < 7.0d)
        {
            tphase = tphase_t1;
        }
        finalLeafNumber.setValue(tfinalLeafNumber, this);
        phase.setValue(tphase, this);
        hasLastPrimordiumAppeared.setValue(thasLastPrimordiumAppeared, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Updatephase(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("cisVernalizable", "true if the plant is vernalizable", DATA_TYPE.INT, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 1, this));
        addVariable(FWSimVariable.createSimVariable("cdse", "Thermal time from sowing to emergence", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 105, this));
        addVariable(FWSimVariable.createSimVariable("cpFLLAnth", "Phyllochronic duration of the period between flag leaf ligule appearance and anthesis", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 2.22, this));
        addVariable(FWSimVariable.createSimVariable("cdcd", "Duration of the endosperm cell division phase", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 100, this));
        addVariable(FWSimVariable.createSimVariable("cdgf", "Grain filling duration (from anthesis to physiological maturity)", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 450, this));
        addVariable(FWSimVariable.createSimVariable("cdegfm", "Grain maturation duration (from physiological maturity to harvest ripeness)", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 50, 0, this));
        addVariable(FWSimVariable.createSimVariable("cmaxDL", "Saturating photoperiod above which final leaf number is not influenced by daylength", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 24, 15, this));
        addVariable(FWSimVariable.createSimVariable("csLDL", "Daylength response of leaf production", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.85, this));
        addVariable(FWSimVariable.createSimVariable("cignoreGrainMaturation", "true to ignore grain maturation", DATA_TYPE.BOOLEAN, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, false, this));
        addVariable(FWSimVariable.createSimVariable("cpHEADANTH", "Number of phyllochron between heading and anthesiss", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 1, this));
        addVariable(FWSimVariable.createSimVariable("cchoosePhyllUse", "Switch to choose the type of phyllochron calculation to be used", DATA_TYPE.CHAR, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, "Default", this));
        addVariable(FWSimVariable.createSimVariable("cp", "Phyllochron (Varietal parameter)", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 120, this));
        addVariable(FWSimVariable.createSimVariable("icumulTT", "cumul thermal times at current date", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -200, 10000, 354.582294511779, this));
        addVariable(FWSimVariable.createSimVariable("icumulTTFromZC_39", "cumul of the thermal time ( DeltaTT) since the moment ZC_39", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 0, this));
        addVariable(FWSimVariable.createSimVariable("igAI", "used to calculate Terminal spikelet", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 0.3255196285135, this));
        addVariable(FWSimVariable.createSimVariable("igrainCumulTT", "cumulTT used for the grain developpment", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 0, this));
        addVariable(FWSimVariable.createSimVariable("idayLength", "length of the day", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 24, 12.7433275303389, this));
        addVariable(FWSimVariable.createSimVariable("ifixPhyll", "Phyllochron with sowing date fix", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 91.2, this));
        addVariable(FWSimVariable.createSimVariable("icumulTTFromZC_91", "cumul of the thermal time (DeltaTT) since the moment ZC_91", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, 0, this));
        addVariable(FWSimVariable.createSimVariable("sleafNumber", "Actual number of phytomers", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 25,  4.620511621863958, this));
        addVariable(FWSimVariable.createSimVariable("sisMomentRegistredZC_39", "true if ZC_39 is registered in the calendar", DATA_TYPE.INT, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0, this));
        addVariable(FWSimVariable.createSimVariable("svernaprog", "progression on a 0  to 1 scale of the vernalization", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10,  1.0532526829571554, this));
        addVariable(FWSimVariable.createSimVariable("sminFinalNumber", "minimum final leaf number", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 25, 6.879410413987549, this));
        addVariable(FWSimVariable.createSimVariable("sphase", " the name of the phase", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 7, 1, this));
        addVariable(FWSimVariable.createSimVariable("sphyllochron", "Phyllochron", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 91.2, this));
        addVariable(FWSimVariable.createSimVariable("shasLastPrimordiumAppeared", "if Last Primordium has Appeared", DATA_TYPE.INT, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0, this));
        addVariable(FWSimVariable.createSimVariable("sfinalLeafNumber", "final leaf number", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 25, 0, this));

        return iFieldMap;
    }
}
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


public class Phyllochron extends FWSimComponent
{
    private FWSimVariable<Double> lincr;
    private FWSimVariable<Double> ldecr;
    private FWSimVariable<Double> pdecr;
    private FWSimVariable<Double> pincr;
    private FWSimVariable<Double> kl;
    private FWSimVariable<Double> pTQhf;
    private FWSimVariable<Double> B;
    private FWSimVariable<Double> p;
    private FWSimVariable<String> choosePhyllUse;
    private FWSimVariable<Double> areaSL;
    private FWSimVariable<Double> areaSS;
    private FWSimVariable<Double> lARmin;
    private FWSimVariable<Double> lARmax;
    private FWSimVariable<Double> sowingDensity;
    private FWSimVariable<Double> lNeff;
    private FWSimVariable<Double> fixPhyll;
    private FWSimVariable<Double> leafNumber;
    private FWSimVariable<Double> ptq;
    private FWSimVariable<Double> gAImean;
    private FWSimVariable<Double> phyllochron;

    public Phyllochron(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Phyllochron(){
        super();
    }
    @Override
    protected void process()
    {
        double tfixPhyll = fixPhyll.getValue();
        double tleafNumber = leafNumber.getValue();
        double tlincr = lincr.getValue();
        double tldecr = ldecr.getValue();
        double tpdecr = pdecr.getValue();
        double tpincr = pincr.getValue();
        double tptq = ptq.getValue();
        double tgAImean = gAImean.getValue();
        double tkl = kl.getValue();
        double tpTQhf = pTQhf.getValue();
        double tB = B.getValue();
        double tp = p.getValue();
        String tchoosePhyllUse = choosePhyllUse.getValue();
        double tareaSL = areaSL.getValue();
        double tareaSS = areaSS.getValue();
        double tlARmin = lARmin.getValue();
        double tlARmax = lARmax.getValue();
        double tsowingDensity = sowingDensity.getValue();
        double tlNeff = lNeff.getValue();
        double tphyllochron;
        double gaiLim;
        double LAR;
        tphyllochron = 0.0d;
        LAR = 0.0d;
        gaiLim = tlNeff * ((tareaSL + tareaSS) / 10000.0d) * tsowingDensity;
        if (tchoosePhyllUse == "Default")
        {
            if (tleafNumber < tldecr)
            {
                tphyllochron = tfixPhyll * tpdecr;
            }
            else if ( tleafNumber >= tldecr && tleafNumber < tlincr)
            {
                tphyllochron = tfixPhyll;
            }
            else
            {
                tphyllochron = tfixPhyll * tpincr;
            }
        }
        if (tchoosePhyllUse == "PTQ")
        {
            if (tgAImean > gaiLim)
            {
                LAR = (tlARmin + ((tlARmax - tlARmin) * tptq / (tpTQhf + tptq))) / (tB * tgAImean);
            }
            else
            {
                LAR = (tlARmin + ((tlARmax - tlARmin) * tptq / (tpTQhf + tptq))) / (tB * gaiLim);
            }
            tphyllochron = 1.0d / LAR;
        }
        if (tchoosePhyllUse == "Test")
        {
            if (tleafNumber < tldecr)
            {
                tphyllochron = tp * tpdecr;
            }
            else if ( tleafNumber >= tldecr && tleafNumber < tlincr)
            {
                tphyllochron = tp;
            }
            else
            {
                tphyllochron = tp * tpincr;
            }
        }
        phyllochron.setValue(tphyllochron, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Phyllochron(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("clincr", "Leaf number above which the phyllochron is increased by Pincr", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 30.0, 8.0, this));
        addVariable(FWSimVariable.createSimVariable("cldecr", "Leaf number up to which the phyllochron is decreased by Pdecr", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 100.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("cpdecr", "Factor decreasing the phyllochron for leaf number less than Ldecr", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 10.0, 0.4, this));
        addVariable(FWSimVariable.createSimVariable("cpincr", "Factor increasing the phyllochron for leaf number higher than Lincr", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 10.0, 1.5, this));
        addVariable(FWSimVariable.createSimVariable("ckl", "Exctinction Coefficient", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 50.0, 0.45, this));
        addVariable(FWSimVariable.createSimVariable("cpTQhf", "Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 1000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("cB", "Phyllochron at PTQ equal 1", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 1000.0, 20.0, this));
        addVariable(FWSimVariable.createSimVariable("cp", "Phyllochron (Varietal parameter)", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 1000.0, 120.0, this));
        addVariable(FWSimVariable.createSimVariable("cchoosePhyllUse", "Switch to choose the type of phyllochron calculation to be used", DATA_TYPE.CHAR, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, "Default", this));
        addVariable(FWSimVariable.createSimVariable("careaSL", " Area Leaf", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 1000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("careaSS", "Area Sheath", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 1000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("clARmin", "LAR minimum", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 1000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("clARmax", "LAR maximum", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 1000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("csowingDensity", "Sowing Density", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 1000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("clNeff", "Leaf Number efficace", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 1000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("ifixPhyll", "Sowing date corrected Phyllochron", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 10000.0, 5.0, this));
        addVariable(FWSimVariable.createSimVariable("sleafNumber", "Actual number of phytomers", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 25.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("sptq", "Photothermal quotient ", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 10000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("sgAImean", "Green Area Index", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 10000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("sphyllochron", " the rate of leaf appearance ", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, null, this));

        return iFieldMap;
    }
}
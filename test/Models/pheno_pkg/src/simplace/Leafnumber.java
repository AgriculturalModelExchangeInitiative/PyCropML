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


public class Leafnumber extends FWSimComponent
{
    private FWSimVariable<Double> deltaTT;
    private FWSimVariable<Double> phyllochron_t1;
    private FWSimVariable<Integer> hasFlagLeafLiguleAppeared;
    private FWSimVariable<Double> leafNumber_t1;
    private FWSimVariable<Double> phase;
    private FWSimVariable<Double> leafNumber;

    public Leafnumber(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Leafnumber(){
        super();
    }
    @Override
    protected void process()
    {
        double tdeltaTT = deltaTT.getValue();
        double tphyllochron_t1 = phyllochron_t1.getValue();
        int thasFlagLeafLiguleAppeared = hasFlagLeafLiguleAppeared.getValue();
        double tleafNumber_t1 = leafNumber_t1.getValue();
        double tphase = phase.getValue();
        double tleafNumber;
        tleafNumber = tleafNumber_t1;
        double phyllochron_;
        if (tphase >= 1.0d && tphase < 4.0d)
        {
            if (thasFlagLeafLiguleAppeared == 0)
            {
                if (tphyllochron_t1 == 0.0d)
                {
                    phyllochron_ = 0.0000001d;
                }
                else
                {
                    phyllochron_ = tphyllochron_t1;
                }
                tleafNumber = tleafNumber_t1 + Math.min(tdeltaTT / phyllochron_, 0.999d);
            }
        }
        leafNumber.setValue(tleafNumber, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Leafnumber(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("ideltaTT", "daily delta TT ", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -20, 100, 23.5895677277199, this));
        addVariable(FWSimVariable.createSimVariable("sphyllochron", "phyllochron", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 0, this));
        addVariable(FWSimVariable.createSimVariable("shasFlagLeafLiguleAppeared", "true if flag leaf has appeared (leafnumber reached finalLeafNumber)", DATA_TYPE.INT, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0, this));
        addVariable(FWSimVariable.createSimVariable("sleafNumber", " Actual number of phytomers", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 25, 0, this));
        addVariable(FWSimVariable.createSimVariable("sphase", " the name of the phase", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 7, 1, this));

        return iFieldMap;
    }
}
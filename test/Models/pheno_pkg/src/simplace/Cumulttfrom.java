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


public class Cumulttfrom extends FWSimComponent
{
    private FWSimVariable<Double> cumulTT;
    private FWSimVariable<Double> cumulTTFromZC_65;
    private FWSimVariable<Double> cumulTTFromZC_39;
    private FWSimVariable<Double> cumulTTFromZC_91;
    private FWSimVariable<String[]> calendarMoments_t1;
    private FWSimVariable<Double[]> calendarCumuls_t1;

    public Cumulttfrom(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Cumulttfrom(){
        super();
    }
    @Override
    protected void process()
    {
        List<String> tcalendarMoments_t1 = Arrays.asList(calendarMoments_t1.getValue());
        List<Double> tcalendarCumuls_t1 = Arrays.asList(calendarCumuls_t1.getValue());
        double tcumulTT = cumulTT.getValue();
        double tcumulTTFromZC_65;
        double tcumulTTFromZC_39;
        double tcumulTTFromZC_91;
        tcumulTTFromZC_65 = 0.0d;
        tcumulTTFromZC_39 = 0.0d;
        tcumulTTFromZC_91 = 0.0d;
        if (tcalendarMoments_t1.contains("Anthesis"))
        {
            tcumulTTFromZC_65 = tcumulTT - tcalendarCumuls_t1.get(tcalendarMoments_t1.indexOf("Anthesis"));
        }
        if (tcalendarMoments_t1.contains("FlagLeafLiguleJustVisible"))
        {
            tcumulTTFromZC_39 = tcumulTT - tcalendarCumuls_t1.get(tcalendarMoments_t1.indexOf("FlagLeafLiguleJustVisible"));
        }
        if (tcalendarMoments_t1.contains("EndGrainFilling"))
        {
            tcumulTTFromZC_91 = tcumulTT - tcalendarCumuls_t1.get(tcalendarMoments_t1.indexOf("EndGrainFilling"));
        }
        cumulTTFromZC_65.setValue(tcumulTTFromZC_65, this);
        cumulTTFromZC_39.setValue(tcumulTTFromZC_39, this);
        cumulTTFromZC_91.setValue(tcumulTTFromZC_91, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Cumulttfrom(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("icumulTT", "cumul TT at current date", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -200, 10000, 8.0, this));
        addVariable(FWSimVariable.createSimVariable("cumulTTFromZC_65", " cumul TT from Anthesis to current date ", DATA_TYPE.DOUBLE, CONTENT_TYPE.out,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, null, this));
        addVariable(FWSimVariable.createSimVariable("cumulTTFromZC_39", " cumul TT from FlagLeafLiguleJustVisible to current date ", DATA_TYPE.DOUBLE, CONTENT_TYPE.out,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, null, this));
        addVariable(FWSimVariable.createSimVariable("cumulTTFromZC_91", " cumul TT from EndGrainFilling to current date ", DATA_TYPE.DOUBLE, CONTENT_TYPE.out,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, null, this));
        addVariable(FWSimVariable.createSimVariable("scalendarMoments", "List containing appearance of each stage at previous day", DATA_TYPE.CHARARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new String[] {"Sowing"}, this));
        addVariable(FWSimVariable.createSimVariable("scalendarCumuls", "list containing for each stage occured its cumulated thermal times at previous day", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Double[] {0.0}, this));

        return iFieldMap;
    }
}
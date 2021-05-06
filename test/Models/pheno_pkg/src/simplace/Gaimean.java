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


public class Gaimean extends FWSimComponent
{
    private FWSimVariable<Double> tTWindowForPTQ;
    private FWSimVariable<Double> gAI;
    private FWSimVariable<Double> deltaTT;
    private FWSimVariable<Double> pastMaxAI_t1;
    private FWSimVariable<Double[]> listTTShootWindowForPTQ1_t1;
    private FWSimVariable<Double[]> listGAITTWindowForPTQ_t1;
    private FWSimVariable<Double> gAImean;
    private FWSimVariable<Double> pastMaxAI;
    private FWSimVariable<Double[]> listTTShootWindowForPTQ1;
    private FWSimVariable<Double[]> listGAITTWindowForPTQ;

    public Gaimean(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Gaimean(){
        super();
    }
    @Override
    protected void process()
    {
        double tgAI = gAI.getValue();
        double ttTWindowForPTQ = tTWindowForPTQ.getValue();
        double tdeltaTT = deltaTT.getValue();
        double tpastMaxAI_t1 = pastMaxAI_t1.getValue();
        List<Double> tlistTTShootWindowForPTQ1_t1 = Arrays.asList(listTTShootWindowForPTQ1_t1.getValue());
        List<Double> tlistGAITTWindowForPTQ_t1 = Arrays.asList(listGAITTWindowForPTQ_t1.getValue());
        double tgAImean;
        double tpastMaxAI;
        List<Double> tlistTTShootWindowForPTQ1;
        List<Double> tlistGAITTWindowForPTQ;
        List<Double> TTList = new ArrayList<>(Arrays.asList());
        List<Double> GAIList = new ArrayList<>(Arrays.asList());
        double SumTT;
        int count = 0;
        double gai_ = 0.0d;
        double gaiMean_ = 0.0d;
        int countGaiMean = 0;
        int i;
        for (i=0 ; i<tlistTTShootWindowForPTQ1_t1.size() ; i+=1)
        {
            TTList.add(tlistTTShootWindowForPTQ1_t1.get(i));
            GAIList.add(tlistGAITTWindowForPTQ_t1.get(i));
        }
        TTList.add(tdeltaTT);
        GAIList.add(tgAI);
        SumTT = TTList.stream().mapToDouble(Double::doubleValue).sum();
        while ( SumTT > ttTWindowForPTQ)
        {
            SumTT = SumTT - TTList.get(count);
            count = count + 1;
        }
        for (i=count ; i<TTList.size() ; i+=1)
        {
            tlistTTShootWindowForPTQ1.add(TTList.get(i));
            tlistGAITTWindowForPTQ.add(GAIList.get(i));
        }
        for (i=0 ; i<tlistGAITTWindowForPTQ.size() ; i+=1)
        {
            gaiMean_ = gaiMean_ + tlistGAITTWindowForPTQ.get(i);
            countGaiMean = countGaiMean + 1;
        }
        gaiMean_ = gaiMean_ / countGaiMean;
        gai_ = Math.max(tpastMaxAI_t1, gaiMean_);
        tpastMaxAI = gai_;
        tgAImean = gai_;
        gAImean.setValue(tgAImean, this);
        pastMaxAI.setValue(tpastMaxAI, this);
        listTTShootWindowForPTQ1.setValue(tlistTTShootWindowForPTQ1.toArray(new Double[0]), this);
        listGAITTWindowForPTQ.setValue(tlistGAITTWindowForPTQ.toArray(new Double[0]), this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Gaimean(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("ctTWindowForPTQ", "Thermal Time window for average", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 5000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("igAI", "Green Area Index of the day", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 500.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("ideltaTT", "Thermal time increase of the day", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 100.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("spastMaxAI", "Maximum Leaf Area Index reached the current day", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 5000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("slistTTShootWindowForPTQ1", "List of daily shoot thermal time in the window dedicated to average", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Double[] {0.0}, this));
        addVariable(FWSimVariable.createSimVariable("slistGAITTWindowForPTQ", "List of daily Green Area Index in the window dedicated to average", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Double[] {0.0}, this));
        addVariable(FWSimVariable.createSimVariable("sgAImean", "Mean Green Area Index", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 500.0, null, this));

        return iFieldMap;
    }
}
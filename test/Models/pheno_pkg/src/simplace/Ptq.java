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


public class Ptq extends FWSimComponent
{
    private FWSimVariable<Double> tTWindowForPTQ;
    private FWSimVariable<Double> kl;
    private FWSimVariable<Double> pAR;
    private FWSimVariable<Double> deltaTT;
    private FWSimVariable<Double[]> listTTShootWindowForPTQ_t1;
    private FWSimVariable<Double[]> listPARTTWindowForPTQ_t1;
    private FWSimVariable<Double[]> listGAITTWindowForPTQ;
    private FWSimVariable<Double[]> listPARTTWindowForPTQ;
    private FWSimVariable<Double[]> listTTShootWindowForPTQ;
    private FWSimVariable<Double> ptq;

    public Ptq(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Ptq(){
        super();
    }
    @Override
    protected void process()
    {
        double ttTWindowForPTQ = tTWindowForPTQ.getValue();
        double tkl = kl.getValue();
        List<Double> tlistTTShootWindowForPTQ_t1 = Arrays.asList(listTTShootWindowForPTQ_t1.getValue());
        List<Double> tlistPARTTWindowForPTQ_t1 = Arrays.asList(listPARTTWindowForPTQ_t1.getValue());
        List<Double> tlistGAITTWindowForPTQ = Arrays.asList(listGAITTWindowForPTQ.getValue());
        double tpAR = pAR.getValue();
        double tdeltaTT = deltaTT.getValue();
        List<Double> tlistPARTTWindowForPTQ;
        List<Double> tlistTTShootWindowForPTQ;
        double tptq;
        List<Double> TTList = new ArrayList<>(Arrays.asList());
        List<Double> PARList = new ArrayList<>(Arrays.asList());
        int i;
        int count;
        double SumTT;
        double parInt = 0.0d;
        double TTShoot;
        for (i=0 ; i<tlistTTShootWindowForPTQ_t1.size() ; i+=1)
        {
            TTList.add(tlistTTShootWindowForPTQ_t1.get(i));
            PARList.add(tlistPARTTWindowForPTQ_t1.get(i));
        }
        TTList.add(tdeltaTT);
        PARList.add(tpAR);
        SumTT = TTList.stream().mapToDouble(Double::doubleValue).sum();
        count = 0;
        while ( SumTT > ttTWindowForPTQ)
        {
            SumTT = SumTT - TTList.get(count);
            count = count + 1;
        }
        for (i=count ; i<TTList.size() ; i+=1)
        {
            tlistTTShootWindowForPTQ.add(TTList.get(i));
            tlistPARTTWindowForPTQ.add(PARList.get(i));
        }
        for (i=0 ; i<tlistTTShootWindowForPTQ.size() ; i+=1)
        {
            parInt = parInt + (tlistPARTTWindowForPTQ.get(i) * (1 - Math.exp(-tkl * tlistGAITTWindowForPTQ.get(i))));
        }
        TTShoot = tlistTTShootWindowForPTQ.stream().mapToDouble(Double::doubleValue).sum();
        tptq = parInt / TTShoot;
        listPARTTWindowForPTQ.setValue(tlistPARTTWindowForPTQ.toArray(new Double[0]), this);
        listTTShootWindowForPTQ.setValue(tlistTTShootWindowForPTQ.toArray(new Double[0]), this);
        ptq.setValue(tptq, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Ptq(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("ctTWindowForPTQ", "Thermal time window in which averages are computed", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 70000.0, 70.0, this));
        addVariable(FWSimVariable.createSimVariable("ckl", "Exctinction Coefficient", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 50.0, 0.45, this));
        addVariable(FWSimVariable.createSimVariable("ipAR", "Daily Photosyntetically Active Radiation", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 10000.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("ideltaTT", "daily delta TT ", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0.0, 100.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("slistTTShootWindowForPTQ", "List of Daily Shoot thermal time during TTWindowForPTQ thermal time period", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Double[] {0.0}, this));
        addVariable(FWSimVariable.createSimVariable("slistPARTTWindowForPTQ", "List of Daily PAR during TTWindowForPTQ thermal time period", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Double[] {0.0}, this));
        addVariable(FWSimVariable.createSimVariable("slistGAITTWindowForPTQ", "List of daily GAI over TTWindowForPTQ thermal time period", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Double[] {0.0,5.2}, this));
        addVariable(FWSimVariable.createSimVariable("sptq", "Photothermal Quotient", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, null, this));

        return iFieldMap;
    }
}
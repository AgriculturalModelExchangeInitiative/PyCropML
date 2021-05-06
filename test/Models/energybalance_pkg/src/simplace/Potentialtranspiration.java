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


public class Potentialtranspiration extends FWSimComponent
{
    private FWSimVariable<Double> tau;
    private FWSimVariable<Double> evapoTranspiration;
    private FWSimVariable<Double> potentialTranspiration;

    private Potentialtranspiration(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Potentialtranspiration(){
        super();
    }
    @Override
    protected void process()
    {
        double tevapoTranspiration = evapoTranspiration.getValue();
        double ttau = tau.getValue();
        double tpotentialTranspiration = potentialTranspiration.getValue();
        tpotentialTranspiration = tevapoTranspiration * (1.0d - ttau);
        potentialTranspiration.setValue(tpotentialTranspiration, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Potentialtranspiration(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("ctau", "plant cover factor", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.9983, this));
        addVariable(FWSimVariable.createSimVariable("revapoTranspiration", "evapoTranspiration", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 830.958, this));
        addVariable(FWSimVariable.createSimVariable("rpotentialTranspiration", "potential Transpiration ", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, null, this));

        return iFieldMap;
    }
}
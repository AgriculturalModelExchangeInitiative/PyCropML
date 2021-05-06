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


public class Evapotranspiration extends FWSimComponent
{
    private FWSimVariable<Integer> isWindVpDefined;
    private FWSimVariable<Double> evapoTranspirationPriestlyTaylor;
    private FWSimVariable<Double> evapoTranspirationPenman;
    private FWSimVariable<Double> evapoTranspiration;

    private Evapotranspiration(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Evapotranspiration(){
        super();
    }
    @Override
    protected void process()
    {
        int tisWindVpDefined = isWindVpDefined.getValue();
        double tevapoTranspirationPriestlyTaylor = evapoTranspirationPriestlyTaylor.getValue();
        double tevapoTranspirationPenman = evapoTranspirationPenman.getValue();
        double tevapoTranspiration = evapoTranspiration.getValue();
        if (tisWindVpDefined == 1)
        {
            tevapoTranspiration = tevapoTranspirationPenman;
        }
        else
        {
            tevapoTranspiration = tevapoTranspirationPriestlyTaylor;
        }
        evapoTranspiration.setValue(tevapoTranspiration, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Evapotranspiration(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("cisWindVpDefined", "if wind and vapour pressure are defined", DATA_TYPE.INT, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 1, this));
        addVariable(FWSimVariable.createSimVariable("revapoTranspirationPriestlyTaylor", "evapoTranspiration of Priestly Taylor ", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 449.367, this));
        addVariable(FWSimVariable.createSimVariable("revapoTranspirationPenman", "evapoTranspiration of Penman ", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 830.958, this));
        addVariable(FWSimVariable.createSimVariable("revapoTranspiration", "evapoTranspiration", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, null, this));

        return iFieldMap;
    }
}
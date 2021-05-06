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


public class Priestlytaylor extends FWSimComponent
{
    private FWSimVariable<Double> psychrometricConstant;
    private FWSimVariable<Double> Alpha;
    private FWSimVariable<Double> hslope;
    private FWSimVariable<Double> netRadiationEquivalentEvaporation;
    private FWSimVariable<Double> evapoTranspirationPriestlyTaylor;

    private Priestlytaylor(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Priestlytaylor(){
        super();
    }
    @Override
    protected void process()
    {
        double tnetRadiationEquivalentEvaporation = netRadiationEquivalentEvaporation.getValue();
        double thslope = hslope.getValue();
        double tpsychrometricConstant = psychrometricConstant.getValue();
        double tAlpha = Alpha.getValue();
        double tevapoTranspirationPriestlyTaylor = evapoTranspirationPriestlyTaylor.getValue();
        tevapoTranspirationPriestlyTaylor = Math.max(tAlpha * thslope * tnetRadiationEquivalentEvaporation / (thslope + tpsychrometricConstant), 0.0d);
        evapoTranspirationPriestlyTaylor.setValue(tevapoTranspirationPriestlyTaylor, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Priestlytaylor(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("cpsychrometricConstant", "psychrometric constant", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.66, this));
        addVariable(FWSimVariable.createSimVariable("cAlpha", "Priestley-Taylor evapotranspiration proportionality constant", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 100, 1.5, this));
        addVariable(FWSimVariable.createSimVariable("ihslope", "the slope of saturated vapor pressure temperature curve at a given temperature ", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 0.584, this));
        addVariable(FWSimVariable.createSimVariable("snetRadiationEquivalentEvaporation", "net Radiation in Equivalent Evaporation", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, 638.142, this));
        addVariable(FWSimVariable.createSimVariable("revapoTranspirationPriestlyTaylor", "evapoTranspiration of Priestly Taylor ", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, null, this));

        return iFieldMap;
    }
}
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


public class Netradiationequivalentevaporation extends FWSimComponent
{
    private FWSimVariable<Double> lambdaV;
    private FWSimVariable<Double> netRadiationEquivalentEvaporation;
    private FWSimVariable<Double> netRadiation;

    private Netradiationequivalentevaporation(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Netradiationequivalentevaporation(){
        super();
    }
    @Override
    protected void process()
    {
        double tlambdaV = lambdaV.getValue();
        double tnetRadiation = netRadiation.getValue();
        double tnetRadiationEquivalentEvaporation = netRadiationEquivalentEvaporation.getValue();
        tnetRadiationEquivalentEvaporation = tnetRadiation / tlambdaV * 1000.0d;
        netRadiationEquivalentEvaporation.setValue(tnetRadiationEquivalentEvaporation, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Netradiationequivalentevaporation(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("clambdaV", "latent heat of vaporization of water", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10, 2.454, this));
        addVariable(FWSimVariable.createSimVariable("netRadiationEquivalentEvaporation", "net Radiation in Equivalent Evaporation ", DATA_TYPE.DOUBLE, CONTENT_TYPE.out,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, null, this));
        addVariable(FWSimVariable.createSimVariable("snetRadiation", "net radiation", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, 1.566, this));

        return iFieldMap;
    }
}
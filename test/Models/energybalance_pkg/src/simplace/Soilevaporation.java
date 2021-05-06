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


public class Soilevaporation extends FWSimComponent
{
    private FWSimVariable<Double> soilEvaporation;
    private FWSimVariable<Double> diffusionLimitedEvaporation;
    private FWSimVariable<Double> energyLimitedEvaporation;

    private Soilevaporation(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Soilevaporation(){
        super();
    }
    @Override
    protected void process()
    {
        double tdiffusionLimitedEvaporation = diffusionLimitedEvaporation.getValue();
        double tenergyLimitedEvaporation = energyLimitedEvaporation.getValue();
        double tsoilEvaporation = soilEvaporation.getValue();
        tsoilEvaporation = Math.min(tdiffusionLimitedEvaporation, tenergyLimitedEvaporation);
        soilEvaporation.setValue(tsoilEvaporation, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Soilevaporation(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("soilEvaporation", "soil Evaporation", DATA_TYPE.DOUBLE, CONTENT_TYPE.out,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, null, this));
        addVariable(FWSimVariable.createSimVariable("sdiffusionLimitedEvaporation", "diffusion Limited Evaporation", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 6605.505, this));
        addVariable(FWSimVariable.createSimVariable("senergyLimitedEvaporation", "energy Limited Evaporation", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 448.240, this));

        return iFieldMap;
    }
}
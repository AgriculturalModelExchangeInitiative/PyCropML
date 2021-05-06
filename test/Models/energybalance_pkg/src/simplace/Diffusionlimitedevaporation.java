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


public class Diffusionlimitedevaporation extends FWSimComponent
{
    private FWSimVariable<Double> soilDiffusionConstant;
    private FWSimVariable<Double> deficitOnTopLayers;
    private FWSimVariable<Double> diffusionLimitedEvaporation;

    private Diffusionlimitedevaporation(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Diffusionlimitedevaporation(){
        super();
    }
    @Override
    protected void process()
    {
        double tdeficitOnTopLayers = deficitOnTopLayers.getValue();
        double tsoilDiffusionConstant = soilDiffusionConstant.getValue();
        double tdiffusionLimitedEvaporation = diffusionLimitedEvaporation.getValue();
        if (tdeficitOnTopLayers / 1000.0d <= 0.0d)
        {
            tdiffusionLimitedEvaporation = 8.3d * 1000.0d;
        }
        else
        {
            if (tdeficitOnTopLayers / 1000.0d < 25.0d)
            {
                tdiffusionLimitedEvaporation = 2.0d * tsoilDiffusionConstant * tsoilDiffusionConstant / (tdeficitOnTopLayers / 1000.0d) * 1000.0d;
            }
            else
            {
                tdiffusionLimitedEvaporation = 0.0d;
            }
        }
        diffusionLimitedEvaporation.setValue(tdiffusionLimitedEvaporation, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Diffusionlimitedevaporation(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("csoilDiffusionConstant", "soil Diffusion Constant", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10, 4.2, this));
        addVariable(FWSimVariable.createSimVariable("ideficitOnTopLayers", "deficit On TopLayers", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 5341, this));
        addVariable(FWSimVariable.createSimVariable("sdiffusionLimitedEvaporation", "the evaporation from the diffusion limited soil ", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, null, this));

        return iFieldMap;
    }
}
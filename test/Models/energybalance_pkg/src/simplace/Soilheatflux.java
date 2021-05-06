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


public class Soilheatflux extends FWSimComponent
{
    private FWSimVariable<Double> tau;
    private FWSimVariable<Double> netRadiationEquivalentEvaporation;
    private FWSimVariable<Double> soilEvaporation;
    private FWSimVariable<Double> soilHeatFlux;

    private Soilheatflux(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Soilheatflux(){
        super();
    }
    @Override
    protected void process()
    {
        double tnetRadiationEquivalentEvaporation = netRadiationEquivalentEvaporation.getValue();
        double ttau = tau.getValue();
        double tsoilEvaporation = soilEvaporation.getValue();
        double tsoilHeatFlux = soilHeatFlux.getValue();
        tsoilHeatFlux = ttau * tnetRadiationEquivalentEvaporation - tsoilEvaporation;
        soilHeatFlux.setValue(tsoilHeatFlux, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Soilheatflux(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("ctau", "plant cover factor", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 100, 0.9983, this));
        addVariable(FWSimVariable.createSimVariable("snetRadiationEquivalentEvaporation", "net Radiation Equivalent Evaporation", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, 638.142, this));
        addVariable(FWSimVariable.createSimVariable("ssoilEvaporation", "soil Evaporation", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 448.240, this));
        addVariable(FWSimVariable.createSimVariable("rsoilHeatFlux", "soil Heat Flux ", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, null, this));

        return iFieldMap;
    }
}
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


public class Cropheatflux extends FWSimComponent
{
    private FWSimVariable<Double> netRadiationEquivalentEvaporation;
    private FWSimVariable<Double> soilHeatFlux;
    private FWSimVariable<Double> potentialTranspiration;
    private FWSimVariable<Double> cropHeatFlux;

    private Cropheatflux(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Cropheatflux(){
        super();
    }
    @Override
    protected void process()
    {
        double tnetRadiationEquivalentEvaporation = netRadiationEquivalentEvaporation.getValue();
        double tsoilHeatFlux = soilHeatFlux.getValue();
        double tpotentialTranspiration = potentialTranspiration.getValue();
        double tcropHeatFlux = cropHeatFlux.getValue();
        tcropHeatFlux = tnetRadiationEquivalentEvaporation - tsoilHeatFlux - tpotentialTranspiration;
        cropHeatFlux.setValue(tcropHeatFlux, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Cropheatflux(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("inetRadiationEquivalentEvaporation", "net Radiation Equivalent Evaporation", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 638.142, this));
        addVariable(FWSimVariable.createSimVariable("rsoilHeatFlux", "soil Heat Flux", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 188.817, this));
        addVariable(FWSimVariable.createSimVariable("rpotentialTranspiration", "potential Transpiration", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000,  1.413, this));
        addVariable(FWSimVariable.createSimVariable("rcropHeatFlux", " crop Heat Flux", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, null, this));

        return iFieldMap;
    }
}
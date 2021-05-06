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


public class Canopytemperature extends FWSimComponent
{
    private FWSimVariable<Double> lambdaV;
    private FWSimVariable<Double> rhoDensityAir;
    private FWSimVariable<Double> specificHeatCapacityAir;
    private FWSimVariable<Double> minTair;
    private FWSimVariable<Double> maxTair;
    private FWSimVariable<Double> conductance;
    private FWSimVariable<Double> minCanopyTemperature;
    private FWSimVariable<Double> maxCanopyTemperature;
    private FWSimVariable<Double> cropHeatFlux;

    private Canopytemperature(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Canopytemperature(){
        super();
    }
    @Override
    protected void process()
    {
        double tminTair = minTair.getValue();
        double tmaxTair = maxTair.getValue();
        double tcropHeatFlux = cropHeatFlux.getValue();
        double tconductance = conductance.getValue();
        double tlambdaV = lambdaV.getValue();
        double trhoDensityAir = rhoDensityAir.getValue();
        double tspecificHeatCapacityAir = specificHeatCapacityAir.getValue();
        double tminCanopyTemperature = minCanopyTemperature.getValue();
        double tmaxCanopyTemperature = maxCanopyTemperature.getValue();
        tminCanopyTemperature = tminTair + (tcropHeatFlux / (trhoDensityAir * tspecificHeatCapacityAir * tconductance / tlambdaV * 1000.0d));
        tmaxCanopyTemperature = tmaxTair + (tcropHeatFlux / (trhoDensityAir * tspecificHeatCapacityAir * tconductance / tlambdaV * 1000.0d));
        minCanopyTemperature.setValue(tminCanopyTemperature, this);
        maxCanopyTemperature.setValue(tmaxCanopyTemperature, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Canopytemperature(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("clambdaV", "latent heat of vaporization of water", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10, 2.454, this));
        addVariable(FWSimVariable.createSimVariable("crhoDensityAir", "Density of air", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, 1.225, this));
        addVariable(FWSimVariable.createSimVariable("cspecificHeatCapacityAir", "Specific heat capacity of dry air", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, 0.00101, this));
        addVariable(FWSimVariable.createSimVariable("iminTair", "minimum air temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -30, 45, 0.7, this));
        addVariable(FWSimVariable.createSimVariable("imaxTair", "maximum air Temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -30, 45, 7.2, this));
        addVariable(FWSimVariable.createSimVariable("sconductance", "the boundary layer conductance", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 598.685, this));
        addVariable(FWSimVariable.createSimVariable("sminCanopyTemperature", "minimal Canopy Temperature  ", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", -30, 45, null, this));
        addVariable(FWSimVariable.createSimVariable("smaxCanopyTemperature", "maximal Canopy Temperature ", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", -30, 45, null, this));
        addVariable(FWSimVariable.createSimVariable("rcropHeatFlux", "Crop heat flux", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 447.912, this));

        return iFieldMap;
    }
}
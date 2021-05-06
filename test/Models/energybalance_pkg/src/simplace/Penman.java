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


public class Penman extends FWSimComponent
{
    private FWSimVariable<Double> psychrometricConstant;
    private FWSimVariable<Double> Alpha;
    private FWSimVariable<Double> lambdaV;
    private FWSimVariable<Double> rhoDensityAir;
    private FWSimVariable<Double> specificHeatCapacityAir;
    private FWSimVariable<Double> hslope;
    private FWSimVariable<Double> VPDair;
    private FWSimVariable<Double> conductance;
    private FWSimVariable<Double> evapoTranspirationPriestlyTaylor;
    private FWSimVariable<Double> evapoTranspirationPenman;

    private Penman(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Penman(){
        super();
    }
    @Override
    protected void process()
    {
        double tevapoTranspirationPriestlyTaylor = evapoTranspirationPriestlyTaylor.getValue();
        double thslope = hslope.getValue();
        double tVPDair = VPDair.getValue();
        double tpsychrometricConstant = psychrometricConstant.getValue();
        double tAlpha = Alpha.getValue();
        double tlambdaV = lambdaV.getValue();
        double trhoDensityAir = rhoDensityAir.getValue();
        double tspecificHeatCapacityAir = specificHeatCapacityAir.getValue();
        double tconductance = conductance.getValue();
        double tevapoTranspirationPenman = evapoTranspirationPenman.getValue();
        tevapoTranspirationPenman = tevapoTranspirationPriestlyTaylor / tAlpha + (1000.0d * (trhoDensityAir * tspecificHeatCapacityAir * tVPDair * tconductance / (tlambdaV * (thslope + tpsychrometricConstant))));
        evapoTranspirationPenman.setValue(tevapoTranspirationPenman, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Penman(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("cpsychrometricConstant", "psychrometric constant", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.66, this));
        addVariable(FWSimVariable.createSimVariable("cAlpha", "Priestley-Taylor evapotranspiration proportionality constant", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 100, 1.5, this));
        addVariable(FWSimVariable.createSimVariable("clambdaV", "latent heat of vaporization of water", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10, 2.454, this));
        addVariable(FWSimVariable.createSimVariable("crhoDensityAir", "Density of air", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, 1.225, this));
        addVariable(FWSimVariable.createSimVariable("cspecificHeatCapacityAir", "Specific heat capacity of dry air", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.00101, this));
        addVariable(FWSimVariable.createSimVariable("ihslope", "the slope of saturated vapor pressure temperature curve at a given temperature ", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 0.584, this));
        addVariable(FWSimVariable.createSimVariable("iVPDair", " vapour pressure density", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 2.19, this));
        addVariable(FWSimVariable.createSimVariable("sconductance", "conductance", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 598.685, this));
        addVariable(FWSimVariable.createSimVariable("revapoTranspirationPriestlyTaylor", "evapoTranspiration of Priestly Taylor ", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 449.367, this));
        addVariable(FWSimVariable.createSimVariable("revapoTranspirationPenman", " evapoTranspiration of Penman Monteith", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, null, this));

        return iFieldMap;
    }
}
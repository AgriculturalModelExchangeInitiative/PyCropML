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


public class Netradiation extends FWSimComponent
{
    private FWSimVariable<Double> albedoCoefficient;
    private FWSimVariable<Double> stefanBoltzman;
    private FWSimVariable<Double> elevation;
    private FWSimVariable<Double> minTair;
    private FWSimVariable<Double> maxTair;
    private FWSimVariable<Double> solarRadiation;
    private FWSimVariable<Double> vaporPressure;
    private FWSimVariable<Double> extraSolarRadiation;
    private FWSimVariable<Double> netRadiation;
    private FWSimVariable<Double> netOutGoingLongWaveRadiation;

    private Netradiation(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Netradiation(){
        super();
    }
    @Override
    protected void process()
    {
        double tminTair = minTair.getValue();
        double tmaxTair = maxTair.getValue();
        double talbedoCoefficient = albedoCoefficient.getValue();
        double tstefanBoltzman = stefanBoltzman.getValue();
        double televation = elevation.getValue();
        double tsolarRadiation = solarRadiation.getValue();
        double tvaporPressure = vaporPressure.getValue();
        double textraSolarRadiation = extraSolarRadiation.getValue();
        double tnetRadiation = netRadiation.getValue();
        double tnetOutGoingLongWaveRadiation = netOutGoingLongWaveRadiation.getValue();
        double Nsr;
        double clearSkySolarRadiation;
        double averageT;
        double surfaceEmissivity;
        double cloudCoverFactor;
        double Nolr;
        Nsr = (1.0d - talbedoCoefficient) * tsolarRadiation;
        clearSkySolarRadiation = (0.75d + (2 * Math.pow(10.0d, -5) * televation)) * textraSolarRadiation;
        averageT = (Math.pow(tmaxTair + 273.16d, 4) + Math.pow(tminTair + 273.16d, 4)) / 2.0d;
        surfaceEmissivity = 0.34d - (0.14d * Math.sqrt(tvaporPressure / 10.0d));
        cloudCoverFactor = 1.35d * (tsolarRadiation / clearSkySolarRadiation) - 0.35d;
        Nolr = tstefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor;
        tnetRadiation = Nsr - Nolr;
        tnetOutGoingLongWaveRadiation = Nolr;
        netRadiation.setValue(tnetRadiation, this);
        netOutGoingLongWaveRadiation.setValue(tnetOutGoingLongWaveRadiation, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Netradiation(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("calbedoCoefficient", "albedo Coefficient", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.23, this));
        addVariable(FWSimVariable.createSimVariable("cstefanBoltzman", "stefan Boltzman constant", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 4.903E-09, this));
        addVariable(FWSimVariable.createSimVariable("celevation", "elevation", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", -500, 10000, 0, this));
        addVariable(FWSimVariable.createSimVariable("iminTair", "minimum air temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -30, 45, 0.7, this));
        addVariable(FWSimVariable.createSimVariable("imaxTair", "maximum air Temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -30, 45, 7.2, this));
        addVariable(FWSimVariable.createSimVariable("isolarRadiation", "solar Radiation", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 3, this));
        addVariable(FWSimVariable.createSimVariable("ivaporPressure", "vapor Pressure", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 6.1, this));
        addVariable(FWSimVariable.createSimVariable("iextraSolarRadiation", "extra Solar Radiation", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 11.7, this));
        addVariable(FWSimVariable.createSimVariable("netRadiation", " net radiation ", DATA_TYPE.DOUBLE, CONTENT_TYPE.out,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, null, this));
        addVariable(FWSimVariable.createSimVariable("netOutGoingLongWaveRadiation", "net OutGoing Long Wave Radiation ", DATA_TYPE.DOUBLE, CONTENT_TYPE.out,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, null, this));

        return iFieldMap;
    }
}
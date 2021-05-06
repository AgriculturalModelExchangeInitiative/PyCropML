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


public class Conductance extends FWSimComponent
{
    private FWSimVariable<Double> vonKarman;
    private FWSimVariable<Double> heightWeatherMeasurements;
    private FWSimVariable<Double> zm;
    private FWSimVariable<Double> zh;
    private FWSimVariable<Double> d;
    private FWSimVariable<Double> plantHeight;
    private FWSimVariable<Double> wind;
    private FWSimVariable<Double> conductance;

    private Conductance(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Conductance(){
        super();
    }
    @Override
    protected void process()
    {
        double tvonKarman = vonKarman.getValue();
        double theightWeatherMeasurements = heightWeatherMeasurements.getValue();
        double tzm = zm.getValue();
        double tzh = zh.getValue();
        double td = d.getValue();
        double tplantHeight = plantHeight.getValue();
        double twind = wind.getValue();
        double tconductance = conductance.getValue();
        double h;
        h = Math.max(10.0d, tplantHeight) / 100.0d;
        tconductance = twind * Math.pow(tvonKarman, 2) / (Math.log((theightWeatherMeasurements - (td * h)) / (tzm * h)) * Math.log((theightWeatherMeasurements - (td * h)) / (tzh * h)));
        conductance.setValue(tconductance, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Conductance(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("cvonKarman", "von Karman constant", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.42, this));
        addVariable(FWSimVariable.createSimVariable("cheightWeatherMeasurements", "reference height of wind and humidity measurements", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10, 2, this));
        addVariable(FWSimVariable.createSimVariable("czm", "roughness length governing momentum transfer, FAO", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.13, this));
        addVariable(FWSimVariable.createSimVariable("czh", "roughness length governing transfer of heat and vapour, FAO", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.013, this));
        addVariable(FWSimVariable.createSimVariable("cd", "corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.67, this));
        addVariable(FWSimVariable.createSimVariable("iplantHeight", "plant Height", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 0, this));
        addVariable(FWSimVariable.createSimVariable("iwind", "wind", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000000, 124000, this));
        addVariable(FWSimVariable.createSimVariable("sconductance", "the boundary layer conductance", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, null, this));

        return iFieldMap;
    }
}
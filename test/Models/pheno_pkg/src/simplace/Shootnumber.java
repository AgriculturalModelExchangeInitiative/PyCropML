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


public class Shootnumber extends FWSimComponent
{
    private FWSimVariable<Double> sowingDensity;
    private FWSimVariable<Double> targetFertileShoot;
    private FWSimVariable<Double> canopyShootNumber_t1;
    private FWSimVariable<Double> leafNumber;
    private FWSimVariable<Double[]> tilleringProfile_t1;
    private FWSimVariable<Integer[]> leafTillerNumberArray_t1;
    private FWSimVariable<Integer> numberTillerCohort_t1;
    private FWSimVariable<Double> averageShootNumberPerPlant;
    private FWSimVariable<Double> canopyShootNumber;
    private FWSimVariable<Integer[]> leafTillerNumberArray;
    private FWSimVariable<Double[]> tilleringProfile;
    private FWSimVariable<Integer> numberTillerCohort;

    public Shootnumber(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Shootnumber(){
        super();
    }
    @Override
    protected void process()
    {
        double tcanopyShootNumber_t1 = canopyShootNumber_t1.getValue();
        double tleafNumber = leafNumber.getValue();
        double tsowingDensity = sowingDensity.getValue();
        double ttargetFertileShoot = targetFertileShoot.getValue();
        List<Double> ttilleringProfile_t1 = Arrays.asList(tilleringProfile_t1.getValue());
        List<Integer> tleafTillerNumberArray_t1 = Arrays.asList(leafTillerNumberArray_t1.getValue());
        int tnumberTillerCohort_t1 = numberTillerCohort_t1.getValue();
        double taverageShootNumberPerPlant;
        double tcanopyShootNumber;
        List<Integer> tleafTillerNumberArray;
        List<Double> ttilleringProfile;
        int tnumberTillerCohort;
        int emergedLeaves;
        int shoots;
        int i;
        List<Integer> lNumberArray_rate = new ArrayList<>(Arrays.asList());
        emergedLeaves = Math.max(1, (int) Math.ceil(tleafNumber - 1.0d));
        shoots = fibonacci(emergedLeaves);
        tcanopyShootNumber = Math.min(shoots * tsowingDensity, ttargetFertileShoot);
        taverageShootNumberPerPlant = tcanopyShootNumber / tsowingDensity;
        if (tcanopyShootNumber != tcanopyShootNumber_t1)
        {
            tilleringProfile = new ArrayList<>(tilleringProfile_t1);
            tilleringProfile.add(tcanopyShootNumber - tcanopyShootNumber_t1);
        }
        tnumberTillerCohort = ttilleringProfile.size();
        for (i=tleafTillerNumberArray_t1.size() ; i<(int) Math.ceil(tleafNumber) ; i+=1)
        {
            lNumberArray_rate.add(tnumberTillerCohort);
        }
        leafTillerNumberArray = new ArrayList<>(leafTillerNumberArray_t1);
        leafTillerNumberArray.addAll(lNumberArray_rate);
        averageShootNumberPerPlant.setValue(taverageShootNumberPerPlant, this);
        canopyShootNumber.setValue(tcanopyShootNumber, this);
        leafTillerNumberArray.setValue(tleafTillerNumberArray.toArray(new Integer[0]), this);
        tilleringProfile.setValue(ttilleringProfile.toArray(new Double[0]), this);
        numberTillerCohort.setValue(tnumberTillerCohort, this);
    }
    public static int fibonacci(int n)
    {
    if (n <= 1)
    {
        return n;
    }
    else
    {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
@Override
protected void init()
{
    double tsowingDensity = sowingDensity.getValue();
    double ttargetFertileShoot = targetFertileShoot.getValue();
    double taverageShootNumberPerPlant;
    double tcanopyShootNumber;
    List<Integer> tleafTillerNumberArray;
    List<Double> ttilleringProfile;
    int tnumberTillerCohort;
    tcanopyShootNumber = tsowingDensity;
    taverageShootNumberPerPlant = 1.0d;
    ttilleringProfile.add(tsowingDensity);
    tnumberTillerCohort = 1;
    tleafTillerNumberArray = new ArrayList<>(Arrays.asList());
    averageShootNumberPerPlant.setValue(taverageShootNumberPerPlant, this);
    canopyShootNumber.setValue(tcanopyShootNumber, this);
    leafTillerNumberArray.setValue(tleafTillerNumberArray.toArray(new Integer[0]), this);
    tilleringProfile.setValue(ttilleringProfile.toArray(new Double[0]), this);
    numberTillerCohort.setValue(tnumberTillerCohort, this);
}

@Override
protected FWSimComponent clone(FWSimVarMap aVarMap)
{
    return new Shootnumber(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
}

@Override
public HashMap<String, FWSimVariable<?>> createVariables()
{
    addVariable(FWSimVariable.createSimVariable("csowingDensity", "number of plant /m²", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 500, 288.0, this));
    addVariable(FWSimVariable.createSimVariable("ctargetFertileShoot", "max value of shoot number for the canopy", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 280, 1000, 600.0, this));
    addVariable(FWSimVariable.createSimVariable("scanopyShootNumber", "shoot number for the whole canopy", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 288.0, this));
    addVariable(FWSimVariable.createSimVariable("sleafNumber", "Leaf number ", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 3.34, this));
    addVariable(FWSimVariable.createSimVariable("stilleringProfile", " store the amount of new tiller created at each time a new tiller appears", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Double[] {288.0}, this));
    addVariable(FWSimVariable.createSimVariable("sleafTillerNumberArray", "store the number of tiller for each leaf layer", DATA_TYPE.INTARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Integer[] {1,1,1}, this));
    addVariable(FWSimVariable.createSimVariable("snumberTillerCohort", " Number of tiller which appears", DATA_TYPE.INT, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 1, this));
    addVariable(FWSimVariable.createSimVariable("saverageShootNumberPerPlant", "average shoot number per plant in the canopy", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, null, this));

    return iFieldMap;
}
}
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


public class Phylsowingdatecorrection extends FWSimComponent
{
    private FWSimVariable<Integer> sowingDay;
    private FWSimVariable<Double> latitude;
    private FWSimVariable<Double> sDsa_sh;
    private FWSimVariable<Double> rp;
    private FWSimVariable<Integer> sDws;
    private FWSimVariable<Double> sDsa_nh;
    private FWSimVariable<Double> p;
    private FWSimVariable<Double> fixPhyll;

    public Phylsowingdatecorrection(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Phylsowingdatecorrection(){
        super();
    }
    @Override
    protected void process()
    {
        int tsowingDay = sowingDay.getValue();
        double tlatitude = latitude.getValue();
        double tsDsa_sh = sDsa_sh.getValue();
        double trp = rp.getValue();
        int tsDws = sDws.getValue();
        double tsDsa_nh = sDsa_nh.getValue();
        double tp = p.getValue();
        double tfixPhyll;
        if (tlatitude < 0.0d)
        {
            if (tsowingDay > (int)(tsDsa_sh))
            {
                tfixPhyll = tp * (1 - (trp * Math.min((tsowingDay - tsDsa_sh), tsDws)));
            }
            else
            {
                tfixPhyll = tp;
            }
        }
        else
        {
            if (tsowingDay < (int)(tsDsa_nh))
            {
                tfixPhyll = tp * (1 - (trp * Math.min(tsowingDay, tsDws)));
            }
            else
            {
                tfixPhyll = tp;
            }
        }
        fixPhyll.setValue(tfixPhyll, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Phylsowingdatecorrection(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("csowingDay", "Day of Year at sowing", DATA_TYPE.INT, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 1, 365, 1, this));
        addVariable(FWSimVariable.createSimVariable("clatitude", "Latitude", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", -90, 90, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("csDsa_sh", "Sowing date at which Phyllochrone is maximum in southern hemispher", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 1, 365, 1.0, this));
        addVariable(FWSimVariable.createSimVariable("crp", "Rate of change of Phyllochrone with sowing date", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 365, 0, this));
        addVariable(FWSimVariable.createSimVariable("csDws", "Sowing date at which Phyllochrone is minimum", DATA_TYPE.INT, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 1, 365, 1, this));
        addVariable(FWSimVariable.createSimVariable("csDsa_nh", "Sowing date at which Phyllochrone is maximum in northern hemispher", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 1, 365, 1.0, this));
        addVariable(FWSimVariable.createSimVariable("cp", "Phyllochron (Varietal parameter)", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 120, this));
        addVariable(FWSimVariable.createSimVariable("fixPhyll", " Phyllochron Varietal parameter ", DATA_TYPE.DOUBLE, CONTENT_TYPE.out,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, null, this));

        return iFieldMap;
    }
}
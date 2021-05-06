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


public class Ismomentregistredzc_39 extends FWSimComponent
{
    private FWSimVariable<String[]> calendarMoments_t1;
    private FWSimVariable<Integer> isMomentRegistredZC_39;

    public Ismomentregistredzc_39(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Ismomentregistredzc_39(){
        super();
    }
    @Override
    protected void process()
    {
        List<String> tcalendarMoments_t1 = Arrays.asList(calendarMoments_t1.getValue());
        int tisMomentRegistredZC_39;
        tisMomentRegistredZC_39 = tcalendarMoments_t1.contains("FlagLeafLiguleJustVisible") ? 1 : 0;
        isMomentRegistredZC_39.setValue(tisMomentRegistredZC_39, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Ismomentregistredzc_39(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("scalendarMoments", "List containing appearance of each stage at previous time", DATA_TYPE.CHARARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new String[] {"Sowing"}, this));
        addVariable(FWSimVariable.createSimVariable("sisMomentRegistredZC_39", " if Flag leaf ligule has already appeared ", DATA_TYPE.INT, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, null, this));

        return iFieldMap;
    }
}
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


public class Updateleafflag extends FWSimComponent
{
    private FWSimVariable<Double> cumulTT;
    private FWSimVariable<LocalDateTime> currentdate;
    private FWSimVariable<Double> leafNumber;
    private FWSimVariable<String[]> calendarMoments;
    private FWSimVariable<LocalDateTime[]> calendarDates;
    private FWSimVariable<Double[]> calendarCumuls;
    private FWSimVariable<Double> finalLeafNumber;
    private FWSimVariable<Integer> hasFlagLeafLiguleAppeared_t1;
    private FWSimVariable<Double> phase;
    private FWSimVariable<Integer> hasFlagLeafLiguleAppeared;

    public Updateleafflag(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Updateleafflag(){
        super();
    }
    @Override
    protected void process()
    {
        double tcumulTT = cumulTT.getValue();
        double tleafNumber = leafNumber.getValue();
        LocalDateTime tcurrentdate = currentdate.getValue();
        double tfinalLeafNumber = finalLeafNumber.getValue();
        int thasFlagLeafLiguleAppeared_t1 = hasFlagLeafLiguleAppeared_t1.getValue();
        double tphase = phase.getValue();
        int thasFlagLeafLiguleAppeared;
        thasFlagLeafLiguleAppeared = 0;
        if (tphase >= 1.0d && tphase < 4.0d)
        {
            if (tleafNumber > 0.0d)
            {
                if (thasFlagLeafLiguleAppeared == 0 && (tfinalLeafNumber > 0.0d && tleafNumber >= tfinalLeafNumber))
                {
                    thasFlagLeafLiguleAppeared = 1;
                    if (!tcalendarMoments.contains("FlagLeafLiguleJustVisible"))
                    {
                        tcalendarMoments.add("FlagLeafLiguleJustVisible");
                        tcalendarCumuls.add(tcumulTT);
                        tcalendarDates.add(tcurrentdate);
                    }
                }
            }
        }
        calendarMoments.setValue(tcalendarMoments.toArray(new String[0]), this);
        calendarDates.setValue(tcalendarDates.toArray(new LocalDateTime[0]), this);
        calendarCumuls.setValue(tcalendarCumuls.toArray(new Double[0]), this);
        hasFlagLeafLiguleAppeared.setValue(thasFlagLeafLiguleAppeared, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Updateleafflag(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("icumulTT", "cumul thermal times at current date", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -200, 10000, 741.510096671757, this));
        addVariable(FWSimVariable.createSimVariable("icurrentdate", " current date", DATA_TYPE.DATE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, null, this));
        addVariable(FWSimVariable.createSimVariable("sleafNumber", "Actual number of phytomers", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 25, 8.919453833361189, this));
        addVariable(FWSimVariable.createSimVariable("scalendarMoments", "List containing apparition of each stage", DATA_TYPE.CHARARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new String[] {"Sowing"}, this));
        addVariable(FWSimVariable.createSimVariable("scalendarDates", "List containing  the dates of the wheat developmental phases", DATA_TYPE.CHARARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, null, this));
        addVariable(FWSimVariable.createSimVariable("scalendarCumuls", "list containing for each stage occured its cumulated thermal times", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Double[] {0.0}, this));
        addVariable(FWSimVariable.createSimVariable("sfinalLeafNumber", "final leaf number", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 8.797582013199484, this));
        addVariable(FWSimVariable.createSimVariable("shasFlagLeafLiguleAppeared", "true if flag leaf has appeared (leafnumber reached finalLeafNumber)", DATA_TYPE.INT, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 1, this));
        addVariable(FWSimVariable.createSimVariable("sphase", " the name of the phase", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 7, 1, this));

        return iFieldMap;
    }
}
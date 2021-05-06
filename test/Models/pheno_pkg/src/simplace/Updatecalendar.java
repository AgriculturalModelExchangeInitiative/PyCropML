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


public class Updatecalendar extends FWSimComponent
{
    private FWSimVariable<Double> cumulTT;
    private FWSimVariable<LocalDateTime> currentdate;
    private FWSimVariable<String[]> calendarMoments;
    private FWSimVariable<LocalDateTime[]> calendarDates;
    private FWSimVariable<Double[]> calendarCumuls;
    private FWSimVariable<Double> phase;

    public Updatecalendar(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Updatecalendar(){
        super();
    }
    @Override
    protected void process()
    {
        double tcumulTT = cumulTT.getValue();
        LocalDateTime tcurrentdate = currentdate.getValue();
        double tphase = phase.getValue();
        if (tphase >= 1.0d && tphase < 2.0d && !tcalendarMoments.contains("Emergence"))
        {
            tcalendarMoments.add("Emergence");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
        }
        else if ( tphase >= 2.0d && tphase < 3.0d && !tcalendarMoments.contains("FloralInitiation"))
        {
            tcalendarMoments.add("FloralInitiation");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
        }
        else if ( tphase >= 3.0d && tphase < 4.0d && !tcalendarMoments.contains("Heading"))
        {
            tcalendarMoments.add("Heading");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
        }
        else if ( tphase == 4.0d && !tcalendarMoments.contains("Anthesis"))
        {
            tcalendarMoments.add("Anthesis");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
        }
        else if ( tphase == 4.5d && !tcalendarMoments.contains("EndCellDivision"))
        {
            tcalendarMoments.add("EndCellDivision");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
        }
        else if ( tphase >= 5.0d && tphase < 6.0d && !tcalendarMoments.contains("EndGrainFilling"))
        {
            tcalendarMoments.add("EndGrainFilling");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
        }
        else if ( tphase >= 6.0d && tphase < 7.0d && !tcalendarMoments.contains("Maturity"))
        {
            tcalendarMoments.add("Maturity");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
        }
        calendarMoments.setValue(tcalendarMoments.toArray(new String[0]), this);
        calendarDates.setValue(tcalendarDates.toArray(new LocalDateTime[0]), this);
        calendarCumuls.setValue(tcalendarCumuls.toArray(new Double[0]), this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Updatecalendar(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("icumulTT", "cumul thermal times at current date", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -200, 10000, 741.510096671757, this));
        addVariable(FWSimVariable.createSimVariable("icurrentdate", "current date", DATA_TYPE.DATE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, null, this));
        addVariable(FWSimVariable.createSimVariable("scalendarMoments", "List containing apparition of each stage", DATA_TYPE.CHARARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new String[] {"Sowing"}, this));
        addVariable(FWSimVariable.createSimVariable("scalendarDates", "List containing  the dates of the wheat developmental phases", DATA_TYPE.CHARARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, null, this));
        addVariable(FWSimVariable.createSimVariable("scalendarCumuls", "list containing for each stage occured its cumulated thermal times", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Double[] {0.0}, this));
        addVariable(FWSimVariable.createSimVariable("sphase", " the name of the phase", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 7, 1, this));

        return iFieldMap;
    }
}
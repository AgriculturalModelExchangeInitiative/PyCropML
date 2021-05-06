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


public class Vernalizationprogress extends FWSimComponent
{
    private FWSimVariable<Double> minTvern;
    private FWSimVariable<Double> intTvern;
    private FWSimVariable<Double> vAI;
    private FWSimVariable<Double> vBEE;
    private FWSimVariable<Double> minDL;
    private FWSimVariable<Double> maxDL;
    private FWSimVariable<Double> maxTvern;
    private FWSimVariable<Double> pNini;
    private FWSimVariable<Double> aMXLFNO;
    private FWSimVariable<Integer> isVernalizable;
    private FWSimVariable<Double> dayLength;
    private FWSimVariable<Double> deltaTT;
    private FWSimVariable<Double> cumulTT;
    private FWSimVariable<LocalDateTime> currentdate;
    private FWSimVariable<Double> leafNumber_t1;
    private FWSimVariable<String[]> calendarMoments_t1;
    private FWSimVariable<LocalDateTime[]> calendarDates_t1;
    private FWSimVariable<Double[]> calendarCumuls_t1;
    private FWSimVariable<Double> vernaprog_t1;
    private FWSimVariable<Double> minFinalNumber_t1;
    private FWSimVariable<Double> vernaprog;
    private FWSimVariable<Double> minFinalNumber;
    private FWSimVariable<String[]> calendarMoments;
    private FWSimVariable<LocalDateTime[]> calendarDates;
    private FWSimVariable<Double[]> calendarCumuls;

    public Vernalizationprogress(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Vernalizationprogress(){
        super();
    }
    @Override
    protected void process()
    {
        double tdayLength = dayLength.getValue();
        double tdeltaTT = deltaTT.getValue();
        double tcumulTT = cumulTT.getValue();
        double tleafNumber_t1 = leafNumber_t1.getValue();
        List<String> tcalendarMoments_t1 = Arrays.asList(calendarMoments_t1.getValue());
        List<LocalDateTime> tcalendarDates_t1 = Arrays.asList(calendarDates_t1.getValue());
        List<Double> tcalendarCumuls_t1 = Arrays.asList(calendarCumuls_t1.getValue());
        double tminTvern = minTvern.getValue();
        double tintTvern = intTvern.getValue();
        double tvAI = vAI.getValue();
        double tvBEE = vBEE.getValue();
        double tminDL = minDL.getValue();
        double tmaxDL = maxDL.getValue();
        double tmaxTvern = maxTvern.getValue();
        double tpNini = pNini.getValue();
        double taMXLFNO = aMXLFNO.getValue();
        double tvernaprog_t1 = vernaprog_t1.getValue();
        LocalDateTime tcurrentdate = currentdate.getValue();
        int tisVernalizable = isVernalizable.getValue();
        double tminFinalNumber_t1 = minFinalNumber_t1.getValue();
        double tvernaprog;
        double tminFinalNumber;
        List<String> tcalendarMoments;
        List<LocalDateTime> tcalendarDates;
        List<Double> tcalendarCumuls;
        double maxVernaProg;
        double dLverna;
        double primordno;
        double minLeafNumber;
        double potlfno;
        double tt;
        tcalendarMoments = new ArrayList<>(tcalendarMoments_t1);
        tcalendarCumuls = new ArrayList<>(tcalendarCumuls_t1);
        tcalendarDates = new ArrayList<>(tcalendarDates_t1);
        tminFinalNumber = tminFinalNumber_t1;
        tvernaprog = tvernaprog_t1;
        if (tisVernalizable == 1 && tvernaprog_t1 < 1.0d)
        {
            tt = tdeltaTT;
            if (tt >= tminTvern && tt <= tintTvern)
            {
                tvernaprog = tvernaprog_t1 + (tvAI * tt) + tvBEE;
            }
            else
            {
                tvernaprog = tvernaprog_t1;
            }
            if (tt > tintTvern)
            {
                maxVernaProg = tvAI * tintTvern + tvBEE;
                dLverna = Math.max(tminDL, Math.min(tmaxDL, tdayLength));
                tvernaprog = tvernaprog + Math.max(0.0d, maxVernaProg * (1.0d + ((tintTvern - tt) / (tmaxTvern - tintTvern) * ((dLverna - tminDL) / (tmaxDL - tminDL)))));
            }
            primordno = 2.0d * tleafNumber_t1 + tpNini;
            minLeafNumber = tminFinalNumber_t1;
            if (tvernaprog >= 1.0d || primordno >= taMXLFNO)
            {
                tminFinalNumber = Math.max(primordno, tminFinalNumber_t1);
                tcalendarMoments.add("EndVernalisation");
                tcalendarCumuls.add(tcumulTT);
                tcalendarDates.add(tcurrentdate);
                tvernaprog = Math.max(1.0d, tvernaprog);
            }
            else
            {
                potlfno = taMXLFNO - ((taMXLFNO - minLeafNumber) * tvernaprog);
                if (primordno >= potlfno)
                {
                    tminFinalNumber = Math.max((potlfno + primordno) / 2.0d, tminFinalNumber_t1);
                    tvernaprog = Math.max(1.0d, tvernaprog);
                    tcalendarMoments.add("EndVernalisation");
                    tcalendarCumuls.add(tcumulTT);
                    tcalendarDates.add(tcurrentdate);
                }
            }
        }
        vernaprog.setValue(tvernaprog, this);
        minFinalNumber.setValue(tminFinalNumber, this);
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
        return new Vernalizationprogress(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("cminTvern", "Minimum temperature for vernalization to occur", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", -20, 60, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("cintTvern", "Intermediate temperature for vernalization to occur", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", -20, 60,  11.0, this));
        addVariable(FWSimVariable.createSimVariable("cvAI", "Response of vernalization rate to temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1,  0.015, this));
        addVariable(FWSimVariable.createSimVariable("cvBEE", "Vernalization rate at 0°C", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.01, this));
        addVariable(FWSimVariable.createSimVariable("cminDL", "Threshold daylength below which it does influence vernalization rate", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 12, 24, 8.0, this));
        addVariable(FWSimVariable.createSimVariable("cmaxDL", "Saturating photoperiod above which final leaf number is not influenced by daylength", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 24, 15.0, this));
        addVariable(FWSimVariable.createSimVariable("cmaxTvern", "Maximum temperature for vernalization to occur", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", -20, 60,  23.0, this));
        addVariable(FWSimVariable.createSimVariable("cpNini", "Number of primorida in the apex at emergence", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 24, 4.0, this));
        addVariable(FWSimVariable.createSimVariable("caMXLFNO", "Absolute maximum leaf number", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 25, 24.0, this));
        addVariable(FWSimVariable.createSimVariable("cisVernalizable", "true if the plant is vernalizable", DATA_TYPE.INT, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 1, this));
        addVariable(FWSimVariable.createSimVariable("idayLength", "day length", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 12.3037621834005, this));
        addVariable(FWSimVariable.createSimVariable("ideltaTT", "difference cumul TT between j and j-1 day ", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -20, 100, 20.3429985011972, this));
        addVariable(FWSimVariable.createSimVariable("icumulTT", "cumul thermal times at currentdate", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -200, 10000, 112.330110409888, this));
        addVariable(FWSimVariable.createSimVariable("icurrentdate", "current date ", DATA_TYPE.DATE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, null, this));
        addVariable(FWSimVariable.createSimVariable("sleafNumber", "Actual number of phytomers", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 25, 0, this));
        addVariable(FWSimVariable.createSimVariable("scalendarMoments", "List containing appearance of each stage", DATA_TYPE.CHARARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new String[] {"Sowing"}, this));
        addVariable(FWSimVariable.createSimVariable("scalendarDates", "List containing  the dates of the wheat developmental phases", DATA_TYPE.CHARARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, null, this));
        addVariable(FWSimVariable.createSimVariable("scalendarCumuls", "list containing for each stage occured its cumulated thermal times", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Double[] {0.0}, this));
        addVariable(FWSimVariable.createSimVariable("svernaprog", "progression on a 0  to 1 scale of the vernalization", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1,  0.5517254187376879, this));
        addVariable(FWSimVariable.createSimVariable("sminFinalNumber", "minimum final leaf number", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 25, 5.5, this));

        return iFieldMap;
    }
}
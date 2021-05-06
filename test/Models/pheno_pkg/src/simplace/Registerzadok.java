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


public class Registerzadok extends FWSimComponent
{
    private FWSimVariable<Double> der;
    private FWSimVariable<Double> slopeTSFLN;
    private FWSimVariable<Double> intTSFLN;
    private FWSimVariable<LocalDateTime> sowingDate;
    private FWSimVariable<Double> cumulTT;
    private FWSimVariable<Double> cumulTTFromZC_65;
    private FWSimVariable<LocalDateTime> currentdate;
    private FWSimVariable<Double> phase;
    private FWSimVariable<Double> leafNumber;
    private FWSimVariable<String[]> calendarMoments;
    private FWSimVariable<LocalDateTime[]> calendarDates;
    private FWSimVariable<Double[]> calendarCumuls;
    private FWSimVariable<Double> finalLeafNumber;
    private FWSimVariable<String> currentZadokStage;
    private FWSimVariable<Integer> hasZadokStageChanged_t1;
    private FWSimVariable<Integer> hasZadokStageChanged;

    public Registerzadok(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Registerzadok(){
        super();
    }
    @Override
    protected void process()
    {
        double tcumulTT = cumulTT.getValue();
        double tphase = phase.getValue();
        double tleafNumber = leafNumber.getValue();
        double tcumulTTFromZC_65 = cumulTTFromZC_65.getValue();
        LocalDateTime tcurrentdate = currentdate.getValue();
        double tder = der.getValue();
        double tslopeTSFLN = slopeTSFLN.getValue();
        double tintTSFLN = intTSFLN.getValue();
        double tfinalLeafNumber = finalLeafNumber.getValue();
        int thasZadokStageChanged_t1 = hasZadokStageChanged_t1.getValue();
        LocalDateTime tsowingDate = sowingDate.getValue();
        int thasZadokStageChanged;
        int roundedFinalLeafNumber;
        roundedFinalLeafNumber = (int)(tfinalLeafNumber + 0.5d);
        if (tleafNumber >= 4.0d && !tcalendarMoments.contains("MainShootPlus1Tiller"))
        {
            tcalendarMoments.add("MainShootPlus1Tiller");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
            thasZadokStageChanged = 1;
            tcurrentZadokStage = "MainShootPlus1Tiller";
        }
        else if ( tleafNumber >= 5.0d && !tcalendarMoments.contains("MainShootPlus2Tiller"))
        {
            tcalendarMoments.add("MainShootPlus2Tiller");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
            thasZadokStageChanged = 1;
            tcurrentZadokStage = "MainShootPlus2Tiller";
        }
        else if ( tleafNumber >= 6.0d && !tcalendarMoments.contains("MainShootPlus3Tiller"))
        {
            tcalendarMoments.add("MainShootPlus3Tiller");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
            thasZadokStageChanged = 1;
            tcurrentZadokStage = "MainShootPlus3Tiller";
        }
        else if ( tfinalLeafNumber > 0.0d && (tleafNumber >= tslopeTSFLN * tfinalLeafNumber - tintTSFLN && !tcalendarMoments.contains("TerminalSpikelet")))
        {
            tcalendarMoments.add("TerminalSpikelet");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
            thasZadokStageChanged = 1;
            tcurrentZadokStage = "TerminalSpikelet";
        }
        else if ( tleafNumber >= roundedFinalLeafNumber - 4.0d && roundedFinalLeafNumber - 4 > 0 && !tcalendarMoments.contains("PseudoStemErection"))
        {
            tcalendarMoments.add("PseudoStemErection");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
            thasZadokStageChanged = 1;
            tcurrentZadokStage = "PseudoStemErection";
        }
        else if ( tleafNumber >= roundedFinalLeafNumber - 3.0d && roundedFinalLeafNumber - 3 > 0 && !tcalendarMoments.contains("1stNodeDetectable"))
        {
            tcalendarMoments.add("1stNodeDetectable");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
            thasZadokStageChanged = 1;
            tcurrentZadokStage = "1stNodeDetectable";
        }
        else if ( tleafNumber >= roundedFinalLeafNumber - 2.0d && roundedFinalLeafNumber - 2 > 0 && !tcalendarMoments.contains("2ndNodeDetectable"))
        {
            tcalendarMoments.add("2ndNodeDetectable");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
            thasZadokStageChanged = 1;
            tcurrentZadokStage = "2ndNodeDetectable";
        }
        else if ( tleafNumber >= roundedFinalLeafNumber - 1.0d && roundedFinalLeafNumber - 1 > 0 && !tcalendarMoments.contains("FlagLeafJustVisible"))
        {
            tcalendarMoments.add("FlagLeafJustVisible");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
            thasZadokStageChanged = 1;
            tcurrentZadokStage = "FlagLeafJustVisible";
        }
        else if ( !tcalendarMoments.contains("MidGrainFilling") && (tphase == 4.5d && tcumulTTFromZC_65 >= tder))
        {
            tcalendarMoments.add("MidGrainFilling");
            tcalendarCumuls.add(tcumulTT);
            tcalendarDates.add(tcurrentdate);
            thasZadokStageChanged = 1;
            tcurrentZadokStage = "MidGrainFilling";
        }
        else
        {
            thasZadokStageChanged = 0;
        }
        calendarMoments.setValue(tcalendarMoments.toArray(new String[0]), this);
        calendarDates.setValue(tcalendarDates.toArray(new LocalDateTime[0]), this);
        calendarCumuls.setValue(tcalendarCumuls.toArray(new Double[0]), this);
        currentZadokStage.setValue(tcurrentZadokStage, this);
        hasZadokStageChanged.setValue(thasZadokStageChanged, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Registerzadok(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("cder", "Duration of the endosperm endoreduplication phase", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 300.0, this));
        addVariable(FWSimVariable.createSimVariable("cslopeTSFLN", "used to calculate Terminal spikelet", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 0.9, this));
        addVariable(FWSimVariable.createSimVariable("cintTSFLN", "used to calculate Terminal spikelet", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 0.9, this));
        addVariable(FWSimVariable.createSimVariable("csowingDate", " Date of Sowing", DATA_TYPE.DATE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, null, this));
        addVariable(FWSimVariable.createSimVariable("icumulTT", "", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -200, 10000, 354.582294511779, this));
        addVariable(FWSimVariable.createSimVariable("icumulTTFromZC_65", "cumul of the thermal time (DeltaTT) since the moment ZC_65", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", -200, 10000, 0, this));
        addVariable(FWSimVariable.createSimVariable("icurrentdate", "current date", DATA_TYPE.DATE, CONTENT_TYPE.input,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, null, this));
        addVariable(FWSimVariable.createSimVariable("sphase", "instance of the phase class . You can get the name of the phase using phase.getPhaseAsString(PhaseValue) ", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 7, 2, this));
        addVariable(FWSimVariable.createSimVariable("sleafNumber", "Actual number of phytomers", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 25, 4.8854219661087575, this));
        addVariable(FWSimVariable.createSimVariable("scalendarMoments", "List containing apparition of each stage", DATA_TYPE.CHARARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new String[] {"Sowing"}, this));
        addVariable(FWSimVariable.createSimVariable("scalendarDates", "List containing  the dates of the wheat developmental phases", DATA_TYPE.CHARARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, null, this));
        addVariable(FWSimVariable.createSimVariable("scalendarCumuls", "list containing for each stage occured its cumulated thermal times", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, new Double[] {0.0}, this));
        addVariable(FWSimVariable.createSimVariable("sfinalLeafNumber", "final leaf number", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 10000, 8.797582013199484, this));
        addVariable(FWSimVariable.createSimVariable("scurrentZadokStage", "current zadok stage", DATA_TYPE.CHAR, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", null, null, "MainShootPlus1Tiller", this));
        addVariable(FWSimVariable.createSimVariable("shasZadokStageChanged", "true if the zadok stage has changed this time step", DATA_TYPE.INT, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0, this));

        return iFieldMap;
    }
}
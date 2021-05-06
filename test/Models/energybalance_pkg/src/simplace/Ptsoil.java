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


public class Ptsoil extends FWSimComponent
{
    private FWSimVariable<Double> Alpha;
    private FWSimVariable<Double> tau;
    private FWSimVariable<Double> tauAlpha;
    private FWSimVariable<Double> energyLimitedEvaporation;
    private FWSimVariable<Double> evapoTranspirationPriestlyTaylor;

    private Ptsoil(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Ptsoil(){
        super();
    }
    @Override
    protected void process()
    {
        double tevapoTranspirationPriestlyTaylor = evapoTranspirationPriestlyTaylor.getValue();
        double tAlpha = Alpha.getValue();
        double ttau = tau.getValue();
        double ttauAlpha = tauAlpha.getValue();
        double tenergyLimitedEvaporation = energyLimitedEvaporation.getValue();
        double AlphaE;
        if (ttau < ttauAlpha)
        {
            AlphaE = 1.0d;
        }
        else
        {
            AlphaE = tAlpha - ((tAlpha - 1.0d) * (1.0d - ttau) / (1.0d - ttauAlpha));
        }
        tenergyLimitedEvaporation = tevapoTranspirationPriestlyTaylor / tAlpha * AlphaE * ttau;
        energyLimitedEvaporation.setValue(tenergyLimitedEvaporation, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new Ptsoil(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("cAlpha", "Priestley-Taylor evapotranspiration proportionality constant", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 100, 1.5, this));
        addVariable(FWSimVariable.createSimVariable("ctau", "plant cover factor", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 100, 0.9983, this));
        addVariable(FWSimVariable.createSimVariable("ctauAlpha", "Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1, 0.3, this));
        addVariable(FWSimVariable.createSimVariable("energyLimitedEvaporation", "energy Limited Evaporation ", DATA_TYPE.DOUBLE, CONTENT_TYPE.out,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 5000, null, this));
        addVariable(FWSimVariable.createSimVariable("sevapoTranspirationPriestlyTaylor", "evapoTranspiration Priestly Taylor", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"http://www.wurvoc.org/vocabularies/om-1.8/", 0, 1000, 120, this));

        return iFieldMap;
    }
}
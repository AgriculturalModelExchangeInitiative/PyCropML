import  java.io.*;
import  java.util.*;
public class Ptsoil
{
    private double Alpha;
    public double getAlpha()
    {
        return Alpha;
    }

    public void setAlpha(double _Alpha)
    {
        this.Alpha= _Alpha;
    } 
    
    private double tau;
    public double gettau()
    {
        return tau;
    }

    public void settau(double _tau)
    {
        this.tau= _tau;
    } 
    
    private double tauAlpha;
    public double gettauAlpha()
    {
        return tauAlpha;
    }

    public void settauAlpha(double _tauAlpha)
    {
        this.tauAlpha= _tauAlpha;
    } 
    
    public Ptsoil()
    {
           
    }
    public void  Calculate_ptsoil(EnergybalanceState s, EnergybalanceRate r, EnergybalanceAuxiliary a)
    {
        //- Description:
    //            - Model Name: PtSoil EnergyLimitedEvaporation Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA Montpellier
    //            - Abstract: Evaporation from the soil in the energy-limited stage 
        //- inputs:
    //            - name: evapoTranspirationPriestlyTaylor
    //                          - description : evapoTranspiration Priestly Taylor
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - default : 120
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : g m-2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: Alpha
    //                          - description : Priestley-Taylor evapotranspiration proportionality constant
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 1.5
    //                          - min : 0
    //                          - max : 100
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: tau
    //                          - description : plant cover factor
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - default : 0.9983
    //                          - min : 0
    //                          - max : 100
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: tauAlpha
    //                          - description : Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1
    //                          - parametercategory : soil
    //                          - datatype : DOUBLE
    //                          - default : 0.3
    //                          - min : 0
    //                          - max : 1
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
        //- outputs:
    //            - name: energyLimitedEvaporation
    //                          - description : energy Limited Evaporation 
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 5000
    //                          - unit : g m-2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        double evapoTranspirationPriestlyTaylor = s.getevapoTranspirationPriestlyTaylor();
        double energyLimitedEvaporation;
        double AlphaE;
        if (tau < tauAlpha)
        {
            AlphaE = 1.0d;
        }
        else
        {
            AlphaE = Alpha - ((Alpha - 1.0d) * (1.0d - tau) / (1.0d - tauAlpha));
        }
        energyLimitedEvaporation = evapoTranspirationPriestlyTaylor / Alpha * AlphaE * tau;
        a.setenergyLimitedEvaporation(energyLimitedEvaporation);
    }
}
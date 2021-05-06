import  java.io.*;
import  java.util.*;
public class Diffusionlimitedevaporation
{
    private double soilDiffusionConstant;
    public double getsoilDiffusionConstant()
    {
        return soilDiffusionConstant;
    }

    public void setsoilDiffusionConstant(double _soilDiffusionConstant)
    {
        this.soilDiffusionConstant= _soilDiffusionConstant;
    } 
    
    public Diffusionlimitedevaporation()
    {
           
    }
    public void  Calculate_diffusionlimitedevaporation(EnergybalanceState s, EnergybalanceRate r, EnergybalanceAuxiliary a)
    {
        //- Description:
    //            - Model Name: DiffusionLimitedEvaporation Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA Montpellier
    //            - Abstract: the evaporation from the diffusion limited soil 
        //- inputs:
    //            - name: deficitOnTopLayers
    //                          - description : deficit On TopLayers
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - default : 5341
    //                          - min : 0
    //                          - max : 10000
    //                          - unit : g m-2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: soilDiffusionConstant
    //                          - description : soil Diffusion Constant
    //                          - parametercategory : soil
    //                          - datatype : DOUBLE
    //                          - default : 4.2
    //                          - min : 0
    //                          - max : 10
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
        //- outputs:
    //            - name: diffusionLimitedEvaporation
    //                          - description : the evaporation from the diffusion limited soil 
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 5000
    //                          - unit : g m-2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        double deficitOnTopLayers = a.getdeficitOnTopLayers();
        double diffusionLimitedEvaporation;
        if (deficitOnTopLayers / 1000.0d <= 0.0d)
        {
            diffusionLimitedEvaporation = 8.3d * 1000.0d;
        }
        else
        {
            if (deficitOnTopLayers / 1000.0d < 25.0d)
            {
                diffusionLimitedEvaporation = 2.0d * soilDiffusionConstant * soilDiffusionConstant / (deficitOnTopLayers / 1000.0d) * 1000.0d;
            }
            else
            {
                diffusionLimitedEvaporation = 0.0d;
            }
        }
        s.setdiffusionLimitedEvaporation(diffusionLimitedEvaporation);
    }
}
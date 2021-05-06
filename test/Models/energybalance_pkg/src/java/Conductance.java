import  java.io.*;
import  java.util.*;
public class Conductance
{
    private double vonKarman;
    public double getvonKarman()
    {
        return vonKarman;
    }

    public void setvonKarman(double _vonKarman)
    {
        this.vonKarman= _vonKarman;
    } 
    
    private double heightWeatherMeasurements;
    public double getheightWeatherMeasurements()
    {
        return heightWeatherMeasurements;
    }

    public void setheightWeatherMeasurements(double _heightWeatherMeasurements)
    {
        this.heightWeatherMeasurements= _heightWeatherMeasurements;
    } 
    
    private double zm;
    public double getzm()
    {
        return zm;
    }

    public void setzm(double _zm)
    {
        this.zm= _zm;
    } 
    
    private double zh;
    public double getzh()
    {
        return zh;
    }

    public void setzh(double _zh)
    {
        this.zh= _zh;
    } 
    
    private double d;
    public double getd()
    {
        return d;
    }

    public void setd(double _d)
    {
        this.d= _d;
    } 
    
    public Conductance()
    {
           
    }
    public void  Calculate_conductance(EnergybalanceState s, EnergybalanceRate r, EnergybalanceAuxiliary a)
    {
        //- Description:
    //            - Model Name: Conductance Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA/LEPSE Montpellier
    //            - Abstract: The boundary layer conductance is expressed as the wind speed profile above the
    //            canopy and the canopy structure. The approach does not take into account buoyancy
    //            effects. 
        //- inputs:
    //            - name: vonKarman
    //                          - description : von Karman constant
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 1
    //                          - default : 0.42
    //                          - unit :  
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //                          - parametercategory : constant
    //            - name: heightWeatherMeasurements
    //                          - description : reference height of wind and humidity measurements
    //                          - parametercategory : soil
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10
    //                          - default : 2
    //                          - unit : m
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: zm
    //                          - description : roughness length governing momentum transfer, FAO
    //                          - parametercategory : constant
    //                          - inputtype : parameter
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 1
    //                          - default : 0.13
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            - name: zh
    //                          - description : roughness length governing transfer of heat and vapour, FAO
    //                          - parametercategory : constant
    //                          - inputtype : parameter
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 1
    //                          - default : 0.013
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            - name: d
    //                          - description : corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO
    //                          - inputtype : parameter
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 0.67
    //                          - min : 0
    //                          - max : 1
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547rl
    //            - name: plantHeight
    //                          - description : plant Height
    //                          - datatype : DOUBLE
    //                          - default : 0
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : mm
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //                          - variablecategory : auxiliary
    //            - name: wind
    //                          - description : wind
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - default : 124000
    //                          - min : 0
    //                          - max : 1000000
    //                          - unit : m d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
        //- outputs:
    //            - name: conductance
    //                          - description : the boundary layer conductance
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - unit : m d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        double plantHeight = a.getplantHeight();
        double wind = a.getwind();
        double conductance;
        double h;
        h = Math.max(10.0d, plantHeight) / 100.0d;
        conductance = wind * Math.pow(vonKarman, 2) / (Math.log((heightWeatherMeasurements - (d * h)) / (zm * h)) * Math.log((heightWeatherMeasurements - (d * h)) / (zh * h)));
        s.setconductance(conductance);
    }
}
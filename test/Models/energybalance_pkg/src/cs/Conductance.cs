using System;
using System.Collections.Generic;
using System.Linq;
public class Conductance
{
    private double _vonKarman;
    public double vonKarman
    {
        get { return this._vonKarman; }
        set { this._vonKarman= value; } 
    }
    private double _heightWeatherMeasurements;
    public double heightWeatherMeasurements
    {
        get { return this._heightWeatherMeasurements; }
        set { this._heightWeatherMeasurements= value; } 
    }
    private double _zm;
    public double zm
    {
        get { return this._zm; }
        set { this._zm= value; } 
    }
    private double _zh;
    public double zh
    {
        get { return this._zh; }
        set { this._zh= value; } 
    }
    private double _d;
    public double d
    {
        get { return this._d; }
        set { this._d= value; } 
    }
    public Conductance() { }
    
    public void  Calculate_conductance(EnergybalanceState s, EnergybalanceState s1, EnergybalanceRate r, EnergybalanceAuxiliary a)
    {
        //- Name: Conductance -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: Conductance Model
    //            * Author: Pierre Martre
    //            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //        
    //            * Institution: INRA/LEPSE Montpellier
    //            * Abstract: The boundary layer conductance is expressed as the wind speed profile above the
    //            canopy and the canopy structure. The approach does not take into account buoyancy
    //            effects. 
    //        
        //- inputs:
    //            * name: vonKarman
    //                          ** description : von Karman constant
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.42
    //                          ** unit : dimensionless
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //            * name: heightWeatherMeasurements
    //                          ** description : reference height of wind and humidity measurements
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10
    //                          ** default : 2
    //                          ** unit : m
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: zm
    //                          ** description : roughness length governing momentum transfer, FAO
    //                          ** parametercategory : constant
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.13
    //                          ** unit : m
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            * name: zh
    //                          ** description : roughness length governing transfer of heat and vapour, FAO
    //                          ** parametercategory : constant
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0.013
    //                          ** unit : m
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            * name: d
    //                          ** description : corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 0.67
    //                          ** min : 0
    //                          ** max : 1
    //                          ** unit : dimensionless
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547rl
    //            * name: plantHeight
    //                          ** description : plant Height
    //                          ** datatype : DOUBLE
    //                          ** default : 0
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : mm
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //                          ** variablecategory : auxiliary
    //            * name: wind
    //                          ** description : wind
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 124000
    //                          ** min : 0
    //                          ** max : 1000000
    //                          ** unit : m/d
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
        //- outputs:
    //            * name: conductance
    //                          ** description : the boundary layer conductance
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : m/d
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        double plantHeight = a.plantHeight;
        double wind = a.wind;
        double conductance;
        double h;
        h = Math.Max(10.0d, plantHeight) / 100.0d;
        conductance = wind * Math.Pow(vonKarman, 2) / (Math.Log((heightWeatherMeasurements - (d * h)) / (zm * h)) * Math.Log((heightWeatherMeasurements - (d * h)) / (zh * h)));
        s.conductance= conductance;
    }
}
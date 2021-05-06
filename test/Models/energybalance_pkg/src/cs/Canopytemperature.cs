using System;
using System.Collections.Generic;
using System.Linq;
public class Canopytemperature
{
    private double _lambdaV;
    public double lambdaV
    {
        get { return this._lambdaV; }
        set { this._lambdaV= value; } 
    }
    private double _rhoDensityAir;
    public double rhoDensityAir
    {
        get { return this._rhoDensityAir; }
        set { this._rhoDensityAir= value; } 
    }
    private double _specificHeatCapacityAir;
    public double specificHeatCapacityAir
    {
        get { return this._specificHeatCapacityAir; }
        set { this._specificHeatCapacityAir= value; } 
    }
    public Canopytemperature() { }
    
    public void  Calculate_canopytemperature(EnergybalanceState s, EnergybalanceState s1, EnergybalanceRate r, EnergybalanceAuxiliary a)
    {
        //- Name: CanopyTemperature -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: CanopyTemperature Model
    //            * Author: Pierre Martre
    //            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            * Institution: INRA/LEPSE Montpellier
    //            * Abstract: It is calculated from the crop heat flux and the boundary layer conductance 
        //- inputs:
    //            * name: minTair
    //                          ** description : minimum air temperature
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : auxiliary
    //                          ** min : -30
    //                          ** max : 45
    //                          ** default : 0.7
    //                          ** unit : degC
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //            * name: maxTair
    //                          ** description : maximum air Temperature
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : auxiliary
    //                          ** min : -30
    //                          ** max : 45
    //                          ** default : 7.2
    //                          ** unit : degC
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //            * name: cropHeatFlux
    //                          ** description : Crop heat flux
    //                          ** variablecategory : rate
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 447.912
    //                          ** unit : g/m**2/d
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            * name: conductance
    //                          ** description : the boundary layer conductance
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 598.685
    //                          ** unit : m/d
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            * name: lambdaV
    //                          ** description : latent heat of vaporization of water
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 2.454
    //                          ** min : 0
    //                          ** max : 10
    //                          ** unit : MJ/kg
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: rhoDensityAir
    //                          ** description : Density of air
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 1.225
    //                          ** unit : kg/m**3
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: specificHeatCapacityAir
    //                          ** description : Specific heat capacity of dry air
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 0.00101
    //                          ** unit : MJ/kg/degC
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
        //- outputs:
    //            * name: minCanopyTemperature
    //                          ** description : minimal Canopy Temperature  
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : state
    //                          ** min : -30
    //                          ** max : 45
    //                          ** unit : degC
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            * name: maxCanopyTemperature
    //                          ** description : maximal Canopy Temperature 
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : state
    //                          ** min : -30
    //                          ** max : 45
    //                          ** unit : degC
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        double minTair = a.minTair;
        double maxTair = a.maxTair;
        double cropHeatFlux = r.cropHeatFlux;
        double conductance = s.conductance;
        double minCanopyTemperature;
        double maxCanopyTemperature;
        minCanopyTemperature = minTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0d));
        maxCanopyTemperature = maxTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0d));
        s.minCanopyTemperature= minCanopyTemperature;
        s.maxCanopyTemperature= maxCanopyTemperature;
    }
}
using System;
using System.Collections.Generic;
using System.Linq;
public class Soilheatflux
{
    private double _tau;
    public double tau
    {
        get { return this._tau; }
        set { this._tau= value; } 
    }
    public Soilheatflux() { }
    
    public void  Calculate_soilheatflux(EnergybalanceState s, EnergybalanceState s1, EnergybalanceRate r, EnergybalanceAuxiliary a)
    {
        //- Name: SoilHeatFlux -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: SoilHeatFlux Model
    //            * Author: Pierre Martre
    //            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            * Institution: INRA/LEPSE Montpellier
    //            * Abstract: The available energy in the soil 
        //- inputs:
    //            * name: netRadiationEquivalentEvaporation
    //                          ** variablecategory : state
    //                          ** description : net Radiation Equivalent Evaporation
    //                          ** datatype : DOUBLE
    //                          ** default : 638.142
    //                          ** min : 0
    //                          ** max : 5000
    //                          ** unit : g m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //            * name: tau
    //                          ** description : plant cover factor
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 0.9983
    //                          ** min : 0
    //                          ** max : 100
    //                          ** unit : 
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: soilEvaporation
    //                          ** description : soil Evaporation
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** default : 448.240
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : g m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
        //- outputs:
    //            * name: soilHeatFlux
    //                          ** description : soil Heat Flux 
    //                          ** variablecategory : rate
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : g m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        double netRadiationEquivalentEvaporation = s.netRadiationEquivalentEvaporation;
        double soilEvaporation = s.soilEvaporation;
        double soilHeatFlux;
        soilHeatFlux = tau * netRadiationEquivalentEvaporation - soilEvaporation;
        r.soilHeatFlux = soilHeatFlux;
    }
}
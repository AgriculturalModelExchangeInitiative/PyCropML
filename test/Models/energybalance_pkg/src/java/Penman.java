import  java.io.*;
import  java.util.*;
public class Penman
{
    private double psychrometricConstant;
    public double getpsychrometricConstant()
    {
        return psychrometricConstant;
    }

    public void setpsychrometricConstant(double _psychrometricConstant)
    {
        this.psychrometricConstant= _psychrometricConstant;
    } 
    
    private double Alpha;
    public double getAlpha()
    {
        return Alpha;
    }

    public void setAlpha(double _Alpha)
    {
        this.Alpha= _Alpha;
    } 
    
    private double lambdaV;
    public double getlambdaV()
    {
        return lambdaV;
    }

    public void setlambdaV(double _lambdaV)
    {
        this.lambdaV= _lambdaV;
    } 
    
    private double rhoDensityAir;
    public double getrhoDensityAir()
    {
        return rhoDensityAir;
    }

    public void setrhoDensityAir(double _rhoDensityAir)
    {
        this.rhoDensityAir= _rhoDensityAir;
    } 
    
    private double specificHeatCapacityAir;
    public double getspecificHeatCapacityAir()
    {
        return specificHeatCapacityAir;
    }

    public void setspecificHeatCapacityAir(double _specificHeatCapacityAir)
    {
        this.specificHeatCapacityAir= _specificHeatCapacityAir;
    } 
    
    public Penman()
    {
           
    }
    public void  Calculate_penman(EnergybalanceState s, EnergybalanceRate r, EnergybalanceAuxiliary a)
    {
        //- Description:
    //            - Model Name: Penman Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA/LEPSE Montpellier
    //            - Abstract: This method is used when wind and vapor pressure daily data are available
    //        
        //- inputs:
    //            - name: evapoTranspirationPriestlyTaylor
    //                          - description : evapoTranspiration of Priestly Taylor 
    //                          - variablecategory : rate
    //                          - datatype : DOUBLE
    //                          - default : 449.367
    //                          - min : 0
    //                          - max : 10000
    //                          - unit : g m-2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: hslope
    //                          - description : the slope of saturated vapor pressure temperature curve at a given temperature 
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - default : 0.584
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : hPa °C-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: VPDair
    //                          - description :  vapour pressure density
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - default : 2.19
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : hPa
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: psychrometricConstant
    //                          - description : psychrometric constant
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 0.66
    //                          - min : 0
    //                          - max : 1
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
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
    //            - name: lambdaV
    //                          - description : latent heat of vaporization of water
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 2.454
    //                          - min : 0
    //                          - max : 10
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: rhoDensityAir
    //                          - description : Density of air
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 1.225
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: specificHeatCapacityAir
    //                          - description : Specific heat capacity of dry air
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 0.00101
    //                          - min : 0
    //                          - max : 1
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: conductance
    //                          - description : conductance
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 598.685
    //                          - unit : m d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
        //- outputs:
    //            - name: evapoTranspirationPenman
    //                          - description :  evapoTranspiration of Penman Monteith
    //                          - variablecategory : rate
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 5000
    //                          - unit : g m-2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        double evapoTranspirationPriestlyTaylor = r.getevapoTranspirationPriestlyTaylor();
        double hslope = a.gethslope();
        double VPDair = a.getVPDair();
        double conductance = s.getconductance();
        double evapoTranspirationPenman;
        evapoTranspirationPenman = evapoTranspirationPriestlyTaylor / Alpha + (1000.0d * (rhoDensityAir * specificHeatCapacityAir * VPDair * conductance / (lambdaV * (hslope + psychrometricConstant))));
        r.setevapoTranspirationPenman(evapoTranspirationPenman);
    }
}
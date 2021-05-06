import  java.io.*;
import  java.util.*;
public class Netradiation
{
    private double albedoCoefficient;
    public double getalbedoCoefficient()
    {
        return albedoCoefficient;
    }

    public void setalbedoCoefficient(double _albedoCoefficient)
    {
        this.albedoCoefficient= _albedoCoefficient;
    } 
    
    private double stefanBoltzman;
    public double getstefanBoltzman()
    {
        return stefanBoltzman;
    }

    public void setstefanBoltzman(double _stefanBoltzman)
    {
        this.stefanBoltzman= _stefanBoltzman;
    } 
    
    private double elevation;
    public double getelevation()
    {
        return elevation;
    }

    public void setelevation(double _elevation)
    {
        this.elevation= _elevation;
    } 
    
    public Netradiation()
    {
           
    }
    public void  Calculate_netradiation(EnergybalanceState s, EnergybalanceRate r, EnergybalanceAuxiliary a)
    {
        //- Description:
    //            - Model Name: NetRadiation Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA Montpellier
    //            - Abstract: It is calculated at the surface of the canopy and is givenby the difference between incoming and outgoing radiation of both short
    //                     and long wavelength radiation 
        //- inputs:
    //            - name: minTair
    //                          - description : minimum air temperature
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : -30
    //                          - max : 45
    //                          - default : 0.7
    //                          - unit : °C
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: maxTair
    //                          - description : maximum air Temperature
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : -30
    //                          - max : 45
    //                          - default : 7.2
    //                          - unit : °C
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: albedoCoefficient
    //                          - description : albedo Coefficient
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 0.23
    //                          - min : 0
    //                          - max : 1
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: stefanBoltzman
    //                          - description : stefan Boltzman constant
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 4.903E-09
    //                          - min : 0
    //                          - max : 1
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: elevation
    //                          - description : elevation
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 0
    //                          - min : -500
    //                          - max : 10000
    //                          - unit : m
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: solarRadiation
    //                          - description : solar Radiation
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - default : 3
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : MJ m-2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: vaporPressure
    //                          - description : vapor Pressure
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - default : 6.1
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : hPa
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: extraSolarRadiation
    //                          - description : extra Solar Radiation
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - default : 11.7
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : MJ m2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
        //- outputs:
    //            - name: netRadiation
    //                          - description :  net radiation 
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 5000
    //                          - unit : MJ m-2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            - name: netOutGoingLongWaveRadiation
    //                          - description : net OutGoing Long Wave Radiation 
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 5000
    //                          - unit : g m-2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        double minTair = a.getminTair();
        double maxTair = a.getmaxTair();
        double solarRadiation = a.getsolarRadiation();
        double vaporPressure = a.getvaporPressure();
        double extraSolarRadiation = a.getextraSolarRadiation();
        double netRadiation;
        double netOutGoingLongWaveRadiation;
        double Nsr;
        double clearSkySolarRadiation;
        double averageT;
        double surfaceEmissivity;
        double cloudCoverFactor;
        double Nolr;
        Nsr = (1.0d - albedoCoefficient) * solarRadiation;
        clearSkySolarRadiation = (0.75d + (2 * Math.pow(10.0d, -5) * elevation)) * extraSolarRadiation;
        averageT = (Math.pow(maxTair + 273.16d, 4) + Math.pow(minTair + 273.16d, 4)) / 2.0d;
        surfaceEmissivity = 0.34d - (0.14d * Math.sqrt(vaporPressure / 10.0d));
        cloudCoverFactor = 1.35d * (solarRadiation / clearSkySolarRadiation) - 0.35d;
        Nolr = stefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor;
        netRadiation = Nsr - Nolr;
        netOutGoingLongWaveRadiation = Nolr;
        a.setnetRadiation(netRadiation);
        a.setnetOutGoingLongWaveRadiation(netOutGoingLongWaveRadiation);
    }
}
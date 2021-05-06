import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import javafx.util.*;
import java.time.LocalDateTime;
public class Phylsowingdatecorrection
{
    private int sowingDay;
    public int getsowingDay()
    { return sowingDay; }

    public void setsowingDay(int _sowingDay)
    { this.sowingDay= _sowingDay; } 
    
    private double latitude;
    public double getlatitude()
    { return latitude; }

    public void setlatitude(double _latitude)
    { this.latitude= _latitude; } 
    
    private double sDsa_sh;
    public double getsDsa_sh()
    { return sDsa_sh; }

    public void setsDsa_sh(double _sDsa_sh)
    { this.sDsa_sh= _sDsa_sh; } 
    
    private double rp;
    public double getrp()
    { return rp; }

    public void setrp(double _rp)
    { this.rp= _rp; } 
    
    private int sDws;
    public int getsDws()
    { return sDws; }

    public void setsDws(int _sDws)
    { this.sDws= _sDws; } 
    
    private double sDsa_nh;
    public double getsDsa_nh()
    { return sDsa_nh; }

    public void setsDsa_nh(double _sDsa_nh)
    { this.sDsa_nh= _sDsa_nh; } 
    
    private double p;
    public double getp()
    { return p; }

    public void setp(double _p)
    { this.p= _p; } 
    
    public Phylsowingdatecorrection() { }
    public void  Calculate_phylsowingdatecorrection(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: PhylSowingDateCorrection -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: PhylSowingDateCorrection Model
    //            * Author: Loic Manceau
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Correction of the Phyllochron Varietal parameter according to sowing date 
        //- inputs:
    //            * name: sowingDay
    //                          ** description : Day of Year at sowing
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** min : 1
    //                          ** max : 365
    //                          ** default : 1
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: latitude
    //                          ** description : Latitude
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLE
    //                          ** min : -90
    //                          ** max : 90
    //                          ** default : 0.0
    //                          ** unit : °
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: sDsa_sh
    //                          ** description : Sowing date at which Phyllochrone is maximum in southern hemispher
    //                          ** parametercategory : species
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 1
    //                          ** max : 365
    //                          ** default : 1.0
    //                          ** unit : d
    //                          ** uri : some url
    //            * name: rp
    //                          ** description : Rate of change of Phyllochrone with sowing date
    //                          ** parametercategory : species
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 365
    //                          ** default : 0
    //                          ** unit : d-1
    //                          ** uri : some url
    //            * name: sDws
    //                          ** description : Sowing date at which Phyllochrone is minimum
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** default : 1
    //                          ** min : 1
    //                          ** max : 365
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: sDsa_nh
    //                          ** description : Sowing date at which Phyllochrone is maximum in northern hemispher
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 1.0
    //                          ** min : 1
    //                          ** max : 365
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: p
    //                          ** description : Phyllochron (Varietal parameter)
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 120
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : °C d leaf-1
    //                          ** uri : some url
    //                          ** inputtype : parameter
        //- outputs:
    //            * name: fixPhyll
    //                          ** description :  Phyllochron Varietal parameter 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : °C d leaf-1
        double fixPhyll;
        if (latitude < 0.0d)
        {
            if (sowingDay > (int)(sDsa_sh))
            {
                fixPhyll = p * (1 - (rp * Math.min((sowingDay - sDsa_sh), sDws)));
            }
            else
            {
                fixPhyll = p;
            }
        }
        else
        {
            if (sowingDay < (int)(sDsa_nh))
            {
                fixPhyll = p * (1 - (rp * Math.min(sowingDay, sDws)));
            }
            else
            {
                fixPhyll = p;
            }
        }
        a.setfixPhyll(fixPhyll);
    }
}
import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import javafx.util.*;
import java.time.LocalDateTime;
public class Gaimean
{
    private double tTWindowForPTQ;
    public double gettTWindowForPTQ()
    { return tTWindowForPTQ; }

    public void settTWindowForPTQ(double _tTWindowForPTQ)
    { this.tTWindowForPTQ= _tTWindowForPTQ; } 
    
    public Gaimean() { }
    public void  Calculate_gaimean(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: GAImean -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: Average GAI on a specific thermal time window
    //            * Author: Loïc Manceau
    //            * Reference: -
    //            * Institution: INRA
    //            * Abstract: -
        //- inputs:
    //            * name: gAI
    //                          ** description : Green Area Index of the day
    //                          ** inputtype : variable
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 500.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: tTWindowForPTQ
    //                          ** description : Thermal Time window for average
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 5000.0
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: deltaTT
    //                          ** description : Thermal time increase of the day
    //                          ** inputtype : variable
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 100.0
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: pastMaxAI_t1
    //                          ** description : Maximum Leaf Area Index reached the current day
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 5000.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: listTTShootWindowForPTQ1_t1
    //                          ** description : List of daily shoot thermal time in the window dedicated to average
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: listGAITTWindowForPTQ_t1
    //                          ** description : List of daily Green Area Index in the window dedicated to average
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [0.0]
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
        //- outputs:
    //            * name: gAImean
    //                          ** description : Mean Green Area Index
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 500.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: pastMaxAI
    //                          ** description : Maximum Leaf Area Index reached the current day
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 5000.0
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
    //            * name: listTTShootWindowForPTQ1
    //                          ** description : List of daily shoot thermal time in the window dedicated to average
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : °C d
    //                          ** uri : 
    //            * name: listGAITTWindowForPTQ
    //                          ** description : List of daily Green Area Index in the window dedicated to average
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : m2 leaf m-2 ground
    //                          ** uri : 
        double gAI = a.getgAI();
        double deltaTT = a.getdeltaTT();
        double pastMaxAI_t1 = s1.getpastMaxAI();
        List<Double> listTTShootWindowForPTQ1_t1 = s1.getlistTTShootWindowForPTQ1();
        List<Double> listGAITTWindowForPTQ_t1 = s1.getlistGAITTWindowForPTQ();
        double gAImean;
        double pastMaxAI;
        List<Double> listTTShootWindowForPTQ1 = new ArrayList<>(Arrays.asList());
        List<Double> listGAITTWindowForPTQ = new ArrayList<>(Arrays.asList());
        List<Double> TTList = new ArrayList<>(Arrays.asList());
        List<Double> GAIList = new ArrayList<>(Arrays.asList());
        double SumTT;
        int count = 0;
        double gai_ = 0.0d;
        double gaiMean_ = 0.0d;
        int countGaiMean = 0;
        int i;
        for (i=0 ; i<listTTShootWindowForPTQ1_t1.size() ; i+=1)
        {
            TTList.add(listTTShootWindowForPTQ1_t1.get(i));
            GAIList.add(listGAITTWindowForPTQ_t1.get(i));
        }
        TTList.add(deltaTT);
        GAIList.add(gAI);
        SumTT = TTList.stream().mapToDouble(Double::doubleValue).sum();
        while ( SumTT > tTWindowForPTQ)
        {
            SumTT = SumTT - TTList.get(count);
            count = count + 1;
        }
        for (i=count ; i<TTList.size() ; i+=1)
        {
            listTTShootWindowForPTQ1.add(TTList.get(i));
            listGAITTWindowForPTQ.add(GAIList.get(i));
        }
        for (i=0 ; i<listGAITTWindowForPTQ.size() ; i+=1)
        {
            gaiMean_ = gaiMean_ + listGAITTWindowForPTQ.get(i);
            countGaiMean = countGaiMean + 1;
        }
        gaiMean_ = gaiMean_ / countGaiMean;
        gai_ = Math.max(pastMaxAI_t1, gaiMean_);
        pastMaxAI = gai_;
        gAImean = gai_;
        s.setgAImean(gAImean);
        s.setpastMaxAI(pastMaxAI);
        s.setlistTTShootWindowForPTQ1(listTTShootWindowForPTQ1);
        s.setlistGAITTWindowForPTQ(listGAITTWindowForPTQ);
    }
}
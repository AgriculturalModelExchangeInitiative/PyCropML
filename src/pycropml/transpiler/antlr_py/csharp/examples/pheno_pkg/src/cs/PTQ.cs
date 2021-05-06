using System;
using System.Collections.Generic;
using System.Linq;
public class PTQ
{
    private double _tTWindowForPTQ;
    public double tTWindowForPTQ
        {
            get { return this._tTWindowForPTQ; }
            set { this._tTWindowForPTQ= value; } 
        }
    private double _kl;
    public double kl
        {
            get { return this._kl; }
            set { this._kl= value; } 
        }
    public PTQ() { }
    
    public void  CalculateModel(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: PTQ -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: Phyllochron Model
    //            * Author: Pierre Martre
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Calculate Photothermal Quaotient 
        //- inputs:
    //            * name: tTWindowForPTQ
    //                          ** description : Thermal time window in which averages are computed
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 70000.0
    //                          ** default : 70.0
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: kl
    //                          ** description : Exctinction Coefficient
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 50.0
    //                          ** default : 0.45
    //                          ** unit : 
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: listTTShootWindowForPTQ_t1
    //                          ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** default : [0.0]
    //                          ** unit : °C d
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: listPARTTWindowForPTQ_t1
    //                          ** description : List of Daily PAR during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** default : [0.0]
    //                          ** unit : MJ m2 d
    //                          ** uri : some url
    //            * name: listGAITTWindowForPTQ
    //                          ** description : List of daily GAI over TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** default : [0.0, 5.2]
    //                          ** unit : m2 m-2
    //                          ** uri : some url
    //            * name: pAR
    //                          ** description : Daily Photosyntetically Active Radiation
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 0.0
    //                          ** min : 0.0
    //                          ** max : 10000.0
    //                          ** unit : MJ m² d
    //                          ** uri : some url
    //                          ** inputtype : variable
    //            * name: deltaTT
    //                          ** description : daily delta TT 
    //                          ** variablecategory : auxiliary
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0.0
    //                          ** max : 100.0
    //                          ** default : 0.0
    //                          ** unit : °C d
    //                          ** uri : some url
        //- outputs:
    //            * name: listPARTTWindowForPTQ
    //                          ** description :  List of Daily PAR during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : MJ m2 d
    //            * name: listTTShootWindowForPTQ
    //                          ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** min : 
    //                          ** max : 
    //                          ** unit : °C d
    //            * name: ptq
    //                          ** description : Photothermal Quotient
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : MJ °C-1 d m-2)
        List<double> listTTShootWindowForPTQ_t1 = s1.listTTShootWindowForPTQ;
        List<double> listPARTTWindowForPTQ_t1 = s1.listPARTTWindowForPTQ;
        List<double> listGAITTWindowForPTQ = s.listGAITTWindowForPTQ;
        double pAR = a.pAR;
        double deltaTT = a.deltaTT;
        List<double> listPARTTWindowForPTQ = new List<double>();
        List<double> listTTShootWindowForPTQ = new List<double>();
        double ptq;
        List<double> TTList = new List<double>();
        List<double> PARList = new List<double>();
        int i;
        int count;
        double SumTT;
        double parInt = 0.0d;
        double TTShoot;
        for (i=0 ; i<listTTShootWindowForPTQ_t1.Count ; i+=1)
        {
            TTList.Add(listTTShootWindowForPTQ_t1[i]);
            PARList.Add(listPARTTWindowForPTQ_t1[i]);
        }
        TTList.Add(deltaTT);
        PARList.Add(pAR);
        SumTT = TTList.Sum();
        count = 0;
        while ( SumTT > tTWindowForPTQ)
        {
            SumTT = SumTT - TTList[count];
            count = count + 1;
        }
        for (i=count ; i<TTList.Count ; i+=1)
        {
            listTTShootWindowForPTQ.Add(TTList[i]);
            listPARTTWindowForPTQ.Add(PARList[i]);
        }
        for (i=0 ; i<listTTShootWindowForPTQ.Count ; i+=1)
        {
            parInt = parInt + (listPARTTWindowForPTQ[i] * (1 - Math.Exp(-kl * listGAITTWindowForPTQ[i])));
        }
        TTShoot = listTTShootWindowForPTQ.Sum();
        ptq = parInt / TTShoot;
        s.listPARTTWindowForPTQ= listPARTTWindowForPTQ;
        s.listTTShootWindowForPTQ= listTTShootWindowForPTQ;
        s.ptq= ptq;
    }
}
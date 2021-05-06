using System;
using System.Collections.Generic;
using System.Linq;
public class LeafNumber
{
    
    public LeafNumber() { }
    
    public void  CalculateModel(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: LeafNumber -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: CalculateLeafNumber Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day
        //- inputs:
    //            * name: deltaTT
    //                          ** description : daily delta TT 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : -20
    //                          ** max : 100
    //                          ** default : 23.5895677277199
    //                          ** unit : °C d
    //                          ** inputtype : variable
    //            * name: phyllochron_t1
    //                          ** description : phyllochron
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** default : 0
    //                          ** unit : °C d leaf-1
    //            * name: hasFlagLeafLiguleAppeared
    //                          ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 1
    //                          ** default : 0
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: leafNumber_t1
    //                          ** description :  Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 25
    //                          ** default : 0
    //                          ** unit : leaf
    //                          ** inputtype : variable
    //            * name: phase
    //                          ** description :  the name of the phase
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 7
    //                          ** default : 1
    //                          ** unit :  
    //                          ** uri : some url
    //                          ** inputtype : variable
        //- outputs:
    //            * name: leafNumber
    //                          ** description : Actual number of phytomers
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : leaf
    //                          ** uri : some url
        double deltaTT = a.deltaTT;
        double phyllochron_t1 = s1.phyllochron;
        int hasFlagLeafLiguleAppeared = s.hasFlagLeafLiguleAppeared;
        double leafNumber_t1 = s1.leafNumber;
        double phase = s.phase;
        double leafNumber;
        leafNumber = leafNumber_t1;
        double phyllochron_;
        if (phase >= 1.0d && phase < 4.0d)
        {
            if (hasFlagLeafLiguleAppeared == 0)
            {
                if (phyllochron_t1 == 0.0d)
                {
                    phyllochron_ = 0.0000001d;
                }
                else
                {
                    phyllochron_ = phyllochron_t1;
                }
                leafNumber = leafNumber_t1 + Math.Min(deltaTT / phyllochron_, 0.999d);
            }
        }
        s.leafNumber= leafNumber;
    }
}
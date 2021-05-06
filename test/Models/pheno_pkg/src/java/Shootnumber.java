import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
public class Shootnumber
{
    private double sowingDensity;
    public double getsowingDensity()
    { return sowingDensity; }

    public void setsowingDensity(double _sowingDensity)
    { this.sowingDensity= _sowingDensity; } 
    
    private double targetFertileShoot;
    public double gettargetFertileShoot()
    { return targetFertileShoot; }

    public void settargetFertileShoot(double _targetFertileShoot)
    { this.targetFertileShoot= _targetFertileShoot; } 
    
    public Shootnumber() { }
    public void  Calculate_shootnumber(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        //- Name: ShootNumber -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: CalculateShootNumber Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA/LEPSE Montpellier
    //            * Abstract: calculate the shoot number and update the related variables if needed
        //- inputs:
    //            * name: canopyShootNumber_t1
    //                          ** description : shoot number for the whole canopy
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 288.0
    //                          ** unit : shoot m-2
    //                          ** inputtype : variable
    //            * name: leafNumber
    //                          ** description : Leaf number 
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 3.34
    //                          ** unit : leaf
    //            * name: sowingDensity
    //                          ** description : number of plant /m²
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 500
    //                          ** default : 288.0
    //                          ** unit : plant m-2
    //                          ** inputtype : parameter
    //            * name: targetFertileShoot
    //                          ** description : max value of shoot number for the canopy
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 280
    //                          ** max : 1000
    //                          ** default : 600.0
    //                          ** unit : shoot
    //                          ** inputtype : variable
    //            * name: tilleringProfile_t1
    //                          ** description :  store the amount of new tiller created at each time a new tiller appears
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [288.0]
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: leafTillerNumberArray_t1
    //                          ** description : store the number of tiller for each leaf layer
    //                          ** variablecategory : state
    //                          ** datatype : INTLIST
    //                          ** unit : leaf
    //                          ** default : [1, 1, 1]
    //                          ** inputtype : variable
    //            * name: numberTillerCohort_t1
    //                          ** description :  Number of tiller which appears
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : variable
        //- outputs:
    //            * name: averageShootNumberPerPlant
    //                          ** description : average shoot number per plant in the canopy
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : shoot m-2
    //            * name: canopyShootNumber
    //                          ** description : shoot number for the whole canopy
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : shoot m-2
    //            * name: leafTillerNumberArray
    //                          ** description : store the number of tiller for each leaf layer
    //                          ** variablecategory : state
    //                          ** datatype : INTLIST
    //                          ** unit : leaf
    //            * name: tilleringProfile
    //                          ** description :  store the amount of new tiller created at each time a new tiller appears
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** unit : dimensionless
    //            * name: numberTillerCohort
    //                          ** description : Number of tiller which appears
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : dimensionless
        double canopyShootNumber_t1 = s1.getcanopyShootNumber();
        double leafNumber = s.getleafNumber();
        List<Double> tilleringProfile_t1 = s1.gettilleringProfile();
        List<Integer> leafTillerNumberArray_t1 = s1.getleafTillerNumberArray();
        int numberTillerCohort_t1 = s1.getnumberTillerCohort();
        double averageShootNumberPerPlant;
        double canopyShootNumber;
        List<Integer> leafTillerNumberArray = new ArrayList<>(Arrays.asList());
        List<Double> tilleringProfile = new ArrayList<>(Arrays.asList());
        int numberTillerCohort;
        int emergedLeaves;
        int shoots;
        int i;
        List<Integer> lNumberArray_rate = new ArrayList<>(Arrays.asList());
        emergedLeaves = Math.max(1, (int) Math.ceil(leafNumber - 1.0d));
        shoots = fibonacci(emergedLeaves);
        canopyShootNumber = Math.min(shoots * sowingDensity, targetFertileShoot);
        averageShootNumberPerPlant = canopyShootNumber / sowingDensity;
        if (canopyShootNumber != canopyShootNumber_t1)
        {
            tilleringProfile = new ArrayList<>(tilleringProfile_t1);
            tilleringProfile.add(canopyShootNumber - canopyShootNumber_t1);
        }
        numberTillerCohort = tilleringProfile.size();
        for (i=leafTillerNumberArray_t1.size() ; i<(int) Math.ceil(leafNumber) ; i+=1)
        {
            lNumberArray_rate.add(numberTillerCohort);
        }
        leafTillerNumberArray = new ArrayList<>(leafTillerNumberArray_t1);
        leafTillerNumberArray.addAll(lNumberArray_rate);
        s.setaverageShootNumberPerPlant(averageShootNumberPerPlant);
        s.setcanopyShootNumber(canopyShootNumber);
        s.setleafTillerNumberArray(leafTillerNumberArray);
        s.settilleringProfile(tilleringProfile);
        s.setnumberTillerCohort(numberTillerCohort);
    }
    public static int fibonacci(int n)
    {
        if (n <= 1)
        {
            return n;
        }
        else
        {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }
    public void Init(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a)
    {
        double canopyShootNumber_t1;
        double leafNumber;
        List<Double> tilleringProfile_t1 = new ArrayList<>(Arrays.asList());
        List<Integer> leafTillerNumberArray_t1 = new ArrayList<>(Arrays.asList());
        int numberTillerCohort_t1;
        double averageShootNumberPerPlant;
        double canopyShootNumber;
        List<Integer> leafTillerNumberArray = new ArrayList<>(Arrays.asList());
        List<Double> tilleringProfile = new ArrayList<>(Arrays.asList());
        int numberTillerCohort;
        canopyShootNumber = sowingDensity;
        averageShootNumberPerPlant = 1.0d;
        tilleringProfile.add(sowingDensity);
        numberTillerCohort = 1;
        leafTillerNumberArray = new ArrayList<>(Arrays.asList());
        s.setaverageShootNumberPerPlant(averageShootNumberPerPlant);
        s.setcanopyShootNumber(canopyShootNumber);
        s.setleafTillerNumberArray(leafTillerNumberArray);
        s.settilleringProfile(tilleringProfile);
        s.setnumberTillerCohort(numberTillerCohort);
    }
}
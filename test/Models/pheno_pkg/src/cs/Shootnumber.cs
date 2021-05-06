


















    public void  Calculate_shootnumber(State s, State s1, Rate r, Auxiliary a)
    {
        ...
        double canopyShootNumber_t1 = s1.canopyShootNumber;
        double leafNumber = s.leafNumber;
        List<double> tilleringProfile_t1 = s1.tilleringProfile;
        List<int> leafTillerNumberArray_t1 = s1.leafTillerNumberArray;
        int numberTillerCohort_t1 = s1.numberTillerCohort;
        
        ...  
              
    }

        double averageShootNumberPerPlant;
        double canopyShootNumber;
        List<int> leafTillerNumberArray = new List<int>();
        List<double> tilleringProfile = new List<double>();
        int numberTillerCohort;
        int emergedLeaves;
        int shoots;
        int i;
        List<int> lNumberArray_rate = new List<int>();
        emergedLeaves = Math.Max(1, (int) Math.Ceiling(leafNumber - 1.0d));
        shoots = fibonacci(emergedLeaves);
        canopyShootNumber = Math.Min(shoots * sowingDensity, targetFertileShoot);
        averageShootNumberPerPlant = canopyShootNumber / sowingDensity;
        if (canopyShootNumber != canopyShootNumber_t1)
        {
            tilleringProfile = new List<double>(tilleringProfile_t1);
            tilleringProfile.Add(canopyShootNumber - canopyShootNumber_t1);
        }
        numberTillerCohort = tilleringProfile.Count;
        for (i=leafTillerNumberArray_t1.Count ; i<(int) Math.Ceiling(leafNumber) ; i+=1)
        {
            lNumberArray_rate.Add(numberTillerCohort);
        }
        leafTillerNumberArray = new List<int>(leafTillerNumberArray_t1);
        leafTillerNumberArray.AddRange(lNumberArray_rate);
        s.averageShootNumberPerPlant= averageShootNumberPerPlant;
        s.canopyShootNumber= canopyShootNumber;
        s.leafTillerNumberArray= leafTillerNumberArray;
        s.tilleringProfile= tilleringProfile;
        s.numberTillerCohort= numberTillerCohort;
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
        List<double> tilleringProfile_t1 = new List<double>();
        List<int> leafTillerNumberArray_t1 = new List<int>();
        int numberTillerCohort_t1;
        double averageShootNumberPerPlant;
        double canopyShootNumber;
        List<int> leafTillerNumberArray = new List<int>();
        List<double> tilleringProfile = new List<double>();
        int numberTillerCohort;
        canopyShootNumber = sowingDensity;
        averageShootNumberPerPlant = 1.0d;
        tilleringProfile.Add(sowingDensity);
        numberTillerCohort = 1;
        leafTillerNumberArray = new List<int>{};
        s.averageShootNumberPerPlant= averageShootNumberPerPlant;
        s.canopyShootNumber= canopyShootNumber;
        s.leafTillerNumberArray= leafTillerNumberArray;
        s.tilleringProfile= tilleringProfile;
        s.numberTillerCohort= numberTillerCohort;
    }
}
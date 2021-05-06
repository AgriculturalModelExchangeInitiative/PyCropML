    for (i=leafTillerNumberArray_t1.size() ; i<(int) ceil(leafNumber) ; i+=1)
    {
        lNumberArray_rate.push_back(numberTillerCohort);
    }

    leafTillerNumberArray = leafTillerNumberArray_t1;
    leafTillerNumberArray.reserve(leafTillerNumberArray.size() + distance(lNumberArray_rate.begin(),lNumberArray_rate.end()));
    leafTillerNumberArray.insert(leafTillerNumberArray.end(),lNumberArray_rate.begin(),lNumberArray_rate.end());
    s.setaverageShootNumberPerPlant(averageShootNumberPerPlant);
    s.setcanopyShootNumber(canopyShootNumber);
    s.setleafTillerNumberArray(leafTillerNumberArray);
    s.settilleringProfile(tilleringProfile);
    s.setnumberTillerCohort(numberTillerCohort);
}
int Shootnumber:: fibonacci(int n)
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
void Shootnumber::Init(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
{
    float canopyShootNumber_t1;
    float leafNumber;
    vector<float> tilleringProfile_t1;
    vector<int> leafTillerNumberArray_t1;
    int numberTillerCohort_t1;
    float averageShootNumberPerPlant;
    float canopyShootNumber;
    vector<int> leafTillerNumberArray;
    vector<float> tilleringProfile;
    int numberTillerCohort;
    canopyShootNumber = sowingDensity;
    averageShootNumberPerPlant = 1.0f;
    tilleringProfile.push_back(sowingDensity);
    numberTillerCohort = 1;
    leafTillerNumberArray = vector<int>{};
    s.setaverageShootNumberPerPlant(averageShootNumberPerPlant);
    s.setcanopyShootNumber(canopyShootNumber);
    s.setleafTillerNumberArray(leafTillerNumberArray);
    s.settilleringProfile(tilleringProfile);
    s.setnumberTillerCohort(numberTillerCohort);
}
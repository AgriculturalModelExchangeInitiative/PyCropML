#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "PhenologyState.h"
#include "PhenologyRate.h"
#include "PhenologyAuxiliary.h"
using namespace std;
class Registerzadok
{
    private:
        float der;
        float slopeTSFLN;
        float intTSFLN;
        string sowingDate;
    public:
        Registerzadok();
        void  Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        void  Init(PhenologyState& s,PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        float getder();
        void setder(float _der);
        float getslopeTSFLN();
        void setslopeTSFLN(float _slopeTSFLN);
        float getintTSFLN();
        void setintTSFLN(float _intTSFLN);
        string getsowingDate();
        void setsowingDate(string _sowingDate);

};
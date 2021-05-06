#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "EnergybalanceState.h"
#include "EnergybalanceRate.h"
#include "EnergybalanceAuxiliary.h"
using namespace std;
class Evapotranspiration
{
    private:
        int isWindVpDefined;
    public:
        Evapotranspiration();
        void  Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a);
        int getisWindVpDefined();
        void setisWindVpDefined(int _isWindVpDefined);

};
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "EnergybalanceState.h"
#include "EnergybalanceRate.h"
#include "EnergybalanceAuxiliary.h"
using namespace std;
class Canopytemperature
{
    private:
        float lambdaV;
        float rhoDensityAir;
        float specificHeatCapacityAir;
    public:
        Canopytemperature();
        void  Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a);
        float getlambdaV();
        void setlambdaV(float _lambdaV);
        float getrhoDensityAir();
        void setrhoDensityAir(float _rhoDensityAir);
        float getspecificHeatCapacityAir();
        void setspecificHeatCapacityAir(float _specificHeatCapacityAir);

};
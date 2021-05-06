#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "EnergybalanceState.h"
#include "EnergybalanceRate.h"
#include "EnergybalanceAuxiliary.h"
using namespace std;
class Penman
{
    private:
        float psychrometricConstant;
        float Alpha;
        float lambdaV;
        float rhoDensityAir;
        float specificHeatCapacityAir;
    public:
        Penman();
        void  Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a);
        float getpsychrometricConstant();
        void setpsychrometricConstant(float _psychrometricConstant);
        float getAlpha();
        void setAlpha(float _Alpha);
        float getlambdaV();
        void setlambdaV(float _lambdaV);
        float getrhoDensityAir();
        void setrhoDensityAir(float _rhoDensityAir);
        float getspecificHeatCapacityAir();
        void setspecificHeatCapacityAir(float _specificHeatCapacityAir);

};
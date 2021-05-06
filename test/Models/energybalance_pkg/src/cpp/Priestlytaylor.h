#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "EnergybalanceState.h"
#include "EnergybalanceRate.h"
#include "EnergybalanceAuxiliary.h"
using namespace std;
class Priestlytaylor
{
    private:
        float psychrometricConstant;
        float Alpha;
    public:
        Priestlytaylor();
        void  Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a);
        float getpsychrometricConstant();
        void setpsychrometricConstant(float _psychrometricConstant);
        float getAlpha();
        void setAlpha(float _Alpha);

};
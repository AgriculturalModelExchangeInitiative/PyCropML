#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "EnergybalanceState.h"
#include "EnergybalanceRate.h"
#include "EnergybalanceAuxiliary.h"
using namespace std;
class Ptsoil
{
    private:
        float Alpha;
        float tau;
        float tauAlpha;
    public:
        Ptsoil();
        void  Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a);
        float getAlpha();
        void setAlpha(float _Alpha);
        float gettau();
        void settau(float _tau);
        float gettauAlpha();
        void settauAlpha(float _tauAlpha);

};
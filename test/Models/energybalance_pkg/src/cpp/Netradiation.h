#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "EnergybalanceState.h"
#include "EnergybalanceRate.h"
#include "EnergybalanceAuxiliary.h"
using namespace std;
class Netradiation
{
    private:
        float albedoCoefficient;
        float stefanBoltzman;
        float elevation;
    public:
        Netradiation();
        void  Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a);
        float getalbedoCoefficient();
        void setalbedoCoefficient(float _albedoCoefficient);
        float getstefanBoltzman();
        void setstefanBoltzman(float _stefanBoltzman);
        float getelevation();
        void setelevation(float _elevation);

};
#ifndef _EnergybalanceState_
#define _EnergybalanceState_
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
using namespace std;
class EnergybalanceState
{
    private:
        float diffusionLimitedEvaporation;
        float conductance;
        float minCanopyTemperature;
        float maxCanopyTemperature;
    public:
        EnergybalanceState();
        float getdiffusionLimitedEvaporation();
        void setdiffusionLimitedEvaporation(float _diffusionLimitedEvaporation);
        float getconductance();
        void setconductance(float _conductance);
        float getminCanopyTemperature();
        void setminCanopyTemperature(float _minCanopyTemperature);
        float getmaxCanopyTemperature();
        void setmaxCanopyTemperature(float _maxCanopyTemperature);

};
#endif
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "EnergybalanceState.h"
#include "EnergybalanceRate.h"
#include "EnergybalanceAuxiliary.h"
using namespace std;
class Conductance
{
    private:
        float vonKarman;
        float heightWeatherMeasurements;
        float zm;
        float zh;
        float d;
    public:
        Conductance();
        void  Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a);
        float getvonKarman();
        void setvonKarman(float _vonKarman);
        float getheightWeatherMeasurements();
        void setheightWeatherMeasurements(float _heightWeatherMeasurements);
        float getzm();
        void setzm(float _zm);
        float getzh();
        void setzh(float _zh);
        float getd();
        void setd(float _d);

};
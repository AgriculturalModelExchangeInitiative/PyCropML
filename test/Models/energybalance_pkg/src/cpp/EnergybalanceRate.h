#ifndef _EnergybalanceRate_
#define _EnergybalanceRate_
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
using namespace std;
class EnergybalanceRate
{
    private:
        float evapoTranspirationPriestlyTaylor;
        float evapoTranspirationPenman;
        float evapoTranspiration;
        float potentialTranspiration;
        float soilHeatFlux;
        float cropHeatFlux;
    public:
        EnergybalanceRate();
        float getevapoTranspirationPriestlyTaylor();
        void setevapoTranspirationPriestlyTaylor(float _evapoTranspirationPriestlyTaylor);
        float getevapoTranspirationPenman();
        void setevapoTranspirationPenman(float _evapoTranspirationPenman);
        float getevapoTranspiration();
        void setevapoTranspiration(float _evapoTranspiration);
        float getpotentialTranspiration();
        void setpotentialTranspiration(float _potentialTranspiration);
        float getsoilHeatFlux();
        void setsoilHeatFlux(float _soilHeatFlux);
        float getcropHeatFlux();
        void setcropHeatFlux(float _cropHeatFlux);

};
#endif
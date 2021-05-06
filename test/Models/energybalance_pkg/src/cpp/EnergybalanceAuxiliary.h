#ifndef _EnergybalanceAuxiliary_
#define _EnergybalanceAuxiliary_
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
using namespace std;
class EnergybalanceAuxiliary
{
    private:
        float minTair;
        float maxTair;
        float solarRadiation;
        float vaporPressure;
        float extraSolarRadiation;
        float hslope;
        float plantHeight;
        float wind;
        float deficitOnTopLayers;
        float VPDair;
        float netRadiation;
        float netOutGoingLongWaveRadiation;
        float netRadiationEquivalentEvaporation;
        float energyLimitedEvaporation;
        float soilEvaporation;
    public:
        EnergybalanceAuxiliary();
        float getminTair();
        void setminTair(float _minTair);
        float getmaxTair();
        void setmaxTair(float _maxTair);
        float getsolarRadiation();
        void setsolarRadiation(float _solarRadiation);
        float getvaporPressure();
        void setvaporPressure(float _vaporPressure);
        float getextraSolarRadiation();
        void setextraSolarRadiation(float _extraSolarRadiation);
        float gethslope();
        void sethslope(float _hslope);
        float getplantHeight();
        void setplantHeight(float _plantHeight);
        float getwind();
        void setwind(float _wind);
        float getdeficitOnTopLayers();
        void setdeficitOnTopLayers(float _deficitOnTopLayers);
        float getVPDair();
        void setVPDair(float _VPDair);
        float getnetRadiation();
        void setnetRadiation(float _netRadiation);
        float getnetOutGoingLongWaveRadiation();
        void setnetOutGoingLongWaveRadiation(float _netOutGoingLongWaveRadiation);
        float getnetRadiationEquivalentEvaporation();
        void setnetRadiationEquivalentEvaporation(float _netRadiationEquivalentEvaporation);
        float getenergyLimitedEvaporation();
        void setenergyLimitedEvaporation(float _energyLimitedEvaporation);
        float getsoilEvaporation();
        void setsoilEvaporation(float _soilEvaporation);

};
#endif
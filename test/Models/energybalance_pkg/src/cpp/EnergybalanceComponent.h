#include "Netradiation.h"
#include "Netradiationequivalentevaporation.h"
#include "Priestlytaylor.h"
#include "Conductance.h"
#include "Diffusionlimitedevaporation.h"
#include "Penman.h"
#include "Ptsoil.h"
#include "Soilevaporation.h"
#include "Evapotranspiration.h"
#include "Soilheatflux.h"
#include "Potentialtranspiration.h"
#include "Cropheatflux.h"
#include "Canopytemperature.h"
using namespace std;

class EnergybalanceComponent
{
    private:
        float albedoCoefficient;
        float stefanBoltzman;
        float elevation;
        float lambdaV;
        float psychrometricConstant;
        float Alpha;
        float vonKarman;
        float heightWeatherMeasurements;
        float zm;
        float d;
        float zh;
        float soilDiffusionConstant;
        float rhoDensityAir;
        float specificHeatCapacityAir;
        float tau;
        float tauAlpha;
        int isWindVpDefined;
    public:
        EnergybalanceComponent();
        EnergybalanceComponent(const EnergybalanceComponent& copy);
        void  Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a);
        void  Init(EnergybalanceState& s,EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a);
        float getalbedoCoefficient();
        void setalbedoCoefficient(float _albedoCoefficient);
        float getstefanBoltzman();
        void setstefanBoltzman(float _stefanBoltzman);
        float getelevation();
        void setelevation(float _elevation);
        float getlambdaV();
        void setlambdaV(float _lambdaV);
        float getpsychrometricConstant();
        void setpsychrometricConstant(float _psychrometricConstant);
        float getAlpha();
        void setAlpha(float _Alpha);
        float getvonKarman();
        void setvonKarman(float _vonKarman);
        float getheightWeatherMeasurements();
        void setheightWeatherMeasurements(float _heightWeatherMeasurements);
        float getzm();
        void setzm(float _zm);
        float getd();
        void setd(float _d);
        float getzh();
        void setzh(float _zh);
        float getsoilDiffusionConstant();
        void setsoilDiffusionConstant(float _soilDiffusionConstant);
        float getrhoDensityAir();
        void setrhoDensityAir(float _rhoDensityAir);
        float getspecificHeatCapacityAir();
        void setspecificHeatCapacityAir(float _specificHeatCapacityAir);
        float gettau();
        void settau(float _tau);
        float gettauAlpha();
        void settauAlpha(float _tauAlpha);
        int getisWindVpDefined();
        void setisWindVpDefined(int _isWindVpDefined);

        Netradiation _Netradiation;
        Netradiationequivalentevaporation _Netradiationequivalentevaporation;
        Priestlytaylor _Priestlytaylor;
        Conductance _Conductance;
        Diffusionlimitedevaporation _Diffusionlimitedevaporation;
        Penman _Penman;
        Ptsoil _Ptsoil;
        Soilevaporation _Soilevaporation;
        Evapotranspiration _Evapotranspiration;
        Soilheatflux _Soilheatflux;
        Potentialtranspiration _Potentialtranspiration;
        Cropheatflux _Cropheatflux;
        Canopytemperature _Canopytemperature;

};
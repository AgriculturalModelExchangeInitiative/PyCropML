#include "EnergybalanceComponent.h"

    EnergybalanceComponent::EnergybalanceComponent()
    {
           
    }
    

float EnergybalanceComponent::getalbedoCoefficient() {return this-> albedoCoefficient; }
float EnergybalanceComponent::getstefanBoltzman() {return this-> stefanBoltzman; }
float EnergybalanceComponent::getelevation() {return this-> elevation; }
float EnergybalanceComponent::getlambdaV() {return this-> lambdaV; }
float EnergybalanceComponent::getpsychrometricConstant() {return this-> psychrometricConstant; }
float EnergybalanceComponent::getAlpha() {return this-> Alpha; }
float EnergybalanceComponent::getvonKarman() {return this-> vonKarman; }
float EnergybalanceComponent::getheightWeatherMeasurements() {return this-> heightWeatherMeasurements; }
float EnergybalanceComponent::getzm() {return this-> zm; }
float EnergybalanceComponent::getd() {return this-> d; }
float EnergybalanceComponent::getzh() {return this-> zh; }
float EnergybalanceComponent::getsoilDiffusionConstant() {return this-> soilDiffusionConstant; }
float EnergybalanceComponent::getrhoDensityAir() {return this-> rhoDensityAir; }
float EnergybalanceComponent::getspecificHeatCapacityAir() {return this-> specificHeatCapacityAir; }
float EnergybalanceComponent::gettau() {return this-> tau; }
float EnergybalanceComponent::gettauAlpha() {return this-> tauAlpha; }
int EnergybalanceComponent::getisWindVpDefined() {return this-> isWindVpDefined; }

void EnergybalanceComponent::setalbedoCoefficient(float _albedoCoefficient)
{
    _Netradiation.setalbedoCoefficient(_albedoCoefficient);
}
void EnergybalanceComponent::setstefanBoltzman(float _stefanBoltzman)
{
    _Netradiation.setstefanBoltzman(_stefanBoltzman);
}
void EnergybalanceComponent::setelevation(float _elevation)
{
    _Netradiation.setelevation(_elevation);
}
void EnergybalanceComponent::setlambdaV(float _lambdaV)
{
    _Netradiationequivalentevaporation.setlambdaV(_lambdaV);
    _Penman.setlambdaV(_lambdaV);
    _Canopytemperature.setlambdaV(_lambdaV);
}
void EnergybalanceComponent::setpsychrometricConstant(float _psychrometricConstant)
{
    _Priestlytaylor.setpsychrometricConstant(_psychrometricConstant);
    _Penman.setpsychrometricConstant(_psychrometricConstant);
}
void EnergybalanceComponent::setAlpha(float _Alpha)
{
    _Priestlytaylor.setAlpha(_Alpha);
    _Penman.setAlpha(_Alpha);
    _Ptsoil.setAlpha(_Alpha);
}
void EnergybalanceComponent::setvonKarman(float _vonKarman)
{
    _Conductance.setvonKarman(_vonKarman);
}
void EnergybalanceComponent::setheightWeatherMeasurements(float _heightWeatherMeasurements)
{
    _Conductance.setheightWeatherMeasurements(_heightWeatherMeasurements);
}
void EnergybalanceComponent::setzm(float _zm)
{
    _Conductance.setzm(_zm);
}
void EnergybalanceComponent::setd(float _d)
{
    _Conductance.setd(_d);
}
void EnergybalanceComponent::setzh(float _zh)
{
    _Conductance.setzh(_zh);
}
void EnergybalanceComponent::setsoilDiffusionConstant(float _soilDiffusionConstant)
{
    _Diffusionlimitedevaporation.setsoilDiffusionConstant(_soilDiffusionConstant);
}
void EnergybalanceComponent::setrhoDensityAir(float _rhoDensityAir)
{
    _Penman.setrhoDensityAir(_rhoDensityAir);
    _Canopytemperature.setrhoDensityAir(_rhoDensityAir);
}
void EnergybalanceComponent::setspecificHeatCapacityAir(float _specificHeatCapacityAir)
{
    _Penman.setspecificHeatCapacityAir(_specificHeatCapacityAir);
    _Canopytemperature.setspecificHeatCapacityAir(_specificHeatCapacityAir);
}
void EnergybalanceComponent::settau(float _tau)
{
    _Ptsoil.settau(_tau);
    _Soilheatflux.settau(_tau);
    _Potentialtranspiration.settau(_tau);
}
void EnergybalanceComponent::settauAlpha(float _tauAlpha)
{
    _Ptsoil.settauAlpha(_tauAlpha);
}
void EnergybalanceComponent::setisWindVpDefined(int _isWindVpDefined)
{
    _Evapotranspiration.setisWindVpDefined(_isWindVpDefined);
}
void EnergybalanceComponent::Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a)
{
    _Diffusionlimitedevaporation.Calculate_Model(s, s1, r, a);
    _Conductance.Calculate_Model(s, s1, r, a);
    _Netradiation.Calculate_Model(s, s1, r, a);
    _Netradiationequivalentevaporation.Calculate_Model(s, s1, r, a);
    _Priestlytaylor.Calculate_Model(s, s1, r, a);
    _Penman.Calculate_Model(s, s1, r, a);
    _Evapotranspiration.Calculate_Model(s, s1, r, a);
    _Potentialtranspiration.Calculate_Model(s, s1, r, a);
    _Ptsoil.Calculate_Model(s, s1, r, a);
    _Soilevaporation.Calculate_Model(s, s1, r, a);
    _Soilheatflux.Calculate_Model(s, s1, r, a);
    _Cropheatflux.Calculate_Model(s, s1, r, a);
    _Canopytemperature.Calculate_Model(s, s1, r, a);
}
EnergybalanceComponent::EnergybalanceComponent(const EnergybalanceComponent& toCopy)
{
    albedoCoefficient = toCopy.albedoCoefficient;
    stefanBoltzman = toCopy.stefanBoltzman;
    elevation = toCopy.elevation;
    lambdaV = toCopy.lambdaV;
    psychrometricConstant = toCopy.psychrometricConstant;
    Alpha = toCopy.Alpha;
    vonKarman = toCopy.vonKarman;
    heightWeatherMeasurements = toCopy.heightWeatherMeasurements;
    zm = toCopy.zm;
    d = toCopy.d;
    zh = toCopy.zh;
    soilDiffusionConstant = toCopy.soilDiffusionConstant;
    rhoDensityAir = toCopy.rhoDensityAir;
    specificHeatCapacityAir = toCopy.specificHeatCapacityAir;
    tau = toCopy.tau;
    tauAlpha = toCopy.tauAlpha;
    isWindVpDefined = toCopy.isWindVpDefined;
}
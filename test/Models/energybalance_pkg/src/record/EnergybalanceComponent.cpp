#include "EnergybalanceComponent.h"

    EnergybalanceComponent::EnergybalanceComponent()
    {
           
    }
    

double EnergybalanceComponent::getalbedoCoefficient() {return this-> albedoCoefficient; }
double EnergybalanceComponent::getstefanBoltzman() {return this-> stefanBoltzman; }
double EnergybalanceComponent::getelevation() {return this-> elevation; }
double EnergybalanceComponent::getlambdaV() {return this-> lambdaV; }
double EnergybalanceComponent::getpsychrometricConstant() {return this-> psychrometricConstant; }
double EnergybalanceComponent::getAlpha() {return this-> Alpha; }
double EnergybalanceComponent::getvonKarman() {return this-> vonKarman; }
double EnergybalanceComponent::getheightWeatherMeasurements() {return this-> heightWeatherMeasurements; }
double EnergybalanceComponent::getzm() {return this-> zm; }
double EnergybalanceComponent::getd() {return this-> d; }
double EnergybalanceComponent::getzh() {return this-> zh; }
double EnergybalanceComponent::getsoilDiffusionConstant() {return this-> soilDiffusionConstant; }
double EnergybalanceComponent::getrhoDensityAir() {return this-> rhoDensityAir; }
double EnergybalanceComponent::getspecificHeatCapacityAir() {return this-> specificHeatCapacityAir; }
double EnergybalanceComponent::gettau() {return this-> tau; }
double EnergybalanceComponent::gettauAlpha() {return this-> tauAlpha; }
int EnergybalanceComponent::getisWindVpDefined() {return this-> isWindVpDefined; }

void EnergybalanceComponent::setalbedoCoefficient(double _albedoCoefficient)
{
    _Netradiation.setalbedoCoefficient(_albedoCoefficient);
}
void EnergybalanceComponent::setstefanBoltzman(double _stefanBoltzman)
{
    _Netradiation.setstefanBoltzman(_stefanBoltzman);
}
void EnergybalanceComponent::setelevation(double _elevation)
{
    _Netradiation.setelevation(_elevation);
}
void EnergybalanceComponent::setlambdaV(double _lambdaV)
{
    _Netradiationequivalentevaporation.setlambdaV(_lambdaV);
    _Penman.setlambdaV(_lambdaV);
    _Canopytemperature.setlambdaV(_lambdaV);
}
void EnergybalanceComponent::setpsychrometricConstant(double _psychrometricConstant)
{
    _Priestlytaylor.setpsychrometricConstant(_psychrometricConstant);
    _Penman.setpsychrometricConstant(_psychrometricConstant);
}
void EnergybalanceComponent::setAlpha(double _Alpha)
{
    _Priestlytaylor.setAlpha(_Alpha);
    _Penman.setAlpha(_Alpha);
    _Ptsoil.setAlpha(_Alpha);
}
void EnergybalanceComponent::setvonKarman(double _vonKarman)
{
    _Conductance.setvonKarman(_vonKarman);
}
void EnergybalanceComponent::setheightWeatherMeasurements(double _heightWeatherMeasurements)
{
    _Conductance.setheightWeatherMeasurements(_heightWeatherMeasurements);
}
void EnergybalanceComponent::setzm(double _zm)
{
    _Conductance.setzm(_zm);
}
void EnergybalanceComponent::setd(double _d)
{
    _Conductance.setd(_d);
}
void EnergybalanceComponent::setzh(double _zh)
{
    _Conductance.setzh(_zh);
}
void EnergybalanceComponent::setsoilDiffusionConstant(double _soilDiffusionConstant)
{
    _Diffusionlimitedevaporation.setsoilDiffusionConstant(_soilDiffusionConstant);
}
void EnergybalanceComponent::setrhoDensityAir(double _rhoDensityAir)
{
    _Penman.setrhoDensityAir(_rhoDensityAir);
    _Canopytemperature.setrhoDensityAir(_rhoDensityAir);
}
void EnergybalanceComponent::setspecificHeatCapacityAir(double _specificHeatCapacityAir)
{
    _Penman.setspecificHeatCapacityAir(_specificHeatCapacityAir);
    _Canopytemperature.setspecificHeatCapacityAir(_specificHeatCapacityAir);
}
void EnergybalanceComponent::settau(double _tau)
{
    _Ptsoil.settau(_tau);
    _Soilheatflux.settau(_tau);
    _Potentialtranspiration.settau(_tau);
}
void EnergybalanceComponent::settauAlpha(double _tauAlpha)
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
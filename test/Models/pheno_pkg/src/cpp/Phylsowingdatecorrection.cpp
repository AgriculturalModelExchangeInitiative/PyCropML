#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
# include<numeric>
# include<algorithm>
# include<array>
#include <map>
# include <tuple>
#include "Phylsowingdatecorrection.h"
using namespace std;

Phylsowingdatecorrection::Phylsowingdatecorrection() { }
int Phylsowingdatecorrection::getsowingDay() {return this-> sowingDay; }
float Phylsowingdatecorrection::getlatitude() {return this-> latitude; }
float Phylsowingdatecorrection::getsDsa_sh() {return this-> sDsa_sh; }
float Phylsowingdatecorrection::getrp() {return this-> rp; }
int Phylsowingdatecorrection::getsDws() {return this-> sDws; }
float Phylsowingdatecorrection::getsDsa_nh() {return this-> sDsa_nh; }
float Phylsowingdatecorrection::getp() {return this-> p; }
void Phylsowingdatecorrection::setsowingDay(int _sowingDay) { this->sowingDay = _sowingDay; }
void Phylsowingdatecorrection::setlatitude(float _latitude) { this->latitude = _latitude; }
void Phylsowingdatecorrection::setsDsa_sh(float _sDsa_sh) { this->sDsa_sh = _sDsa_sh; }
void Phylsowingdatecorrection::setrp(float _rp) { this->rp = _rp; }
void Phylsowingdatecorrection::setsDws(int _sDws) { this->sDws = _sDws; }
void Phylsowingdatecorrection::setsDsa_nh(float _sDsa_nh) { this->sDsa_nh = _sDsa_nh; }
void Phylsowingdatecorrection::setp(float _p) { this->p = _p; }
void Phylsowingdatecorrection::Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a)
{
    //- Name: PhylSowingDateCorrection -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: PhylSowingDateCorrection Model
    //            * Author: Loic Manceau
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA Montpellier
    //            * Abstract: Correction of the Phyllochron Varietal parameter according to sowing date 
    //- inputs:
    //            * name: sowingDay
    //                          ** description : Day of Year at sowing
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** min : 1
    //                          ** max : 365
    //                          ** default : 1
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: latitude
    //                          ** description : Latitude
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLE
    //                          ** min : -90
    //                          ** max : 90
    //                          ** default : 0.0
    //                          ** unit : °
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: sDsa_sh
    //                          ** description : Sowing date at which Phyllochrone is maximum in southern hemispher
    //                          ** parametercategory : species
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 1
    //                          ** max : 365
    //                          ** default : 1.0
    //                          ** unit : d
    //                          ** uri : some url
    //            * name: rp
    //                          ** description : Rate of change of Phyllochrone with sowing date
    //                          ** parametercategory : species
    //                          ** inputtype : parameter
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 365
    //                          ** default : 0
    //                          ** unit : d-1
    //                          ** uri : some url
    //            * name: sDws
    //                          ** description : Sowing date at which Phyllochrone is minimum
    //                          ** parametercategory : species
    //                          ** datatype : INT
    //                          ** default : 1
    //                          ** min : 1
    //                          ** max : 365
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: sDsa_nh
    //                          ** description : Sowing date at which Phyllochrone is maximum in northern hemispher
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 1.0
    //                          ** min : 1
    //                          ** max : 365
    //                          ** unit : d
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //            * name: p
    //                          ** description : Phyllochron (Varietal parameter)
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** default : 120
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : °C d leaf-1
    //                          ** uri : some url
    //                          ** inputtype : parameter
    //- outputs:
    //            * name: fixPhyll
    //                          ** description :  Phyllochron Varietal parameter 
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 1000
    //                          ** unit : °C d leaf-1
    float fixPhyll;
    if (latitude < 0.0f)
    {
        if (sowingDay > int(sDsa_sh))
        {
            fixPhyll = p * (1 - (rp * min((sowingDay - sDsa_sh), float(sDws))));
        }
        else
        {
            fixPhyll = p;
        }
    }
    else
    {
        if (sowingDay < int(sDsa_nh))
        {
            fixPhyll = p * (1 - (rp * min(sowingDay, sDws)));
        }
        else
        {
            fixPhyll = p;
        }
    }
    a.setfixPhyll(fixPhyll);
}
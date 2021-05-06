#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "PhenologyState.h"
#include "PhenologyRate.h"
#include "PhenologyAuxiliary.h"
using namespace std;
class Phylsowingdatecorrection
{
    private:
        int sowingDay;
        float latitude;
        float sDsa_sh;
        float rp;
        int sDws;
        float sDsa_nh;
        float p;
    public:
        Phylsowingdatecorrection();
        void  Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        int getsowingDay();
        void setsowingDay(int _sowingDay);
        float getlatitude();
        void setlatitude(float _latitude);
        float getsDsa_sh();
        void setsDsa_sh(float _sDsa_sh);
        float getrp();
        void setrp(float _rp);
        int getsDws();
        void setsDws(int _sDws);
        float getsDsa_nh();
        void setsDsa_nh(float _sDsa_nh);
        float getp();
        void setp(float _p);

};
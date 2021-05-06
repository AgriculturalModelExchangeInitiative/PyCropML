#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
#include "PhenologyState.h"
#include "PhenologyRate.h"
#include "PhenologyAuxiliary.h"
using namespace std;
class Ptq
{
    private:
        float tTWindowForPTQ;
        float kl;
    public:
        Ptq();
        void  Calculate_Model(PhenologyState& s, PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        void  Init(PhenologyState& s,PhenologyState& s1, PhenologyRate& r, PhenologyAuxiliary& a);
        float gettTWindowForPTQ();
        void settTWindowForPTQ(float _tTWindowForPTQ);
        float getkl();
        void setkl(float _kl);

};
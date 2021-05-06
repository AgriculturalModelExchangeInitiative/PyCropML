#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
# include<numeric>
# include<algorithm>
# include<array>
using namespace std;

template<size_t n>
float AFGEN1(array<float, n>& xy, float t)
{
    float x1;
    float x2;
    float y1;
    float y2;
    float res;
    int i;
    res = NAN;
    if (n > 1)
    {
        i = 0;
        while ( i < n - 1 && t >= xy[i])
        {
            i = i + 2;
        }
        if (i == 0)
        {
            res = xy[1];
        }
        else if ( i > n - 2)
        {
            res = xy[i - 1];
        }
        else
        {
            x1 = xy[i - 2];
            x2 = xy[i];
            y1 = xy[i - 1];
            y2 = xy[i + 1];
            res = (y2 - y1) / (x2 - x1) * (t - x1) + y1;
        }
    }
    return res;
}
int main()
{
    array<float, 10> x ={10.2,52.3,14.6,75.3,36.6,152.5,40.5,160.5,45.5,178.2};
    float y;
    y = AFGEN1(x, 12.2);
    cout<<y<<"\n";

}
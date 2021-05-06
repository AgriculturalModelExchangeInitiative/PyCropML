#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
# include<array>
# include<time.h>
#include<cmath>
#include<numeric>
using namespace std;
template<size_t SIZE_0>
int sum_(const array<int, SIZE_0>& x)
{
    int i;
    int y = 0;
    for(const auto& i_cyml : x)
    {
        i = i_cyml;
        y = y + i;
    }
    return y;
}

int fib( int n)
{
    if(n<=1) return n;
    else return fib(n-1)+fib(n-2);
}

int toto(const array<int, 5>& g)
{
    int a;
    a = g[1];
    return a;
}


int main()
{
	array<int,5> g={15,20,30,60,70};
	int h;
	h=sum_(g);
    cout<<h<<"\n";
    cout<<fib(5);
    cout<<toto(g)<<"\n";
	array<int, 5> t = {15,14,13,12,1};
    h = t[6];
    vector<int> t2 = {15,12,12,12,12};
    h = t2[0];
    cout<<h<<endl;
    int x = 15;
    double result;
    result = ceil(x);
    cout << "Ceil of " << x<< " = " << result << max(5, (int)result)<<endl;
    t2 = vector<int>{};
    t2.push_back(120);
    cout<<t2.at(0)<<endl;
    int res = 0;
    int i;
    vector<int>hh = {5,20,12};
    res = accumulate(hh.begin(), hh.end(), decltype(hh)::value_type(0)); 
    cout<<res;   
    return 0;
}
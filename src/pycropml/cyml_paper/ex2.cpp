#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
# include<array>
using namespace std;

int sum_(vector<int>& x)
{
    int y = 0;
    for(int i: x)
    {
        y = y + i;
    }
    cout<<x.at(2)<<"\n";

    std::vector<int> vec(20);

    vec[15] = 10;
    vec.at(5) = 12;
    vec.push_back(16);
    cout<<vec.at(20)<<"\n";
    return y;
}

int main()
{
	vector<int>g={15,20,30};
	int h;
	h=sum_(g);
    cout<<h;
	
}
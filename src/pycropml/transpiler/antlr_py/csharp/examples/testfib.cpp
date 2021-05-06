#include<iostream>
#include<vector>
using namespace std;

int testfib(int a)
{
    vector<int> h = {15};
    int j;
    for (j=10 ; j!=6 ; j+=-2)
    {
        a = j;
    }
    std::cout<< testfib(10)<<endl;
    return a;
}


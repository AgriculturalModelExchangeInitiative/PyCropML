#include <iostream>
# include<vector>
# include<string>
# include<numeric>
# include<algorithm>
# include<array>
# include <tuple>
# include<map>
using namespace std;

tuple<int,int,vector<int> >  toto(int x, int y)
{
    map<string,int>z = {{"v", 1}, {"jj", 5}};
    int a;
    int b;
    vector<string> j;
    vector<int> gg;
    a = z.size();
    b = z["v"];
    gg.reserve(z.size());
    for(auto const&i : z)
    {
        gg.push_back(i.second);
    }
    return make_tuple(a, b, gg);
}

int main(){
    tuple<int,int,vector<int>> te = toto(5,6);
    vector<int> yy = get<2>(te);
    std::cout << yy[1] <<"\n";

}
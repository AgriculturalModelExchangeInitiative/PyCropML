// array::at
#include <iostream>
#include <array>
using namespace std;

template<size_t SIZE,size_t SIZE2>
void test(array<int,SIZE>& myarray, const array<int,SIZE2>& myarray2)
{
  array<int, SIZE2> myarray3;
  int sum=0;
  int numbers[] = { 1, 2, 3, 4, 5 };
  for (const auto& i: myarray)
    sum = sum+i ;

   cout << "myarray3 contains:"<<sum<<"\n";

}

int main()
{
    array<int,4> myarray={0,15,14,12};
    array<int,7> myarray2={0,15,14, 12, 18, 30, 40};
    test( myarray, myarray2);
}
#include<iostream>
using namespace std;
int main()
{
    int x = 5;
    int *p = &x;


    cout<<x<<" "<<*p<<endl;
    cout<<&x<<" "<<p<<endl;
    cout<<&p;
    return 0;
}
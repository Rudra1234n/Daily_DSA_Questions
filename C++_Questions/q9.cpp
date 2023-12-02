#include<iostream>
using namespace std;
int main()
{
    int first = 8; 
    int second  = 18;
    int *p = &second;
    *p = 5; // It will replace the value 
    cout<<first<<" "<<second;
    return 0;
}
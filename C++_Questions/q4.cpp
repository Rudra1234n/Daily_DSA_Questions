#include<iostream>
using namespace std;
int main()
{
    char ch[6] = "abcde";

    char *p = &ch[0];
    // Gonna print the entire string 
    cout<<p<<endl;
    return 0;
}
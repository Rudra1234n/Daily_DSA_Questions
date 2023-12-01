// Copying a pointer
/*
#include<iostream>
using namespace std;
int main()
{
    int num = 5;

    int *p = &num;
    int *q = p;

    cout<<p<<"-"<<q<<endl;
    cout<<*p<<"-"<<*q<<endl;

    (*q)++;
    cout<<"After addition: "<<*q<<endl;
    cout<<*p<<endl;

    return 0;
}

*/

// Important Concept

#include<iostream>
using namespace std;
int main()
{
    int i = 5;
    int *p = &i;
    cout<<"Before: "<<p<<endl;
    p++;
    cout<<"After: "<<p<<endl;

    return 0;
}
/*
#include<iostream>
using namespace std;
int is_prime(int x)
{
    for(int i=1; i<x; i++)
    {
        if(x%i==0)
        return false;
    }
    return true;

}
int fac(int y)
{
    for (int i=1; i<=y; i++)
    {
        if (is_prime(i))
        {
            int a;
            while(y%a==0)
            {
                cout<<i<<" ";
                a= a*i;
            }

        }
       
    }
}
*/

#include<iostream>
using namespace std;
int fac(int x)
{
    int f = 1;
    if(x == 1 || x==0)
        return f;
    for(int i =1; i<=x; i++)
        f=f*i;
        return f;    
}


int main()
{
    int q;
    cin>>q;
    cout<<fac(q);

    return 0;

}

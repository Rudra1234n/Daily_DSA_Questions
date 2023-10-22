/*
#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter the value of n: ";
    cin>>n;

    //using While loop
    int i=2;
    while(i<=n)
    {
        if(n%i==0)
        {
            cout<<i<<" ";
            break;
        }
       
        i++;

        
    }*/
    
    /*for(int i=2; i<=n; i++)
    {
        if(n%i==0)
        {
            cout<<i;
            break;
        }
    }
    
    return 0;
}
*/

#include<iostream>
using namespace std;
int main(){
    int i=1;
    while (i<=5)
    {
        if (i==3)
        {
            break;
        }
        cout<<i<<" ";
        i++;
    }
    cout<<i<<" ";
    return 0;
    
}
}

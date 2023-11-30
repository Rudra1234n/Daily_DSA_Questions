// basic ponter knowledge is 
/*
#include<iostream>
using namespace std ;
int main()
{
    int x = 5;
    int * ptr = &x;

    cout<<"Value: "<<x<<endl;
    cout<<"Pointer address: "<<ptr<<" "<<*ptr;


    return 0;

}

*/

/*
#include<iostream>
using namespace std;
int main()
{
    int x = 5;
    int *p = &x;
    int **p1 = &p;


    cout<<"Everything is running fine."<<endl;

    //cout<<"Printing x: "<<x<<endl;
    //cout<<"Printing p: "<<p<<endl;// 0x61ff08
    //cout<<"Printing *p"<<*p<<endl;
    //cout<<"Printing **P"<<**p1<<endl;
    //cout<<"Printing p1: "<<p1<<endl;


    cout<<"Adress of x: "<<p<<endl;
    cout<<"Address of p: "<<&p<<endl;
    cout<<*p1<<endl; 

    cout<<endl;

    cout<<x<<endl;
    cout<<*p<<endl;
    cout<<**p1;

    cout<<endl;

    //Printing the address
    cout<<&x<<endl;
    cout<<p<<endl;
    cout<<*p1<<endl;

    cout<<endl;

    // Printing address of another 
    cout<<&p<<endl;
    cout<<p1<<endl; 
    return 0;
}
*/



// Pointers and Functions 
#include<iostream>
using namespace std;
void update(int **p)
{
    // p = p+1; No, change
    // *p = *p+1;, Chnage occured

    **p = **p+1;
}
int main()
{
    int x = 5;
    int *p = &x;
    int **p1 = &p;

    cout<<"Before: "<<x<<endl;
    cout<<"Before: "<<p<<endl;
    cout<<"Before: "<<p1<<endl;

    cout<<endl;
    update(p1);

    cout<<"After: "<<x<<endl;
    cout<<"After: "<<p<<endl;
    cout<<"After: "<<p1<<endl;

    return 0;
}
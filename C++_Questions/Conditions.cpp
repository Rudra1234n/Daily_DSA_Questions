// Basic example of function
/*
#include<iostream>
using namespace std;

void fun()
{
    cout<<"Fun() has been called. "<<endl;
}
int main(){
    cout<<"Before calling fun(). \n";
    fun();
    cout<<"After callingt the fun().";

    return 0;

}
*/

/*
#include<iostream>
using namespace std;

void fuc()
{
    cout<<"Fuc() has been called. "<<endl;
}

int main(){
    cout<<"Before calling the fuc(). \n";
    fuc();
    fuc();
    cout<<"After calling the fuc().";

    return 0;
}
*/

/*

#include<iostream>
using namespace std;

int gt_max(int x, int y)
{
    if(x<y)
    {
        return y;
    }
    else
    {
        return x;
    }
}

int main()
{
    int a,b;
    cin>>a>>b;

    cout<<gt_max(a,b);
    return 0;
}
*/

/*
#include<iostream>
using namespace std;

void entry_mess()
{
    cout<<"Hello."<<endl;
    cout<<"Welcome to gfg."<<endl;
}
void exit_mess()
{
    cout<<"Bye!!"<<endl;
    cout<<"Come Back.";
}

int main()
{
    entry_mess();
    cout<<"Hope you are enjoying. "<<endl;

    exit_mess();

    return 0; 
}

*/


/*
#include<iostream>
using namespace std;
void func2()
{
    cout<<"Inside the func2(). \n";
}
void func1()
{
    cout<<"Before calling the func2(). \n";
    func2();
    cout<<"After calling the func2(). \n";
}

int main()
{
    cout<<"Before calling the func1(). \n";
    func1();
    cout<<"Before calling the func1(). ";

    return 0;
}
*/

/*
#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    double a =2, b=4;
    cout<<pow(a,b)<<endl;

    double x=100;
    cout<<log10(x);

    return 0; 
}

*/

/*
#include<iostream>
using namespace std;
void print_details(int id, string name="NA", string address="NA")
{
    cout<<"Id is "<<id<<endl;
    cout<<"Name is "<<name<<endl;
    cout<<"Adress is "<<address;
}
int main(){

    print_details(124, "Ravi", "Lahore");
    cout<<"\n";
    print_details(102,"Kiran");
    cout<<"\n";
    print_details(200);

    return 0;


}

*/
/*
#include<iostream>
using namespace std;

int sum(int a, int b, int c=0, int d=0)
{
    return(a+b+c+d);
} 

int main()
{
    cout<<sum(10,20,30)<<"\n";
    
    cout<<sum(20,3);

    return 0;
}
*/

// Write a program to print the circumference and area of a circle of radius entered by user by defining your own function.

/*
#include<iostream>
using namespace std;
int ra(double r)
{
    cout<<"Circumference of a circle: "<<(2*3.14*r)<<endl;
    cout<<"Area of a circle: "<<(3.14*r*r);
    return 0;
}
int main()
{
    double x;
    cout<<"Enter the radius: "<<endl;
    cin>>x;

    cout<<ra(x);

    return 0;

}
*/
// Define a program to find out whether a given number is even or odd.
/*
#include<iostream>
using namespace std;
int num(int a)
{

    if (a %2 ==0)
    {
        cout<<"Even"<<endl;
    }
    else
    {
        cout<<"Odd";
    }
    return 0;
       
    
}

int main()
{
    int x;
    cin>>x;
    cout<<num(x);

    return 0;

}
*/
// A person is elligible to vote if his/her age is greater than or equal to 18. Define a function to find out if he/she is elligible to vote.
/*
#include<iostream>
using namespace std;
int vote(int x)
{
    if (x>18)
    {
        cout<<"He's eligible to give vote"<<endl;
    }
    else
    {
        cout<<"He's not eligible to give vote";
    }
}

int main()
{
    int a;
    cout<<"Enter your age:"<<" ";
    cin>>a;
    vote(a);
    return 0;

}
*/

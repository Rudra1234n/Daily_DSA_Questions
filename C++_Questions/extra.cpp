/*
#include <iostream>
using namespace std;
int cal(int a,int b){
    int ask;
    cout<<"what you want to do:(addition(1),substraction(-),multiplication(3),,division(4) ";
    cin>>ask;
    cout<<"result :";
    if(ask==1){
        cout<<a+b;

    }
    else if(ask==2){
        cout<<a-b;

    }

    else if(ask==3){
        cout<<a*b;

    }
    else if(ask==4){
        cout<<a/b;

    }


}

int main(){
    int x,y;
    cout<<"enter first number:";
    cin>>x;
    cout<<"enter second number:";
    cin>>y;
    cal(x,y);
    return 0;
}

// Uskai liyai incorrect value show kerna chaiyai?

*/

// Prime Number function
#include <iostream>
using namespace std;
int chk(int n)
{

    if (n == 0 || n == 1)
    {
        cout << "It's not a prime a number nor composite.";
    }
    else if (n % 2 == 0)
    {
        cout << n << " IS PRIME NUMBER";
    }

    else
    {
        cout << "not a prime number";
    }
}

int main()
{
    int num;
    bool enter;

    cout<<"Take input: ";
    cin>>enter;
    while (enter)
    {
        cout << "Do you want to enter number: ";
        cin >> enter;
        if (enter == false)
        {
            break;
        }

        cout << "enter your number: ";
        cin >> num;

        chk(num);
    }
    return 0;
}

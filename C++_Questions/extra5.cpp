/*
#include<iostream>
using namespace std;
void print_details(int id, string name ="NA", string Address ="NA")
{
    cout<<"Id: "<<id<<endl;
    cout<<"Name: "<<name<<endl;
    cout<<"Address: "<<Address<<endl;
}

int main()
{
    print_details(101, "Rudra", "Udaipur");
    cout<<endl;
    print_details(102, "Bhav");
    cout<<endl;
    print_details(302);

    return 0;
}
*/
#include<iostream>
using namespace std;
int sum(int a, int b, int c=0, int d=0);
int main(){
    cout<<sum(10,20,30)<<endl;
    cout<<sum(40,20);
    return 0;
}
int sum(int a, int b, int c, int d)
{
    return(a+b+c+d);
}

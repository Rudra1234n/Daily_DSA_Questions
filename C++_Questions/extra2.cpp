/*
#include<iostream>
using namespace std;
int num_max(int x, int y)
{
    return(x>y)?x:y;
}
int numMax(int x, int y, int z)
{
    return num_max(num_max(x,y),z);
}
int main(){
    int a,b,c;
    cout<<"Enter the integer: "<<endl;
    cin>>a;
    cout<<"Enter the integer: "<<endl;
    cin>>b;
    cout<<"Enter the integer: "<<endl;
    cin>>c;

    cout<<num_max(a,b)<<endl;
    cout<<numMax(a,b,c)<<endl;

    return 0;
}
*/

#include<iostream>
using namespace std;
void details(int id, string name= "NA", string address = "Na")
{
    cout<<"Id: "<<id<<endl;
    cout<<"Name: "<<name<<endl;
    cout<<"Name: "<<address<<endl;
}
int main(){

    details(10, "Bhavi", "Palwal");
    cout<<"\n";
    details(11, "Rohan");
    cout<<"\n";
    details(1);
    cout<<"\n";


    
    return 0;

}

/*
#include<iostream>
using namespace std;
int main()
{
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};

    for(int i = 0; i<10; i++)
    {
        int *p = &arr[i];
        cout<<p<<endl;
        cout<<endl;
        cout<<*p<<endl;
    }

    return 0;
}

*/

/*
#include<iostream>
using namespace std;
int main(){
    int arr[10] = {45,78,88,102,56};

    cout<<"4th: "<<*arr<<endl;
    cout<<"5th: "<<*arr + 1<<endl;
    cout<<"6th: "<<*(arr + 1)<<endl;
    cout<<"7th: "<<*(arr + 2)<<endl;
    cout<<"8th: "<<(*arr) + 1<<endl;
    cout<<"9th: "<<arr[2]<<endl;

    cout<<endl;
    for(int i = 0; i<4; i++)
    {
        int *q = &arr[i];
        cout<<"Value: "<<*q<<", "<<"Address: "<<q<<endl;
    }

    return 0;
}
*/
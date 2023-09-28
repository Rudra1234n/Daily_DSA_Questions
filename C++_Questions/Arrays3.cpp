//using normal loop of travesal array
/*
#include<iostream>
using namespace std;
int main(){
    int arr[] = {10,20,30,40};
    int n=sizeof(arr)/sizeof(arr[0]);
    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
*/

// Using range based system 
/*
#include<iostream>
using namespace std; 
int main()
{
    int arr[] = {10,20,30,40};
    for(int x:arr)
    {
        cout<<x<<" ";
    }
    return 0;
}
*/

//Modification of array elements during traversal
// normal loop method 
/*
#include<iostream>
using namespace std;
int main(){
    int arr[] = {10, 20, 30};
    int n = sizeof(arr)/sizeof(arr[0]);
    for(int i=0; i<n; i++)
    {
        arr[i] = arr[i]*2;
        cout<<arr[i]<<" ";
    }
    return 0;
}
*/
// Range based methode
#include<iostream>
using namespace std;
int main(){
    int arr[]={10,20,30};
    for(int x:arr)
    {
        x = x*2;
        cout<<x<<" ";
    }
    return 0;

}

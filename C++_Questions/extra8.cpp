// traversal of the array
/*
#include<iostream>
using namespace std;
int main(){
    int arr[] = {10,20,30,40};
    int n = sizeof(arr)/sizeof(arr[0]);
    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }

    return 0;

}
*/

//using range based

/*
#include<iostream>
using namespace std;
int main(){
    int arr[]={10,20,30,45};
    for(int x:arr)
    {
        cout<<x<<" ";
    }
    return 0;
}
*/

#include<iostream>
using namespace std;
int main()
{
    int ar[] = {10,20,30};
    int n = sizeof(ar)/sizeof(ar[0]);
    for(int i=0; i<n; i++)
    {
        ar[i] = ar[i]*2;
        cout<<ar[i]<<" ";
    }
    return 0;

}

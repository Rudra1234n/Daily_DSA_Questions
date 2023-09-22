/*
#include<iostream>
using namespace std;
int main()
{
    int arr[15];
    cout<<arr[4];

    return 0;
}
*/

/*
#include<iostream>
using namespace std;
int main()
{
    int n[] = {10,20,35};
    
    // Size of Array
    int x = sizeof(n);
    cout<<"Size of Array: "<<x<<endl;

    int y = sizeof(n)/sizeof(n[0]);
    // Elements of array
    cout<<"Total Number of elements in Array: "<<y<<endl;


    

    return 0;
}
*/

/*
// printing all the elements of array
#include<iostream>
using namespace std;
int main()
{
    int arr[] = {2, 2 , 5 , 6 , 45};

    int n = sizeof(arr)/ sizeof(arr[0]);

    for(int i =0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }

    return 0;
}
*/


// Printing Array using function

#include<iostream>
using namespace std;
void print_array(int arr[], int n)
{
    for(int i =0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }
}

int main()
{
    int num[] = {45, 32, 21, 42};
    int m = 4;

    print_array(num, m);

    return 0;
}

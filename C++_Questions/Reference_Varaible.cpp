/*
#include<iostream>
using namespace std;
int main()
{
    int i =5;
    // creating refrence variable
    int &j=i;

    cout<<i<<endl;
    i++;
    cout<<i<<endl;
    j++;
    cout<<i;

    return 0;

}
*/


// Pass by value

/*
#include<iostream>
using namespace std;
void update(int n)
{
    n++;
}


int main()
{
    int n = 5;

    cout<<"Before Func "<<n<<endl;
    update(n);

    cout<<"After Func "<<n;

    return 0;

}
*/


// pass by refrence 

/*
#include<iostream>
using namespace std;
void update(int &m)
{
    m++;
}

int main()
{
    int n=5;
    cout<<"Before func: "<<n<<endl;
    update(n);
    cout<<"After Func: "<<n<<endl;

    return 0;
}
*/

// Allocating array into heap memory


/*
#include<iostream>
using namespace std;
int main()
{

    int* arr = new int[5];

    return 0;
}

*/


#include<iostream>
using namespace std;
int get_sum(int *num, int n) // The value we need to pass in our main function should be same as parameters decalre in the fumctionn
{
    int sum = 0;
    for(int i = 0; i<n; i++)
    {
        sum += num[i];
    }
    return sum;
}


int main()
{
    int m;
    cin>>m;


    // Allocating Heap memory
    int *arr = new int[m];
    
    //taking input for array 
    for(int i=0; i<m; i++)
    {
        cin>>arr[i];
    }

    int ans = get_sum(arr, m);
    cout<<ans;

    return 0;

    
}


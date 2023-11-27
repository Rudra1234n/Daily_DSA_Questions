/*
#include<iostream>
using namespace std;
void print(int *p)
{
    cout<<"Adress: "<<p<<" Pointer: "<<*p;
}

void update(int*p)
{
    p++;
    cout<<"Inside "<<p<<endl;
}

int main()
{
    int value = 5;
    
    int *q = &value;

    //print(q);
    cout<<"Before "<<q<<endl;
    update(q);
    cout<<"After "<<q;// Will get the same result 

    return 0;
}

*/

// Now lets' talk about the value 

/*
#include<iostream>
using namespace std;
void update(int*q)
{
    *q = *q+1;
    
}
int main()
{
    int value = 5;
    int *p = &value;

    cout<<"Before "<<*p<<endl;
    update(p);
    cout<<"After "<<*p<<endl;

    return 0;

}

*/



#include<iostream>
using namespace std;
int get_sum(int *arr, int n)
{
    cout<<"Size: "<<sizeof(arr)<<endl;
    
    int sum = 0;
    for(int i=0; i<n; i++)
    {
        sum += arr[i];
    }
    return sum;
}

int main()
{
    int num[5] = {1,2,3,4,5};

    cout<<get_sum(num, 5);

    return 0;


}
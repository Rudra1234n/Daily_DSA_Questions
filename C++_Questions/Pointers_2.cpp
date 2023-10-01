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

/*
#include<iostream>
using namespace std;
int main()
{
    int num[10] = {2,5,6};
    //int *ptr = &num[5];
    cout<<"The address of the 0th index array "<<&num[0]<<endl;
    cout<<"Address of first memory block is: "<<num<<endl;
    cout<<"4th "<<*num<<endl;
    cout<<"5th "<<*num + 1<<endl;
    cout<<"6th "<<*(num + 1)<<endl;
    cout<<"7th "<<(*num) + 1<<endl;
    cout<<"8th "<<1[num]<<endl;
    cout<<"8th "<<*(1+num);
    
    

    return 0;
}

*/

/*
#include<iostream>
using namespace std;
int main()
{
    int num[10];
    cout<<sizeof(num)<<endl;

    int *ptr = &num[0];

    cout<<sizeof(ptr)<<endl;

    return 0;
}

*/




/*
#include<iostream>
using namespace std;
int main()
{
    int a[20] = {1,2,3,4,5};

    cout<<a<<endl;
    cout<<&a<<endl;
    cout<<&a[0]<<endl;



    cout<<"Now about pointer"<<endl;


    int *p = &a[0];

    cout<<&p<<endl;
    cout<<p<<endl;
    cout<<*p;




    return 0;
}

*/



/*
#include<iostream>
using namespace std;
int main()
{
    int num[10];
    // Error will be shown
    //num = num+1;
    //cout<<num;


    int *ptr = &num[0];
    cout<<"Before"<<ptr<<endl;
    ptr++;
    cout<<"After"<<ptr<<endl;
    return 0;
}

*/
/*
#include<iostream>
using namespace std; 
int main()
{
    int num[5] = {1,2,3,4,5};
    char ch[6] = "abcde"; 
    cout<<num<<endl;

    cout<<endl;

    cout<<ch;

    

    return 0;
}
*/

#include<iostream>
using namespace std;
int main()
{
    char ch[6] = "abcde";

    char *p = &ch[0];
    // Gonna print the entire string 
    cout<<p<<endl;
    return 0;
}

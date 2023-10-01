/*
#include<iostream>
using namespace std;
int main()
{
    int num = 5;

    // Address of opreator - &

    cout<<"The address of num is: "<<&num;

    return 0;
}

*/

/*
#include<iostream>
using namespace std;
int main()
{
    int num = 5;

    int *p = &num;

    cout<<"Value is: "<<*p<<endl;
    cout<<"Address is: "<<p<<endl;


    cout<<endl;

    double num1 = 4.5;
    double *p1 = &num1;

    cout<<"Value is: "<<*p1<<endl;
    cout<<"Address is: "<<num1<<endl;

    

    return 0;
}

*/

/*
#include<iostream>
using namespace std;
int main()
{
    int i = 5;
    int x = i;
    x++;

    cout<<"The value of i: "<<i<<endl;
    cout<<"The value of x: "<<x<<endl;


    return 0;
}

*/

/*
#include<iostream>
using namespace std;
int main()
{
    int num = 5;

    int*i = &num;
    int a = *i;

    a++;

    cout<<"The value of a: "<<a<<endl;
    cout<<"The value of pointer: "<<*i<<endl;
    cout<<"The value of num: "<<num<<endl;


    return 0;
}

*/


/*
#include<iostream>
using namespace std;
int main()
{
    int num = 5;
    
    
    int *i = &num;
    (*i)++;


    cout<<"The value of pointer: "<<*i<<endl;
    cout<<"The value of num: "<<num<<endl;

    return 0;
}

*/

// Copying a pointer
/*
#include<iostream>
using namespace std;
int main()
{
    int num = 5;

    int *p = &num;
    int *q = p;

    cout<<p<<"-"<<q<<endl;
    cout<<*p<<"-"<<*q<<endl;

    (*q)++;
    cout<<"After addition: "<<*q<<endl;
    cout<<*p<<endl;

    return 0;
}

*/

// Important Concept

#include<iostream>
using namespace std;
int main()
{
    int i = 5;
    int *p = &i;
    cout<<"Before: "<<p<<endl;
    p++;
    cout<<"After: "<<p<<endl;

    return 0;
}

/*
#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int i=0;
    while(i<n)
    {
        int j=0;
        while(j<n)
        {
            cout<<"*";
            j++;
        }
        cout<<"\n";
        i++;
    }
    return 0;
}
*/

/*
#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;

    int i =1;
    while(i<=n)
    {
        int j=1;
        while(j<=n)
        {
            cout<<i;
            j++;
        }
        cout<<"\n";
        i++;
    }
    return 0;

}
*/

/*
#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;

    int i=1;
    while(i<=n)
    {
        int j=1;
        while(j<=n)
        {
            cout<<j;
            j++;
        }
        cout<<"\n";
        i++;
    }
    return 0;
}
*/

/*
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int c = 1;

    int i=1;
    while(i<=n)
    {
        int j=1;
        while(j<=n)
        {
            cout<<c<<" ";
            c=c+1;
            j++;
        }
        cout<<"\n";
        i++;
    }
    return 0;
}

*/
/*
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int i=1;
    while(i<=n)
    {
        int j=1;
        while(j<=i)
        {
            cout<<"*";
            j++;
        }
        cout<<"\n";
        i++;
    }
    return 0;
}
*/
/*
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int i= 1;
    while(i<=n)
    {
        int j=1;
        while(j<=i)
        {
            cout<<i;
            j++;
        }
        cout<<"\n";
        i++;
    }
    return 0;
}    

*/

/*
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int c=1;
    int i= 1;
    while(i<=n)
    {
        int j=1;
        while(j<=i)
        {
            cout<<c;
            c=c+1;
            j++;
        }
        cout<<"\n";
        i++;

    }
    return 0;
}
*/

/*
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int i= 1;
    while(i<=n)
    {
        int j=1, value =i;
        while(j<=i)
        {
            cout<<value;
            value++;
            j++;
        }
        cout<<"\n";
        i++;

    }
    return 0;
}
*/

/*
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;


    int i=1;
    while(i<=n)
    {
        int j=1;
        while(j<=n)
        {
            char ch='A'+j-1;
            cout<<ch;
            j++;
        }
        cout<<"\n";
        i++;
    }
    return 0; 
}

*/


/*
#include<iostream>
using namespace std;
int main()
{
    int x;
    cin>>x;

    int row=1;
    while(row<=x)
    {
        int space=x-row;
        while(space)
        {
            cout<<" ";
            space--;
        }
        int col = 1;
        while(col<=row)
        {
            cout<<"*";
            col++;
        } 
        cout<<"\n";
        row++;
    }
    return 0;
}

*/


#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;

    int row=n;
    while(row>0)
    {
        int col=0;
        while(col<row)
        {
            cout<<"* ";
            col++;
        }
        col=0;
        row--;
        cout<<"\n";
    }
    return 0;
}

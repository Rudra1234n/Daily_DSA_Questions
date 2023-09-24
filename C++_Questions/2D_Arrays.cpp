
/*
#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;

    int **arr = new int*[n];

    for(int i=0;i<n;i++)
    {   
        arr[i] = new int[n];
    }

    // Taking input in the 2d array

    for(int i = 0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            cin>>arr[i][j];
        }
    }
    cout<<endl;

    // Printing the outputs
    for(int i = 0; i<n; i++)
    {
        for(int j = 0; j<n; j++)
        {
            cout<<arr[i][j]<<" ";
        }

        cout<<endl;
    }


    
    return 0;
}




*/


/*
#include<iostream>
using namespace std;
int main()
{
    int row,col;
    cin>>row>>col;


    int** num = new int*[row];
    for(int i = 0; i<row; i++)
    {
        num[i] = new int[col];
    }
    
    // taking input in 2d array 

    for(int i=0; i<row; i++)
    {
        for(int j = 0; j<col; j++)
        {
            cin>>num[i][j];
        }
    }

    cout<<endl;


    // Printing the output
    for(int i = 0; i<row; i++)
    {
        for(int j = 0; j<col; j++)
        {
            cout<<num[i][j]<<" ";
        }
        cout<<endl;
    }


    // Releasing memory 
    for(int i =0; i<row; i++)
    {
        delete [] num[i];
    }

    delete [] num;


    return 0;


}

*/


/*
// building a 2 d array usng heap memory
#include<iostream>
using namespace std;
int main()
{
    int row, col;
    cin>>row>>col;

    // building 2d array 
    int**num = new int*[row];
    for(int i= 0; i<row; i++)
    {
        num[i] = new int[col];
    }

    for(int i =0; i<row; i++)
    {
        for(int j = 0; j<col; j++)
        {
            cin>>num[i][j];
        }

    }
    cout<<endl;


    for(int i = 0; i<row; i++)
    {
        for(int j=0; j<col; j++)
        {
            cout<<num[i][j]<<" ";
        }
        cout<<endl;
    }


    // clearing the memory


    for(int i= 0; i<row; i++)
    {
        delete [] num[i];
    }

    delete [] num;


    return 0;

}



*/

#include<iostream>
using namespace std;
int main()
{
    int row,col;
    cin>>row>>col;

    int **num = new int*[row];
    for(int i=0; i<row; i++)
    {
        num[i] = new int[i];
    }

    for(int i=0; i<row; i++)
    {
        for(int j=0; j<col; j++)
        {
            cin>>num[i][j];
        }
    }

    
    for(int i=0; i<row; i++)
    {
        for(int j=0; j<col; j++)
        {
            cout<<num[i][j]<<" ";
        }
        cout<<endl;

    }
    


    return 0;
}


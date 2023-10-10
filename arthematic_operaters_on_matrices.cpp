/******Topics:  Function overloading and operator overloading


Question 1.   Given two matrix M and N, use function overloading and operator
overloading to perform the following operations:


            1. 
    M+N


2.      M-N 


3.      Transpose(M)


4.      M*N


5.      Inverse(M)


6.      Rank(M) 










For each class, create both constructor and
destructors, and put output statements (if needed) to show the order of
constructor/destructor invoked.******/

#include<iostream>
using namespace std;

class matrix
{
        int a[3][3];
    public:
        void accept();
        void display();
        void operator +(matrix x);
        void operator -(matrix x);
        void operator *(matrix x);
        void operator =(matrix x);
        void operator ^(matrix x);
        void operator !=(matrix x);
        
};
void matrix::accept()
{
    cout<<"\n Enter Matrix Element (3 X 3) : \n";
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
        {
            cout<<" ";
            cin>>a[i][j];
        }
    }
}
void matrix::display()
{
    for(int i=0; i<3; i++)
    {
        cout<<" ";
        for(int j=0; j<3; j++)
        {
            cout<<a[i][j]<<"\t";
        }
            cout<<"\n";
    }
}
void matrix::operator +(matrix x)
{
    int mat[3][3];
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
        {
            mat[i][j]=a[i][j]+x.a[i][j];
        }
    }
    cout<<"\n Addition of Matrix : \n\n";
    for(int i=0; i<3; i++)
    {
        cout<<" ";
        for(int j=0; j<3; j++)
        {
            cout<<mat[i][j]<<"\t";
        }
        cout<<"\n";
    }
}
void  matrix::operator -(matrix x)
{
    int mat[3][3];
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
        {
            mat[i][j]=a[i][j]-x.a[i][j];
        }
    }
    cout<<"\n subtraction of Matrix : \n\n";
    for(int i=0; i<3; i++)
    {
        cout<<" ";
        for(int j=0; j<3; j++)
        {
            cout<<mat[i][j]<<"\t";
        }
        cout<<"\n";
    }
}
void  matrix::operator *(matrix x)
{
    int mat[3][3];
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
        {
            mat[i][j]=a[i][j]*x.a[i][j];
        }
    }
    cout<<"\n multiplication of Matrix : \n\n";
    for(int i=0; i<3; i++)
    {
        cout<<" ";
        for(int j=0; j<3; j++)
        {
            cout<<mat[i][j]<<"\t";
        }
            cout<<"\n";
    }
}
void matrix::operator =(matrix x)
{
     int mat[3][3];
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
        {
            mat[i][j]=x.a[j][i];
        }
    }
    cout<<"\n transpose of **2nd input ***Matrix : \n\n";
    for(int i=0; i<3; i++)
    {
        cout<<" ";
        for(int j=0; j<3; j++)
        {
            cout<<mat[i][j]<<"\t";
        }
            cout<<"\n";
    }
}
void matrix::operator^(matrix x)
{
    int mat[3][3];
    float determinant=0;
    for(int i=0;i<3;i++)
    {
        determinant = determinant + (x.a[0][i]*(x.a[1][(i+1)%3]*
        x.a[2][(i+2)%3] - x.a[1][(i+2)%3]*x.a[2][(i+1)%3]));
    }
    if(determinant==0)
    {
    cout<<"Inverse does not exist (Determinant=0).\n";
    }
    else
    {
    cout<<"\nInverse of **2nd input *** matrix is: \n";
    }
    for(int i=0;i<3;i++)
    {
    for(int j=0;j<3;j++)
    {
        cout<<((x.a[(i+1)%3][(j+1)%3] *
        x.a[(i+2)%3][(j+2)%3]) - (x.a[(i+1)%3][(j+2)%3]*
        x.a[(i+2)%3][(j+1)%3]))/ determinant<<"\t";
    }
    cout<<"\n";
    }
 
    }

void matrix::operator!=(matrix x)
{
    int order=3,mat[3][3];
    float determinant=0;
    for(int i=0;i<3;i++)
    {
        determinant = determinant + (x.a[0][i]*(x.a[1][(i+1)%3]*
        x.a[2][(i+2)%3] - x.a[1][(i+2)%3]*x.a[2][(i+1)%3]));
    }
    if(determinant==0)
    {
        cout<<"\n\nthe rank of the **2nd input *** matrix is 3\n";
    }
     else
    {
        cout<<"\nthe rank of the matrix is 2 \n";
    }
}

int main()
{
    matrix m,n;
    m.accept();       
    n.accept();      
    cout<<"\n First Matrix : \n\n";
    m.display();   
    cout<<"\n Second Matrix : \n\n";
    n.display(); 
    m+n;
    m-n;
    m*n;
    m=n;
    m^n;
    m!=n;
    return 0;
}

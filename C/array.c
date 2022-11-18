#include <stdio.h>

int main()
{
    int arr[5];
    int x;
    for (int i = 0; i < 5; i++)
    {
        scanf("%i", &x);
        arr[i]=x;
        

    }
    for (int i = 0; i < 5; i++)
    {
        printf("%i\n", arr[i]);
        

    }
    
    
}
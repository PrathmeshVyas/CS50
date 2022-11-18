#include <stdio.h>

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("happy navaratri\n");
    }
    
}

int gpi(void);

int main(void)
{

    char x;
    scanf("%c", &x);
   
    
    if (x == 'y' || x == 'Y')
    {
        printf("Agreed\n");
    }
    else
    {
        printf("denied");
    }

    int i = 0;
    while (i<50)
    {
        printf("har har mahadev\n");
        i++;
    }

    for (int x=0; x<50; x++)
    {
        printf("jay shree radha krishna\n");
    }
    
    meow(7);
    int ii; gpi();
    printf("%i\n", ii);
}

int gpi(void)
{
    int x;

    do
    {
        scanf("%d", &x);
    } 
    while (x<1);
    return x;
    
    
}
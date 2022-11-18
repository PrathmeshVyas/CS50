#include <stdio.h>
#include <conio.h>

int main()
{
    int i,j,rows;

    printf("enter number of rows: ");
    scanf("%d", &rows);

    for (i = 1; i <= rows; i++)
    {
    

        for (j = 1; j <= i; j++)
        {
            printf("%s", "#");
        }
        printf("\n");
    }
    return 0;
    
    
}
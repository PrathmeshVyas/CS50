#include <stdio.h>
#include <string.h>

int main()
{
    char s[10];
    scanf("%s", &s);
    char j[10];
    scanf("%s", &j);

    if(strcmp(s, j)==0)
    {
        printf("same");
    }
    else
    {
        printf("different");
    }
}
#include <stdio.h>
#include <ctype.h>
#include <string.h>


int main()
{
    char *s;
    scanf("%s", &s);
    char *t=s;

    t[0] = toupper(t[0]);

    printf("%s\n", s);
    printf("%s\n", t); 

}

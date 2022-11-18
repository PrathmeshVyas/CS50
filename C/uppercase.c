#include <ctype.h>
#include <stdio.h>
#include <conio.h>
#include <string.h>


int main(void)
{
    char s[5];
    char x;
    gets(s);


    for (int i = 0; i < 5; i++)
    {
        if (islower(s[i]))
        {
            printf("%c", toupper(s[i]));
        }
        else
        {
            printf("%c", s[i]);
        }

    }
    
    
}
#include <stdio.h>
#include <string.h>

int main()
{
    char s[][10] = {"ram","laxman","hanuman"};
    char n[][10] = {"56325625","256325632","2589632514"};

    for (int i=0; i < 3; i++)
    {
        if(strcmp(s[i], "ram")==0)
        {
            printf("%s", n[i]);
        }
    }
 
}
#include<stdio.h>
#include<string.h>


int main()
{
    FILE *file = fopen("contacts.csv", "a");
    if (file == NULL)
    {
        return 1;
    }

    char s[100];
    scanf("%s", &s);
    char n[100];
    scanf("%s", &n);

    fprintf(file, "%s,%s\n", s, n);

    fclose(file);
}
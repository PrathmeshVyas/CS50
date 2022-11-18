#include<stdio.h>


int main()
{

    int n=50;
    int *p = &n;
    char *a="hi";
    printf("%c\n", *a);
    printf("%c\n", *(a+1));

}
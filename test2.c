#include <stdio.h>

void temp(char[]);

int main()
{
	char a[10];
	a[0] = 'a';
	temp(a);
	printf("%s\n", a);
}

void temp(char b[])
{
	b[0] = 'b';
}

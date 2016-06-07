#include <stdio.h>

int temp(int);

int main()
{
	int a;
	a = 5;
	temp(a);
	printf("%d\n", a);
}

int temp(int b)
{
	b = 10;
}

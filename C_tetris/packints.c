#include <stdio.h>
#include <stdlib.h>

/* pack two ints < 20 into a single int */
int packints(int a, int b)
{
	a <<= 5;
	a |= b;
	return a;
}

/* unpack two ints < 20 */
int *unpackints(int a)
{
	int *points = malloc(sizeof(int)*2);
	points[0] = (a & 0x3E0) >> 5;
	points[1] = a & 0x1F;
	return points;
}

int main()
{
	int a = 0, b;
	while (1) {
		scanf("%d%d", &a, &b);
		int n = packints(a,b);
		int* points = unpackints(n);
		printf("%d %d\n", points[0], points[1]);
	}
	return 0;
}


#include<stdio.h>
#include<math.h>
main()
{
	double a,b,c,x1,x2,r;
	printf("Dame un valor para A\n");
	scanf("%lf",&a);
	printf("Dame un valor para A\n");
	scanf("%lf",&b);
	printf("Dame un valor para A\n");
	scanf("%lf",&c);
	r=pow(b,2)-4*a*c;//(b*b)-4*a*b;
	printf("R=%lf",r);
	printf("%lf",r);
	if(r>=0)
	{
		printf("la raiz es real\n");
	}
	else
	{
		printf("es compleja\n");	
	}
}

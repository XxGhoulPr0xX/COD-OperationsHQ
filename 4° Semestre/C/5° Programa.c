#include<stdio.h>
#include<math.h>
main()
{
	double a,b,c,x1,x2,d,i;
	printf("Dame un valor para A\n");
	scanf("%lf",&a);
	printf("Dame un valor para B\n");
	scanf("%lf",&b);
	printf("Dame un valor para C\n");
	scanf("%lf",&c);
	d=pow(b,2)-4*a*c;//(b*b)-4*a*b;
	printf("R=%lf\n",d);
	
	if(d>=0)
	{
		x1=(-b+(sqrt(d)))/(2*a);
		x2=(-b-(sqrt(d)))/(2*a);
		printf("x1=%lf\n",x1);
		printf("x2=%lf\n",x2);
	}
	else
	{
		i=d*(-1);
		double x3=sqrt(i);
		double l=x3/(2*a);
		x1=-b/(2*a);
		x2=-b/(2*a);
		printf("x1=%1.2lf",x1);
		printf("+%1.2lfi\n",l);
		printf("x2=%1.2lf",x2);
		printf("-%1.2lfi\n",l);
	}
}

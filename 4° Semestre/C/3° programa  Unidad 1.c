#include<stdio.h>
#include<math.h>
main()
{
	double a,b,c;
	printf("Dame un valor para A\n");
	scanf("%lf",&a);
	printf("Dame un valor para B\n");
	scanf("%lf",&b);
	//a=2;
	//b=3;
	//c=a/b;
	//c=pow(a,1.0/2.0);
	c=pow(a,b);//a+b;//sqrt(a);//c=raiz
	printf("%lf",c);
}


#include<stdio.h>
#include<math.h>
double f(double x)
{
	return(pow(x,5)-100);
}
main()
{
	double p0,p1,p2,e;
	int i;
	e=0.01;
	p0= 1;
	p1= 3;
	p2= p0-((f(p0)*(p1-p0))/(f(p1)-f(p0)));
	
	printf("p0\t\tp1\t\tp2\t\tf(p2)\n");
	printf("%0.5lf\t\t%0.5lf\t\t\%0.5lf\t\t%0.5lf\n",p0,p1,p2,f(p2));
	for(i=1;fabs(f(p2))>e;i++)
	{
		p0=p1;
		p1=p2;
		p2= p0-((f(p0)*(p1-p0))/(f(p1)-f(p0)));
		printf("%0.5lf\t\t%0.5lf\t\t\%0.5lf\t\t%0.5lf\n",p0,p1,p2,f(p2));
	}
	
printf("La raiz es: %0.5lf\n Con una tolerancia de %0.4lf",p2,e);
	
}


#include<stdio.h>
#include<math.h>

double f(double x){
	return (pow(x,5)-100);
}
main(){
	double a,b,k,e;
	int i;
	e=0.01;
	a=1;
	b=3;
	k=a+((b-a)/2);
	printf("a\tb\tf(a)\tf(b)\tk\tf(k)\n");
	printf("%1.2lf\t%1.2lf\t%1.2lf\t%1.2lf\t%1.2lf\t%1.2lf\n",a,b,f(a),f(b),k,f(k));
	if((f(a)*f(b))<0)
	{
		k=a+((b-a)/2);
		for(i=1;f(k)>e;i++);
			{
			if((f(a)*f(k))<0)
				{
					a=a;
					b=k;
					k=a+((b-a)/2);
					printf("%1.2lf\t%1.2lf\t%1.2lf\t%1.2lf\t%1.2lf\t%1.2lf\n",a,b,f(a),f(b),k,f(k));
				}
			else
				{
					a=k;
					b=b;
					k=a+((b-a)/2);
					printf("%1.2lf\t%1.2lf\t%1.2lf\t%1.2lf\t%1.2lf\t%1.2lf\n",a,b,f(a),f(b),k,f(k));
				}
			}
	}
	else
	{
		printf("\nNo hay raices");	
	}
	//printf("f(f%lf)=%lf",a,b);
/*	for(i=0;i<=10;i++){
		//printf("%d\n\t%lf",i,f(i));
		printf("%d\t",i);
		printf("%lf\n",f(i));
	}*/
}

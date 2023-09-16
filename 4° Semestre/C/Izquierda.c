#include<stdio.h>
#include<math.h>
double f(double x){
	return(pow(x,2));
}
main(){
	int i,n;
	double x,h,a,b,suma;
	n=5;
	a=1;
	b=3;
	h=(b-a)/n;
	suma=0;
	for(i=0;i<=n-1;i++)
	{
		x=a+i*h;
		suma+=f(x)*h;
	}
	printf("Int=%1.4lf", suma);
}

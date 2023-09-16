#include<stdio.h>
#include<math.h>
double f(double x){
return(pow(x,2));
}
main(){
	int i,n;
	double x,h,a,b,suma,Integral;
	n=5;
	a=1;
	b=3;
	h=(b-a)/n;
	suma=0;
	for(i=1;i<=n-1;i++)
	{
		x=a+i*h;
		suma+=f(x)*h;
	}
Integral=(h/2)*(f(a)+2*suma+f(b));
printf("Int=%1.4lf", Integral);
}

#include<stdio.h>
#include<math.h>

double f(double x){
	double r;
	r=x-3;
	return(r);
}
main(){
	double a,b;
	a=0;
	b=f(a);
	printf("f(%lf)=%lf",a,b);
}

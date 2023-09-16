#include<stdio.h>
#include<math.h>
double f(double x){
	return(pow(x,5)-100);
}
double f1(double x){//f1 es la derivada de f
	return(5*pow(x,4));
}
main(){
	int i;
	double p0,p1,e;
	e=0.01;
	p0=1;
	printf("i\t\tPi\t\tF(Pi)\n");
	for(i=0;fabs(f(p0))>e;i++){
		p1=p0-(f(p0)/f1(p0));
		printf("%i\t\t%1.5lf\t\t%1.5lf\n",i,p0,f(p0));
		p0=p1;
	}
}

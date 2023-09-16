#include<stdio.h>
#include<math.h>

double F(double x, double y){
	return(y);
}
main(){
	double x,y,h,a,b,a0;
	int i,n;
	FILE *Archivo;
	Archivo=fopen("datos_1.txt","w");
	n=4;
	a=0;
	b=4;
	h=(b-a)/n;
	a0=1;
	y=a0;
	for(i=0;i<=n;i++){
		x=a+i*h;
		y=y+h*F(x,y);
		fprintf(Archivo,"%1.3lf\t%1.3lf\n",x,y);
	}
	fclose(Archivo);
}

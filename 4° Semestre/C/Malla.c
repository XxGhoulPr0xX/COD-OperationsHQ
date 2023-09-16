#include<stdio.h>

main(){
	int a=1; int b=3; int c=1; int d=4; int n=2; int m=3;
	double dx,dy,x,y,i,j;
	FILE *COORDENADAS;
	COORDENADAS=fopen("datas.txt","w");
	dx=(b-a)/n;
	dy=(d-c)/m;
	for(i=0;i<=n;i++){
		x=a+(i+dx);
		for(j=0;j<=m;j++){
			y=c+(j*dy);
			fprintf(COORDENADAS,"%1.2lf\t%1.2lf\n",x,y);
		}
	}
	fclose(COORDENADAS);
}

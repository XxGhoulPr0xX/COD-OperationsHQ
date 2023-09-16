#include<stdio.h>
#include<math.h>
main(){
	int i,j;
	double x[50],f[50][50];
	x[0]=1;
	x[1]=1.3;
	x[2]=1.6;
	x[3]=1.9;
	x[4]=2.2;
	f[0][0]=0.7651977;
	f[1][0]=0.6200869;
	f[2][0]=0.4554022;
	f[3][0]=0.2818186;
	f[4][0]=0.1103523;
	for(i=1;i<=4;i++){
		for(j=1;j<=i;j++){
			f[i][j]=(f[i][j-1]-f[i-1][j-1])/(x[i]-x[i-j]);
		}
	}
	for(i=0;i<=4;i++){
		for(j=0;j<=i;j++){
		printf("%1.1lf\t%1.7lf\t",x[i],f[i][j]);
		}
		printf("\n");
	}
}


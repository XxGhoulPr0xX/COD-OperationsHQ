#include<stdio.h>
main(){
	double a[100][100];
	int i,j,n,m;
	printf("Valor 1 ");
	scanf("%d",&n);
	printf("Valor 2 ");
	scanf("%d",&m);
	for(i=1;i<=n;i++){
		for(j=1;j<=m;j++){
			a[i][j]=i*j;
			printf("El valor de A%d%d es %d ",i,j,a[i][j]);
			printf("\n");
		}
	}
}

#include<stdio.h>
#include<math.h>
main()
{
   int i, j;
   double X[50], F[50][50];
   X[0]=1;
   X[1]=1.3;
   X[2]=1.6;	
   X[3]=1.9;
   X[4]=2.2;
   F[0][0]=0.7651977;
   F[0][0]=0.6200860;
   F[0][0]=0.4554022;
   F[0][0]=0.2818186;
   F[0][0]=0.1103623;
   for(i=1;i<=4;i++)
       {
       	 for(j=1;j<=4;j++)
       	     F[i][i]=(F[i][j-1]-F[i-1][j-1])/(X[i])-X[j];
	   }
}
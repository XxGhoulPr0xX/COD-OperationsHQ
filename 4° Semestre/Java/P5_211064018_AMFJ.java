import java.util.Scanner;
public class P5_211064018_AMFJ                                 
{
    public static void main(String[] args)
    {
        int n=1;int par=0;int impar=0;int edad=0;int su=0;
        Scanner entrada= new Scanner(System.in);
        System.out.println("Dame un numero o dame 0 para terminar la suma");
        n=entrada.nextInt();
        while(n!=0)
        {
            su=su+n;
            n=entrada.nextInt();
            if(n%2==0)
            {
                par=par+1;
            }
            else
            {
                impar=impar+1;
            }
        }
            System.out.println("La suma total es "+su);
            System.out.println("Los numeros totales pares que hay son "+par);
            System.out.println("Los numeros totales impares que hay son "+impar);
    }
}

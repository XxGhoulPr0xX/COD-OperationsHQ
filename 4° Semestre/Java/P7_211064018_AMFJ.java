import java.util.Scanner;
public class P7_211064018_AMFJ                                 
{
    public static void main(String[] args)
    {
        Scanner entrada= new Scanner(System.in);
        int impar=0; int par=0; int m=0; int n=0;
        System.out.println("Dame el primer numero");
        m=entrada.nextInt();
        System.out.println("Dame el segundo numero");
        n=entrada.nextInt();
        for(int i=m;i<=n;i++){
            if((i%2)==0){
                System.out.println("Pares "+i);
                par=par+i;
            }
            else{
                System.out.println("Impares "+i);
                impar=impar+i;
            }
        }
        System.out.println("La suma total de numeros pares es "+par+" y la suma total de numeros impares es "+impar);
    }
}

import java.util.Scanner;
public class P1_211064018_AMFJ                                 
{
    public static void main(String[] args)
    {
        Scanner entrada= new Scanner(System.in);
        int n1=0; int n2=0;
        n1=entrada.nextInt();
        n2=entrada.nextInt();
        if(n2<n1){
            System.out.println(n1+" es mayor que "+n2);
        }
        else{
            System.out.println(n2+" es mayor que "+n1);
        }
    }
}

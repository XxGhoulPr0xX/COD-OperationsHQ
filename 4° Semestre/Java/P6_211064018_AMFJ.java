import java.util.Scanner;
public class P6_211064018_AMFJ                                 
{
    public static void main(String[] args)
    {
        Scanner entrada= new Scanner(System.in);
        double r=0; double tabla=0;
        System.out.println("Dame un numero para la raiz");
        r=entrada.nextInt();
        double resulta=Math.sqrt(r);
        System.out.println("La raiz del numero "+r+" es "+resulta);
        for(double i=1;i<=10;i++){
            tabla=resulta*i;
            System.out.println(resulta+"*"+i+"="+tabla);
        }
    }
}

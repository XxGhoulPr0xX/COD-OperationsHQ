import java.util.Scanner;
//y=((bc-d)^3/7+4a)+d-(1/3b)
public class P4_211064018_AMFJ                                 
{
    public static void main(String[] args)
    {
        Scanner entrada= new Scanner(System.in);
        double a,b,c,d,resultado;
        System.out.println("Dame los numeros para resolver la ecuacion");
        a=entrada.nextInt();
        b=entrada.nextInt();
        c=entrada.nextInt();
        d=entrada.nextInt();
        resultado=(Math.pow(((b*c)-d),3)/(7+4+a)+(d)+1/(3+b));
        System.out.println("El resultado es"+resultado);
    }
}

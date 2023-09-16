import java.util.Scanner;
//y=5x^3+ (ax-b/8+x/x^2-1)}
public class P3_211064018_AMFJ
{
    public static void main(String[] args)
    {
        Scanner entrada= new Scanner(System.in);
        double a,b,x,resultado;
        System.out.println("Dame los numeros");
        a=entrada.nextDouble();
        b=entrada.nextDouble();
        x=entrada.nextDouble();
        double operation1=5*Math.pow(x,3);
        double operation2=a*x-b;
        double operation3=8*x;
        double operation4=Math.pow(x,2)-1;
        double Division1=operation2/operation3;
        double Division2=Division1/operation4;
        
        resultado=operation1+Division2;
        
        System.out.println("El resultado es "+resultado);
    }
}
import java.util.Scanner;
public class FormulaGeneral
{
    Scanner in = new Scanner(System.in);
    public void Resultado()
    {
        System.out.print("Agrega el primer digito de tu ecuacion ");
        int a = in.nextInt();
        System.out.print("Agrega el segundo digito de tu ecuacion ");
        int b = in.nextInt();
        System.out.print("Agrega el tercer digito de tu ecuacion ");
        int c = in.nextInt();
        in.close();
        System.out.println(a+","+b+","+","+c);
        double before=(b*b)-4*a*c;
        double after=Math.sqrt(before);
        if(after>0)
        {
            double resultado1=(-b+after)/2*a;
            double resultado2=(-b-after)/2*a;
            System.out.println("el resultado de la ecuacion fue x1 es "+resultado1+" y x2 es "+resultado2);
        }
        else
        {
            System.out.println("Se trata de una solucion compleja");
        }
    }
}

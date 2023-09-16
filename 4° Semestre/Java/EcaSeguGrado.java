public class EcaSeguGrado
{
    private int a;
    private int b;
    private int c;
    public EcaSeguGrado(int a, int b, int c)
    {
        a=a; b=b; c=c;
    }
    public EcaSeguGrado()
    {
        a=4; b=8; c=0;
    }
    public void Resultado()
    {
        double operacion=(b*b)-4*a*c;
        double raiz=Math.sqrt(operacion);
        if(raiz>0)
        {
            double resultado1=(-b+raiz)/2*a;
            double resultado2=(-b-raiz)/2*a;
            System.out.println("el resultado de la ecuacion que pusiste fue "+resultado1+" y x2 es "+resultado2);
        }
        else
        {
            System.out.println("Se trata de una solucion compleja");
        }
    }
}

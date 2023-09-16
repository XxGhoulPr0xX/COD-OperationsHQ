import Formulas.Formulas;
public class Prueba1
{
    Formulas alfa=new Formulas(0.0,0.0,0.0,0.0,0.0,0.0);
    public void sampleMethod()
    {
        int a=1;
        int b=2;
        alfa=new Formulas(a,b,0.0,0.0,0.0,0.0);
        System.out.println(""+alfa.hipotenusa());
    }
}

//import java.util.Scanner;
public class P2_211064018_AMFJ                                 
{
    double Horas[];
    
    public void Nomina()
    {
        //Scanner obj=new Scanner (System.in);
        Horas=new  double[51];
        double Pagohoras=150;int HorasTrabajando;
        for(int i=1;i<=Horas.length-1;i++){
            System.out.println("Cuantas horas trabajo el obrero "+i);
            //Horas[i]=HorasTrabajando=obj.nextInt();
            Horas[i]= Math.floor(Math.random()*100);
            System.out.println("El obrero "+i+" ha trabajado un total de "+Horas[i]+" horas trabajando");
            double suma=Horas[i]*Pagohoras;
            System.out.println("La nomina total a pagar del trabajador "+i+" es de "+suma);
          }
    }
}

import java.util.Scanner;

public class uno
{
    public  static void main(String[] args){
        String fecha="";
        String name="";
        int edad=0;
        Scanner input= new Scanner (System.in);
        System.out.println("Nombre");
        name= input.nextLine();
        System.out.println("Edad");
        edad= input.nextInt();
        fecha= input.nextLine();
        System.out.println("Fecha");
    }
}

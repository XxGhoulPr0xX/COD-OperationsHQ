public class Edad
{
    public void Edad(int n){
        if(n<=12){
            System.out.println("Es un niño");
        }
        else if((n>=12)&&(n<=17)){
            System.out.println("Es un adolescente");
        }
        else if((n>=18)&&(n<=25)){
            System.out.println("Es un joven");
        }
        else if((n>=26)&&(n<=55)){
            System.out.println("Es un adulto");
        }
        else if(n>56){
            System.out.println("Adulto Mayor");
        }
        else{
            System.out.println("Error de edad");
        }
    }
}

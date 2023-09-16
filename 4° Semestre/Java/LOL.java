import java.util.Scanner;
public class LOL
{
        char[] abc;
        String[] palabras;
    public static void abc(){
        Scanner obj=new Scanner (System.in);
            char[] abc =new char[]          {'+','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',' '};//{"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"}}};
            String[] palabras= new String[] {"-","Alfa","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliett","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","X-ray","Yankee","Zulu","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Zero","Decimal"};
            String s=obj.nextLine();
        for(int i=0; i<s.length();i++){//separa la palabra
            char c = s.charAt(i);
            for(int j=0;j<abc.length;j++){;//el arreglo del abecedario
                if(s.charAt(i)==abc[j]){
                    //System.out.println("La letra "+abc[j]+" se encuentra en la posicion: "+j+" y el binario es "+palabras[j]);
                    System.out.print(" "+palabras[j]);
                }
            }
        }
    }
    public static void main(String[] args){
        abc();
    }
}

import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        System.out.println("Que operación quieres hacer: \n1.-Suma\n2.-Resta \n3.-Divison \n4.-Multiplicacion");
        int Opcion = scanner.nextInt();
        switch (Opcion) {
            case 1:
                {
                    System.out.println("Ingresa el dato 1 \nIngresa el dato 2");
                    int a = scanner.nextInt();
                    int b = scanner.nextInt();
                    int totalS=a+b;
                    System.out.println(totalS);
                    break;
                }
            case 2:
                {
                    System.out.println("Ingresa el dato 1 \nIngresa el dato 2");
                    int a = scanner.nextInt();
                    int b = scanner.nextInt();
                    int totalS=a-b;
                    System.out.println(totalS);
                    break;
                }
            case 3:
                {
                    System.out.println("Ingresa el dato 1 \nIngresa el dato 2");
                    int a = scanner.nextInt();
                    int b = scanner.nextInt();
                    int totalS=a*b;
                    System.out.println(totalS);
                    break;
                }
            case 4:
                {
                    System.out.println("Ingresa el dato 1 \nIngresa el dato 2");
                    int a = scanner.nextInt();
                    int b = scanner.nextInt();
                    int totalS=a/b;
                    System.out.println(totalS);
                    break;
                }
            default:
                break;
        }
    }
}

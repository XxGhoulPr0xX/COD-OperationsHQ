import java.util.Scanner;

public class CalculadoraOp {

    public static int suma(int a, int b) {
        return a + b;
    }

    public static int resta(int a, int b) {
        return a - b;
    }

    public static float division(int a, int b) {
        if (b == 0) {
            System.out.println("Error: No se puede dividir por cero.");
            return 0; // Devuelve 0 en caso de división por cero
        } else {
            return (float) a / b; // Convierte al menos uno de los operandos a float para obtener el resultado con decimales
        }
    }

    public static int multiplicacion(int a, int b) {
        return a * b;
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Qué operación quieres hacer: \n1.-Suma\n2.-Resta \n3.-División \n4.-Multiplicación");
            int opcion = scanner.nextInt();
            System.out.println("Ingresa el primer número:");
            int a = scanner.nextInt();
            System.out.println("Ingresa el segundo número:");
            int b = scanner.nextInt();
            float resultado = 0; // Inicializamos la variable resultado

            // Switch para realizar la operación seleccionada
            switch (opcion) {
                case 1:
                    resultado = suma(a, b);
                    break;
                case 2:
                    resultado = resta(a, b);
                    break;
                case 3:
                    resultado = division(a, b);
                    break;
                case 4:
                    resultado = multiplicacion(a, b);
                    break;
                default:
                    System.out.println("Opción no válida.");
                    return; // Termina la ejecución si la opción no es válida
            }

            // Mostrar el resultado de la operación
            System.out.println("El resultado es: " + resultado);
        }
    }
}

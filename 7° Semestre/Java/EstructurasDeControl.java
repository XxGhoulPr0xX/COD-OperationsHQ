import java.util.Scanner;

public class EstructurasDeControl {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            // Estructura if-else
            System.out.println("Estructura if-else:");
            System.out.print("Ingresa un número: ");
            int numero = scanner.nextInt();
            if (numero > 0) {
                System.out.println("El número es positivo.");
                        // Estructura switch
            System.out.println("\nEstructura switch:");
            System.out.print("Ingresa un día de la semana (1-7): ");
            int dia = scanner.nextInt();
            switch (dia) {
                case 1:
                    System.out.println("Lunes");
                    break;
                case 2:
                    System.out.println("Martes");
                    break;
                case 3:
                    System.out.println("Miércoles");
                    break;
                case 4:
                    System.out.println("Jueves");
                            // Estructura while
            System.out.println("\nEstructura while:");
            int contador = 1;
            while (contador <= 5) {
                System.out.println("Contador: " + contador);
                contador++;
            }
            
            // Estructura do-while
            System.out.println("\nEstructura do-while:");
            int contadorDoWhile = 1;
            do {
                System.out.println("Contador: " + contadorDoWhile);
                contadorDoWhile++;
            } while (contadorDoWhile <= 5);
            
            // Estructura for
            System.out.println("\nEstructura for:");
            for (int i = 1; i <= 5; i++) {
                System.out.println("Contador: " + i);
            }
            
            // Estructura for-each
            System.out.println("\nEstructura for-each:");
            int[] numeros = {1, 2, 3, 4, 5};
            for (int num : numeros) {
                System.out.println("Número: " + num);
            }
            
            // Estructura break y continue en un bucle
            System.out.println("\nEstructura break y continue en un bucle:");
            for (int i = 1; i <= 10; i++) {
                if (i == 5) {
                    continue; // Salta la iteración actual si i es igual a 5
                }
                if (i == 8) {
                    break; // Sale del bucle si i es igual a 8
                }
                System.out.println("Número: " + i);
            }
            
            // Estructura de control try-catch para manejo de excepciones
            System.out.println("\nEstructura try-catch:");
            System.out.print("Ingresa un número: ");
            try {
                int valor = Integer.parseInt(scanner.next());
                System.out.println("El doble del número es: " + (valor * 2));
            } catch (NumberFormatException e) {
                System.out.println("Error: No has ingresado un número válido.");
            }
            
            // Estructura de control break y continue en un bucle anidado
            System.out.println("\nEstructura break y continue en un bucle anidado:");
            for (int i = 1; i <= 3; i++) {
                for (int j = 1; j <= 3; j++) {
                    if (i == 2 && j == 2) {
                        continue; // Salta la iteración actual del bucle interno si i=2 y j=2
                    }
                    if (i == 3 && j == 3) {
                        break; // Sale del bucle interno si i=3 y j=3
                    }
                    System.out.println("i = " + i + ", j = " + j);
                }
            }
                    break;
                case 5:
                    System.out.println("Viernes");
                    break;
                case 6:
                    System.out.println("Sábado");
                    break;
                case 7:
                    System.out.println("Domingo");
                    break;
                default:
                    System.out.println("Número inválido.");
                    break;
            }
            
            
            // Estructura de control return en un método
            System.out.println("\nEstructura return en un método:");
            int resultado = suma(5, 3);
            System.out.println("Resultado de la suma: " + resultado);
            } else if (numero < 0) {
                System.out.println("El número es negativo.");
            } else {
                System.out.println("El número es cero.");
            }
        }
        
    }
    
    public static int suma(int a, int b) {
        return a + b;
    }
}
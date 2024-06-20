import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Pilas {
    private ArrayList<Integer> pila = new ArrayList<>();

    public ArrayList<Integer> insertarEnPila(int insert) {
        pila.add(insert);
        return pila;
    }

    public void mostrarPila() {
        System.out.println("Elementos en la pila:");
        for (int elemento : pila) {
            System.out.println(elemento);
        }
    }

    public String eliminarDePila(int eliminar) {
        String resultado = "";
        if (pila.contains(eliminar)) {
            pila.remove(Integer.valueOf(eliminar));
            resultado = "Se eliminó el elemento " + eliminar + " de la pila.";
        } else {
            resultado = "El elemento " + eliminar + " no está en la pila.";
        }
        return resultado;
    }

    public boolean buscarEnPila(int buscar) {
        return pila.contains(buscar);
    }

    public void mostrarAscendente() {
        System.out.println("Elementos en la pila en orden ascendente:");
        Collections.sort(pila); // Ordena la pila en orden ascendente
        for (int elemento : pila) {
            System.out.println(elemento);
        }
    }

    public void mostrarDescendente() {
        System.out.println("Elementos en la pila en orden descendente:");
        Collections.sort(pila, Collections.reverseOrder()); // Ordena la pila en orden descendente
        for (int elemento : pila) {
            System.out.println(elemento);
        }
    }

    public static void main(String[] args) {
        Pilas pilas = new Pilas(); // Instanciamos la clase Pilas para poder acceder a sus métodos
        try (Scanner scanner = new Scanner(System.in)) {
            while (true) {
                System.out.println("Qué operación quieres hacer: \n1.-Insertar \n2.-Mostrar \n3.-Buscar \n4.-Mostrar Ascendente \n5.-Mostrar Descendente \n6.-Eliminar \n7.-Salir");
                int opcion = scanner.nextInt();
                switch (opcion) {
                    case 1:
                        System.out.println("Ingresa el valor que deseas insertar en la pila:");
                        int valorInsertar = scanner.nextInt();
                        pilas.insertarEnPila(valorInsertar);
                        break;
                    case 2:
                        pilas.mostrarPila();
                        break;
                    case 3:
                        System.out.println("Ingresa el valor que deseas buscar en la pila:");
                        int valorBuscar = scanner.nextInt();
                        System.out.println("El valor " + valorBuscar + " está en la pila: " + pilas.buscarEnPila(valorBuscar));
                        break;
                    case 4:
                        pilas.mostrarAscendente();
                        break;
                    case 5:
                        pilas.mostrarDescendente();
                        break;
                    case 6:
                        System.out.println("Ingresa el valor que deseas eliminar de la pila:");
                        int valorEliminar = scanner.nextInt();
                        System.out.println(pilas.eliminarDePila(valorEliminar));
                        break;
                    case 7:
                        System.out.println("Saliendo del programa...");
                        System.exit(0); // Terminamos el programa
                    default:
                        System.out.println("Opción no válida. Por favor, elige otra opción.");
                        break;
                }
            }
        }
    }
}

import java.util.ArrayList;
import java.util.Scanner;

public class ChecadorExpresion {

    public static ArrayList<String> cadenaSeparada(String cadena) {
        ArrayList<String> caracteresSeparados = new ArrayList<>();
        char[] chars = cadena.toCharArray();
        for (char c : chars) {
            caracteresSeparados.add(String.valueOf(c));
        }
        return caracteresSeparados;
    }

    public static String comprobadorOperadores(ArrayList<String> caracteres) {
        StringBuilder errores = new StringBuilder();
        for (int i = 0; i < caracteres.size() - 1; i++) {
            String actual = caracteres.get(i);
            String siguiente = caracteres.get(i + 1);
            if (esOperador(actual) && esOperador(siguiente)) {
                if (errores.length() > 0) {
                    errores.append(", ");
                }
                errores.append("Error: operador '").append(actual)
                        .append("' en la posición ").append(i + 1)
                        .append(" seguido por otro operador '").append(siguiente)
                        .append("' en la posición ").append(i + 2);
            }
        }
        return errores.toString();
    }

    public static boolean esOperador(String caracter) {
        return "+-*/".contains(caracter);
    }

    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese la expresión matemática:");
        String expresion = scanner.nextLine();
        ArrayList<String> caracteres = cadenaSeparada(expresion);
        String resultado = comprobadorOperadores(caracteres);
        if (resultado.isEmpty()) {
            System.out.println("La expresión es válida.");
        } else {
            System.out.println(resultado);
        }
    }
}

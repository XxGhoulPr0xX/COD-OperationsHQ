public class Funcionalidad {
    private static int def; // Declarar 'def' como variable de instancia

    // Valida el código de la tarjeta prepago
    public static boolean validarCodigo(String codigo) {
        boolean bandera = false;
        if (codigo.length() != 6) {
            return false; // El código debe tener exactamente 6 caracteres
        }
        char a = codigo.charAt(0);
        String bc = codigo.substring(1, 3);
        char d = codigo.charAt(3);
        def = Integer.parseInt(codigo.substring(3, 6));
        if ((a == '2' || a == '4' || a == '6') && (d == '0' || d == '1')) {
            if (bc.equals("10") || bc.equals("20") || bc.equals("40") || bc.equals("86") || bc.equals("78") || bc.equals("30")) {
                bandera = true;
            }
        } else if ((a == '0' || a == '1' || a == '3') && d == '0') {
            bandera = true;
        }
        return bandera;
    }
    //Realiza la recarga del saldo
    public static String recargarSaldo(String codigo, int montoRecarga) {
        String resultado = codigo;
        if (validarCodigo(codigo)) {
            if (def <= 199) {
                int nuevoSaldo = def + montoRecarga;
                if (nuevoSaldo <= 199) {
                    resultado = codigo.substring(0, 3) + String.format("%03d", nuevoSaldo);
                } else {
                    resultado = codigo.substring(0, 3) + "199"; // Limitar el saldo máximo a 199
                }
            }
            if (resultado.charAt(0) == '0' || resultado.charAt(0) == '1' || resultado.charAt(0) == '3') {
                resultado = "2" + resultado.substring(1);
            }
        } else {
            resultado = "CODIGO INVALIDO";
        }
        return resultado;
    }
}
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] mesesDelAnio = {"","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};
        System.out.print("Ingresa una CURP: ");
        String curp = input.nextLine();
        if (curp.length() == 18) {
            System.out.println("El tamaño de la CURP es correcto.");
        } else {
            System.out.println("El tamaño de la CURP es incorrecto.");
        }
        if (curp.substring(0, 4).matches("[a-zA-Z]+")) {
            System.out.println("Las primeras cuatro letras de la CURP son válidas.");
        } else {
            System.out.println("Las primeras cuatro letras de la CURP son incorrectas.");
        }
        String anio = "";
        if (Character.isDigit(curp.charAt(4)) && Character.isDigit(curp.charAt(5))) {
            int anioInt = Integer.parseInt(curp.substring(4, 6));
            if (anioInt >= 0 && anioInt <= 99) {
                if (anioInt >= 0 && anioInt <= 21) {
                    anio = "20" + String.format("%02d", anioInt);
                } else {
                    anio = "19" + String.format("%02d", anioInt);
                }
                System.out.println("Los dígitos 5 y 6 de la CURP son números.");
            } else {
                System.out.println("Los dígitos 5 y 6 de la CURP no corresponden a un año válido.");
            }
        } else {
            System.out.println("Los dígitos 5 y 6 de la CURP no son números.");
        }
        int mes = 0;
        if (Character.isDigit(curp.charAt(6)) && Character.isDigit(curp.charAt(7))) {
            mes = Integer.parseInt(curp.substring(6, 8));
            System.out.println("Los dígitos 7 y 8 de la CURP son números.");
        } else {
            System.out.println("Los dígitos 7 y 8 de la CURP no son números.");
        }
        int dia = 0;
        if (Character.isDigit(curp.charAt(8)) && Character.isDigit(curp.charAt(9))) {
            dia = Integer.parseInt(curp.substring(8, 10));
            System.out.println("Los dígitos 9 y 10 de la CURP son números.");
        } else {
            System.out.println("Los dígitos 9 y 10 de la CURP no son números.");
        }
        String genero = "";
        if (curp.charAt(10) == 'H') {
            genero = "Hombre";
            System.out.println("El dígito 11 de la CURP corresponde a un género válido: ");
        } else if (curp.charAt(10) == 'M') {
            genero = "Mujer";
            System.out.println("El dígito 11 de la CURP corresponde a un género válido: ");
        } else {
            System.out.println("El dígito 11 de la CURP no corresponde a un género válido.");
        }
        String estado = "";
        if (Character.isLetter(curp.charAt(11)) && Character.isLetter(curp.charAt(12))) {
          estado = curp.substring(11, 13);
          System.out.println("Los dígitos 12 y 13 de la CURP corresponden a letras.");
        } else {
          System.out.println("Los dígitos 12 y 13 de la CURP no corresponden a letras.");
        }
        if (Character.isLetter(curp.charAt(13)) && Character.isLetter(curp.charAt(14)) && Character.isLetter(curp.charAt(15))) {
          System.out.println("Los dígitos 14, 15 y 16 de la CURP corresponden a letras.");
        } else {
          System.out.println("Los dígitos 14, 15 y 16 de la CURP no corresponden a letras.");
        }
        char digito17 = curp.charAt(16);
        char digito18 = curp.charAt(17);
        if (Character.isLetter(digito17) && Character.isDigit(digito18)) {
          System.out.println("El dígito 17 corresponde a una letra y el dígito 18 corresponde a un número.");
          System.out.println("El formato de terminación es letra-número.");
        } else if (Character.isDigit(digito17) && Character.isDigit(digito18)) {
          System.out.println("El dígito 17 corresponde a un número y el dígito 18 corresponde a un número.");
          System.out.println("El formato de terminación es número-número.");
        } else {
        System.out.println("El dígito 17 y/o el dígito 18 de la CURP no cumplen con las características requeridas.");
        }
  System.out.println("CURP CORRECTO\nTu fecha de nacimiento es: " + dia + " de mes " + mesesDelAnio[mes] + " de año " + anio + "\nEres: " + genero + "\nNaciste en el estado: " + estado);
}
}

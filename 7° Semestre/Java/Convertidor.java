public class Convertidor {
    //Clase que convierte una operacion en notacion posfijo

    PilaOperador pila = new PilaOperador();
    String operador;
    char[] cadena;
    String[] posfijo;
    int i = 0;
    int j = 0;

    //Cambia la cadena por un arreglo de caracteres
    public char[] operacionToArray(String operacion) {
        cadena = operacion.toCharArray();
        return cadena;
    }

    public int evaluarPrioridad(char topePila, char cadena) {
        System.out.println(topePila);
        System.out.println(cadena);
        int temp = 1;
        if (null != Character.toString(topePila)) {
            switch (Character.toString(topePila)) {
                case "+":
                    if (null != Character.toString(cadena)) {
                        switch (Character.toString(cadena)) {
                            case "+":
                                temp = 1;
                                break;
                            case "-":
                                temp = 1;
                                break;
                            case "*":
                                temp = 0;
                                break;
                            case "/":
                                temp = 0;
                                break;
                            case "^":
                                temp = 0;
                                break;
                            case ")":
                                temp = 1;
                                break;
                            case "(":
                                temp = 0;
                                break;
                            default:
                                break;
                        }
                    }
                    break;
                case "-":
                    if (null != Character.toString(cadena)) {
                        switch (Character.toString(cadena)) {
                            case "+":
                                temp = 1;
                                break;
                            case "-":
                                temp = 1;
                                break;
                            case "*":
                                temp = 0;
                                break;
                            case "/":
                                temp = 0;
                                break;
                            case "^":
                                temp = 0;
                                break;
                            case ")":
                                temp = 1;
                                break;
                            case "(":
                                temp = 0;
                                break;
                            default:
                                break;
                        }
                    }
                    break;
                case "*":
                    if (null != Character.toString(cadena)) {
                        switch (Character.toString(cadena)) {
                            case "+":
                                temp = 1;
                                break;
                            case "-":
                                temp = 1;
                                break;
                            case "*":
                                temp = 1;
                                break;
                            case "/":
                                temp = 1;
                                break;
                            case "^":
                                temp = 0;
                                break;
                            case ")":
                                temp = 1;
                                break;
                            case "(":
                                temp = 0;
                                break;
                            default:
                                break;
                        }
                    }
                    break;
                case "/":
                    if (null != Character.toString(cadena)) {
                        switch (Character.toString(cadena)) {
                            case "+":
                                temp = 1;
                                break;
                            case "-":
                                temp = 1;
                                break;
                            case "*":
                                temp = 1;
                                break;
                            case "/":
                                temp = 1;
                                break;
                            case "^":
                                temp = 0;
                                break;
                            case ")":
                                temp = 1;
                                break;
                            case "(":
                                temp = 0;
                                break;
                            default:
                                break;
                        }
                    }
                    break;
                case "^":
                    if (null != Character.toString(cadena)) {
                        switch (Character.toString(cadena)) {
                            case "+":
                                temp = 1;
                                break;
                            case "-":
                                temp = 1;
                                break;
                            case "*":
                                temp = 1;
                                break;
                            case "/":
                                temp = 1;
                                break;
                            case "^":
                                temp = 1;
                                break;
                            case ")":
                                temp = 1;
                                break;
                            case "(":
                                temp = 0;
                                break;
                            default:
                                break;
                        }
                    }
                    break;
                case "(":
                    if (null != Character.toString(cadena)) {
                        switch (Character.toString(cadena)) {
                            case "+":
                                temp = 0;
                                break;
                            case "-":
                                temp = 0;
                                break;
                            case "*":
                                temp = 0;
                                break;
                            case "/":
                                temp = 0;
                                break;
                            case "^":
                                temp = 0;
                                break;
                            case ")":
                                temp = 2;
                                break;
                            case "(":
                                temp = 0;
                                break;
                            default:
                                break;
                        }
                    }
                    break;
                default:
                    break;
            }
        }
        System.out.println(temp);
        return temp;
    }

    //Evalua si es u operador

    public static boolean esOperador(String letra) {
        if (letra.equals("=") || letra.equals("^") || letra.equals("/") || letra.equals("*") || letra.equals("+") || letra.equals("-") || letra.equals("(") || letra.equals(")")) {
            return true;
        }
        return false;
    }

    // Convertir a posfijo  

    public String[] convertir(char[] cadena) {

        PilaOperador pila = new PilaOperador();
        i = 0;
        j = 0;

        posfijo = new String[cadena.length];
        while (i < cadena.length) {
            if (!esOperador(Character.toString(cadena[i]))) {
                posfijo[j] = "";
                while (!esOperador(Character.toString(cadena[i]))) {
                    posfijo[j] = posfijo[j] + cadena[i] + "";
                    i++;
                    if (i == cadena.length) {
                        break;
                    }

                }
                j++;
            } else if (esOperador(Character.toString(cadena[i]))) {
                if (pila.estaVacia()) {
                    pila.insertarPila(cadena[i]);
                    i++;
                } else if (evaluarPrioridad(pila.topePila(), cadena[i]) == 0) {
                    pila.insertarPila(cadena[i]);
                    i++;
                } else if (evaluarPrioridad(pila.topePila(), cadena[i]) == 1) {
                    posfijo[j] = Character.toString(pila.retirarPila());
                    j++;
                } else if (evaluarPrioridad(pila.topePila(), cadena[i]) == 2) {
                    pila.retirarPila();
                    i++;
                }
            }
        }
        if (i == cadena.length) {
            while (!pila.estaVacia()) {
                posfijo[j] = Character.toString(pila.retirarPila());
                j++;
            }
        }
        return posfijo;
    }
    public static String arrayToString(String[] array) {
        StringBuilder sb = new StringBuilder();
        for (String s : array) {
            if (s != null) {
                sb.append(s).append(" ");
            }
        }
        return sb.toString().trim();
    }
    public static void main(String[] args) {
        // Expresión a convertir
        String expresion = "{[3+5^10]}^(x-y*2)";
        Convertidor convertidor = new Convertidor();
        char[] cadena = convertidor.operacionToArray(expresion);
        String[] posfijo = convertidor.convertir(cadena);
        System.out.println("Expresión original: " + expresion);
        System.out.println("Expresión posfija: " + arrayToString(posfijo));
    }
    public class PilaOperador {
        NodoOperador p;
        PilaOperador() {
            p = null;
        }
    
        public void insertarPila(char x) {
            NodoOperador n;
            n = new NodoOperador(x);
            n.sig = p;
            p = n;
        }
        public char retirarPila() {
            char t = p.info;
            p = p.sig;
            return t;
        }
    
    
        public char topePila() {
            return p.info;
        }
    
        public boolean estaVacia() {
            return !(p != null);
        }
    }
    public class NodoOperador {

        char info;
        NodoOperador sig;
    
        NodoOperador(char i) {
            info = i;
            sig = null;
        }
    }
    
}

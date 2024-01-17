import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Token {
    String tipo;
    String valor;

    public Token(String tipo, String valor) {
        this.tipo = tipo;
        this.valor = valor;
    }
}

class AnalizadorLexico {
    List<String[]> patrones;

    public AnalizadorLexico() {
        patrones = new ArrayList<>();
        patrones.add(new String[] { "[0-9]+", "ENTERO" });
        patrones.add(new String[] { "[a-zA-Z_][a-zA-Z0-9_]*", "IDENTIFICADOR" });
        patrones.add(new String[] { "\\+", "SUMA" });
        patrones.add(new String[] { "-", "RESTA" });
        patrones.add(new String[] { "\\*", "MULTIPLICACION" });
        patrones.add(new String[] { "/", "DIVISION" });
    }

    public List<Token> analizar(String entrada) {
        // Eliminar espacios en blanco
        entrada = entrada.replace(" ", "");
        List<Token> tokens = new ArrayList<>();
        while (!entrada.isEmpty()) {
            for (String[] patron : patrones) {
                Pattern pattern = Pattern.compile(patron[0]);
                Matcher matcher = pattern.matcher(entrada);
                if (matcher.find() && matcher.start() == 0) {
                    String valor = matcher.group();
                    tokens.add(new Token(patron[1], valor));
                    entrada = entrada.substring(valor.length());
                    break;
                }
            }
        }
        return tokens;
    }

    public static void main(String[] args) {
        AnalizadorLexico analizador = new AnalizadorLexico();
        String entrada = "3 + 4 * x - y / 2";
        List<Token> tokens = analizador.analizar(entrada);
        for (Token token : tokens) {
            System.out.println("Tipo: " + token.tipo + ", Valor: " + token.valor);
        }
    }
}

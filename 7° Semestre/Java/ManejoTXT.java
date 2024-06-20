import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ManejoTXT {
    private String filePath;

    public ManejoTXT(String filePath) {
        this.filePath = filePath;
    }

    public String convertirATextoBinario() throws IOException {
        StringBuilder binaryContent = new StringBuilder();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                for (char c : line.toCharArray()) {
                    String binaryChar = Integer.toBinaryString(c);
                    binaryContent.append(binaryChar).append(" ");
                }
                binaryContent.append("\n");
            }
        }

        return binaryContent.toString();
    }

    public int sumarBinarios(String binaryText) {
        String[] lines = binaryText.split("\n");
        int sum = 0;

        for (String line : lines) {
            String[] binaries = line.split(" ");
            for (String binary : binaries) {
                if (!binary.isEmpty()) {
                    sum += Integer.parseInt(binary, 2); // Convertir binario a entero y sumar
                }
            }
        }

        return sum;
    }
    public int conversion(int suma) {
        double tresTan30 = 3 * Math.tan(Math.toRadians(30));
        double resultado = tresTan30 * suma;
        return (int) resultado;
    }
    
    public String[] extraerDatos(String texto) {
        String[] lineas = texto.split("\n");
        String[] datos = new String[4];

        for (String linea : lineas) {
            String[] partes = linea.split(":");
            if (partes.length == 2) {
                String clave = partes[0].trim().toLowerCase();
                String valor = partes[1].trim();
                switch (clave) {
                    case "formato de música":
                        datos[0] = valor;
                        break;
                    case "autor":
                        datos[1] = valor;
                        break;
                    case "año":
                        datos[2] = valor;
                        break;
                    case "título":
                        datos[3] = valor;
                        break;
                }
            }
        }

        return datos;
    }

    public String leerTexto() throws IOException {
        StringBuilder contenidoTexto = new StringBuilder();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                contenidoTexto.append(line).append("\n");
            }
        }

        return contenidoTexto.toString();
    }

    public static void main(String[] args) {
    String filePath = "C:\\Users\\XxGho\\Documents\\Escuela\\7° Semestre\\Base de datos no relacionales\\Entregable 1\\Deep Purple Live 2000.txt";
    ManejoTXT txtABinario = new ManejoTXT(filePath);

    try {
        String texto = txtABinario.leerTexto();
        String[] datos = txtABinario.extraerDatos(texto);

        String binaryText = txtABinario.convertirATextoBinario();
        int binarySum = txtABinario.sumarBinarios(binaryText);
        int resultadoFinal = txtABinario.conversion(binarySum);
        String formatoMusica = datos[0];
        String autor = datos[1];
        String año = datos[2];
        String titulo = datos[3];
            
        System.out.println("Formato de musica: " + formatoMusica);
        System.out.println("Autor: " + autor);
        System.out.println("Anio: " + año);
        System.out.println("Titulo: " + titulo);
        System.out.println(resultadoFinal);
    } catch (IOException e) {
        System.err.println("Error al leer el archivo: " + e.getMessage());
    }
}

}

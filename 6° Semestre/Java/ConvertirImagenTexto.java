import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;

import javax.imageio.ImageIO;

public class ConvertirImagenTexto {
    public byte[] ImagenABytes(String ImagenPath){
        byte[] bytesDeLaImagen = null;
        try {
            BufferedImage imagen = ImageIO.read(new File(ImagenPath));
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(imagen, "png", baos);
            bytesDeLaImagen = baos.toByteArray();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return bytesDeLaImagen;
    }
    public byte[] cadenaABytes(String cadena) {
        return cadena.getBytes();
    }
    public byte[] buscarBytesEnImagen(byte[] bytesCadena, byte[] bytesImagen) {
        int[] lps = computeLPSArray(bytesCadena);
        int i = 0;  // índice para bytesImagen[]
        int j = 0;  // índice para bytesCadena[]
        System.out.println(bytesCadena.length);
        while (i < bytesImagen.length) {
            if (bytesCadena[j] == bytesImagen[i]) {
                j++;
                i++;
            }
            if (j == bytesCadena.length) {
                // Coincidencia encontrada, imprimir información
                System.out.println("Coincidencia encontrada en el índice: " + (i - j));
                for (int k = i - j; k < i; k++) {
                    System.out.print(bytesImagen[k] + " ");
                }
                System.out.println();
    
                // Verificar si la cadena completa coincide
                if (Arrays.equals(bytesCadena, Arrays.copyOfRange(bytesImagen, i - j, i))) {
                    System.out.println("Coincidencia completa encontrada");
                    return Arrays.copyOfRange(bytesImagen, i - j, i);
                }
                // Reiniciar el índice de la cadena para buscar coincidencias adicionales
                j = lps[j - 1];
            } else if (i < bytesImagen.length && bytesCadena[j] != bytesImagen[i]) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i = i + 1;
                }
            }
            // Imprimir información adicional
        }
        // No se encontró ninguna coincidencia
        System.out.println("Los bytes de la cadena no fueron encontrados en la imagen");
        return null;
    }    
    private int[] computeLPSArray(byte[] pat) {
        int[] lps = new int[pat.length];
        int len = 0;
        int i = 1;
        while (i < pat.length) {
            if (pat[i] == pat[len]) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }
}

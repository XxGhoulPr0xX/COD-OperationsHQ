import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class ConvertirTextoImagen {

    public void ocultarDatosEnImagen(String imagePath, String mensaje, String outputImagePath) {
        try {
            BufferedImage imagen = ImageIO.read(new File(imagePath));
            byte[] bytesMensaje = mensaje.getBytes();
            int contador = 0;
            for (int y = 0; y < imagen.getHeight(); y++) {
                for (int x = 0; x < imagen.getWidth(); x++) {
                    if (contador < bytesMensaje.length) {
                        int rgb = imagen.getRGB(x, y);
                        rgb = (rgb & 0xFFFF00FF) | ((bytesMensaje[contador] & 0xFF) << 8);
                        imagen.setRGB(x, y, rgb);
                        contador++;
                    } else {
                        break; // Detener el bucle cuando todos los datos se han ocultado
                    }
                }
            }

            ImageIO.write(imagen, "png", new File(outputImagePath));
            System.out.println("Datos ocultos en la imagen con éxito.");
            System.out.println("Cantidad de datos ocultos: " + contador + " bytes.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}


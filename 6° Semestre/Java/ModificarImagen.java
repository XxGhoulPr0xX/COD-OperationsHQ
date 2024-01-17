import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Iterator;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.imageio.ImageReadParam;
import javax.imageio.ImageReader;
import javax.imageio.stream.ImageInputStream;

public class ModificarImagen {
public static void main(String[] args) throws FileNotFoundException, IOException {
    ModificarImagen modificador = new ModificarImagen();
    Scanner scanner = new Scanner(System.in);
    System.out.print("Introduce la cadena a ocultar: ");
    String frase = scanner.nextLine();
    String fraseSinEspacios = frase.replace(" ", "");
    byte[] bytesDeLaFrase = modificador.stringABytes(fraseSinEspacios);
    File file = new File("C:\\Users\\XxGho\\Pictures\\cropped-1366-768-60527.jpg");
    byte[] bytesDeLaImagen = modificador.imagenABytes(file);
    int inicio = 100;
    for (int i = 0; i < bytesDeLaFrase.length && inicio < bytesDeLaImagen.length; i++, inicio++) {
        bytesDeLaImagen[inicio] = bytesDeLaFrase[i];
    }
    modificador.bytesAImagen(bytesDeLaImagen, "C:\\Users\\XxGho\\Pictures\\cropped-1366-768-60527 -copia.jpg");
    System.out.print("Introduce la cantidad de bytes que va imprimir: ");
    int canBytes = scanner.nextInt();
    for (int i = 100; i  < 100+canBytes; i++) {
        System.out.println("Byte en posición " + i + ": " + String.valueOf((char) bytesDeLaImagen[i]));
    scanner.close();
    }
}
    public byte[] stringABytes(String str) {
        return str.getBytes();
    }
    public byte[] imagenABytes(File file) throws FileNotFoundException, IOException {
        FileInputStream ptr = new FileInputStream(file);
        ByteArrayOutputStream ptr1 = new ByteArrayOutputStream();
        byte[] buf = new byte[1024];
        try {
            for (int readNum; (readNum = ptr.read(buf)) != -1;) {
                ptr1.write(buf, 0, readNum);
            }
        } catch (IOException ex) {
            Logger.getLogger(ModificarImagen.class.getName()).log(Level.SEVERE, null, ex);
        }
        return ptr1.toByteArray();
    }
    public void bytesAImagen(byte[] bytesDeLaImagen, String rutaDestino) throws FileNotFoundException, IOException {
        ByteArrayInputStream bis = new ByteArrayInputStream(bytesDeLaImagen);
        Iterator<?> readers = ImageIO.getImageReadersByFormatName("jpg");
        ImageReader reader = (ImageReader) readers.next();
        Object source = bis;
        ImageInputStream iis = ImageIO.createImageInputStream(source);
        reader.setInput(iis, true);
        ImageReadParam param = reader.getDefaultReadParam();
        Image image = reader.read(0, param);
        BufferedImage bufferedImage = new BufferedImage(image.getWidth(null), image.getHeight(null),
                BufferedImage.TYPE_INT_RGB);
        Graphics2D g2 = bufferedImage.createGraphics();
        g2.drawImage(image, null, null);
        // Guarda la nueva imagen con los bytes modificados
        File imageFile = new File(rutaDestino);
        ImageIO.write(bufferedImage, "jpg", imageFile);
        System.out.println("Nueva imagen creada en: " + imageFile.getPath());
    }
}

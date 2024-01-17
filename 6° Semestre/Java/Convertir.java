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
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.imageio.ImageReadParam;
import javax.imageio.ImageReader;
import javax.imageio.stream.ImageInputStream;
public class Convertir 
{
    public static void main(String[] args) throws FileNotFoundException, IOException 
    {	
        Convertir a1 = new Convertir();
        File file = new File("C:\\Users\\XxGho\\Pictures\\cropped-1366-768-318314.jpg");
        byte[] bytesDeLaImagen = a1.imagenABytes(file);
        String [] binarios = new String[5024];
        System.out.println("Binario de la imagen");
        for (int i = 0; i < 100; i++) {
            System.out.println(binarios[i]);
        }
        binarios= a1.byteABinario(bytesDeLaImagen);
        a1.bytesAImagen(bytesDeLaImagen);
    }//main
    public byte [] imagenABytes(File file) throws FileNotFoundException, IOException
    {
        FileInputStream ptr = new FileInputStream(file);
        ByteArrayOutputStream ptr1 = new ByteArrayOutputStream();
        byte[] buf = new byte[1024];
        try {
                for (int readNum; (readNum = ptr.read(buf)) != -1;) {
                    ptr1.write(buf, 0, readNum); 
                }
            } catch (IOException ex) {
                Logger.getLogger(Convertir.class.getName()).log(Level.SEVERE, null, ex);
            }   
            byte[] bytesDeLaImagen = ptr1.toByteArray();
            return bytesDeLaImagen;
    }
    public void bytesAImagen(byte [] bytesDeLaImagen) throws FileNotFoundException, IOException
    {
        ByteArrayInputStream bis = new ByteArrayInputStream(bytesDeLaImagen);
        Iterator<?> readers = ImageIO.getImageReadersByFormatName("jpg");
        ImageReader reader = (ImageReader) readers.next();
        Object source = bis; 
        ImageInputStream iis = ImageIO.createImageInputStream(source); 
        reader.setInput(iis, true);
        ImageReadParam param = reader.getDefaultReadParam();
        Image image = reader.read(0, param);     
        BufferedImage bufferedImage = new BufferedImage(image.getWidth(null), image.getHeight(null),BufferedImage.TYPE_INT_RGB);
        Graphics2D g2 = bufferedImage.createGraphics();
        g2.drawImage(image, null, null);
        File imageFile = new File("C:\\Users\\XxGho\\Pictures\\cropped-1366-768-318314.jpg");
        ImageIO.write(bufferedImage, "jpg", imageFile);
        System.out.println(imageFile.getPath());
    }
    
    public String [] byteABinario(byte [] bytesDeLaImagen) 
    {
        int j=0;
        System.out.println(j);
        String [] binarios  = new String[bytesDeLaImagen.length];
        for (int k= 0; k < bytesDeLaImagen.length; k++)
        {
            byte b1 = (byte)bytesDeLaImagen[k];
            String s1 = String.format("%8s", Integer.toBinaryString(b1 & 0xFF)).replace(' ', '0');
            binarios[k]=s1;   
            if (k+1 == bytesDeLaImagen.length)
                j=k;
        }
        return binarios;
    }
}
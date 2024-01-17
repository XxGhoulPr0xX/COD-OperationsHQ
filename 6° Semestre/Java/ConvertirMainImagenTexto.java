import java.util.Scanner;

public class ConvertirMainImagenTexto {
    public static void main(String[] args) {
        ConvertirImagenTexto convertidor = new ConvertirImagenTexto();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce la ruta de la imagen: ");
        String imagePath = scanner.nextLine();
        System.out.print("Introduce el mensaje a buscar: ");
        String mensaje = scanner.nextLine();
        byte[] bytesDeLaImagen = convertidor.ImagenABytes(imagePath);
        byte[] bytesDeLaCadena = convertidor.cadenaABytes(mensaje);
        byte[] bytesRecuperados = convertidor.buscarBytesEnImagen(bytesDeLaCadena, bytesDeLaImagen);
        System.out.println(bytesRecuperados);
        scanner.close();
    }
}

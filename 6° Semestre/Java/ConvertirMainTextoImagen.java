import java.util.Scanner;

public class ConvertirMainTextoImagen {
        public static void main(String[] args) {
        ConvertirTextoImagen alpha= new ConvertirTextoImagen();
        Scanner scanner = new Scanner(System.in);
        String imagePath = "C:\\Users\\XxGho\\Pictures\\R.png";
        System.out.print("Introduce el mensaje que deseas ocultar: ");
        String mensaje = scanner.nextLine();
        String outputImagePath = "C:\\Users\\XxGho\\Pictures\\R- copia.png";
        alpha.ocultarDatosEnImagen(imagePath, mensaje, outputImagePath);
        scanner.close();
    }
}

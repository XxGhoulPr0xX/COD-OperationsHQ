import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;

public class Cliente {

    public static void main(String[] args) {
        final String direccionServidor = "192.168.137.253"; // Cambia esto a la dirección IP del servidor
        final int puerto = 9876;

        try (Socket socket = new Socket(direccionServidor, puerto);
            ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream());
            ObjectInputStream in = new ObjectInputStream(socket.getInputStream())) {

            String mensaje = "Hola desde el cliente";
            out.writeObject(mensaje);

            String respuestaServidor = (String) in.readObject();
            System.out.println("Respuesta del servidor: " + respuestaServidor);

        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}

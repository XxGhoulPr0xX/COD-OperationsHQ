package Algoritmo;
import java.io.IOException;

public class ReplicacionBD {

    public static void main(String[] args) {
        String dbName = "juego";
        String backupFile = "databaseBackup.sql";
        replicateDatabaseForXAMPP(dbName, backupFile);
    }

    private static void replicateDatabaseForXAMPP(String dbName, String backupFile) {
        String xamppPath = "C:\\xampp\\mysql\\bin\\";
        String username = "sa"; // Cambia esto si tu usuario de MySQL es diferente
        String password = "123456789"; // Deja esto vacío si no tienes una contraseña para root

        try {
            // Realizar dump de la base de datos
            String dumpCommand = String.format("%smysqldump -u %s -p%s %s -r %s",
                    xamppPath, username, password, dbName, backupFile);
            Process dumpProcess = Runtime.getRuntime().exec(dumpCommand);
            int dumpResult = dumpProcess.waitFor();
            if (dumpResult == 0) {
                System.out.println("Dump de la base de datos realizado correctamente.");
            } else {
                System.err.println("Error al realizar el dump de la base de datos.");
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}

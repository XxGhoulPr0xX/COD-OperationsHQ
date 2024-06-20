package Algoritmo;
import java.io.File;
import java.io.IOException;

public class RestauracionBD {
    public static void main(String[] args) {
        String backupFile = "databaseBackup.sql";
        String newDbName = "juego";

        recoverDatabaseForXAMPP(newDbName, backupFile);
    }

    private static void recoverDatabaseForXAMPP(String newDbName, String backupFile) {
        String xamppPath = "C:\\xampp\\mysql\\bin\\";
        String username = "sa"; // Cambia esto si tu usuario de MySQL es diferente
        String password = "123456789"; // Deja esto vacío si no tienes una contraseña para root

        try {
            // Crear una nueva base de datos
            String createDbCommand = String.format("%smysql -u %s -p%s -e \"CREATE DATABASE IF NOT EXISTS %s\"",
                    xamppPath, username, password, newDbName);
            Process createDbProcess = Runtime.getRuntime().exec(createDbCommand);
            int createDbResult = createDbProcess.waitFor();
            if (createDbResult == 0) {
                System.out.println("Nueva base de datos creada correctamente.");
            } else {
                System.err.println("Error al crear la nueva base de datos.");
                return;
            }

            // Restaurar la base de datos desde el archivo de respaldo
            ProcessBuilder restoreProcessBuilder = new ProcessBuilder(
                    xamppPath + "mysql",
                    "-u", username,
                    "-p" + password,
                    newDbName
            );
            restoreProcessBuilder.redirectInput(new File(backupFile));
            Process restoreProcess = restoreProcessBuilder.start();
            int restoreResult = restoreProcess.waitFor();
            if (restoreResult == 0) {
                System.out.println("Base de datos restaurada correctamente.");
            } else {
                System.err.println("Error al restaurar la base de datos.");
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}

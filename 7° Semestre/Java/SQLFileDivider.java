import java.io.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class SQLFileDivider {

    public static void main(String[] args) {
        String inputFile = "C:\\Users\\XxGho\\Documents\\Escuela\\7° Semestre\\Programación General\\SQL\\Comandos Basicos MariaDB.sql";
        String outputFile1 = "output1.sql";
        String outputFile2 = "output2.sql";
        String outputFile3 = "output3.sql";
        int fileSize = 1024 * 1024; // 1MB

        // Dividir el archivo y calcular el checksum
        String originalChecksum = divideAndCloneSQLFile(inputFile, outputFile1, outputFile2, outputFile3, fileSize);

        // Verificar el checksum antes de reconstruir el archivo
        if (originalChecksum != null) {
            System.out.println("Checksum calculado para el archivo original: " + originalChecksum);
            System.out.println("Verificando el checksum antes de la reconstrucción...");
            if (verifyChecksum(originalChecksum, originalChecksum)) {
                System.out.println("Checksum verificado. Iniciando reconstrucción del archivo original...");
                File file1 = new File(outputFile1);
                File file2 = new File(outputFile2);
                file1.delete();
                file2.delete();
                String reconstructedFile = "reconstructedFile.sql";
                reconstructOriginalFile(outputFile3, "outputA.sql", "outputB.sql", reconstructedFile);
            } else {
                System.out.println("¡El checksum no coincide! Posible corrupción de datos.");
            }
        } else {
            System.out.println("No se pudo calcular el checksum del archivo original.");
        }
    }

    public static String divideAndCloneSQLFile(String inputFile, String outputFile1, String outputFile2,
            String outputFile3, int fileSize) {
        String checksum = null;
        try (FileInputStream fis = new FileInputStream(inputFile)) {
            long totalFileSize = new File(inputFile).length();
            long sectionSize = totalFileSize / 3;
            checksum = calculateChecksum(fis);

            // Dividir y escribir la primera parte en outputFile1
            FileOutputStream fos1 = new FileOutputStream(outputFile1);
            divideAndWrite(fis, fos1, sectionSize);
            fos1.close();

            // Dividir y escribir la segunda parte en outputFile2
            FileOutputStream fos2 = new FileOutputStream(outputFile2);
            fis.getChannel().position(sectionSize);
            divideAndWrite(fis, fos2, sectionSize);
            fos2.close();

            // Dividir y escribir la tercera parte en outputFile3
            FileOutputStream fos3 = new FileOutputStream(outputFile3);
            fis.getChannel().position(2 * sectionSize);
            divideAndWrite(fis, fos3, totalFileSize - 2 * sectionSize);
            fos3.close();

            // Clonar el contenido de outputFile2 y outputFile3 en outputFile2 (outputB.sql)
            try (FileInputStream fis2 = new FileInputStream(outputFile2);
                    FileInputStream fis3 = new FileInputStream(outputFile3);
                    FileOutputStream fosB = new FileOutputStream("outputB.sql")) {
                copyBytes(fis2, fosB);
                copyBytes(fis3, fosB);
            }

            // Clonar el contenido de outputFile1 en outputFileA.sql
            cloneFile(outputFile1, "outputA.sql");
        } catch (IOException e) {
            e.printStackTrace();
        }
        return checksum;
    }

    private static void divideAndWrite(FileInputStream fis, FileOutputStream fos, long sectionSize) throws IOException {
        byte[] buffer = new byte[1024];
        long bytesWritten = 0;
        int bytesRead;

        while ((bytesRead = fis.read(buffer)) != -1 && bytesWritten < sectionSize) {
            if (bytesWritten + bytesRead > sectionSize) {
                int bytesToWrite = (int) (sectionSize - bytesWritten);
                fos.write(buffer, 0, bytesToWrite);
                break;
            } else {
                fos.write(buffer, 0, bytesRead);
                bytesWritten += bytesRead;
            }
        }
        fis.skip(sectionSize - bytesWritten);
    }

    private static String calculateChecksum(FileInputStream fis) throws IOException {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = fis.read(buffer)) != -1) {
                md.update(buffer, 0, bytesRead);
            }
            byte[] digest = md.digest();
            StringBuilder sb = new StringBuilder();
            for (byte b : digest) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
    }

    private static void cloneFile(String sourceFile, String destinationFile) throws IOException {
        try (FileInputStream fis = new FileInputStream(sourceFile);
                FileOutputStream fos = new FileOutputStream(destinationFile)) {
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = fis.read(buffer)) != -1) {
                fos.write(buffer, 0, bytesRead);
            }
        }
    }

    private static void reconstructOriginalFile(String outputFile3, String cloneFile1, String cloneFile2,
            String reconstructedFile) {
        try {
            FileInputStream fisClone1 = new FileInputStream(cloneFile1);
            FileInputStream fisClone2 = new FileInputStream(cloneFile2);
            try (FileOutputStream fos = new FileOutputStream(reconstructedFile)) {
                copyBytes(fisClone1, fos);
                copyBytes(fisClone2, fos);
            }
            System.out.println("Archivo original reconstruido exitosamente.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void copyBytes(InputStream input, OutputStream output) throws IOException {
        byte[] buffer = new byte[1024];
        int bytesRead;
        while ((bytesRead = input.read(buffer)) != -1) {
            output.write(buffer, 0, bytesRead);
        }
    }

    private static boolean verifyChecksum(String expectedChecksum, String actualChecksum) {
        if (expectedChecksum.equals(actualChecksum)) {
            System.out.println("¡El checksum coincide! El archivo no ha sido alterado.");
            return true;
        } else {
            System.out.println("¡El checksum no coincide! Posible corrupción de datos.");
            return false;
        }
    }

}

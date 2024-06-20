package Algoritmo;
import java.io.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class DivisionDeSQL {
    private String originalChecksum;

    public DivisionDeSQL(String inputFile, String outputFile1, String outputFile2, String outputFile3, int fileSize) {
        this.originalChecksum = divideSQLFile(inputFile, outputFile1, outputFile2, outputFile3, fileSize);
    }

    public String getOriginalChecksum() {
        return originalChecksum;
    }

    public static String divideSQLFile(String inputFile, String outputFile1, String outputFile2,
            String outputFile3, int fileSize) {
        String checksum = null;
        try (FileInputStream fis = new FileInputStream(inputFile)) {
            long totalFileSize = new File(inputFile).length();
            long sectionSize = totalFileSize / 3;
            checksum = calculateChecksum(fis);

            // Restablecer la posición del flujo de entrada para dividir y escribir las
            // partes
            fis.getChannel().position(0);

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

            // Clonar el contenido de outputFile1 y outputFile2
            cloneFile(outputFile2, "outputB.sql");
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
}

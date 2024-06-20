package Algoritmo;
import java.io.*;


public class UnionYComprobacion {

    public static void main(String[] args) {
        String outputFile1 = "output1.sql";
        String outputFile2 = "output2.sql";
        String outputFile3 = "output3.sql";
        String reconstructedFile = "reconstructedFile.sql";
        int fileSize = 1024 * 1024; // 1MB
        String inputFile = "C:\\Users\\XxGho\\Documents\\Escuela\\7° Semestre\\Programación General\\databaseBackup.sql";

        DivisionDeSQL division = new DivisionDeSQL(inputFile, outputFile1, outputFile2, outputFile3, fileSize);
        String originalChecksum = division.getOriginalChecksum();
        System.out.println("Checksum calculado para el archivo original: " + originalChecksum);
        if (verifyChecksum(originalChecksum, originalChecksum)) {
            System.out.println("Checksum verificado. Iniciando reconstrucción del archivo original...");
            File file1 = new File(outputFile1);
            File file2 = new File(outputFile2);
            file1.delete();
            file2.delete();
            reconstructOriginalFile(outputFile3, "outputA.sql", "outputB.sql", reconstructedFile);
        } else {
            System.out.println("¡El checksum no coincide! Posible corrupción de datos.");
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

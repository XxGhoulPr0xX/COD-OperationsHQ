import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class InterfazGrafica extends JFrame {

    private JTextField txtCodigo;
    private JTextField txtRecarga;
    private JButton btnRecargar;
    private JTextArea txtResultado;
    //Crea la interfaz
    public InterfazGrafica() {
        setTitle("Recarga de Tarjeta");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        JPanel panelEntrada = new JPanel();
        panelEntrada.setLayout(new GridLayout(3, 2));

        JLabel lblCodigo = new JLabel("Código de Tarjeta:");
        txtCodigo = new JTextField();
        JLabel lblMonto = new JLabel("Monto a Recargar:");
        txtRecarga = new JTextField();
        btnRecargar = new JButton("Recargar");

        panelEntrada.add(lblCodigo);
        panelEntrada.add(txtCodigo);
        panelEntrada.add(lblMonto);
        panelEntrada.add(txtRecarga);
        panelEntrada.add(new JLabel()); // Espacio en blanco
        panelEntrada.add(btnRecargar);

        txtResultado = new JTextArea();
        txtResultado.setEditable(false);

        add(panelEntrada, BorderLayout.NORTH);
        add(txtResultado, BorderLayout.CENTER);

        btnRecargar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String codigo = txtCodigo.getText();
                String recargaText = txtRecarga.getText();
                if (codigo.isEmpty() || recargaText.isEmpty()) {
                    txtResultado.setText("Falta ingresar el código o el monto de recarga.");
                } else {
                    int montoRecarga = Integer.parseInt(recargaText);
                    String nuevoCodigo = Funcionalidad.recargarSaldo(codigo, montoRecarga);
                    txtResultado.setText(nuevoCodigo);
                }
            }
        });
    }
    //Corre la interfaz
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                InterfazGrafica interfaz = new InterfazGrafica();
                interfaz.setVisible(true);
            }
        });
    }
}

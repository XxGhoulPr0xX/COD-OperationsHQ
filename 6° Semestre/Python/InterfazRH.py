import tkinter as tk
from tkinter import *
from tkinter import ttk  # Importa el módulo de estilos
from FuncionalidadRH import Funcionalidad

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Práctica 1° Unidad 2")
        self.ventana.state("zoomed")  # Iniciar maximizada
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.configure(bg="black")

        self.estilo_botones = ttk.Style()
        self.estilo_botones.configure("TButton", padding=6, relief="raised", background="white", foreground="black")
        self.estilo_botones.map("TButton",
                                foreground=[("pressed", "black"), ("active", "black")],
                                background=[("pressed", "!disabled", "black"), ("active", "black")])
        self.estilo_labels = ttk.Style()
        self.estilo_labels.configure("TLabel", background="white")

        self.estilo_entry = ttk.Style()
        self.estilo_entry.configure("TEntry", fieldbackground="gray30", foreground="white")

        self.derecho = tk.Frame(self.ventana, bd=2, relief=tk.RAISED)
        self.derecho.grid(row=0, column=1, rowspan=6, padx=10, pady=10, sticky="nsew")
        self.izquierdo = tk.Frame(self.ventana, bd=2, relief=tk.RAISED)
        self.izquierdo.grid(row=0, column=0, rowspan=6, padx=10, pady=10, sticky="nsw")
        self.izquierdo.configure(bg="blue")


        self.btnEditar = ttk.Button(self.izquierdo, text="Editar Usuario", command=self.Editar)
        self.btnEditar.pack(side="top", pady=5, fill=tk.X)
        self.btnAsignar = ttk.Button(self.izquierdo, text="Asignar Credenciales", command=self.Asignar)
        self.btnAsignar.pack(side="top", pady=5, fill=tk.X)
        self.alpha = Funcionalidad(self)  # Crea una instancia de Funcionalidad

    def Asignar(self):
        self.alpha.limpiarPantalla()
        lblRFCPDF = tk.Label(self.derecho, text="Ingrese RFC del trabajador:")
        lblRFCPDF.grid(row=0, column=0, padx=10, pady=10, sticky="n")
        self.txtPDF = tk.Entry(self.derecho)
        self.txtPDF.grid(row=0, column=1, padx=10, pady=10, sticky="n")
        self.btnPDF = ttk.Button(self.derecho, text="Buscar", command=self.alpha.crearPDF)
        self.btnPDF.grid(row=0, column=2, padx=10, pady=10, sticky="n")

    def Editar(self):
        self.alpha.limpiarPantalla()
        self.btnAlta = ttk.Button(self.derecho, text="Alta", command=self.Alta)
        self.btnAlta.grid(row=0, column=0, padx=10, pady=10)
        self.btnBaja = ttk.Button(self.derecho, text="Baja", command=self.Baja)
        self.btnBaja.grid(row=0, column=1, padx=10, pady=10)

    def Alta(self):
        self.btnAlta["state"] = "disabled"  # Habilitar el botón
        self.btnBaja["state"] = "disabled"  # Habilitar el botón
        self.input_frame = tk.Frame(self.derecho)
        self.input_frame.grid(row=1, column=2, rowspan=7, padx=10, pady=10, sticky="w")
        camera_frame = tk.Frame(self.derecho, borderwidth=2, relief="solid")
        camera_frame.grid(row=4, column=3, padx=10, pady=10, sticky="n")
        camera_frame.configure(bg="white")

        lblNombre1 = tk.Label(self.input_frame, text="Nombre")
        lblNombre1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtPaterno = tk.Entry(self.input_frame)
        self.txtPaterno.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        lblPaterno = tk.Label(self.input_frame, text="Paterno")
        lblPaterno.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.txtMaterno = tk.Entry(self.input_frame)
        self.txtMaterno.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        lblMaterno = tk.Label(self.input_frame, text="Materno")
        lblMaterno.grid(row=2, column=2, padx=10, pady=5, sticky="w")

        self.txtNombre = tk.Entry(self.input_frame)
        self.txtNombre.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        lblNombre2 = tk.Label(self.input_frame, text="Nombre (s)")
        lblNombre2.grid(row=2, column=3, padx=10, pady=5, sticky="w")

        lblCURP = tk.Label(self.input_frame, text="CURP")
        lblCURP.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.txtCURP = tk.Entry(self.input_frame)
        self.txtCURP.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.txtCURP.bind('<KeyRelease>', self.alpha.validarCURP)

        lblRFC = tk.Label(self.input_frame, text="RFC")
        lblRFC.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.txtRFC = tk.Entry(self.input_frame)
        self.txtRFC.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.txtRFC.bind('<KeyRelease>', self.alpha.validarRFC)

        lblDireccion = tk.Label(self.input_frame, text="Dirección")
        lblDireccion.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.txtDireccion = tk.Entry(self.input_frame)
        self.txtDireccion.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        lblClaveWorker = tk.Label(self.input_frame, text="Clave de trabajador")
        lblClaveWorker.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.txtClaveWorker = tk.Entry(self.input_frame)
        self.txtClaveWorker.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        lblNumeroSeguro = tk.Label(self.input_frame, text="Número de seguro")
        lblNumeroSeguro.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.txtNumeroSeguro = tk.Entry(self.input_frame)
        self.txtNumeroSeguro.grid(row=7, column=1, padx=10, pady=5, sticky="w")

        lblArea = tk.Label(self.input_frame, text="Área de trabajo")
        lblArea.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.txtArea = tk.Entry(self.input_frame)
        self.txtArea.grid(row=8, column=1, padx=10, pady=5, sticky="w")

        lblFoto = tk.Label(self.input_frame, text="Foto")
        lblFoto.grid(row=4, column=3, padx=10, pady=5, sticky="w")
        self.btnActivar = ttk.Button(self.input_frame, text="Activar", command=self.alpha.activateImagen)
        self.btnActivar.grid(row=5, column=3, padx=10, pady=5, sticky="w")
        self.btnTomarFoto = ttk.Button(self.input_frame, text="Tomar Foto", command=self.alpha.setImagen)
        self.btnTomarFoto.grid(row=6, column=3, padx=10, pady=5, sticky="w")
        self.btnTomarFoto.config(state=tk.DISABLED)
        self.btnGuardar = ttk.Button(self.input_frame, text="Guardar Empleado", command=self.alpha.guardarEmpleado)
        self.btnGuardar.grid(row=7, column=3, padx=10, pady=5, sticky="w")
        self.btnGuardar.config(state=tk.DISABLED)
        self.lblCamara = Label(camera_frame)
        self.lblCamara.pack()

    def Baja(self):
        self.btnAlta["state"] = "disabled"  # Habilitar el botón
        self.btnBaja["state"] = "disabled"  # Habilitar el botón
        lblSeleccionaClave = tk.Label(self.derecho, text="Dame la RFC para realizar la baja")
        lblSeleccionaClave.grid(row=1, column=2, padx=10, pady=10, sticky="n")
        self.txtBaja = tk.Entry(self.derecho)
        self.txtBaja.grid(row=1, column=3, padx=10, pady=10, sticky="n")
        self.btnBaja = ttk.Button(self.derecho, text="Baja", command=self.alpha.eliminarEmpleado)
        self.btnBaja.grid(row=1, column=4, padx=10, pady=10, sticky="n")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = Interfaz()
    app.run()

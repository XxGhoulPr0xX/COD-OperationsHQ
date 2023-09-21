import tkinter as tk
from tkinter import *
from FuncionalidadRH import Funcionalidad

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Práctica 1° Unidad 2")
        self.ventana.state("zoomed")  # Iniciar maximizada
        self.ventana.geometry("640x480")
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)

        self.derecho = tk.Frame(self.ventana, bd=2, relief=tk.RAISED)
        self.derecho.grid(row=0, column=1, rowspan=6, padx=10, pady=10, sticky="nsew")
        self.izquierdo = tk.Frame(self.ventana, bd=2, relief=tk.RAISED)
        self.izquierdo.grid(row=0, column=0, rowspan=6, padx=10, pady=10, sticky="nsw")

        self.btnEditar = tk.Button(self.izquierdo, text="Editar Usuario", command=self.Editar)
        self.btnEditar.pack(side="top", pady=5)
        self.btnAsignar = tk.Button(self.izquierdo, text="Asignar Credenciales")
        self.btnAsignar.pack(side="top", pady=5)
        self.alpha = Funcionalidad(self)  # Crea una instancia de Funcionalidad

    def Asignar(self):
        print("hola")

    def Editar(self):
        self.btnAlta = tk.Button(self.derecho, text="Alta", command=self.Alta)
        self.btnAlta.grid(row=0, column=0, padx=10, pady=10)
        self.btnBaja = tk.Button(self.derecho, text="Baja")
        self.btnBaja.grid(row=0, column=1, padx=10, pady=10)

    def Alta(self):
        self.input_frame = tk.Frame(self.derecho)
        self.input_frame.grid(row=1, column=0, rowspan=7, padx=10, pady=10, sticky="w")
        camera_frame = tk.Frame(self.derecho, borderwidth=2, relief="solid")
        camera_frame.grid(row=5, column=3, padx=10, pady=10, sticky="n")
        lblNombre1= tk.Label(self.input_frame,text="Nombre")
        lblNombre1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txtPaterno= tk.Entry(self.input_frame)
        self.txtPaterno.grid(row=1,column=1,padx=10,pady=10,sticky="w")
        lblPaterno= tk.Label(self.input_frame,text="Paterno")
        lblPaterno.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.txtMaterno= tk.Entry(self.input_frame)
        self.txtMaterno.grid(row=1,column=2,padx=10,pady=10,sticky="w")
        lblMaterno= tk.Label(self.input_frame,text="Materno")
        lblMaterno.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.txtNombre= tk.Entry(self.input_frame)
        self.txtNombre.grid(row=1,column=3,padx=10,pady=10,sticky="w")
        lblNombre2= tk.Label(self.input_frame,text="Nombre (s)")
        lblNombre2.grid(row=2, column=3, padx=10, pady=10, sticky="w")
        lblRFC= tk.Label(self.input_frame,text="RFC")
        lblRFC.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.txtRFC= tk.Entry(self.input_frame)
        self.txtRFC.grid(row=3,column=1,padx=10,pady=10,sticky="w")
        lblDireccion= tk.Label(self.input_frame,text="Direccion")
        lblDireccion.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.txtDireccion= tk.Entry(self.input_frame)
        self.txtDireccion.grid(row=4,column=1,padx=10,pady=10,sticky="w")
        lblClaveWorker= tk.Label(self.input_frame,text="Clave de trabajador")
        lblClaveWorker.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.txtClaveWorker= tk.Entry(self.input_frame)
        self.txtClaveWorker.grid(row=5,column=1,padx=10,pady=10,sticky="w")
        lblNumeroSeguro= tk.Label(self.input_frame,text="Numero de seguro")
        lblNumeroSeguro.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.txtNumeroSeguro= tk.Entry(self.input_frame)
        self.txtNumeroSeguro.grid(row=6,column=1,padx=10,pady=10,sticky="w")
        lblArea= tk.Label(self.input_frame,text="Area de trabajo")
        lblArea.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.txtArea= tk.Entry(self.input_frame)
        self.txtArea.grid(row=7,column=1,padx=10,pady=10,sticky="w")
        self.btnTomarFoto= tk.Button(self.derecho,text="Tomar Foto", command=self.alpha.setImagen)
        self.btnTomarFoto.grid(row=7,column=3,padx=10,pady=10,sticky="n")
        self.btnTomarFoto.config(state=tk.DISABLED)  # Deshabilitar el botón de tomar foto
        self.btnActivar= tk.Button(self.derecho,text="Activar", command=self.alpha.activateImagen)
        self.btnActivar.grid(row=7,column=2,padx=10,pady=10,sticky="n")
        self.lblCamara = Label(camera_frame)
        self.lblCamara.pack()
        lblFoto= tk.Label(self.derecho,text="Foto")
        lblFoto.grid(row=6, column=3, padx=10, pady=10, sticky="n")
    
    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = Interfaz()
    app.run()

import os
import tkinter as tk
from tkinter import filedialog, IntVar, messagebox
import cv2
import threading
from PIL import Image as PILImage
from PIL import ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image as ReportLabImage, Spacer, Paragraph, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import tempfile

class Funcionalidad:
    def __init__(self, interfaz):
        self.alpha = interfaz
        self.url = 'https://192.168.43.1:8080/shot.jpg'
        self.cap = cv2.VideoCapture(self.url)
        self.numImage = IntVar()
        self.numImage.set(0)
        self.camara_activa = False
        self.cap_visible = False
        self.update_interval = 100
        self.capture_thread = None
        self.capture_active = False
        self.saved_image_path = None
        self.empleados = {}
        self.contraseña = "1234"

    # Activa o desactiva la cámara
    def activateImagen(self):
        self.camara_activa = not self.camara_activa
        if self.camara_activa:
            if not self.cap.isOpened():
                self.capture_thread = threading.Thread(target=self.iniciarCamara)
                self.capture_thread.daemon = True
                self.capture_thread.start()
            else:
                self.capture_active = True
                self.alpha.btnActivar.config(text="Desactivar")
                self.alpha.btnTomarFoto.config(state=tk.NORMAL)
                self.alpha.lblCamara.pack()
        else:
            self.capture_active = False
            self.alpha.btnActivar.config(text="Activar")
            self.alpha.btnTomarFoto.config(state=tk.DISABLED)
            self.alpha.lblCamara.pack_forget()

    # Inicia la captura de video desde la cámara
    def iniciarCamara(self):
        try:
            self.cap.open(self.url)
            while self.camara_activa:
                ret, frame = self.cap.read()
                if ret:
                    if self.capture_active:
                        self.cargarCamaraEnFrame(frame)
                else:
                    self.cap.release()
                    break
        except Exception as e:
            print("Error al iniciar la cámara:", str(e))

    # Carga la imagen de la cámara en un widget
    def cargarCamaraEnFrame(self, frame):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (200, 200))
        img = PILImage.fromarray(img)
        tkimage = ImageTk.PhotoImage(img)
        self.alpha.lblCamara.configure(image=tkimage)
        self.alpha.lblCamara.image = tkimage

    # Establece una imagen capturada como fondo
    def setImagen(self):
        try:
            directorio = filedialog.asksaveasfilename(
                defaultextension=".jpg",
                filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")],
                initialfile=f"image{self.numImage.get()}.jpg",
                title="Guardar Imagen"
            )
            if directorio:
                os.chdir(os.path.dirname(directorio))
                self.cap.open(self.url)
                ret, frame = self.cap.read()
                if ret:
                    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = cv2.resize(img, (200, 200))
                    img = PILImage.fromarray(img)
                    tkimage = ImageTk.PhotoImage(img)
                    self.alpha.lblCamara.configure(image=tkimage)
                    self.alpha.lblCamara.image = tkimage
                    self.saved_image_path = os.path.join(os.getcwd(), os.path.basename(directorio))
                    cv2.imwrite(self.saved_image_path, frame)
                    self.numImage.set(self.numImage.get() + 1)
                    print("Imagen guardada en:", self.saved_image_path)
                    self.verificarDatos()
        except Exception as e:
            print("Error al guardar la imagen:", str(e))

    # Actualiza la imagen de la cámara de forma continua
    def callback(self):
        try:
            self.cap.open(self.url)
            ret, frame = self.cap.read()
            if ret:
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = cv2.resize(img, (200, 200))
                img = PILImage.fromarray(img)
                tkimage = ImageTk.PhotoImage(img)
                self.alpha.lblCamara.configure(image=tkimage)
                self.alpha.lblCamara.image = tkimage
                self.alpha.derecho.after(self.update_interval, self.callback)
            else:
                self.cap.release()
        except Exception as e:
            print("Error al actualizar la imagen de la cámara:", str(e))

    # Guarda los datos del empleado en un diccionario
    def guardarEmpleado(self):
        nombre = self.alpha.txtNombre.get()
        paterno = self.alpha.txtPaterno.get()
        materno = self.alpha.txtMaterno.get()
        curp = self.alpha.txtCURP.get()
        rfc = self.alpha.txtRFC.get()
        direccion = self.alpha.txtDireccion.get()
        clave_worker = self.alpha.txtClaveWorker.get()
        numero_seguro = self.alpha.txtNumeroSeguro.get()
        area = self.alpha.txtArea.get()
        empleado = {
            "Nombre": nombre,
            "Apellido Paterno": paterno,
            "Apellido Materno": materno,
            "CURP": curp,
            "RFC": rfc,
            "Direccion": direccion,
            "Clave del Trabajador": clave_worker,
            "Numero de Seguro": numero_seguro,
            "Area de Trabajo": area,
            "Ubicacion de Foto": f"{self.saved_image_path}"
        }
        self.empleados[rfc] = empleado
        self.alpha.txtNombre.delete(0, tk.END)
        self.alpha.txtPaterno.delete(0, tk.END)
        self.alpha.txtMaterno.delete(0, tk.END)
        self.alpha.txtCURP.delete(0, tk.END)
        self.alpha.txtRFC.delete(0, tk.END)
        self.alpha.txtDireccion.delete(0, tk.END)
        self.alpha.txtClaveWorker.delete(0, tk.END)
        self.alpha.txtNumeroSeguro.delete(0, tk.END)
        self.alpha.txtArea.delete(0, tk.END)
        self.limpiarPantalla()
        self.imprimirEmpleados()

    # Imprime los datos de los empleados en la consola
    def imprimirEmpleados(self):
        for rfc, empleado in self.empleados.items():
            print(f"RFC: {rfc}")
            print(f"CURP: {empleado['CURP']}")
            print(f"Nombre: {empleado['Nombre']}")
            print(f"Apellido Paterno: {empleado['Apellido Paterno']}")
            print(f"Apellido Materno: {empleado['Apellido Materno']}")
            print(f"Dirección: {empleado['Direccion']}")
            print(f"Clave del Trabajador: {empleado['Clave del Trabajador']}")
            print(f"Número de Seguro: {empleado['Numero de Seguro']}")
            print(f"Área de Trabajo: {empleado['Area de Trabajo']}")
            print(f"Ubicación de Foto: {empleado['Ubicacion de Foto']}")
            print("\n")  # Agrega un salto de línea entre cada empleado

    # Verifica si se han ingresado datos y se ha capturado una foto
    def verificarDatos(self):
        nombre = self.alpha.txtNombre.get()
        paterno = self.alpha.txtPaterno.get()
        materno = self.alpha.txtMaterno.get()
        rfc = self.alpha.txtRFC.get()
        curp = self.alpha.txtCURP.get()
        direccion = self.alpha.txtDireccion.get()
        clave_worker = self.alpha.txtClaveWorker.get()
        numero_seguro = self.alpha.txtNumeroSeguro.get()
        area = self.alpha.txtArea.get()
        datos_completos = not (not nombre or not paterno or not materno or not rfc or not direccion or not clave_worker or not numero_seguro or not area or not curp)
        foto_tomada = bool(self.saved_image_path)
        if datos_completos and foto_tomada:
            self.alpha.btnGuardar["state"] = "normal"  # Habilitar el botón
        else:
            self.alpha.btnGuardar["state"] = "disabled"  # Deshabilitar el botón
        return datos_completos and foto_tomada

    # Limpia la pantalla principal
    def limpiarPantalla(self):
        for widget in self.alpha.derecho.winfo_children():
            widget.destroy()

    # Elimina un empleado del diccionario
    def eliminarEmpleado(self):
        rfc_a_eliminar = self.alpha.txtBaja.get()
        if rfc_a_eliminar in self.empleados:
            del self.empleados[rfc_a_eliminar]
            self.alpha.txtBaja.delete(0, tk.END)  # Limpiar el campo de texto txtBaja
            self.imprimirEmpleados()  # Actualizar la lista de empleados en la consola
            self.limpiarPantalla()
            messagebox.showinfo("Éxito", "Usuario eliminado")
        else:
            self.limpiarPantalla()
            messagebox.showerror("Error", "Esta clave no existe")

    # Valida y formatea el RFC ingresado
    def validarRFC(self, event):
        rfc = self.alpha.txtRFC.get()
        if len(rfc) > 12:
            rfc = rfc[:12]
        rfc = rfc.upper()
        self.alpha.txtRFC.delete(0, tk.END)
        self.alpha.txtRFC.insert(0, rfc)

    # Valida y formatea el CURP ingresado
    def validarCURP(self, event):
        curp = self.alpha.txtCURP.get()
        if len(curp) > 18:
            curp = curp[:18]
        curp = curp.upper()
        self.alpha.txtCURP.delete(0, tk.END)
        self.alpha.txtCURP.insert(0, curp)

    # Crea un PDF con los datos de un empleado
    def crearPDF(self):
        rfc = self.alpha.txtPDF.get()
        if rfc in self.empleados:
            empleado = self.empleados[rfc]
            pdf_filename = f"{rfc}.pdf"
            directorio_actual = os.getcwd()
            ruta_pdf = os.path.join(directorio_actual, pdf_filename)
            foto_path = empleado["Ubicacion de Foto"]
            if os.path.exists(foto_path):
                img = PILImage.open(foto_path)
                img = img.resize((300, 300))  
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_img:
                    img.save(temp_img.name, "JPEG")
                doc = SimpleDocTemplate(ruta_pdf, pagesize=letter)
                elementos = []
                estilo_titulo = getSampleStyleSheet()["Title"]
                estilo_titulo.alignment = 1  # 0=Left, 1=Center, 2=Right
                estilo_titulo.textColor = colors.blue
                elementos.append(Paragraph("INGENIERIA DE SOFTWARE 6S1", estilo_titulo))
                elementos.append(Spacer(1, 12))  # Espacio en blanco
                img_path = temp_img.name
                img_with_border = PILImage.new('RGB', (320, 320), 'black')
                img_with_border.paste(img, (10, 10))  # Ajusta el tamaño y la posición del marco
                img_with_border.save(img_path)
                elementos.append(ReportLabImage(img_path, width=300, height=300))
                elementos.append(Spacer(1, 12))  # Espacio en blanco
                estilo_nombre = getSampleStyleSheet()["Normal"]
                estilo_nombre.alignment = 1
                estilo_nombre.textColor = colors.black
                elementos.append(Paragraph("Nombre", estilo_titulo))
                nombre_completo = f"{empleado['Nombre']} {empleado['Apellido Paterno']} {empleado['Apellido Materno']}"
                elementos.append(Paragraph(nombre_completo, estilo_nombre))
                elementos.append(Spacer(1, 12))  # Espacio en blanco
                elementos.append(Paragraph("Area de Trabajo", estilo_titulo))
                elementos.append(Paragraph(empleado["Area de Trabajo"], estilo_nombre))
                elementos.append(Spacer(1, 12))  # Espacio en blanco
                elementos.append(Paragraph("RFC", estilo_titulo))
                elementos.append(Paragraph(empleado["RFC"], estilo_nombre))
                elementos.append(PageBreak())  # Separar en una nueva página
                elementos.append(Paragraph("TECNM", estilo_titulo))
                doc.build(elementos)
                os.system(f"start {ruta_pdf}")
                print(f"El PDF se ha guardado en: {ruta_pdf}")
                self.limpiarPantalla()
            else:
                messagebox.showerror("Error", "La imagen no existe")
        else:
            messagebox.showerror("Error", "Esta clave no existe")
            self.limpiarPantalla()

    #Inicia sesion
    def Login(self):
        if self.alpha.txtUsuario.get() == "isoft" and self.alpha.txtContraseña.get() == self.contraseña:
            self.alpha.btnEditar["state"] = "normal"  # Habilitar el botón
            self.alpha.btnAsignar["state"] = "normal"  # Habilitar el botón
            for widget in self.alpha.derecho.winfo_children():
                widget.destroy()
        else:
            self.lblQP = tk.Label(self.alpha.derecho, text="Usuario o Contraseña Incorrectos")
            self.lblQP.grid(row=8, column=0, padx=200, pady=0, sticky="w")

    #Cambia de contraseña
    def ChangePassword(self):
        self.ventana_cambio = tk.Toplevel()
        self.ventana_cambio.title("Cambiar Contraseña")
        lblContraseñaAnterior = tk.Label(self.ventana_cambio, text="Contraseña Anterior:")
        lblContraseñaAnterior.grid(row=1, column=0, padx=200, pady=20, sticky="w")
        self.txtContraseñaAnterior = tk.Entry(self.ventana_cambio, show="*")
        self.txtContraseñaAnterior.grid(row=2, column=0, padx=200, pady=20, sticky="w")
        lblNuevaContraseña = tk.Label(self.ventana_cambio, text="Nueva Contraseña:")
        lblNuevaContraseña.grid(row=3, column=0, padx=200, pady=20, sticky="w")
        self.txtNuevaContraseña = tk.Entry(self.ventana_cambio, show="*")
        self.txtNuevaContraseña.grid(row=4, column=0, padx=200, pady=20, sticky="w")
        self.btnGuardar = tk.Button(self.ventana_cambio, text="Guardar Cambio", command=self.UpdatePassword)
        self.btnGuardar.grid(row=5, column=0, padx=200, pady=20, sticky="w")
        btnMostrar = tk.Button(self.ventana_cambio, text="Mostrar Contraseña", command=self.ShowPassword1)
        btnMostrar.grid(row=6, column=0, padx=200, pady=20, sticky="w")

    #Actualiza la contraseña
    def UpdatePassword(self):
        if self.contraseña == self.txtContraseñaAnterior.get():
            self.contraseña = self.txtNuevaContraseña.get()
            self.ventana_cambio.destroy()
        else:
            self.lblQP = tk.Label(self.ventana_cambio, text="Contraseña Anterior Incorrecta")
            self.lblQP.grid(row=5, column=0, padx=200, pady=20, sticky="w")

    #Mostra la contraseña
    def ShowPassword(self):
        self.bandera = not self.bandera
        if self.bandera:
            self.alpha.txtContraseña.config(show="")
        else:
            self.alpha.txtContraseña.config(show="*")

    #Muestra la segunda contraseña
    def ShowPassword1(self):
        self.botón_presionado = not self.botón_presionado
        if self.botón_presionado:
            self.txtContraseñaAnterior.config(show="")
            self.txtNuevaContraseña.config(show="")
        else:
            self.txtContraseñaAnterior.config(show="*")
            self.txtNuevaContraseña.config(show="*")

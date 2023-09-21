from tkinter import filedialog, IntVar
import tkinter as tk
from PIL import Image, ImageTk
import os
import cv2

class Funcionalidad:
    def __init__(self, interfaz):
        self.alpha = interfaz
        self.contador = 0
        self.url = 'https://192.168.0.202:8080/shot.jpg'
        self.cap = cv2.VideoCapture(self.url)  # Inicializa la captura de la cámara
        self.numImage = IntVar()
        self.numImage.set(0)
        self.camara_activa = False  # Variable para controlar si la cámara está activa
        self.cap_visible = False  # Variable para controlar si el frame de la cámara es visible o no


    def activateImagen(self):
        self.camara_activa = not self.camara_activa  # Invierte el valor de la cámara
        
        if self.camara_activa:
            if not self.cap.isOpened():  # Verifica si la cámara no está abierta
                self.iniciarCamara()  # Inicializa la cámara
            else:
                self.cargarCamaraEnFrame()  # Carga la cámara en el frame
            self.alpha.btnActivar.config(text="Desactivar")  # Cambiar el texto del botón
            self.alpha.btnTomarFoto.config(state=tk.NORMAL)  # Habilitar el botón de tomar foto
            self.alpha.lblCamara.pack()  # Hacer visible el frame de la cámara
        else:
            if self.cap.isOpened():  # Verifica si la cámara está abierta
                self.cap.release()  # Libera la cámara
            self.alpha.btnActivar.config(text="Activar")  # Cambiar el texto del botón
            self.alpha.btnTomarFoto.config(state=tk.DISABLED)  # Deshabilitar el botón de tomar foto
            self.alpha.lblCamara.pack_forget()  # Ocultar el frame de la cámara


    def iniciarCamara(self):
        self.cap.open(self.url)
        self.callback()

    def cargarCamaraEnFrame(self):
        ret, frame = self.cap.read()
        if ret:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (200, 200))  # Redimensiona la imagen a 200x200
            img = Image.fromarray(img)
            tkimage = ImageTk.PhotoImage(img)
            self.alpha.lblCamara.configure(image=tkimage)
            self.alpha.lblCamara.image = tkimage


    def setImagen(self):
        try:
            directorio = filedialog.asksaveasfilename(
                defaultextension=".jpg",
                filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")],
                initialfile=f"image{self.numImage.get()}.jpg",
                title="Guardar Imagen"  # Cambia el título del cuadro de diálogo
            )
            if directorio:
                os.chdir(os.path.dirname(directorio))  # Cambia al directorio donde se guardará la imagen
                self.cap.open(self.url)
                ret, frame = self.cap.read()
                if ret:
                    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = cv2.resize(img, (200, 200))  # Redimensiona la imagen a 400x400
                    img = Image.fromarray(img)
                    tkimage = ImageTk.PhotoImage(img)
                    self.alpha.lblCamara.configure(image=tkimage)
                    self.alpha.lblCamara.image = tkimage
                    saved_image_path = os.path.join(os.getcwd(), os.path.basename(directorio))
                    cv2.imwrite(saved_image_path, frame)
                    self.numImage.set(self.numImage.get() + 1)
                    print("Imagen guardada en:", saved_image_path)
        except Exception as e:
            print("Error al guardar la imagen:", str(e))

    def callback(self):
        self.cap.open(self.url)
        ret, frame = self.cap.read()
        if ret:
            img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (200, 200)) # Redimensiona la imagen a 400x400
            img=Image.fromarray(img)
            tkimage=ImageTk.PhotoImage(img)
            self.alpha.lblCamara.configure(image=tkimage)
            self.alpha.lblCamara.image = tkimage
            self.alpha.derecho.after(10,self.callback)
        else:
            self.cap.release()
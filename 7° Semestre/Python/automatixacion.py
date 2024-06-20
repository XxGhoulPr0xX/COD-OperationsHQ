from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Configuración de respuestas
respuestas = {
    "pregunta1": random.choice(["Poco", "Media", "Alta"]),
    "pregunta2": random.choice(["Sí", "No"]),
    "pregunta3": random.choice(["Sí", "No"]),
    "pregunta4": random.randint(1, 5),  # Respuesta numérica del 1 al 5
    "pregunta5": random.choice(["Sí", "No"]),
    "pregunta6": random.choice(["Precisión", "Facilidad de uso", "Accesibilidad", "Costo", "Otros"])
}

# Inicializar el navegador
driver = webdriver.Chrome()  # Asegúrate de tener el controlador de Chrome instalado y en el PATH

# Abrir el formulario
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc9Ido6X8pi5I0VKUOpK5S9hCrB9ZSglzU5JY9M3fdqX2NFGg/viewform")

# Esperar un momento para que se cargue el formulario
time.sleep(2)

# Rellenar el formulario con las respuestas
for pregunta, respuesta in respuestas.items():
    input_element = driver.find_element(By.XPATH, f"//div[contains(text(), '{pregunta}')]/../..//div[@role='radio' and contains(text(), '{respuesta}')]")
    input_element.click()
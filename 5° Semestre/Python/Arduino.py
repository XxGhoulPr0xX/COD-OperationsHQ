import serial
import pyautogui

ser = serial.Serial('COM1', 9600)  # Reemplaza 'COM1' por el puerto serial adecuado

while True:
    if ser.in_waiting > 0:
        dato = ser.readline().decode().strip()
        if dato == 'Q':
            pyautogui.press('q')  # Simular la tecla 'q' en el sistema
        elif dato == 'W':
            pyautogui.press('w')  # Simular la tecla 'w' en el sistema
        elif dato == 'E':
            pyautogui.press('e')  # Simular la tecla 'e' en el sistema
        elif dato == 'R':
            pyautogui.press('r')  # Simular la tecla 'r' en el sistema
        elif dato == 'T':
            pyautogui.press('t')  # Simular la tecla 't' en el sistema
        elif dato == 'Y':
            pyautogui.press('y')  # Simular la tecla 'y' en el sistema

import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+525640989191')

sleep(10)

for i in range(1000):
    pyautogui.typewrite('Hola, soy amigo del que le hiciste la broma hace rato, espero que esto tambien te parezca divertido XD')
    pyautogui.press('enter')
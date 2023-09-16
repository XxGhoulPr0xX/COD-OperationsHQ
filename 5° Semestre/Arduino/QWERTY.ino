#include <LiquidCrystal.h>
#include <Keyboard.h>

// Definición de los pines utilizados para los botones
const int pinBtnQ = 2;
const int pinBtnW = 3;
const int pinBtnE = 4;
const int pinBtnR = 5;
const int pinBtnT = 6;
const int pinBtnY = 7;

void setup() {
  // Configurar los pines de los botones como entradas
  pinMode(pinBtnQ, INPUT_PULLUP);
  pinMode(pinBtnW, INPUT_PULLUP);
  pinMode(pinBtnE, INPUT_PULLUP);
  pinMode(pinBtnR, INPUT_PULLUP);
  pinMode(pinBtnT, INPUT_PULLUP);
  pinMode(pinBtnY, INPUT_PULLUP);

  // Iniciar la comunicación con el teclado emulado
  Keyboard.begin();
}

void loop() {
  // Verificar el estado de los botones y enviar la tecla correspondiente
  if (digitalRead(pinBtnQ) == LOW) {
    Keyboard.press('q');
    delay(100);
    Keyboard.release('q');
    delay(100);
  }

  if (digitalRead(pinBtnW) == LOW) {
    Keyboard.press('w');
    delay(100);
    Keyboard.release('w');
    delay(100);
  }

  if (digitalRead(pinBtnE) == LOW) {
    Keyboard.press('e');
    delay(100);
    Keyboard.release('e');
    delay(100);
  }

  if (digitalRead(pinBtnR) == LOW) {
    Keyboard.press('r');
    delay(100);
    Keyboard.release('r');
    delay(100);
  }

  if (digitalRead(pinBtnT) == LOW) {
    Keyboard.press('t');
    delay(100);
    Keyboard.release('t');
    delay(100);
  }

  if (digitalRead(pinBtnY) == LOW) {
    Keyboard.press('y');
    delay(100);
    Keyboard.release('y');
    delay(100);
  }
}

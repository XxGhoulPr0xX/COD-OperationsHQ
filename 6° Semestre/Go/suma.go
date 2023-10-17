package main

import (
	"fmt"
)

func main() {
	var numero1, numero2 int

	fmt.Print("Ingrese el primer número: ")
	_, err := fmt.Scanln(&numero1)
	if err != nil {
		fmt.Println("Error al leer el primer número:", err)
		return
	}

	fmt.Print("Ingrese el segundo número: ")
	_, err = fmt.Scanln(&numero2)
	if err != nil {
		fmt.Println("Error al leer el segundo número:", err)
		return
	}

	suma := numero1 + numero2

	fmt.Printf("La suma de %d y %d es %d\n", numero1, numero2, suma)
}

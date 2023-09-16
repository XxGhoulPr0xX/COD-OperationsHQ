.model small
.stack
.data
cadena1 db "Mendoza Rosas", "$"
cadena2 db "Diego", "$"
salto_linea db 13, 10, "$"  ; Definir la cadena de salto de línea (CR+LF)
.code
main proc
    mov ax, @data
    mov ds, ax

    mov ah, 09    ; función para imprimir cadena
    lea dx, cadena1    ; DX = dirección de cadena1 terminada por $
    int 21h    ; interrupción 21h

    mov ah, 09    ; función para imprimir cadena
    lea dx, salto_linea    ; DX = dirección de salto de línea terminado por $
    int 21h    ; interrupción 21h

    mov ah, 09    ; función para imprimir cadena
    lea dx, cadena2    ; DX = dirección de cadena2 terminada por $
    int 21h    ; interrupción 21h

    mov ah, 4Ch    ; función para terminar programa
    int 21h    ; interrupción 21h
main endp
end main


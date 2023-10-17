.model small; Deficinión del segmento pila
.stack 64; El tamaño opcional especifica el numero de bytes para la pila
.data; contenido datos inicializados 
n1 db 0
n2 db 0 
suma db 0
mensaje1 db "ingresa un número:" ,13,10,'$'
mensaje2 db 13,10,"Ingrese el segundo Valor: ",'$'
resultado db 13,10,"El Resultado es: ",'$'
.code
inicio proc far
    mov ax,@data
    mov ds, ax 
    ;muestra mensaje 1
    mov ah,09
    lea dx,mensaje1
    int 21h
    ;leo numero 1
    mov ah,01
    int 21h
    sub al, 30h
    ;guardado el valor de al a n1
    mov n1,al
    ;muestra mensaje 2
    mov ah,09
    lea dx, mensaje2
    int 21h
    ;leo numero 1
    mov ah, 01
    int 21h
    sub al,30h
    ; guardado el valor de al a n2
    mov n2,al
    mov al, n1 ;paso n1 a al
    add al, n2 ;le sumo n2 al
    add al, 30h ; le sumo 30h a al
    mov suma, al ; guardado el resultado de la suma
    ;muestro mensaje 3
    mov ah,09
    lea dx, resultado
    int 21h
    mov ah,02
    mov dl,suma
    int 21h
    mov ah,4ch ;Devuelve el control al equipo 
    int 21h

inicio endp
end
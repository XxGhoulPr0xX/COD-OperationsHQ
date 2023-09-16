.model small
.stack
.data
cadena db "Hola mundo", "$"
.code
main proc; inicia proceso
mov ax,@data
mov ds,ax
mov ah,09;
lea dx, cadena ; DX=cadena terminada po $
int 21h;termina interrupcion 21h
main endp; termina proceso
end main
.model small
.stack 64
.data
	coordX db ?, '$'
	coordY db ?, '$'
	pazul db '1.Pantalla azul','$'
	pverde db 10,13,7,'2.Pantalla verde ', '$'
	ehola db 10,13,7, '3.Mostrar Hola','$'
	eadios db 10,13,7, '4.Salir del programa ', '$'
	msj db 10,13,7,'Hola$'
	msj2 db 10,13,7,'Adios$'
.code
main proc far
	mov ax,@data
	mov ds,ax
	
   	menu:
		Mov ah,02h	;funcion para posicionar cursor en la pantalla
		Mov dx,0000h	;Cursor renglon y columna 
		Mov bh,00h	;Pagina a imprimir
		int 10h		;Interrupcion

		mov ax,0600h;	funcion para desplazar 
		mov bh,10
		mov cx,0000h
		mov dx,184fh
		int 10h

		mov ah,09h
		lea dx,pazul
		int 21h
	
		lea dx,pverde
		int 21h
		lea dx,ehola
		int 21h
		lea dx, eadios
		int 21h
	click:
		mov ax,01h
		int 33h

		mov ax,03h
		int 33h

		cmp bx,1
		je coordenadas
		cmp bx,2
		jmp click
	
 	coordenadas:
		mov ax, cx
		mov bl,8
		div bl
		mov coordX, al

		mov ax, dx
		mov bl,8
		div bl
		mov coordY, al

		cmp coordx, 0
		JA click

		cmp coordY, 0
		je col_azul
		cmp coordY, 1
		je col_verde
		cmp coordY, 2
		je hello
		cmp coordY, 3
		je salir
		jmp click

	col_azul:
		mov ax,0600h
		mov bh,9fh
		mov cx,0000h
		mov dx,184fh
		int 10h

		mov ah,01h
		int 21h
		jmp menu
	
	col_verde:
		mov ax,0600h
		mov bh,2fh
		mov cx,0000h
		mov dx,184fh
		int 10h

		mov ah,01h
		int 21h
		jmp menu
	hello:
		mov ax,0600h
		mov bh,10
		mov cx,0000h
		mov dx, 184fh
		int 10h
	
		mov ah,09h
		lea dx,msj
		int 21h

		mov ah,01h
		int 21h
		jmp menu

	salir:
		mov ax,0600h
		mov bh,10
		mov cx,184fh
		int 10h
		mov ah,09h
		mov dx, offset msj2
		int 21h
		mov ah,01h
		int 21h
		mov ah,4ch
		int 21h
main endp
end main




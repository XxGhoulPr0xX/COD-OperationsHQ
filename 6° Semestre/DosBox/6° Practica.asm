.model small
.stack 64
.data
msg1 db 10, 13, 'Alvarado Marquez Francisco Javier', 24h
.code
mov ax, @data
mov ds, ax

mov cx, 15
mov si, 0

comienzo:
mov ah, 09
lea dx, msg1
int 21h

mov al, 2
mov bl, 3
sub al, bl

inc si

loopne comienzo

mov ah, 4Ch
int 21h
 end
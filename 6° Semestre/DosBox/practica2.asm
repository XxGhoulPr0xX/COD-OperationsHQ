
.model small
.stack 64
.data
.code
main PROC            ; Punto de entrada principal del programa
mov ax,03h ;limpiar pantalla
int 10h
 
;linea recta
   ;posicionamiento
    mov ah,02h ;servicio
     mov dh,15 ;fila
     mov dl,44 ;columna
     int 10h
                       
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                        
                        ;posicionamiento
                        mov ah,02h ;servicio


                        mov dh,15 ;fila
                        mov dl,43 ;columna
                        int 10h
                       
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,42 ;columna
                        int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       


                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,41 ;columna
                        int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,40 ;columna
                        int 10h
 

mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h                        
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,39 ;columna
                        int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila

                        mov dl,38 ;columna
                        int 10h
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,37 ;columna
                        int 10h
                       
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       

                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,36 ;columna
                        int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,35 ;columna
                        int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       

   mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,34 ;columna
                        int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,33 ;columna
                        int 10h
 

mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,32 ;columna
                        int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio

                        mov dh,15 ;fila
                        mov dl,31 ;columna
                        int 10h
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,30 ;columna
                        int 10h
                       
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
                        mov dx,160 ;x
                        mov ah,02h

                        int 21h
                        
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,29 ;columna
                        int 10h
                       
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
                        mov dx,160 ;x
                        mov ah,02h
                        int 21h
 
;posicionamiento
mov ah,02h ;servicio
mov dh,14 ;fila
mov dl,29 ;columna
int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces

mov ah,09h
int 10h
mov dx,160 ;x
mov ah,02h
int 21h
;posicionamiento
mov ah,02h ;servicio
mov dh,13 ;fila
mov dl,29 ;columna
int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
mov dx,160 ;x
mov ah,02h
int 21h
 
;posicionamiento
mov ah,02h ;servicio
mov dh,12 ;fila
mov dl,29 ;columna
int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
mov dx,160 ;x
mov ah,02h
int 21h
 
;posicionamiento
mov ah,02h ;servicio
mov dh,11 ;fila
mov dl,29 ;columna
int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
mov dx,160 ;x
mov ah,02h
int 21h
 
;posicionamiento
mov ah,02h ;servicio

mov dh,10 ;fila
mov dl,29 ;columna
int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
mov dx,160 ;x
mov ah,02h
int 21h
 
;posicionamiento
mov ah,02h ;servicio
mov dh,09 ;fila
mov dl,29 ;columna
int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
mov dx,160 ;x
mov ah,02h

int 21h
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,15 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx,160 ;x
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,14 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h

int 10h   
    mov dx,160 ;x
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,13 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx,160 ;x
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,12 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx,160 ;x
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,11 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx,160 ;x
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
  
  mov dh,10 ;fila
    mov dl,44 ;columna
    int 10h
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx,160 ;x
    mov ah,02h
    int 21h
  
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,09 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx,160 ;x
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,08 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx,160 ;x
    mov ah,02h
    int 21h
 
 
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,43 ;columna
            int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h

int 10h          
            mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,42 ;columna
            int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,41 ;columna
            int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,40 ;columna
            int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
   
mov dh,08 ;fila
            mov dl,39 ;columna
            int 10h
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,38 ;columna
            int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx,160 ;x
            mov ah,02h
            int 21h
        
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,37 ;columna
            int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,36 ;columna
            int 10h
           
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
           
 mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,35 ;columna
            int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,34 ;columna
            int 10h
 

mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,33 ;columna
            int 10h
           
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
            mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
   
  mov dh,08 ;fila
            mov dl,32 ;columna
            int 10h
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,31 ;columna
            int 10h
           
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h
            mov dx,160 ;x
            mov ah,02h
            int 21h
            
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,30 ;columna
            int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx,160 ;x
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,29 ;columna
            int 10h
 
mov bl,2;num color
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
         
   mov dx,160 ;x
            mov ah,02h
            int 21h
           
 
;posicionamiento
mov ah,02h ;servicio
mov dh,11 ;fila
mov dl,34 ;columna
int 10h
mov dx,65;a
mov ah,02h
int 21h
mov dx,76;l
mov ah,02h
int 21h
mov dx,79;o
mov ah,02h
int 21h
mov dx,78;n
mov ah,02h
int 21h
mov dx,83;s
mov ah,02h

int 21h
mov dx,79;o
mov ah,02h
int 21h
         
                ;posicionamiento
                mov ah,02h ;servicio
                mov dh,09 ;fila
                mov dl,36 ;columna
                int 10h
              
                mov dx,65;a
                mov ah,02h
                int 21h
               
                mov ah,02h ;servicio
                mov dh,10 ;fila
                mov dl,36 ;columna
                int 10h
                mov dx,76;l
                mov ah,02h
                int 21h
               
                mov ah,02h ;servicio
              
mov dh,12 ;fila
                mov dl,36 ;columna
                int 10h
                mov dx,78;n
                mov ah,02h
                int 21h
                mov ah,02h ;servicio
                mov dh,13 ;fila
                mov dl,36 ;columna
                int 10h
                mov dx,83;s
                mov ah,02h
                int 21h
                mov ah,02h ;servicio
                mov dh,14 ;fila
                mov dl,36 ;columna
                int 10h
                mov dx,79;o
                mov ah,02h
                int 21h         

end
main PROC            ; Punto de entrada principal del programa

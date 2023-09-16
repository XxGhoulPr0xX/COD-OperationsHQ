
.model small
.stack 64
.data
.code
mov ax,03h ;limpiar pantalla
int 10h
 
;linea recta
   ;posicionamiento
    mov ah,02h ;servicio
     mov dh,15 ;fila
     mov dl,44 ;columna
     int 10h
                       
mov bl, 04h ; Color de texto rojo
mov cx,02h;cantidad de veces
mov ah,09h
int 10h
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                        
                        ;posicionamiento
                        mov ah,02h ;servicio


                        mov dh,15 ;fila
                        mov dl,43 ;columna
                        int 10h
                       
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,42 ;columna
                        int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       


                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,41 ;columna
                        int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,40 ;columna
                        int 10h
 

mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h                        
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,39 ;columna
                        int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila

                        mov dl,38 ;columna
                        int 10h
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,37 ;columna
                        int 10h
                       
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       

                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,36 ;columna
                        int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,35 ;columna
                        int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       

   mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,34 ;columna
                        int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,33 ;columna
                        int 10h
 

mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,32 ;columna
                        int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio

                        mov dh,15 ;fila
                        mov dl,31 ;columna
                        int 10h
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h                       
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
                       
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,30 ;columna
                        int 10h
                       
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h

                        int 21h
                        
                        ;posicionamiento
                        mov ah,02h ;servicio
                        mov dh,15 ;fila
                        mov dl,29 ;columna
                        int 10h
                       
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
                        mov dx, 54   ; Código ASCII para "6"
                        mov ah,02h
                        int 21h
 
;posicionamiento
mov ah,02h ;servicio
mov dh,14 ;fila
mov dl,29 ;columna
int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces

mov ah,09h
int 10h
mov dx, 54   ; Código ASCII para "6"
mov ah,02h
int 21h
;posicionamiento
mov ah,02h ;servicio
mov dh,13 ;fila
mov dl,29 ;columna
int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
mov dx, 54   ; Código ASCII para "6"
mov ah,02h
int 21h
 
;posicionamiento
mov ah,02h ;servicio
mov dh,12 ;fila
mov dl,29 ;columna
int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
mov dx, 54   ; Código ASCII para "6"
mov ah,02h
int 21h
 
;posicionamiento
mov ah,02h ;servicio
mov dh,11 ;fila
mov dl,29 ;columna
int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
mov dx, 54   ; Código ASCII para "6"
mov ah,02h
int 21h
 
;posicionamiento
mov ah,02h ;servicio

mov dh,10 ;fila
mov dl,29 ;columna
int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
mov dx, 54   ; Código ASCII para "6"
mov ah,02h
int 21h
 
;posicionamiento
mov ah,02h ;servicio
mov dh,09 ;fila
mov dl,29 ;columna
int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
mov dx, 54   ; Código ASCII para "6"
mov ah,02h

int 21h
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,15 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx, 54   ; Código ASCII para "6"
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,14 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h

int 10h   
    mov dx, 54   ; Código ASCII para "6"
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,13 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx, 54   ; Código ASCII para "6"
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,12 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx, 54   ; Código ASCII para "6"
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,11 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx, 54   ; Código ASCII para "6"
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
  
  mov dh,10 ;fila
    mov dl,44 ;columna
    int 10h
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx, 54   ; Código ASCII para "6"
    mov ah,02h
    int 21h
  
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,09 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx, 54   ; Código ASCII para "6"
    mov ah,02h
    int 21h
   
    ;posicionamiento
    mov ah,02h ;servicio
    mov dh,08 ;fila
    mov dl,44 ;columna
    int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h   
    mov dx, 54   ; Código ASCII para "6"
    mov ah,02h
    int 21h
 
 
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,43 ;columna
            int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h

int 10h          
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,42 ;columna
            int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,41 ;columna
            int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,40 ;columna
            int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
   
mov dh,08 ;fila
            mov dl,39 ;columna
            int 10h
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,38 ;columna
            int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
        
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,37 ;columna
            int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,36 ;columna
            int 10h
           
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
           
 mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,35 ;columna
            int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,34 ;columna
            int 10h
 

mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,33 ;columna
            int 10h
           
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
   
  mov dh,08 ;fila
            mov dl,32 ;columna
            int 10h
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,31 ;columna
            int 10h
           
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
            
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,30 ;columna
            int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
            mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
            ;posicionamiento
            mov ah,02h ;servicio
            mov dh,08 ;fila
            mov dl,29 ;columna
            int 10h
 
mov bl, 04h ; Color de texto rojo
mov cx,2;cantidad de veces
mov ah,09h
int 10h           
         
   mov dx, 54   ; Código ASCII para "6"
            mov ah,02h
            int 21h
           
 
;posicionamiento
mov ah,02h ;servicio
mov dh,11 ;fila
mov dl,34 ;columna
int 10h
mov dx, 74   ; Código ASCII para "J"
mov ah,02h
int 21h
mov dx, 65   ; Código ASCII para "A"
mov ah,02h
int 21h
mov dx, 86   ; Código ASCII para "V"
mov ah,02h
int 21h
mov dx, 73   ; Código ASCII para "I"
mov ah,02h
int 21h
mov dx, 69   ; Código ASCII para "E"
mov ah,02h

int 21h
mov dx, 82   ; Código ASCII para "R"
mov ah,02h
int 21h
         
                ;posicionamiento
                mov ah,02h ;servicio
                mov dh,09 ;fila
                mov dl,36 ;columna
                int 10h
              
                mov dx, 74   ; Código ASCII para "J"
                mov ah,02h
                int 21h
               
                mov ah,02h ;servicio
                mov dh,10 ;fila
                mov dl,36 ;columna
                int 10h
                mov dx, 65   ; Código ASCII para "A"
                mov ah,02h
                int 21h
               
                mov ah,02h ;servicio
              
mov dh,12 ;fila
                mov dl,36 ;columna
                int 10h
                mov dx, 73   ; Código ASCII para "I"
                mov ah,02h
                int 21h
                mov ah,02h ;servicio
                mov dh,13 ;fila
                mov dl,36 ;columna
                int 10h
                mov dx, 69   ; Código ASCII para "E"
                mov ah,02h
                int 21h
                mov ah,02h ;servicio
                mov dh,14 ;fila
                mov dl,36 ;columna
                int 10h
                mov dx, 82   ; Código ASCII para "R"
                mov ah,02h
                int 21h         
.exit
end
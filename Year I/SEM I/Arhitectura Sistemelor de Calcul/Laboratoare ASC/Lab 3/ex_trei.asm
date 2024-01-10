bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dw 6
    c dw 3
    b db 3
    d dd 6
    x dq 3
; (a*a+b/c-1)/(b+c)+d-x; a-word; b-byte; c-word; d-doubleword; x-qword rezultatul : 0
segment code use32 class=code
    start:
        ; fara semn:
       
        ; (a*a+b/c-1)
        
        ; a * a
        mov ax, [a]
        mul word[a] ; DX:AX -> rez
        
        push dx
        push ax
        pop ebx ; rez in ebx
       
       ; b / c 
       
        mov eax, 0
        mov al, [b]  ; DX:AX/c
        mov dx, 0
        div word[c] ; DX:AX - > rez
       
       
        mov dx, 0 ; partea intreaga
        push dx
        push ax
        pop ecx ; rez in ecx
       
        mov eax, 0
        mov edx, 0 ; reset si la edx
        add eax, ebx ; in eax a * a
        add eax, ecx ; in eax -> a*a + b/c 
        sub eax, 1 ; in eax -> eax - 1
        
        ; (b + c)
        mov ebx, 0
        mov bl, [b]
        add bx, [c]

        ; (a * a + b/c - 1) / (b + c)

        div bx ; -> DX:AX rez
        
        push dx
        push ax
        pop eax ; pun in eax DX:AX
        
        
        ; + d
        add eax, [d]

        
        mov edx, 0 ; catre qword
        sub eax, [x] ; scaderea qword x
        sbb edx, [x + 4]
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

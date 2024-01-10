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
    a db 2
    b dw 3
    c dd 4
    d dq 5 
    ;(c-b+a)-(d+a) = 4 - 3 + 2 = 3 - 7 = -4
; our code starts here
segment code use32 class=code
    start:
        ; ...
       
        mov ecx, [c]
        mov ax, [b]
        mov dx, 0 
        push dx
        push ax
        pop eax 
        sbb eax, ecx
        mov bl, [a]
        mov bh, 0
        mov cx, 0
        push cx
        push bx
        pop ebx
        adc eax, ebx 
        mov edx, 0   
        mov bl, [a]
        mov bh, 0
        mov cx, 0
        push cx
        push bx
        pop ebx
        mov ecx, 0
        add ebx, [d]
        sub eax,ebx
        sbb edx,ecx
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

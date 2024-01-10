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
    b db 1 ; byte
    a dw 1
    c dw 1 ; word
    d dd 1
    x dq 1
; (a*a+b/c-1)/(b+c)+d-x => 0
                           ; a-word; b-byte; c-word; d-doubleword; x-qword 
; cu semn
segment code use32 class=code
    start:
        ; ...
        ; cu semn
        mov ax, [a]
        imul word[a]
        mov bx, ax
        mov cx, dx
        mov al, [b]
        cbw
        cwde
        idiv word[c]
        add ax, bx
        adc dx, cx
        
        push ax
        push dx
        pop ebx
        
        mov al, [b]
        cbw
        add ax, [c]
        mov cx, ax
        mov eax, ebx
        idiv cx
        push dx
        push ax
        pop eax
        
        add eax, [d]
        cdq
        sub eax, [x]
        sbb edx, [x + 4]
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

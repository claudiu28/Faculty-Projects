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
; (c-d-a)+(b+b)-(c+a) = (4 - 5 - 2) + (3 + 3) - (4 + 2) = -3 + 6 - 6 = -3
segment code use32 class=code
    start:
       
       
        mov bx, [b]
        add bx, [b]
      
       
        mov al, [a]
        cbw
        cwde
        add eax, [c]
        
        sub ebx, eax
        push ebx
        
        mov eax, [c]
        cdq
        sub eax, [d]
        sbb edx, [d + 4]
        mov ecx, edx
        mov ebx, eax
        
        mov al, [a]
        cbw
        cwde
        cdq
        sub ebx, eax
        sbb ecx, edx
        
        pop eax
        cdq
        
        add eax, ebx
        adc edx, ecx
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

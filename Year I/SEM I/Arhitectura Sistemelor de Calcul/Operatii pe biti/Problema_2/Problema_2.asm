;2. Se dau cuvintele A si B. Se cere dublucuvantul C:
;     bitii 0-3 ai lui C coincid cu bitii 5-8 ai lui B
;     bitii 4-8 ai lui C coincid cu bitii 0-4 ai lui A
;     bitii 9-15 ai lui C coincid cu bitii 6-12 ai lui A
;     bitii 16-31 ai lui C coincid cu bitii lui B

bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class = data
    A dw 00__FFh    ; 0000__0000__1111__1111
    B dw 0FF__00h   ; 1111__1111__0000__0000
    C resd 1        ; 1111__1111__0000__0000__0000__0111__1111__1000 
    
segment code use32 class = code
    start:
        xor ebx, ebx
        
        mov ax, [B]
        
        and ax, 0000__0001__1110__0000b
        ror ax, 5
        
        or bx, ax
        
        mov ax, [A]
        
        and ax, 0000__0000__0001_1111b 
        rol ax, 4
        
        or bx, ax
        
        mov ax, [A]
        and ax, 0001__1111__1100__0000b
        rol ax, 3
        
        or bx, ax
        
        mov dx, bx
        mov bx, [B]
        rol ebx, 16
        mov bx, dx
        
        mov [C], ebx
        
        push dword 0
        call exit
        
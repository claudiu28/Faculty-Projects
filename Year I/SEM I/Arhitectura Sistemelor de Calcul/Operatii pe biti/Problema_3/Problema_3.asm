; 3. Se dau cuvintele A si B. Sa se obtina dublucuvantul C:
    ; bitii 0-2 ai lui C coincid cu bitii 12-14 ai lui A
    ; bitii 3-8 ai lui C coincid cu bitii 0-5 ai lui B
    ; bitii 9-15 ai lui C coincid cu bitii 3-9 ai lui A
    ; bitii 16-31 ai lui C coincid cu bitii lui A
    
bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class = data
    a dw 00_FFh ; 0000__0000__1111__1111b
    b dw 0F_F0h ; 0000__1111__1111__0000b
    c resd 1    ; 0000__0000__1111__1111__0011__1111__1000__0000b 
segment code use32 class = code
    start:
        xor ebx, ebx
        
        
        mov ax, [a]
        and ax, 0111__0000__0000__0000b
        ror ax, 12
        or bx, ax
        
        mov ax, [b]
        and ax, 0000__0000__0011__1111b
        rol ax, 3
        or bx,ax
        
        mov ax, [a]
        
        and ax, 0000__0011__1111__1000b
        rol ax, 6
        or bx, ax
        
        mov dx, bx
        mov bx, [a]
        rol ebx, 16
        
        mov bx, dx
        
        
        push dword 0
        call exit
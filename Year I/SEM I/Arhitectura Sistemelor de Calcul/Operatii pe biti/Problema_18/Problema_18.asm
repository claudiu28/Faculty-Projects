; 18. Se da un cuvant A. Sa se obtina dublucuvantul B astfel:
        ; bitii 0-3 ai lui B sunt 0;
        ; bitii 4-7 ai lui B sunt bitii 8-11 ai lui A
        ; bitii 8-9 si 10-11 ai lui B sunt bitii 0-1 inversati ca valoare ai lui A (deci de 2 ori) ;
        ; bitii 12-15 ai lui B sunt biti de 1
        ; bitii 16-31 ai lui B sunt identici cu bitii 0-15 ai lui B.
        
bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class = data
    A dw 0FF_00h ; 1111__1111__0000__0000
    B resd 1
segment code use32 class = code
    start:
        xor ebx, ebx
        
        mov ax, [A]
        
        and ax, 0000__1111__0000__0000b
        rol ax, 12

        or bx, ax
    
        mov ax, [A]
        
        not al
        and ax, 0000__0000__0000__1111b
        ror ax, 8
        
        or bx, ax
        
        mov ax, 1111__0000__0000__0000b
        or bx, ax
        
        mov dx, bx
        mov bx, [A]
        ror ebx, 16
        mov bx, dx 
    
        push dword 0
        call exit 
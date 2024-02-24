; 23. Se da octetul A si cuvantul B. Sa se formeze dublucuvantul C:
        ; bitii 24-31 ai lui C sunt bitii lui A
        ; bitii 16-23 ai lui C sunt inversul bitilor din octetul cel mai putin semnificativ al lui B
        ; bitii 10-15 ai lui C sunt 1
        ; bitii 2-9 ai lui C sunt bitii din octetul cel mai semnificativ al lui B
        ; bitii 0-1 se completeaza cu valoarea bitului de semn al lui A
        
bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class = data
    a db 0FFh
    b dw 0F0F0h 
    c resd 1    ; 1111__1111__0000__1111__1111__1111__1100__0011
segment code use32 class = code   
    start:
        
        xor ebx, ebx
        
        mov al, [a]
        and al, 0011b
        or bl, al
        
        mov ax, [b]
        
        and ax, 1111__1111__0000__0000b
        rol ax, 10
        or bx, ax
        
        mov ax, 1111__1100__0000__0000b
        or bx, ax
        
        xor eax, eax
        mov al, byte[b]
        
        not al
        and al, 1111__1111b
        ror eax, 8
        
        or ebx, eax
        
        xor eax, eax
        
        mov al, [a]
        and al, 1111__1111b
        ror eax, 8
        
        or ebx, eax
        
        push dword 0
        call exit
         
        
       
        
           
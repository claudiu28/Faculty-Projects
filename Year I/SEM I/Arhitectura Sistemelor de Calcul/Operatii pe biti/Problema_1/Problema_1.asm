; 1. Se dau dublucuvintele A si B. Sa se obtina dublucuvantul C:
;   bitii 0-4 ai lui C coincid cu bitii 11-15 ai lui A
;   bitii 5-11 ai lui C au valoarea 1
;   bitii 12-15 ai lui C coincid cu bitii 8-11 ai lui B
;   bitii 16-31 ai lui C coincid cu bitii lui A

bits 32

global start

extern exit
import exit msvcrt.dll


segment data use32 class = data
    A dd 00__FF__FF__00h    ; 0000__0000__1111__1111__1111__1111__0000__0000    
    B dd 0FF__00__FF__FFh   ; 1111__1111__0000__0000__1111__1111__1111__1111
    C resd 1                ; 0000__0000__1111__1111__1111__1111__1111__1111                                        

segment code use32 class = code

    start:
        xor ebx, ebx
        
        mov eax, [A]
        
        and eax, 0000__0000__0000__0000__1111__1000__0000__0000b
        ror eax, 11
        
        or ebx, eax
        
        mov eax, 0000__0000__0000__0000__0000__1111__1110__0000b
        or ebx, eax
        
        mov eax, [B]
        and eax, 0000__0000__0000__0000__0000__1111__0000__0000b
        rol eax, 4
        
        or ebx, eax
        
        mov eax, [A]        
        and eax, 1111__1111__1111__1111__0000__0000__0000__0000b
        
        or ebx, eax
        
        mov [C], ebx
        
        push dword 0
        call exit
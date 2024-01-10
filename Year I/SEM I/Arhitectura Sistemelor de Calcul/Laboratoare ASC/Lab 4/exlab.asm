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
    r dd 00001111010110101010110010001001b ;
    t dd 00000111000100000101010111100001b ;
    q resd 1 
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        ;Se dau 2 dublucuvinte R si T. Sa se obtina dublucuvantul Q astfel:
        ;   bitii 0-6 din Q coincid cu bitii 10-16 a lui T
        ;   bitii 7-24 din Q concid cu bitii obtinuti 7-24 in urma aplicarii R XOR T.
        ;   bitii 25-31 din Q coincid cu bitii 5-11 a lui R.
         
        mov ebx, 0; rezultatul se va afla in ebx
        
        
        ;   bitii 0-6 din Q coincid cu bitii 10-16 a lui T
        mov eax, [t]
        and eax, 00000000000000011111110000000000b; izolvam 10-16
        mov cl, 10
        ror eax, cl ; rotesc la dreapta 
        or  ebx, eax ; apoi pun rezultat in ebx 
        
        
        ;   bitii 7-24 din Q concid cu bitii obtinuti 7-24 in urma aplicarii R XOR T.
        
        mov edx, [t]
        mov eax, [r]
        xor edx, eax 
        and edx, 00000001111111111111111110000000b
        or  ebx, edx
        
        ; bitii 25-31 din Q coincid cu bitii 5-11 a lui R.
        mov eax, [r]
        and eax, 00000000000000000000111111100000b
        mov cl, 20
        rol eax, cl
        or ebx, eax
        
        mov [q], ebx
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

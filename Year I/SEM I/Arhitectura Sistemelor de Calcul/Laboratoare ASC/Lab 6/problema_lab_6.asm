bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
 
;Se da un sir de dublucuvinte. Sa se obtina sirul format din octetii superiori ai cuvintelor inferioare din elementele sirului de dublucuvinte, ;care sunt multiplii de 10.
;Exemplu:
;Se da sirul de dublucuvinte:
;s DD 12345678h, 1A2B3C4Dh, FE98DC76h 
;Sa se obtina sirul
;d DB 3Ch, DCh.

segment data use32 class=data
    ; ...
    s dd 12345678h, 1A2B3C4Dh, 0FE98DC76h
    lg equ ($ - s) / 4
    d times lg db 0
; our code starts here
segment code use32 class=code
    start:
        ; // varianta_a
        mov ecx, lg ;lungime sir in ECX
        jecxz Sfarsit  ; daca ecx este 0    
        
        mov esi, s ; la adresa primului sir, s
        mov edi, d ; la adresa celui de al doilea sir, d
        
        cld ; DF = 0 
        repeta:
            lodsd ; EAX dublucuvint
            mov bl, 0 ; rezultat obtinut
            mov bl, ah ; partea superioara din cuvant
            
            mov al, bl ; pun in partea inferioara pentru al putea imparti
            mov ah, 0 ; pentru a avea loc impartirea ax / 10 = al rest ah
            mov dl, 10
            div dl
            
            test ah,ah ; daca ah != 0 modfica valoare zf
            jne not_multiplu ; neg in caz ca s-a modficat
            
            mov al, bl ; in caz ca nu s-a modficat stochez in al valoarea inferioara initiala
            stosb ; incrementez edi si pun in d
        
        not_multiplu:
            loop repeta ; decrementare ecx
        
    Sfarsit:    ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

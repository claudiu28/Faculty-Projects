bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)

; Enunt problema:
; Se da un sir de octeti S. Sa se determine maximul elementelor de pe pozitiile pare si minimul elementelor de pe pozitiile impare din S.
; Exemplu:
; S: 1, 4, 2, 3, 8, 4, 9, 5
; max_poz_pare: 9
; min_poz_impare: 3

segment data use32 class=data
    s db 1, 4, 2, 3, 8, 4, 9, 5
    lungime equ $ - s ; lungime sir
    maxim db 0
    minim db 255
 
; our code starts here
segment code use32 class=code
    start:
        ; ...
       
        mov ecx, lungime
        jecxz Sfarsit
        mov esi, 0
        
        Repeta:
            mov al, [s + esi] ; s[esi]
            test esi, 01h ; verficare ca esi e par
            jz e_par ; in caz e par
            
            
            mov dl, [minim] ; incarca valoarea minim in dl
            cmp al, dl ; vedem zf && cf
            jae mai_departe ; negam conditie normala (minim < s[i])
            
            
            mov [minim], al ; actualizare minim
            jmp mai_departe ; sari mai departe
        
        e_par:
            
            mov bl, [maxim] ; punem maxim in dl 
            cmp al, bl ; vedem zf && cf
            jbe mai_departe ; (maxim > s[i])
            
            mov [maxim], al ;actualizam maxim
        
        mai_departe:
            inc esi ; incrementare
            loop Repeta
        
        Sfarsit:
            push    dword 0
            call    [exit]
;16. Se da un fisier text. Sa se citeasca continutul fisierului, sa se contorizeze ;      numarul de litere 'y' si 'z' si sa se afiseze aceaste valori. Numele fisierului text ;    este definit in segmentul de date.

bits 32

global start

extern fopen, fread, exit, printf, fclose

import fread msvcrt.dll
import exit msvcrt.dll
import printf msvcrt.dll
import fclose msvcrt.dll
import fopen msvcrt.dll

segment data use32 class = data
    
    mod_access db "r", 0
    nume db "nume.txt", 0
    contor db 0
    lg equ 255
    format_lungime db "%d" , 0
    text times 256 db 0
    descriptor dd -1
    lungime db 0
    contor_y dd 0
    contor_z dd 0
    format_print db "In text 'y' se afla de: %d ori, iar 'z' de: %d ori.", 0

    segment code use32 class = code
    start:
        push dword mod_access
        push dword nume
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        
        cmp eax, 0
        je final
        
        push dword [descriptor]
        push dword lg
        push dword 1
        push dword text
        call [fread]
        add esp, 4 * 4    
        
        mov [lungime], eax     
        
        mov ecx, [lungime]
        xor edx, edx
        xor esi, esi
        xor edi, edi
        cld
        
        bucla:
            mov bl, [text + esi]
            
            cmp ecx, 0
            je afisare
            
            cmp bl, 'z'
            je contor_numar_z
            
            cmp bl, 'y'
            je contor_numar_y
            
            jmp urm_caracter
        contor_numar_z:
            add edx, 1
            jmp urm_caracter
            
            
        contor_numar_y:
            add edi, 1
            jmp urm_caracter
        
        urm_caracter:   
            inc esi 
            dec ecx
            jmp bucla
            
        afisare:
            mov [contor_z], edx
            mov [contor_y], edi
            
            push dword [contor_z]
            push dword [contor_y]
            push dword format_print
            call [printf]
            add esp, 4 * 3
            
            jmp final
        
    final:
        push dword [descriptor]
        call [fclose]
        add esp, 4 * 1
        
        push dword 0
        call [exit]
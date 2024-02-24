;19. Se dau in segmentul de date un nume de fisier si un text (poate contine orice tip de caracter). Sa se calculeze suma cifrelor din text. Sa se creeze un fisier cu numele dat si sa se scrie suma obtinuta in fisier.

bits 32
global start
extern exit,fprintf,fclose,fopen 
import exit msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import fopen msvcrt.dll

segment date use32 class = date 
    text db "Ana are 1# mere, $2 pere si pru3ne.", 0
    descriptor dd -1
    suma dd 0
    nume_fisier db "output.txt", 0
    mod_acces db "w", 0
    format db "Suma este: %d", 0
    

segment code use32 class = code
    start:
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        
        cmp eax, 0
        je final
        
        xor esi, esi
        
        bucla:
            mov bl, [text + esi]
            
            cmp bl, 0
            je afisare
            
            cmp bl, '0'
            jl mai_departe
            
            cmp bl, '9'
            jg mai_departe
            
            sub bl, '0'
            mov dl, bl
            add [suma], dl 
            jmp mai_departe
            
        mai_departe:
            inc esi
            jmp bucla
        afisare:
            push dword [suma]
            push dword format
            push dword [descriptor]
            call [fprintf]
            add esp, 4 * 3
            
            jmp final
        final:
            push dword [descriptor]
            call [fclose]
            add esp, 4 * 1
            
            push dword 0
            call [exit]
        
        
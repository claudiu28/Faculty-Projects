;15. Se dau un nume de fisier si un text (definite in segmentul de date). Textul contine litere mici, litere mari, cifre si caractere ;speciale. Sa se inlocuiasca toate caracterele speciale din textul dat cu caracterul 'X'. Sa se creeze un fisier cu numele dat si sa se ;scrie textul obtinut in fisier.

bits 32

global start

extern exit, fclose, fopen, fprintf, scanf
import exit msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll
import fopen msvcrt.dll
import scanf msvcrt.dll

segment date use32 class = date
    text db "Acesta este un te#xt ce cont$ine car%actere sp<e>ciale. Iata textul: %ana^ &are* (mere! si $pere), #dar@ -si_ +prune~.", 0
    lg equ ($ - text)
    mod_access db 'w', 0
    nume_fisier db "nume.txt", 0
    descriptor dd -1
    caractere_speciale db "~`#!@$%^&*()_-=+?><,./';\|"
    
segment code use32 class = code
    start:
        push dword mod_access
        push dword nume_fisier
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        
        cmp eax, 0
        je final
        
        mov ecx, lg
        xor esi, esi
        
        bucla:
           
            
            mov bl, [text + esi]
            
            xor edi, edi
            
            cmp ecx, 0
            je final
       
            repeta:
                mov dl, [caractere_speciale + edi]
                
                cmp dl, 0
                je actualizare
                
                cmp bl, dl
                jne urm_caracter
                
                mov dl, 'X'
                mov [text + esi], dl
                
            urm_caracter:
                inc edi
                jmp repeta
            actualizare:
                inc esi
                dec ecx
                jmp bucla
        
        
    final:
        push dword text
        push dword [descriptor]
        call [fprintf]
        add esp, 4 * 2
        
        push dword [descriptor]
        call [fclose]
        add esp, 4 * 1
    
        push dword 0
        call exit
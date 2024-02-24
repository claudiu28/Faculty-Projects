;17.Se da un nume de fisier (definit in segmentul de date). Sa se creeze un fisier cu numele dat, apoi sa se citeasca de la tastatura numere si sa se scrie din valorile citite in fisier numerele divizibile cu 7, pana cand se citeste de la tastatura valoarea 0.


bits 32

global start

extern fopen,fclose,exit,fprintf,scanf
import fopen msvcrt.dll
import scanf msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll
import exit msvcrt.dll

segment date use32 class = date

    mod_access db "w", 0
    output db "output.txt", 0
    numar dd 0
    format_numar db "%d", 0
    format db "Numarul este: %d ", 13, 10, 0
    descriptor dd -1
    
segment code use32 class = code

    start:
        push dword mod_access
        push dword output
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        
        cmp eax, 0
        je final
        
        bucla:
            push dword numar
            push dword format_numar
            call [scanf]
            add esp, 4 * 2
            
            xor edx, edx
            mov eax, [numar]
            
            cmp eax, 0
            je final
            
            mov ebx, 7
            
            div ebx
            
            cmp edx, 0
            je divizibile
            
            jmp bucla
            
        divizibile:
            push dword [numar]
            push dword format
            push dword [descriptor]
            call [fprintf]
            add esp, 4 * 3
            
            jmp bucla    
    final:
        push dword [descriptor]
        call [fclose]
        add esp, 4 * 1
        
        push dword 0
        call [exit]
    
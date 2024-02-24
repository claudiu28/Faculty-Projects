;30. Se da un nume de fisier (definit in segmentul de date). Sa se creeze un fisier cu numele dat, apoi sa se citeasca de la tastatura ;cuvinte pana cand se citeste de la tastatura caracterul '$'. Sa se scrie in fisier doar cuvintele care contin cel putin o cifra.

bits 32

global start

extern scanf, exit, fprintf, fclose, fopen
import scanf msvcrt.dll
import exit msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import fopen msvcrt.dll

segment date use32 class = date

    nume_fisier db "text_cifre", 0
    format_fisier db "w", 0
    format_string db "%s", 0
    cuvant times 101 dd 0
    descriptor dd -1
    spatiu db " ", 0
segment code use32 class = code
    start:
        
        push dword format_fisier
        push dword nume_fisier
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        
        cmp eax, 0
        je final_program
        
        bucla:
            push dword cuvant
            push dword format_string
            call [scanf]
            add esp, 4 * 2
            
            xor esi, esi
            xor ebx, ebx
        
            cld
            xor edx, edx
            repeta:
                
                mov bl, [cuvant + esi]
                
                cmp bl, '$'
                je final_program
                
                cmp bl, 0
                je verifica_cifra
                
                
                cmp bl, '0'
                jl continua
                
                cmp bl, '9'
                jg continua
            
                mov edx, 1
                
            verifica_cifra:    
                cmp edx, 1
                jne bucla
           
            afiseaza_cuvant:
                push dword cuvant
                push dword [descriptor]
                call [fprintf]
                add esp, 4 * 2
                
                push dword spatiu
                push dword [descriptor]
                call [fprintf]
                add esp, 4 * 2
            
                jmp bucla
            
            continua:
                
                inc esi
                jmp repeta
                
    
    final_program:
        push dword [descriptor]
        call [fclose]
        add esp, 4
        
        push dword 0
        call exit
        
                
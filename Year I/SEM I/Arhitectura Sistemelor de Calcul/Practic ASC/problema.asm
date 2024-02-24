; Se citeste de la tastatura un numar m si un numar n. Se citesc apoi de la tastatura m numere scrise in zecimal, numere fara semn, pe linii diferite. Sa se scrie in fisierul output.txt doar acele numere care au cel putin n cifre zecimale pare.

; Daca m=4 si n=3
; 132463
; 12345 

; 12121212
; 1234568


; output.txt :   132463   12121212    1234568



bits 32 
global start        


extern exit, fprintf, scanf, fopen, fclose               
import exit msvcrt.dll    
import fopen msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll
segment data use32 class=data
   access db "w", 0
   descriptor dd -1
   nume_fisier db "output.txt", 0
   m resd 1
   n resd 1
   numar resd 1
   format_zecimal db "%d", 0
   contor dd 0
segment code use32 class=code
    start:
        push dword m
        push dword format_zecimal
        call [scanf]
        add esp, 4 * 2
        
        push dword n
        push dword format_zecimal
        call [scanf]
        add esp, 4 * 2
        
        push dword access
        push dword nume_fisier
        call [fopen]
        add esp, 4 * 2
        
        cmp eax, 0
        je final
        
        mov [descriptor], eax
        
        mov ebx, [m]
        
        bucla:
            cmp ebx, 0
            je inchidere_fisier
            
            push dword numar
            push dword format_zecimal
            call [scanf]
            add esp, 4 * 2
            xor edx, edx
            
                
            xor esi, numar
            xor eax, eax
            
            mov eax, [numar]
            repeta:
                xor edx, edx
                cmp eax, 0
                je bucla
                
                
                div dword [10]
                
                cmp edx, 2
                je aduna
                
                cmp edx, 4
                je aduna
                
                cmp edx, 6
                je aduna
                
                cmp edx, 8
                je aduna
                
                cmp edx, 0 
                je aduna
                
                jmp repeta
            aduna:
                mov edi, 1
                add [contor], edi
                mov edi, [contor]
                cmp edi, [n]
           
                jbe afisare
                
                inc esi
                jmp repeta
            afisare:
                push dword [numar]
                push dword [format_zecimal]
                push dword [descriptor]
                add esp, 4 * 3
                
                jmp bucla
            flow:
                dec ebx
                jmp bucla
        
        inchidere_fisier:
            push dword [descriptor]
            call [fclose]
            add esp, 4 * 1
        
        final:
            push dword 0
            call [exit]
        
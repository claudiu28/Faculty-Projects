bits 32
global start

;Se da un nume de fisier (definit in segmentul de date). Sa se creeze un fisier cu numele dat, apoi sa se ;citeasca de la tastatura cuvinte pana cand se citeste de la tastatura caracterul '$'. Sa se scrie in fisier ;doar cuvintele care contin cel putin o litera mare (uppercase).


extern exit, fopen, fclose, fprintf, scanf, printf
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll

section data use32 class=data
    cuvant resb 300
    format_access db "%s", 0
    mod_access db 'a', 0
    descriptor dd -1
    fisier db "output_lab8.txt", 0
    spatiu db " ", 0
section code use32 class=code
    start:
        ; accesare fisier -> deschidere    
        push dword mod_access
        push dword fisier
        call [fopen]
        add esp, 4 * 2
        
        ; verificare descriptor fisier diferit de 0, zf = 0
        mov [descriptor], eax
        cmp eax, 0
        je final 
    
    
        repeta:
            ; citire cuvint
            push dword cuvant
            push dword format_access
            call [scanf]
            add esp, 4 * 2
            
            ; verficare primul caracter e $
            mov al, byte[cuvant]
            cmp al, '$'
            je final
            
            mov esi, cuvant ; punem in esi cuvant 
            xor ecx, ecx ; ecx = 0
            xor edx, edx ; edx = 0
            bucla:
                mov bl, byte[esi + ecx] ; pun in bl caracterul curent 
                
                cmp bl, 0 ; verific daca sunt la final de cuvant
                je litera_mare ; daca e la final 
                    
                cmp bl, 'A' ; verifcam daca e mai mic ca 'A'
                jl mai_departe
                
                cmp bl, 'Z' ; verifcam daca e mai mare ca 'Z'
                jg mai_departe
                
                mov edx, 1   ; daca a ajuns aici insemana ca e litera mare si facem edx = 1
                
            litera_mare:
                cmp edx, 1 
                ; dupa ce am terminat cuvantul daca e zf = 1 afisam daca nu repetam cu alt cuvant
                jne repeta
                
                ; afisare in fisier 
                push dword cuvant
                push dword [descriptor]
                call [fprintf]
                add esp, 4 * 2
                
                push dword spatiu 
                push dword [descriptor]
                call [fprintf]
                add esp, 4 * 2
                
                ; continuam cu urmatorul cuvant
                jmp repeta
                
            mai_departe:
                ; incrementare ecx
                inc ecx
                ; salt la urm caracter
                jmp bucla
       
        final:
            ; inchidere fisier
            push dword [descriptor]
            call [fclose]
            add esp, 4 * 1
            
            ; oprire program
            push dword 0
            call [exit]
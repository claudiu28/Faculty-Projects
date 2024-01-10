bits 32 
global start        

extern exit, printf, scanf              
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll
segment data use32 class=data
    ; valoarea operatiei: (b - a) * k este: 
    a dd 0
    b dd 0
    k dd 3
    message_a db "Valoarea lui a este: ", 0
    message_b db "Valoarea lui b este: ", 0
    format db "%d", 0
    format_base16 db "%llx", 0
    message_rezultat db "Valoarea operatiei (b - a) * k este: ", 0
    rezultat dq 0   
segment code use32 class=code
    start:
        ; ...
        push dword message_a ; mesaj introducere pentru a
        call [printf] ; apelare functie printf
        add esp, 4 * 1 ; golire stiva
        
        push dword a ; citire a
        push dword format ; format baza 10
        call [scanf] ; apelare functie citire
        add esp, 4 * 2 ; golire stiva
        
        push dword message_b ; mesaj introducere pt b
        call [printf] ; apelare functie printf
        add esp, 4 * 1 ; golire stiva
        
        push dword b ; adaugare in stiva b
        push dword format ; format baza 10
        call [scanf] ; apelare functie citire 
        add esp, 4 * 2 ; golire citire

        
        mov eax, [b] ; punem in eax valoarea lui [b]
        sub eax, [a] ; scadem valoarea lui [a]   
        imul dword[k] ; obtinem dupa inmultire rezultat in edx : eax 
            
        ; construire rezultat
        add [rezultat], eax ; adunare in rez eax
        adc [rezultat + 4], edx ; adunare in rez edx 
        
        ; mesaj de rezultat 
        push dword message_rezultat
        call [printf] ; apelare functie de print
        add esp, 4 * 1 ; golire stiva
        
        ;printare qward -> 
        push dword [rezultat + 4]; edx
        push dword [rezultat] ; eax
        push dword format_base16 ; format in baza 16
        call [printf] ; apelare functie printf
        add esp, 4 * 3 ; curatare stiva
               
        push    dword 0     
        call    [exit]       

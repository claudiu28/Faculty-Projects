bits 32

global start

extern scanf, exit, fopen, fclose , fprintf
import scanf msvcrt.dll
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll

extern minim_modul



segment data use32 class=data
    nume_fisier db "min.txt", 0
    mod_acces db 'w', 0
    
    descriptor_fisier dd -1
    format db "%d", 0
    format_hexa db "%x", 0
    
    mesaj_intermediar db ",iar in hexazecimal este:", 0
    numar resd 1 
    global minim
    minim dd 7FFFFFFFh
    
    
    mesaj_minim db "Minim este:", 0  
    

segment code use32 class=code
   
    start:
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor_fisier], eax
        cmp eax, 0
        je final
        
        repeta_citire:
            lea eax, [numar]
            push eax
            push dword format
            call [scanf]
            add esp, 4 * 2
             
            cmp eax, 1
            jne afisare_minim 
            
            
            push dword [numar]
            call minim_modul
            
            
            jmp repeta_citire
        
    afisare_minim:
        push dword mesaj_minim
        push dword [descriptor_fisier]
        call [fprintf]
        add esp, 4 * 2
        
        push dword [minim]
        push dword format
        push dword [descriptor_fisier]
        call [fprintf]
        add esp, 4 * 3
        
        push dword mesaj_intermediar
        push dword [descriptor_fisier]
        call [fprintf]
        add esp, 4 * 2
        
        push dword [minim]
        push dword format_hexa
        push dword [descriptor_fisier]
        call [fprintf]
        add esp, 4 * 3
        
    inchidere_fisier:        
        push dword [descriptor_fisier]
        call [fclose]
        add esp, 4
       
    final: 
        push dword 0
        call [exit]

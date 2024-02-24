bits 32

global start

extern exit, scanf, fprintf, fopen, fclose, printf

import exit msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll

segment data use32 class = data
    n dd 0
    sir times 101 dd 0
    descriptor dd -1
    format db "%d", 0
    format_text_dif db "Diferenta: %x ", 10, 0
    format_text_pare db "Pare: %x ", 10, 0
    format_text_imp db "Impare: %x ", 10, 0
    nume_fisier db "output.txt", 0
    mod_access db "w", 0
    pare dd 0
    impare dd 0
    diferenta dd 0
    
segment code use32 class = code
    start:
        push dword mod_access
        push dword nume_fisier
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        cmp eax, 0
        je final

        push dword n
        push dword format
        call [scanf]
        add esp, 4 * 2
        
        mov ebx, [n]
        xor esi, esi

        bucla:
            cmp ebx, 0
            je rezolvare

            lea eax, [sir + esi * 4]
            push eax
            push format
            call [scanf]
            add esp, 4 * 2

            inc esi
            dec ebx 
            jmp bucla

            
        rezolvare:
            xor esi, esi
            xor edi, edi
            mov ebx, [n]
            
            loop_rezolvare:
                cmp ebx, 0
                je afisare
            
                xor edx, edx
                mov eax, [sir + esi * 4]
                mov edi, eax
                
                mov ecx, 2
                div ecx
                
                cmp edx, 0
                je suma_pare
                             
                add [impare], edi
                jmp flow
                
            suma_pare:
                add [pare], edi
                jmp flow
            
            flow:
                dec ebx
                inc esi
                jmp loop_rezolvare
            
        afisare:
            mov eax, [pare]
            sub eax, [impare]
            mov [diferenta], eax
            
            
            push dword [impare]
         
            push dword format_text_imp
            push dword [descriptor]
            call [fprintf]
            add esp, 4 * 3
            
            push dword [pare]
            push dword format_text_pare
            push dword [descriptor]
            call [fprintf]
            add esp, 4 * 3
            
            push dword [diferenta]
            push dword format_text_dif
            push dword [descriptor]
            call [fprintf]
            add esp, 4 * 3
            
            jmp final
        final:
            push dword [descriptor]
            call [fclose]
            add esp, 4
            
            push dword 0
            call [exit]

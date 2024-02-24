bits 32

global start

extern exit, scanf, printf

import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class = data
    cuvant resb 256  
    numar resd 1     
    format db "%s", 0
    format_intreg db "%d", 0
    cuvant_nou resb 256
segment code use32 class = code 
    start:
        push dword cuvant
        push dword format
        call [scanf]
        add esp, 8

        push dword numar
        push dword format_intreg
        call [scanf]
        add esp, 8

        xor edx, edx
        mov eax, [numar]
        
        div dword[2]
        cmp edx, 0
        je par
        
        xor esi, cuvant
        mov edi, cuvant_nou
        bucla_impar:
            lodsb
            mov dl, al
            cmp al, ' '
            je afisare
            
            xor ah, ah
            
            div byte[20]

            add dl, ah
            mov al, dl
            
            stosb
            jmp bucla_impar
        
        par:
            xor esi, cuvant
            mov edi, cuvant_nou
            numar_par:
                lodsb
                mov dl, al
                cmp al, 'a'
                je numar_par
                cmp al, 'e'
                je numar_par
                cmp al, 'i'
                je numar_par
                cmp al, 'o'
                je numar_par
                cmp al, 'u'
                je numar_par
                
                add 
        
        push dword cuvant
        push dword format
        call [printf]
        add esp, 8

        push dword [numar]
        push dword format_intreg
        call [printf]
        add esp, 8

        push dword 0
        call [exit]

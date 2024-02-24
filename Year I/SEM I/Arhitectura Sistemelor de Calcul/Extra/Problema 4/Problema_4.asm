bits 32

global start

extern scanf, printf, exit, gets

import gets msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll
import exit msvcrt.dll

segment data use32 class = data
    propozitie times 101 db 0
    spatiu db " ", 0
    format_int db "%d", 0
    lungime_cuvant dd 0
segment code use32 class = code
    start:
       
        lea eax, [propozitie]
        push dword eax
        call [gets]
        add esp, 4 * 1

        xor esi, esi
        bucla:
            mov bl, [propozitie + esi]
            
            cmp bl, 0
            je numar_caractere
            
            cmp bl, ' '
            je numar_caractere
            
            mov edx, 1
            add [lungime_cuvant], edx
            jmp flow
            
        numar_caractere:
            mov edx, [lungime_cuvant]
            jmp afisare
        
      
        afisare:
            push dword edx
            push dword format_int
            call [printf]
            add esp, 4 * 2
            
            push dword spatiu
            call [printf]
            add esp, 4 * 1
            
            mov edx, 0
            mov [lungime_cuvant], edx
            jmp flow
            
        flow:
            cmp bl, 0
            je final
            
            inc esi
            jmp bucla
        
        final:
            push dword 0
            call [exit]
bits 32

global start

extern scanf, printf, exit, gets

import gets msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll
import exit msvcrt.dll

segment data use32 class = data
    propozitie times 101 db 0
    format db "%d", 0
    invers_propozitie times 101 db 0

segment code use32 class = code
start:
    lea eax, [propozitie]
    push dword eax
    call [gets]
    add esp, 4

    xor esi, esi  
    xor eax, eax 

    bucla:
        mov bl, [propozitie + esi]
        
        cmp bl, ' '
        je invers
        
        cmp bl, 0
        je invers
        
        jmp flow

    invers:
        xor edi,edi
        mov edi, esi  
        inversare:
            
            cmp esi, 0
            je modificare
            
            dec esi
            
            mov dl, [propozitie + esi]
            mov [invers_propozitie + eax], dl
            inc eax
            
            cmp dl, ' '
            je modificare
            jmp inversare

        modificare:
            mov dl, ' '
            mov [invers_propozitie + eax], dl
            inc eax

            mov esi, edi  
            
            jmp flow

        flow:
            cmp bl, 0
            je afisare
     
            inc esi       
            jmp bucla
            
         
            
    afisare:
        lea eax, [invers_propozitie]
        push dword eax
        call [printf]
        add esp, 4
        jmp final

    final:
        push dword 0
        call [exit]
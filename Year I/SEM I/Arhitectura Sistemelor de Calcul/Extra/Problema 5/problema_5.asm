bits 32

global start
extern printf, scanf, exit, gets

import printf msvcrt.dll
import scanf msvcrt.dll
import exit msvcrt.dll
import gets msvcrt.dll

segment data use32 class = data

    text times 200 db 0
    sir_litere_mici times 200 db 0
    sir_litere_mari times 200 db 0
    format db "%s", 10, 0
    
segment code use32 class = code

    start:
        
        push dword text
        call [gets]
        add esp, 4 * 1
        
        xor esi, esi
        xor edi, edi
        rezolva:
            mov bl, [text + esi]
            
            cmp bl, 0
            je litere_mici
            
            cmp bl, 'A'
            jl mai_departe
            
            cmp bl, 'Z'
            jg mai_departe
            
            mov [sir_litere_mari + edi], bl
            inc edi
            jmp mai_departe
            
        mai_departe:
            inc esi
            jmp rezolva
        litere_mici:
            xor edi, edi
            xor esi, esi
            bucla:
                mov bl, [text + esi]
            
                cmp bl, 0
                je afiseaza
                
                cmp bl, 'a'
                jl continua
                
                cmp bl, 'z'
                jg continua
                
                mov [sir_litere_mici + edi], bl
                inc edi
                jmp continua
            continua:
                inc esi
                jmp bucla
                
        afiseaza:
            push dword sir_litere_mari
            push dword format
            call [printf]
            add esp, 4 * 2
            
            push dword sir_litere_mici
            push dword format
            call [printf]
            add esp, 4 * 2
            
            jmp final
        final:
            push dword 0
            call [exit]
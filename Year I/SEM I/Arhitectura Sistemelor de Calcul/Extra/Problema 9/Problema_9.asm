bits 32
global start
extern exit, fopen, fclose, fread, fprintf

import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll
import fprintf msvcrt.dll


segment data use32 class = data
    lg equ 101
    text times (lg + 1) db 0 
    mod_access db "r", 0
    mod_access_write db "w", 0
    descriptor_r dd -1
    descriptor_w dd -1
    output db "output.txt", 0
    input db "input.txt", 0
    format db "%d", 0
    format_s db "%c", 0
segment code use32 class = code

    start:
        push dword mod_access
        push dword input
        call [fopen]
        add esp, 4 * 2
        mov [descriptor_r], eax
        
        cmp eax, 0
        je final
        
        push dword mod_access_write
        push dword output
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor_w], eax
        
        cmp eax, 0
        je final
        
        push dword [descriptor_r]
        push dword lg
        push dword 1
        push dword text
        call [fread]
        add esp, 4 * 4
        xor esi,esi
        bucla:
            mov bl, [text + esi]
            
            cmp bl, 0
            je final
            
            cmp bl, 'a'
            jl mai_departe
            
            cmp bl, 'z'
            jg mai_departe
            
            movsx eax, byte[text + esi]
            push dword eax
            push dword format
            push dword [descriptor_w]
            call [fprintf]
            add esp, 4 * 3
            
            inc esi
            jmp bucla
        mai_departe:
            push dword [text + esi]
            push dword format_s
            push dword [descriptor_w]
            call [fprintf]
            add esp, 4 * 2
        
            inc esi
            jmp bucla
        final:
            push dword [descriptor_r]
            call [fclose]
            add esp, 4
            
            push dword [descriptor_w]
            call [fclose]
            add esp, 4
            
            push dword 0
            call [exit]
        
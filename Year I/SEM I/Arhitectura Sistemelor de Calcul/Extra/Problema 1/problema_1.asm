bits 32
global start        

extern exit, fopen, fclose, printf, fscanf               
import exit msvcrt.dll
import fscanf msvcrt.dll
import fclose msvcrt.dll
import fopen msvcrt.dll
import printf msvcrt.dll    

segment data use32 class=data
   nume db "input.txt", 0
   descriptor dd -1
   access db "r", 0
   caractere resb 1
   format db "%c", 0
   minim dd 100
   format_intreg db "%d ", 0
segment code use32 class=code
    start:
        push dword access
        push dword nume
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        
        cmp eax, 0
        je final
        
        bucla:
            
            push dword caractere
            push dword format
            push dword [descriptor]
            call [fscanf]
            add esp, 4 * 3
            
            cmp eax, -1
            je ultimul_element
            
            mov bl, [caractere]
            
            cmp bl, ' '
            je afisare_minim_curent
            
            cmp bl, '0'
            jl bucla
            
            cmp bl, '9'
            jg litera
            
            sub bl, '0'
            
            movzx ebx, bl
            
            cmp ebx, [minim]
            jge bucla
            
            mov [minim], ebx
            jmp bucla
            
    litera:
        cmp bl, 'A'
        jl bucla
        
        cmp bl, 'F'
        jg bucla
        
        sub bl, 'A'
        add bl, 10
        
        movzx ebx, bl
            
        cmp ebx, [minim]
        jge bucla
            
        mov [minim], ebx
        jmp bucla   
        
    
    afisare_minim_curent:
        push dword [minim]
        push dword format_intreg
        call [printf]
        add esp, 4 * 2
        
        mov dword[minim], 100
        jmp bucla
    ultimul_element:
        movzx ebx, byte[caractere]
        
        cmp ebx, 'A'
        jl Este_cifra
        
        cmp ebx, 'F'
        jg print_ultim_minim
        
        sub ebx, 'A'
        add ebx, 10
        
        cmp ebx, [minim]
        jge print_ultim_minim
        
        mov [minim], ebx
        jmp print_ultim_minim
    Este_cifra:
        cmp ebx, '0'
        jl print_ultim_minim
        cmp ebx, '9'
        jg print_ultim_minim
        
        sub ebx, '0'
        
        cmp ebx, [minim]
        jge print_ultim_minim
        mov [minim], ebx
        jmp print_ultim_minim
        
    print_ultim_minim:    
        push dword [minim]
        push dword format_intreg
        call [printf]
        add esp, 4 * 2
        
    final:
        push dword 0
        call [exit]
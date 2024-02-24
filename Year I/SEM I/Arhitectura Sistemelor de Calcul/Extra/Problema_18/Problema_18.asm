; 18. Se da un fisier text care contine litere, spatii si puncte. Sa se citeasca continutul fisierului, sa se determine numarul de cuvinte si sa se afiseze pe ecran aceasta valoare. (Se considera cuvant orice secventa de litere separate prin spatiu sau punct)

bits 32

global start

extern fopen, printf, fclose, fread, exit
import fopen msvcrt.dll
import printf msvcrt.dll 
import fclose msvcrt.dll
import fread msvcrt.dll
import exit msvcrt.dll

segment date use32 class = date
    mod_acces db "r", 0
    output db "output.txt", 0
    descriptor dd -1
    printf_format db "Numarul de cuvinte este: %d", 0
    lg equ 200
    cuv times (lg + 1) db 0 
    contor dd 0
    contor_general dd 0
segment code use32 class = code
    start:
        
        push dword mod_acces
        push dword output
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        
        cmp eax, 0
        je final
        
        push dword [descriptor]
        push dword lg
        push dword 1
        push dword cuv
        call [fread]
        add esp, 4 * 4
        
        mov ecx, eax
        
        xor edi, edi
        xor esi, esi
        xor edx, edx
        xor ebx, ebx 
  
        cmp ecx, 0
        je final
        
        bucla:
            mov bl, [cuv + esi] ; cuv[esi]

            cmp bl, 0
            je non_litera
            
            cmp bl, '.'
            je non_litera
            
            cmp bl, ' '
            je non_litera
            
            jmp litera
        non_litera:
            
            
            cmp dword[contor], 0
            je flow
            
            mov edi, 1
            add [contor_general], edi
            
            mov edx, [contor]
            sub [contor], edx
            
            cmp bl, 0
            je afisare
            
            jmp flow
           
        flow:
            inc esi
            dec ecx
            jmp bucla
                        
        litera:
            mov edi, 1
            add [contor], edi
            jmp flow
        
         
        afisare:
            push dword [contor_general]
            push dword printf_format
            call [printf]
            add esp, 4 * 2
            
            jmp final
    final: 
        push dword [descriptor]
        call [fclose]
        add esp, 4 * 1
        
        push dword 0
        call [exit]
        
        
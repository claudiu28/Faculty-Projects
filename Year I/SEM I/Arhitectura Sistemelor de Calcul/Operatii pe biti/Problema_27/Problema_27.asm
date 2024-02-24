; 27. Se da quadwordul A. Sa se obtina numarul intreg N reprezentat de bitii 35-37 ai lui A. Sa se obtina apoi in B dublucuvantul rezultat prin rotirea spre dreapta a dublucuvantului inferior al lui A cu N pozitii. Sa se obtina octetul C astfel:
    ; bitii 0-3 ai lui C sunt bitii 8-11 ai lui B
    ; bitii 4-7 ai lui C sunt bitii 16-19 ai lui B
    
    
bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class = data
    A dq 00__FF__FF__FF__FF__FF__FF__00h
    N resb 1
    B resd 1
    C resb 1
segment code use32 class = code
    start:
        xor ebx, ebx
        xor ecx, ecx
        
        xor eax, eax
        
        add ebx, [A]
        adc ecx, [A + 4]
      
        shr ecx, 3
        and ecx, 0111b
        mov [N], cl 
        
        
        ror ebx, cl
        mov [B], ebx
        
        
        xor edx, edx
        
        mov eax, ebx
        shr eax, 8        
        and eax, 0000__1111b    
        or edx, eax       
        
        
        mov eax, ebx
        shr eax, 16       
        and eax, 0000__1111b    
        shl eax, 4        
        or edx, eax       
        
        
        mov [C], dl
        
        push dword 0
        call exit
bits 32
global _minim_modul

segment data public data use32
segment code public code use32
    _minim_modul:
        push ebp
        mov ebp, esp

        mov eax, [ebp+8] 
        mov ebx, [ebp+12] 
        cmp eax, ebx
        jle final

        mov eax, ebx

    final:
        pop ebp
        ret
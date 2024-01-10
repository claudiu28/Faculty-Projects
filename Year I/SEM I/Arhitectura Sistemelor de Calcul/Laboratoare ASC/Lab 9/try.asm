bits 32 

segment data use32 public data
    numar_in_hexa resd 1

segment code use32 public code
global to_hexa_num

       to_hexa_num:
        mov ebx, [esp + 4]
        
        cmp ebx, 0
        jns pozitiv

        neg ebx
        
        mov dword[numar_in_hexa], ebx
        
        pozitiv:
            mov dword[numar_in_hexa], ebx
            
        ret 4    
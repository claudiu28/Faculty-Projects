bits 32 

extern minim            
segment code use32 public code
global minim_modul
    
    
    minim_modul:
    
        mov eax, [esp + 4]
        cmp eax, [minim]
        jge gr_equal
            
        mov [minim], eax
        
        gr_equal:
            ret 4

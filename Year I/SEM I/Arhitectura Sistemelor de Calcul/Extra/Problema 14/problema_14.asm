bits 32

global start

extern exit, fclose, fopen, fread, printf
import exit msvcrt.dll
import fread msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll

segment data use32 class=data
    descriptor dd -1
    nume db "input.txt", 0
    access db "r", 0
    spatiu db " ", 0
    format db "%s", 0
    lungime equ 200
    text times (lungime + 1) db 0
    cuvant times (lungime + 1) db 0

segment code use32 class=code
start:
    
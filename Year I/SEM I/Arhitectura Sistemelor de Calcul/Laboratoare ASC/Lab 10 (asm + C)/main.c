#include <stdio.h>
#include <limits.h>

extern int minim_modul(int a, int b);

int main() {
    int num, min = INT_MAX;
    FILE *file;
    char fileName[] = "min.txt";

    file = fopen(fileName, "w");
    if (file == NULL) {
        perror("Nu se poate deschide!!!");
        return 1;
    }

    while (scanf("%d", &num) == 1) {
        min = minim_modul(min, num);
    }

    fprintf(file, "Minimul este:");
    fprintf(file, "%d\n", min);
    fprintf(file, "in hexa: ");
    fprintf(file, "%x\n", min);
    fclose(file);

    return 0;
}
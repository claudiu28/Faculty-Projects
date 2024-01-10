#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

// strcuctura pentru tranzactii, ce contine data(format: zi luna an), suma, tip si descrierea
struct Tranzactii{
    int zi,luna,an;
    float suma;
    char tip[10], descriere[500];
}tranzactii[1000];

// un contor pentru a numara cate tranzactii avem in cont
int numar_tranzactie;

void meniu_optiuni(){
    // optiuni disponibile in aplicatie
    printf("1. Tranzactie noua: adaugare, retragere;\n");
    printf("2. Vizualizare tranzactii;\n");
    printf("3. Sold actual cont;\n");
    printf("4. Vizualizare tranzactii in functie de tip -> adaugare/retragere;\n");
    printf("5. Vizualizare tranzactii in functie de intervalul de timp;\n");
    printf("6. Descarca in fila txt datele despre cont;\n");
    printf("7. Incarca date financiare in cont;\n");
    printf("8. Iesire aplicatie;\n");
}
int optiune_valida(int optiune){
    // validare optiune este corepsunzatoare
    if(optiune >= 1 && optiune <= 8)
        return 1;
    return 0;
}




void adaugare_tranzactie(){
    // daca am depasit numarul de tranzactii
    if(numar_tranzactie >= 1000){
        printf("Nu mai sunt loc de tranzactii, au depasit limita maxima!!!\n");
    }
    struct Tranzactii *t = &tranzactii[numar_tranzactie];
    while (getchar() != '\n'); // golire buffer

    // citire tipul tranzactiei + compararea pentru a verifica daca corespune datelor valide pe care utilizatorul trebuie sa le introduca pentru tip
    printf("Introduceti tipul(adaugare/retragere): ");
    fgets(t->tip,sizeof (t->tip), stdin);
    t->tip[strcspn(t->tip, "\n")] = '\0';
    if(strcmp(t->tip,"adaugare") !=0 && strcmp(t->tip,"retragere") != 0){ printf("Date invalide!\n"); return; }


    // citire suma + verficare daca suma introdusa este negativa iesim din functie
    float suma;
    printf("Introduceti suma dorita: ");
    scanf("%f", &suma);
    if(suma < 0) {printf("Date invalide!!!\n"); return;}
    else t->suma = suma;
    while (getchar() != '\n');


    // citire descriere + verificare in cazul in care descriere nu exista iesim din functie
    printf("Descriere tranzactie: ");
    fgets(t->descriere, sizeof(t->descriere), stdin);
    t->descriere[strcspn(t->descriere, "\n")] = '\0';
    if(strcmp(t->descriere,"") == 0) { printf("Date invalide!\n"); return; }


    // citire data in care a fost facuta tranzactia + verficarea datelor daca e zi daca e luna + considerare an intre [1900,2050]
    int zi,luna,an;
    printf("Introduceti data tranzactiei: ");
    scanf("%d%d%d",&zi,&luna,&an);
    if(zi >= 1 && zi <= 31 && luna >= 1 && luna <= 12 && an >= 1900 && an <= 2050){
        t->zi = zi;
        t->luna = luna;
        t->an = an;
    }else{
        printf("Date invalide!!\n"); return;
    }

    while (getchar() != '\n');
    // aduna, in contorul de tranzactii + afisam ca s-a creat o noua tranzactie
    numar_tranzactie++;
    printf("Adaugare tranzactie cu success!!!\n");
}

void adauga_tranzactie_test(int zi, int luna, int an, float suma, char *tip, char *descriere) {
    // test pentru adugare tranzactie
    if (numar_tranzactie >= 1000) {
        return;
    }

    struct Tranzactii *t = &tranzactii[numar_tranzactie++];
    t->zi = zi;
    t->luna = luna;
    t->an = an;
    t->suma = suma;
    strcpy(t->tip, tip);
    strcpy(t->descriere, descriere);
}


void test_adauga_test(){
    adauga_tranzactie_test(1, 1, 2020, 100, "adaugare", "Depunere banca");
    adauga_tranzactie_test(2, 1, 2020, 50, "retragere", "Retragere banca");

    // Verificăm că numărul de tranzacții s-a incrementat corect
    assert(numar_tranzactie == 2);

    // Verificăm că tipul, suma și descrierea tranzacțiilor au fost adăugate corect
    assert(strcmp(tranzactii[0].tip, "adaugare") == 0);
    assert(tranzactii[0].suma == 100);
    assert(strcmp(tranzactii[0].descriere, "Depunere banca") == 0);

    assert(strcmp(tranzactii[1].tip, "retragere") == 0);
    assert(tranzactii[1].suma == 50);
    assert(strcmp(tranzactii[1].descriere, "Retragere banca") == 0);
}




void vizualizare(){
    // afisarea tuturor tranzactior
    for(int i = 0; i < numar_tranzactie; ++i){
        struct  Tranzactii *t = &tranzactii[i];
        // afisare numar de ordine pentru a stii la ce tranzactie ne aflam
        printf("Tranzactia cu numarul de ordine: %d\n", i + 1);
        printf("Suma este: %f\n", t->suma);
        printf("Data este: %d-%d-%d\n", t->zi,t->luna,t->an);
        printf("Tipul: %s\n", t->tip);
        printf("Descirerea este: %s\n", t->descriere);
    }
}



float sold_cont_adaugare(){
    float suma = 0;
    // in functie de tip cati bani mai avem in cont pe ramura adaugare
    for(int i = 0; i < numar_tranzactie; ++i){
        struct Tranzactii *t = &tranzactii[i];
        if(strcmp(t->tip, "adaugare") == 0){
            suma = suma + t->suma;
        }
    }
    return suma;
}
float sold_cont_stergere(){
    float suma = 0;
    // in functie de tip cati bani mai avem in cont pe ramura retragere
    for(int i = 0; i < numar_tranzactie; ++i){
        struct Tranzactii *t = &tranzactii[i];
        if(strcmp(t->tip,"retragere") == 0){
            suma = suma - t->suma;
        }
    }
    return suma;
}

float sold_cont(){
    float suma = 0;
    // in functie de tip cati bani mai avem in cont
    for(int i = 0; i < numar_tranzactie; ++i){
        struct Tranzactii *t = &tranzactii[i];
        // verificare daca suntem pe ramura de adaugare sau retragere
        if(strcmp(t->tip, "adaugare") == 0){
            suma = suma + t->suma;
        }else if(strcmp(t->tip,"retragere") == 0){
            suma = suma - t->suma;
        }
    }
    return suma;
}

void testeaza_sold(){
    numar_tranzactie = 0; // Resetăm numărul de tranzacții

    adauga_tranzactie_test(1, 1, 2020, 100, "adaugare", "Depunere banca");
    adauga_tranzactie_test(2, 1, 2020, 50, "retragere", "Retragere banca");

    float sold = sold_cont();
    assert(sold == 50.000000);
    float sold_negativ = sold_cont_stergere();
    assert(sold_negativ == -50.000000);
    float sold_pozitiv = sold_cont_adaugare();
    assert(sold_pozitiv ==100.000000);
}




void vizualizare_in_functie_de_tip(char tipul[]){
    // analizam tipul (adaugare/ retragere) si afisam corespunzator in caz ca nu corespunze tipului afisam un mesaj desptre tipul afisat citit gresit
    for(int i = 0; i < numar_tranzactie; i++){
        struct Tranzactii *t = &tranzactii[i];
        if(strcmp(t->tip,tipul) == 0){
            printf("Tipul: %s\n", t->tip);
            printf("Tranzactia cu numarul de ordine: %d\n", i + 1);
            printf("Suma este: %f\n", t->suma);
            printf("Data este: %d-%d-%d\n", t->zi,t->luna,t->an);
            printf("Descirerea este: %s\n", t->descriere);
        }
    }
}

void test_vizualizare_in_functie_de_tip() {
    numar_tranzactie = 0;
    // teste pentru vizualizare in functie de tip
    adauga_tranzactie_test(1, 1, 2020, 100, "adaugare", "Depunere in banca");
    adauga_tranzactie_test(2, 1, 2020, 50, "retragere", "Retragere in banca");
    adauga_tranzactie_test(3, 1, 2020, 200, "adaugare", "Depunere in banca");

    vizualizare_in_functie_de_tip("adaugare");

    assert(tranzactii[0].suma == 100.000000);
    assert(tranzactii[2].suma == 200.000000);

}





void vizualizare_in_interval_de_la_initial_final(int zi_initial, int luna_initial, int an_initial, int zi_final, int luna_final, int an_final){
    // interval de timp (zi,luna,an -> zi1,luna1,an1)
    for(int i = 0; i < numar_tranzactie; i++) {
        struct Tranzactii *t = &tranzactii[i];
        // verifica, daca anul curent se afla in interval dintre cei doi ani principali, in caz afirmativ afisam
        if(t->an > an_initial && t->an < an_final){
            printf("Tipul: %s\n", t->tip);
            printf("Tranzactia cu numarul de ordine: %d\n", i + 1);
            printf("Suma este: %f\n", t->suma);
            printf("Data este: %d-%d-%d\n", t->zi,t->luna,t->an);
            printf("Descirerea este: %s\n", t->descriere);
        }else if(t->an == an_final || t->an == an_initial){ // in cazul in care este egal cu unul dintre anii principali, analizam in functie de luna
            if(t->luna > luna_initial && t->luna < luna_final){
                printf("Tipul: %s\n", t->tip);
                printf("Tranzactia cu numarul de ordine: %d\n", i + 1);
                printf("Suma este: %f\n", t->suma);
                printf("Data este: %d-%d-%d\n", t->zi,t->luna,t->an);
                printf("Descirerea este: %s\n", t->descriere);
            }else if(t->luna == luna_final || t->luna == luna_initial){ // analog si pentru luna si zi
                if(zi_final >= t->zi && t->zi >= zi_initial){
                    printf("Tipul: %s\n", t->tip);
                    printf("Tranzactia cu numarul de ordine: %d\n", i + 1);
                    printf("Suma este: %f\n", t->suma);
                    printf("Data este: %d-%d-%d\n", t->zi,t->luna,t->an);
                    printf("Descirerea este: %s\n", t->descriere);
                }else{
                    // in caz ca nu se afla data in interval
                    printf("Nu se afla in interval!!!\n");
                }
            }
        }
    }
}


void descarca_date(){
    // salvam datele curente pe care le avem deocamdata in structura
    FILE *date = fopen("save_datatransactions.txt", "w"); // fisierul in care se vor afisa si salva datele
    if(date == NULL){
        printf("Eroare de deschidere a filei!!!\n"); // in caz ca nu putem deschide fila
        return;
    }else{
        // afisam datele in fisier
        for(int i = 0; i < numar_tranzactie; i++){
            struct Tranzactii t = tranzactii[i];
            fprintf(date, "%f %d %d %d %s %s\n", t.suma, t.zi, t.luna, t.an, t.descriere, t.tip);
        }
        // inchidem fisierul cu datele adaugate
        fclose(date);
        printf("File transmise cu succes!!!\n");
    }
}

void incarca_date(){
    // citirie date din fisier a datelor si adaugare in structura
    FILE *date = fopen("data_financiare.txt", "r");
    if (date == NULL) {
        printf("Eroare de deschidere a filei!!!\n");
        return;
    }

    // citim datele din fisier si adunam la numarul de tranzactii
    while (fscanf(date, "%d %d %d %499[^\n] %f %9[^\n]", &tranzactii[numar_tranzactie].zi,&tranzactii[numar_tranzactie].luna,&tranzactii[numar_tranzactie].an,tranzactii[numar_tranzactie].descriere,&tranzactii[numar_tranzactie].suma,tranzactii[numar_tranzactie].tip) == 6) {
        numar_tranzactie++;
        if (numar_tranzactie >= 1000) {
            break;
        }
    }
    printf("Dare adaugate cu succez: %d\n");
    fclose(date);
}

void test_descarca() {
    numar_tranzactie = 0; // reset numar tranzatie

    adauga_tranzactie_test(1, 1, 2020, 100, "adaugare", "Depunere banca");
    adauga_tranzactie_test(2, 2, 2020, 50, "retragere", "Retragere banca");
    adauga_tranzactie_test(3, 3, 2020, 200, "adaugare", "Depunere ATM");
    adauga_tranzactie_test(4, 4, 2020, 300, "retragere", "Retragere ATM");

    // descarcam date in fisierul corepsunzator
    descarca_date();
}


void ruleaza_teste(){
    test_adauga_test();
    testeaza_sold();
    test_vizualizare_in_functie_de_tip();
    test_descarca();
}

void meniu(int optiune){
    int meniu = 0;
    ruleaza_teste();
    system("cls");
    numar_tranzactie = 0;
    // cat timp meniu va fii 0
    while(meniu == 0){
        meniu_optiuni(); // afisam optiunile din meniu
        printf("Optiunea dorita este: "); // introducem o optiune noua
        scanf("%d", &optiune);
        if(optiune_valida(optiune) == 1){ // daca se afla printre optiunile valide
            if(optiune == 1){
                // pentru optiunea 1 adaugam in structura o tranzactie
                adaugare_tranzactie();
            }else if(optiune == 2){
                // daca avem macar o tranzactie deja existenta afisam, altfel transmitem utilizatorului ca nu sunt tranzactii de afisat
                if(numar_tranzactie)
                    vizualizare();
                else{printf("Nu sunt tranzactii de afisat!!!\n");}
            }else if(optiune == 3){
                // in cazul in care avem mai multi bani in cont si suma actuala este pozitiva afisam in functie de cat am adugat in cont cat am retras si diferenta dintre acestea doua
                if((float)(sold_cont_adaugare() + sold_cont_stergere()) > 0){
                    if(sold_cont_adaugare() > 0)printf("Sold pozitiv: %f\n",sold_cont_adaugare());
                    if(sold_cont_stergere() < 0)printf("Sold negativ: %f\n",sold_cont_stergere());
                    if(sold_cont() >= 0)
                        printf("Soldul contului balansat este: %f\n", sold_cont());printf("\n");}
                else
                    printf("Nu se poate calcula soldul contului, va rog revizuiti datele!\n");

            }else if(optiune == 4){
                // citim tipul (adaugare/retragere)
                char tipul[10];
                while (getchar() != '\n'); // golire buffer
                printf("Introduceti tipul(adaugare/retragere): ");
                fgets(tipul,sizeof (tipul), stdin);
                tipul[strcspn(tipul, "\n")] = '\0';
                if(strcmp(tipul,"adaugare") !=0 && strcmp(tipul,"retragere") != 0){ printf("Date invalide!");}
                // afisam in functie de tip -> adaugare/retragere
                if(numar_tranzactie != 0){vizualizare_in_functie_de_tip(tipul);}
                else{printf("Nu sunt tranzactii de afisat!!!\n");}

            }else if(optiune == 5){
                // citim intervalul corespunzator (zi, luna, an -> zi1, luna1, an1);
                int zi,luna,an,zi1,luna1,an1;
                printf("Introduceti intervalul in format(zi/luna/an -> zi/luna/an): ");
                scanf("%d %d %d %d %d %d", &zi, &luna, &an, &zi1, &luna1, &an1);
                // afisam in cazul in care se afla in interval alocat altfel trmitem un mesaj corespunzator
                vizualizare_in_interval_de_la_initial_final(zi,luna,an,zi1,luna1,an1);
            }else if(optiune == 6){
                // salvam datele existenta in structura
                descarca_date();
            }else if(optiune == 7){
                // citim datele din fisierul "data_financiare.txt" si le adaugam in structura
                incarca_date();
            }
            else if(optiune == 8){
                // in cazul in care dorim sa oprim aplicatia oprim executia si afisam un mesaj corespunzator
                meniu = 1;
                printf("La revedere!!!\n");
            }
        }else{
            // caz in care nu e valida optiunea
            printf("Optiune invalida!!!\n");
            break;
        }
    }
}

int main(){
    int optiune = 0;
    meniu(optiune);
    return 0;
}
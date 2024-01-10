from module.third_module import adaugare, stergere, tiparire, rapoarte, filtrare

# clasa Commmand este folosita pentru a apela functiile din modulele de adaugare, stergere, tiparire, rapoarte si filtrare


class Command:
    @staticmethod
    def adaugare_cheltuiala(lista_apartamente, numar_apartament, suma, tip_cheltuiala,
                            data_cheltuiala):
        adaugare.Adaugare.adaugare_date_despre_apartamente(lista_apartamente, numar_apartament, suma,
                                                           tip_cheltuiala, data_cheltuiala)

    @staticmethod
    def modificare_cheltuiala(lista_apartamente, numar_app, suma_noua, tip_nou, data_noua):
        adaugare.Adaugare.modificare_date_despre_apartmante(lista_apartamente,
                                                            numar_app, suma_noua, tip_nou, data_noua)

    @staticmethod
    def stergere_ap(lista_apartamente, numar_apartament):
        stergere.Stergere.stergere_apartament(lista_apartamente, numar_apartament)

    @staticmethod
    def stergere_ap_ab(lista_apartamente, numar_apartament_a, numar_apartament_b):
        stergere.Stergere.stergere_apartament_ab(lista_apartamente, numar_apartament_a, numar_apartament_b)

    @staticmethod
    def stergere_ap_tip(lista_apartamente, tip):
        stergere.Stergere.stergere_apartament_tip(lista_apartamente, tip)

    @staticmethod
    def tipar_suma(lista_apartamente, suma):
        return tiparire.Tiparire.tipar_mare_ca_o_suma(lista_apartamente, suma)

    @staticmethod
    def tipar_tip(lista_apartamente, tipul):
        return tiparire.Tiparire.tipar_date_tip(lista_apartamente, tipul)

    @staticmethod
    def tipar_zi_suma(lista_apartamente, ziua_limita, suma):
        return tiparire.Tiparire.tipar_in_functie_de_zi_suma(lista_apartamente, ziua_limita, suma)

    @staticmethod
    def raport_suma_totala(lista_apartamente, tipul):
        return rapoarte.Rapoarte.suma_totala_dupa_tip(lista_apartamente, tipul)

    @staticmethod
    def raport_suma_totala_numar(lista_apartamente, numar_apartament):
        return rapoarte.Rapoarte.suma_in_functie_de_numar(lista_apartamente, numar_apartament)

    @staticmethod
    def raport_sortare_tip(lista_apartamente, tipul):
        return rapoarte.Rapoarte.date_sortate(lista_apartamente, tipul)

    @staticmethod
    def filtrare_tip(lista_apartamente, tipul):
        return filtrare.Filtrare.filtrare_tip(lista_apartamente, tipul)

    @staticmethod
    def filtrare_suma(lista_apartamente, suma):
        return filtrare.Filtrare.filtrare_suma(lista_apartamente, suma)

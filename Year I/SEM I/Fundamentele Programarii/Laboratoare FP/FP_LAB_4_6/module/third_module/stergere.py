# clasa de Stergere apartament, apartament de la (a -> b) si steegere dupa tip
from module.second_module import models


class Stergere:
    @staticmethod
    def stergere_date(lista_apartament, functie, *args):
        lista_noua = []
        for element in lista_apartament:
            if functie(element, *args):
                element.sterg_date()
        return lista_noua

    @staticmethod
    def stergere_date_apartament(element, nr_apart):
        return element.get_numar_apartament() == nr_apart

    @staticmethod
    def stergere_date_ab(element, numar_a, numar_b):
        return numar_a <= element.get_numar_apartament() <= numar_b

    @staticmethod
    def sterge_date_tip(element, tipul):
        return element.get_tip_cheltuiala() == tipul

    @staticmethod
    def stergere_apartament(lista_apartament, nr_ap):
        return Stergere.stergere_date(lista_apartament, Stergere.stergere_date_apartament, nr_ap)

    @staticmethod
    def stergere_apartament_ab(lista_apartament, nr_a, nr_b):
        return Stergere.stergere_date(lista_apartament, Stergere.stergere_date_ab, nr_a, nr_b)

    @staticmethod
    def stergere_apartament_tip(lista_apartamente, tipul):
        return Stergere.stergere_date(lista_apartamente, Stergere.sterge_date_tip, tipul)

# Rapoarte

class Rapoarte:
    # sablon functie raport pentru suma
    @staticmethod
    def rapoarte_date(lista_apartament, functie, *args):
        suma = 0
        for element in lista_apartament:
            if functie(element, *args):
                suma = suma + element.get_suma()
        return suma

    # conditia de apelare a functiei in functie de tip
    @staticmethod
    def suma_totala(element, tip):
        return element.get_tip_cheltuiala() == tip

    # functia de suma in functie de tip
    @staticmethod
    def suma_totala_dupa_tip(lista_apartamente, tipul):
        return Rapoarte.rapoarte_date(lista_apartamente, Rapoarte.suma_totala, tipul)

    # conditia in functie de numar apartament
    @staticmethod
    def suma_numar_apart(element, numar_dat):
        return element.get_numar_apartament() == numar_dat

    # functia de suma numar apartament
    @staticmethod
    def suma_in_functie_de_numar(lista_apartament, numar_dat):
        return Rapoarte.rapoarte_date(lista_apartament, Rapoarte.suma_numar_apart, numar_dat)

    # date sortarte in functie de tip apoi in functie de numar_apartament
    @staticmethod
    def date_sortate(lista_apartament, tipul):
        lista = []
        for element in lista_apartament:
            if element.get_tip_cheltuiala() == tipul:
                lista.append(element.to_dict())
        lista.sort(key=lambda x: x['numar_apartament'])
        return lista

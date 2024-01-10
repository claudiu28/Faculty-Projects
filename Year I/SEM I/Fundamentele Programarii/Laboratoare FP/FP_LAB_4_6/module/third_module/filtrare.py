# Filtrare

# clasa Filtrare este folosita pentru a filtra datele din lista de apartamente
class Filtrare:
    # functia filtrare_date este folosita pentru a filtra datele din lista de apartamente format general ambele functii folosindu-se de acelasi stil de functie
    @staticmethod
    def filtrare_date(lista_apartament, functie, *args):
        lista = []
        for element in lista_apartament:
            if functie(element, *args):
                lista.append({
                    'numar_apartament': element.get_numar_apartament(),
                    'suma': element.get_suma(),
                    'tip_cheltuiala': element.get_tip_cheltuiala(),
                    'data_cheltuiala': element.get_data_cheltuiala()
                })
        return lista

    # functia pentru conditie pe care o apelam in filtrare_date
    @staticmethod
    def cond_filtrare_tip(element, tip):
        return element.get_tip_cheltuiala() == tip

    # functia de filtrare in functie de de tip
    @staticmethod
    def filtrare_tip(lista_apartament, tip):
        return Filtrare.filtrare_date(lista_apartament, Filtrare.cond_filtrare_tip, tip)

    # functia de filtrare in functie de suma
    @staticmethod
    def filtrare_suma(lista_apartament, suma):
        return Filtrare.filtrare_date(lista_apartament, Filtrare.cond_filtrare_suma, suma)

    # functia pentru conditie in functie de suma
    @staticmethod
    def cond_filtrare_suma(element, suma):
        return element.get_suma() < suma

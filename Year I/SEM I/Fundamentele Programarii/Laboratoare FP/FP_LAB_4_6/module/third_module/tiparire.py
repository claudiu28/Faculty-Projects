from module import user_interface


class Tiparire:
    # sablon functie tiparire
    @staticmethod
    def tipar_date(lista_apartament, function, *args):
        lista_noua = []
        for element in lista_apartament:
            if function(element, *args):
                lista_noua.append({'numar_apartament': element.get_numar_apartament(),
                                   'suma': element.get_suma(), 'tip_cheltuiala': element.get_tip_cheltuiala(),
                                   "data_cheltuiala": element.get_data_cheltuiala()})
        return lista_noua

    # conditie tipar in functie de suma
    @staticmethod
    def tipar_suma(element, suma):
        return element.get_suma() > suma

    # functie de suma tipar
    @staticmethod
    def tipar_mare_ca_o_suma(lista_apartament, suma):
        return Tiparire.tipar_date(lista_apartament, Tiparire.tipar_suma, suma)

    # tipar tip conditie funtie
    @staticmethod
    def tipar_tip(element, tip):
        return element.get_tip_cheltuiala() == tip

    # functie de tipar in functie de tip
    @staticmethod
    def tipar_date_tip(lista_apartament, tipul):
        return Tiparire.tipar_date(lista_apartament, Tiparire.tipar_tip, tipul)

    # conditie in functie de zi si suma
    @staticmethod
    def tipar_zi_suma(element, ziua_limita, suma):
        return (user_interface.convert_datetime(element.get_data_cheltuiala())
                < user_interface.convert_datetime(ziua_limita)
                and element.get_suma() > suma)

    # tipar in functie de zi si de suma
    @staticmethod
    def tipar_in_functie_de_zi_suma(lista_apartmaent, ziua_limita, suma_data):
        return Tiparire.tipar_date(lista_apartmaent, Tiparire.tipar_zi_suma, ziua_limita, suma_data)

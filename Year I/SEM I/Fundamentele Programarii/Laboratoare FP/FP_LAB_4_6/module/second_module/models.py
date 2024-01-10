
# clasa Apartament cu metodele get si set pentru a accesa si modifica datele despre apartament
class Apartament:
    def __init__(self, numar_apartament, suma, tip_cheltuiala, data_cheltuiala):
        self.data = {
            'numar_apartament': numar_apartament,
            'suma': suma,
            'tip_cheltuiala': tip_cheltuiala,
            'data_cheltuiala': data_cheltuiala
        }
    # set si get

    def get_numar_apartament(self):
        return self.data['numar_apartament']

    def set_numar_apartament(self, value):
        self.data['numar_apartament'] = value

    def get_suma(self):
        return self.data['suma']

    def set_suma(self, value):
        self.data['suma'] = value

    def get_tip_cheltuiala(self):
        return self.data['tip_cheltuiala']

    def set_tip_cheltuiala(self, value):
        self.data['tip_cheltuiala'] = value

    def get_data_cheltuiala(self):
        return self.data['data_cheltuiala']

    def set_data_cheltuiala(self, value):
        self.data['data_cheltuiala'] = value

    # setare date to None
    def sterg_date(self):
        self.set_suma(None)
        self.set_tip_cheltuiala(None)
        self.set_data_cheltuiala(None)

    def to_dict(self):
        return self.data.copy()

    # copiere entitati Apartament
    def copy(self):
        return Apartament(
            numar_apartament=self.get_numar_apartament(),
            suma=self.get_suma(),
            tip_cheltuiala=self.get_tip_cheltuiala(),
            data_cheltuiala=(self.get_data_cheltuiala()))


class ListaApartamente:
    def __init__(self, lista_apartamente):
        self.lista_apartamente = lista_apartamente

    # functie folosita pentru a vizualiza lista de apartmente
    def lista_apartamente_vizualizare(self):
        return self.lista_apartamente



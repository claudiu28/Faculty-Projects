from module.second_module.models import Apartament


class Undo:
    def __init__(self):
        self.undo_list = []

    # copiere date din Apartament
    @staticmethod
    def copiere(lista_apartamente):
        return [Apartament(apartament.get_numar_apartament(), apartament.get_suma(),
                           apartament.get_tip_cheltuiala(), apartament.get_data_cheltuiala()) for apartament in
                lista_apartamente]

    # inregistrare in undo list
    def registers(self, lista_apartamente):
        self.undo_list.append(self.copiere(lista_apartamente))

    # functie ultima operatie pop()
    def pop_undo(self):
        if self.undo_list:
            return self.undo_list.pop()
        else:
            raise ValueError("Nu se mai poate face undo!!!")

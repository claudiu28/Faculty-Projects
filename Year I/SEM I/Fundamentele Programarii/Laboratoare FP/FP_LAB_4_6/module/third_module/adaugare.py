from module.second_module import models

# class Adaugare este folosita pentru a adauga si a modifica date despre apartamente


class Adaugare:
    @staticmethod
    def adaugare_date_despre_apartamente(lista_apartamente, numar_apartament, suma, tip_cheltuiala,
                                         data_cheltuiala):
        lista_apartamente_secunda = models.Apartament(numar_apartament, suma, tip_cheltuiala, data_cheltuiala)
        lista_apartamente.append(lista_apartamente_secunda)

    @staticmethod
    def modificare_date_despre_apartmante(lista_apartamente, numar_app, suma_noua, tip_nou, data_noua):
        for apartament in lista_apartamente:
            if apartament.get_numar_apartament() == numar_app:
                apartament.set_suma(suma_noua)
                apartament.set_tip_cheltuiala(tip_nou)
                apartament.set_data_cheltuiala(data_noua)

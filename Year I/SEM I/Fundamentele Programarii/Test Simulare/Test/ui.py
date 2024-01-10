class Consola:
    def __init__(self, service):
        self.__service = service

    @staticmethod
    def comanda():
        # optiune tip numeric pentru utilizator
        optiune = int(input("Introduceti optiunea: "))
        return optiune

    def medie_dupa_tip(self):
        # functie pt media preturilor
        try:
            tip = input("Tipul imobilului(vanzarea / inchiriere):")
            medie = self.__service.medie_pe_pret(tip)

            print("Media preturilor este: ", medie)
        except ValueError:
            print("Mai incercati din nou!")

    def tranzactii(self):
        # functie pt tranzactii imobiliare in functie de comision
        try:
            id_imobil = int(input("Introduceti id-ul imobilului: "))
            pret_negocitat = float(input("Introduceti pretul negociat: "))
            comision = self.__service.tranzactii(id_imobil, pret_negocitat)
            print("Comisionul este: ", comision.get_comision(), ",iar adresa este: ", comision.get_imobil().get_adresa())
        except (ValueError, AttributeError):
            print("Mai incercati din nou!")

    def run(self):
        # meniu pt utilizator
        try:
            while True:
                print("1. Media preturilor pentru un tip de imobil")
                print("2. Tranzactii imobiliare")
                print("3. Iesire")
                optiune = self.comanda()
                if optiune == 1:
                    self.medie_dupa_tip()
                elif optiune == 2:
                    self.tranzactii()
                elif optiune == 3:
                    print("Bye")
                    break
                else:
                    print("Optiune invalida")
        except ValueError:
            print("Optiun invalida")

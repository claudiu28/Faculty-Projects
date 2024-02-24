class UI:
    def __init__(self, service):
        self.__service = service

    @staticmethod
    def afisare_meniu():
        print("Meniul de optiuni este:\n"
              "1.Adaugare spectacol\n"
              "2.Modificare spectacol\n"
              "3.Generare obiecte\n"
              "4.Export spectacole\n"
              "0. Exit\n")

    def adaugare_spectacole_ui(self):
        try:
            titlu = input("Introduceti titlul:")
            artist = input("Introduceti artist:")
            gen = input("Introduceti gen:")
            durata = int(input("Introduceti durata:"))
            self.__service.adaugare_spectacol(titlu, artist, gen, durata)
            print("Adaugare spectacol cu succes!")
        except (ValueError, TypeError) as e:
            print(e)

    def modificare_spectacole_ui(self):
        try:
            titlu = input("Introduceti titlul:")
            artist = input("Introduceti artist:")
            gen = input("Introduceti gen:")
            durata = int(input("Introduceti durata:"))
            self.__service.modificare_spectacol(titlu, artist, gen, durata)
            print("Modificare spectacol cu succes!")
        except (ValueError, TypeError) as e:
            print(e)

    def generare_obiecte_ui(self):
        try:
            numar = input("Introduceti cate obiecte sa se introduca random:")
            self.__service.random_generare(numar)
            print("S-au adaugat in fisier random spectacoele!")
        except (ValueError, TypeError, AttributeError) as e:
            print(e)

    def export_date(self):
        try:
            nume_fisier = input("Introduceti numele fiserului:")
            self.__service.export_date(nume_fisier)
            print("S-au adaugat in fisier!")
        except (ValueError, TypeError) as e:
            print(e)

    def meniu(self):
        try:
            while True:
                self.afisare_meniu()
                option = int(input("Introduceti optiunea dorita:"))
                if option == 1:
                    self.adaugare_spectacole_ui()
                elif option == 2:
                    self.modificare_spectacole_ui()
                elif option == 3:
                    self.generare_obiecte_ui()
                elif option == 4:
                    self.export_date()
                elif option == 0:
                    print("Bye")
                    break
                else:
                    print("Optiunea nu este valida!")
        except Exception:
            print("A APARUT O EROARE, REINCERCATI!")
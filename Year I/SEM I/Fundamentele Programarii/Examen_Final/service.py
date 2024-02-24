from domain import Spectacole
from repo import Repository
from validation import Validation
import random

class Service:
    def __init__(self, validation, repository):
        self.__validation = validation
        self.__repository = repository

    def adaugare_spectacol(self, titlu, artist, gen, durata):
        # adaugare in fisier plus date paramterii int
        spectacole = Spectacole(titlu, artist, gen, durata)

        if (self.__validation.validare_titlu(titlu) == True and self.__validation.validare_artist(artist) == True and
                self.__validation.validare_durata(durata) == True and self.__validation.validare_gen(gen) == True):
            self.__repository.add_spectacol(spectacole)
        else:
            raise ValueError("Datele nu sunt corect introduse!!")

    def modificare_spectacol(self, titlu, artist, gen, durata):
        # parametrii datele obiectului tip str si int plus validare
        spectacole = Spectacole(titlu, artist, gen, durata)
        if (self.__validation.validare_titlu(titlu) == True and self.__validation.validare_artist(artist) == True and
                self.__validation.validare_durata(durata) == True and self.__validation.validare_gen(gen) == True):
            self.__repository.modify_spectacol(spectacole)
        else:
            raise ValueError("Datele nu sunt corect introduse!!")

    def random_generare(self, numar):
        # paramterii numar int -> de cate ori sa creeze un obiect nou
        if numar == 0:
            return
        lista_generare = ["Comedie", "Concert", "Balet", "Altele"]
        caractere_posibile = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ok = 0

        lungime = random.randint(9, 12)
        nume = ''.join(random.choice(caractere_posibile) for _ in range(lungime))
        artiste = ''.join(random.choice(caractere_posibile) for _ in range(lungime))
        gen = random.choice(lista_generare)
        durata = random.randint(0, 2000000)
        self.adaugare_spectacol(nume, artiste, gen, durata)

        self.random_generare(numar - 1)

    def export_date(self, nume_fiser):
        # export fisier: nume fisier, soratre dupa ambele moduri
        lista = self.__repository.load_from_file()
        lst = sorted(lista, key=lambda x: x.get_artist() and x.get_titlu(), reverse=False)

        with open(nume_fiser, "w") as file:
            for line in lst:
                file.write(f"{line.get_titlu()},{line.get_artist()},{line.get_gen()},{line.get_durata()}\n")


def test_service():
    repo = Repository("spectacole_test.txt")
    valid = Validation()
    service = Service(valid, repo)
    service.adaugare_spectacol("CostiMaxShow", "Costi", "Comedie", 20000)
    service.adaugare_spectacol("Teren Minat", "Florin Piersic", "Altele", 10000)
    service.modificare_spectacol("CostiMaxShow", "Costi", "Balet", 100)
    service.random_generare(3)
    service.export_date("mere.txt")


test_service()

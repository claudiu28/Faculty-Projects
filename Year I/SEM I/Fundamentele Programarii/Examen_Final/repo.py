from domain import Spectacole


class Repository:
    def __init__(self, filename):
        self.__filename = filename
        self.__lista = self.load_from_file()

    def load_from_file(self):
        # incarcare date din fisier
        lista = []
        with open(self.__filename, "r") as file:
            for line in file:
                attrs = line.strip().split(",")
                if len(attrs) == 4:
                    titlu = attrs[0]
                    artist = attrs[1]
                    gen = attrs[2]
                    durata = int(attrs[3])
                    spectacol = Spectacole(titlu, artist, gen, durata)
                    lista.append(spectacol)
        return lista

    def save_to_file(self):
        # incaracare date in fisier
        with open(self.__filename, "w") as file:
            for line in self.__lista:
                file.write(f"{line.get_titlu()},{line.get_artist()},{line.get_gen()},{line.get_durata()}\n")

    def add_spectacol(self, spectacol):
        # incarcare date din fisier, parametrii de tip clasa spectacol, apoi printrare in fisier
        lista = self.load_from_file()
        lista.append(spectacol)
        self.__lista = lista
        self.save_to_file()

    def modify_spectacol(self, spectacol):
        # incarcare date din fisier;parametrii de tip clasa spectacol; apoi modificare de date
        lista = self.load_from_file()

        for element in lista:
            if element.get_titlu() == spectacol.get_titlu() and element.get_artist() == spectacol.get_artist():
                element.set_gen(spectacol.get_gen())
                element.set_durata(spectacol.get_durata())
        self.__lista = lista
        self.save_to_file()


def test_repo():
    repo = Repository("spectacole_test.txt")
    spectacole = Spectacole("Capra cu Trei Iezi", "Ion Creanga", "Altele", 20000)
    repo.add_spectacol(spectacole)
    spectacole = Spectacole("O nopate furtunoasa", "FLorin Piersic", "Altele", 50000)
    repo.add_spectacol(spectacole)
    spectacol = Spectacole("Ana are mere","Florin Piersic","Comedie",800)
    repo.modify_spectacol(spectacol)

test_repo()

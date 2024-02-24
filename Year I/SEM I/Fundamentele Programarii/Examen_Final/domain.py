class Spectacole:
    # creacre clasa Specatacole plus gettari si settari
    def __init__(self, titlu, artist, gen, durata):
        self.__tiltu = titlu
        self.__artist = artist
        self.__gen = gen
        self.__durata = durata

    def get_titlu(self):
        return self.__tiltu

    def get_artist(self):
        return self.__artist

    def get_durata(self):
        return self.__durata

    def get_gen(self):
        return self.__gen

    def set_durata(self, durata):
        self.__durata = durata

    def set_gen(self, gen):
        self.__gen = gen

    def __repr__(self):
        return f"{self.__tiltu},{self.__artist},{self.__gen},{self.__durata}"


def test_spectacole():
    spectacole = Spectacole("Capra cu Trei Iezi", "Ion Creanga", "Altele", 20000)
    assert spectacole.get_titlu() == "Capra cu Trei Iezi"
    assert spectacole.get_artist() == "Ion Creanga"
    assert spectacole.get_gen() == "Altele"
    assert spectacole.get_durata() == 20000
    spectacole.set_durata(3000)
    assert spectacole.get_durata() == 3000
    assert spectacole.get_gen() == "Altele"
    spectacole.set_gen("Comedie")
    assert spectacole.get_gen() == "Comedie"


test_spectacole()

from domain import Imobil


class FileRepo:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__objects = self.__load_from_file()

    def __load_from_file(self):
        # preluare din fisier a tuturor obiectelor de tip imobilier
        try:
            lista = []
            with open(self.__file_name, "r") as f:
                lines = f.readlines()
                for line in lines:
                    attrs = line.strip().split(",")
                    if attrs != "" and len(attrs) == 4:
                        id_imobil = int(attrs[0])
                        adresa = attrs[1]
                        pret = float(attrs[2])
                        tip = attrs[3]
                        imobil = Imobil(id_imobil, adresa, pret, tip)
                        lista.append(imobil)
            return lista
        except FileNotFoundError:
            raise FileNotFoundError("Fisierul nu exista!")

    def get_all(self):
        # obiecte de tip imobilier
        return self.__objects


def test_file_repo():
    # testare functionalitate repo (numar de obiecte corepsunde cu cel din fiserul text)
    repo = FileRepo("test.txt")
    assert len(repo.get_all()) == 10


test_file_repo()

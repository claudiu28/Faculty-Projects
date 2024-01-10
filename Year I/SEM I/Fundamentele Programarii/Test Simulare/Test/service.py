from file_repo import FileRepo
from validation import Validation
from domain import Imobil, Comision


class ServiceImobiliar:
    # clasa service
    def __init__(self, validation, repo):
        # validare + file_repo + initializare service
        self.__validation = validation
        self.__repo = repo

    def medie_pe_pret(self, tip):
        # validarea tipului (vanzare sau inchiriere) + calculrarea mediei

        lista = self.__repo.get_all()
        if self.__validation(tip.strip()) == tip.strip():
            suma = 0
            numar = 0
            for element in lista:
                if element.get_tip() == tip:
                    suma = suma + element.get_pret()
                    numar = numar + 1
            medie = float(suma / numar)
            return medie

    def tranzactii(self, id_imobil, pret_negocitat):
        # tranzactie in functie de pretul_negociat si id_imobil
        lista = self.__repo.get_all()
        for element in lista:
            if element.get_id_imobil() == id_imobil:
                if element.get_tip().strip() == "vanzare":
                    comision = float((2 * pret_negocitat) / 100)
                    imo = Imobil(element.get_id_imobil(), element.get_adresa(), element.get_pret(), element.get_tip())
                    comi = Comision(imo, comision)
                    return comi
                elif element.get_tip().strip() == "inchiriere":
                    comision = float(50 * float(pret_negocitat / 12) / 100)
                    imo = Imobil(element.get_id_imobil(), element.get_adresa(), element.get_pret(), element.get_tip())
                    comi = Comision(imo, comision)
                    return comi


def test_service_imobiliar():
    # test functionalitate service medie pe pret
    validation = Validation()
    repo = FileRepo("test.txt")
    service = ServiceImobiliar(validation.verificare_tip, repo)
    assert service.medie_pe_pret("vanzare") == 88333.33333333333
    assert service.medie_pe_pret("inchiriere") == 105000.0


def test_service_imobiliar2():
    # test functionalitate service tranzactii in functie de comision
    validation = Validation()
    repo = FileRepo("test.txt")
    service = ServiceImobiliar(validation.verificare_tip, repo)
    comision = service.tranzactii(1, 40000)
    assert comision.get_comision() == 800.0
    assert comision.get_imobil().get_adresa().strip() == "str.Cernei nr.10 Cluj-Napoca"


test_service_imobiliar()
test_service_imobiliar2()

class Imobil:
    def __init__(self, id_imobil, adresa, pret, tip):
        self.__id_imobil = id_imobil
        self.__adresa = adresa
        self.__pret = pret
        self.__tip = tip

    def get_id_imobil(self):
        # get id imobil
        return self.__id_imobil

    def get_pret(self):
        # get pret imobil
        return self.__pret

    def get_tip(self):
        # get tip imobil
        return self.__tip

    def get_adresa(self):
        # get adresa imobil
        return self.__adresa


class Comision:
    def __init__(self, imobil, comision):
        self.__imobil = imobil
        self.__comision = comision

    def get_imobil(self):
        return self.__imobil

    def get_comision(self):
        return self.__comision


def test_clasa_imobil():
    # test functionalitate clasa imobil
    imobil = Imobil(23, "str. Cernei nr.10 Cluj-Napoca", 50000, "vanzare")
    assert imobil.get_id_imobil() == 23
    assert imobil.get_tip() == "vanzare"
    assert imobil.get_adresa() == "str. Cernei nr.10 Cluj-Napoca"
    assert imobil.get_pret() == 50000


def test_clasa_comision():
    imobil = Imobil(23, "str. Cernei nr.10 Cluj-Napoca", 50000, "vanzare")
    comision = Comision(imobil, 20)
    assert comision.get_imobil() == imobil
    assert comision.get_comision() == 20


test_clasa_comision()
test_clasa_imobil()

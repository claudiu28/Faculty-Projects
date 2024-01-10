from module.third_module.adaugare import Adaugare
from module.third_module.stergere import Stergere
from module.third_module.tiparire import Tiparire
from module.third_module.rapoarte import Rapoarte
from module.third_module.filtrare import Filtrare
from module.third_module.undo import Undo


class TestAdaugareDateDespreApartamente:
    # test pentru adaugarea unui apartament
    def test_adugare_date_despre_apartamente(self):
        lista_apartamente = []
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 1, 100, "canal", "24 January 2021")
        assert lista_apartamente[0].get_numar_apartament() == 1
        assert lista_apartamente[0].get_suma() == 100
        assert lista_apartamente[0].get_tip_cheltuiala() == "canal"
        assert lista_apartamente[0].get_data_cheltuiala() == "24 January 2021"


class TestStergereDateDespreApartamente:
    # test pentru stergerea unui apartament
    def test_stergere_date_despre_apartamente(self):
        lista_apartamente = []
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 1, 100, "canal", "24 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 2, 200, "intretinere", "25 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 3, 300, "canal", "26 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 4, 400, "intretinere", "27 January 2021")

        Stergere.stergere_apartament(lista_apartamente, 1)
        Stergere.stergere_apartament_ab(lista_apartamente, 2, 3)
        Stergere.stergere_apartament_tip(lista_apartamente, "intretinere")
        assert len(lista_apartamente) == 4


class TestTiparDateDespreApartamente:
    # test pentru tiparirea unui apartament mai mare ca o suma data
    def test_tipar_mare_ca_o_suma(self):
        lista_apartamente = []
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 1, 100, "canal", "24 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 2, 200, "intretinere", "25 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 3, 300, "canal", "26 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 4, 400, "intretinere", "27 January 2021")
        tiparitor = Tiparire()
        filtered_apartments = tiparitor.tipar_mare_ca_o_suma(lista_apartamente, 250)
        assert all(ap['suma'] > 250 for ap in filtered_apartments)
        assert {ap['numar_apartament'] for ap in filtered_apartments} == {3, 4}

    def test_tipar_date_tip(self):
        # test pentru tiparirea unui apartament de un anumit tip
        lista_apartamente = []
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 1, 100, "canal", "24 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 2, 200, "intretinere", "25 January 2021")
        tiparitor = Tiparire()
        filtered_apartments = tiparitor.tipar_date_tip(lista_apartamente, "intretinere")
        assert all(ap['tip_cheltuiala'] == "intretinere" for ap in filtered_apartments)
        assert len(filtered_apartments) == 1
        assert filtered_apartments[0]['numar_apartament'] == 2

    def test_tipar_in_functie_de_zi_suma(self):
        # test pentru tiparirea unui apartament mai mare ca o suma data de la o zi data
        lista_apartamente = []
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 1, 100, "canal", "24 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 2, 200, "intretinere", "25 January 2021")
        tiparitor = Tiparire()
        filtered_apartments = tiparitor.tipar_in_functie_de_zi_suma(lista_apartamente, "26 January 2021", 150)
        assert all(ap['suma'] > 150 and ap['data_cheltuiala'] < "26 January 2021" for ap in filtered_apartments)
        assert {ap['numar_apartament'] for ap in filtered_apartments} == {2}


class TestRaportDateApartament:
    def test_suma_totala_dupa_tip(self):
        # test pentru raportul sumei totale pentru un anumit tip de cheltuiala
        lista_apartamente = []
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 1, 100, "canal", "24 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 2, 200, "intretinere", "25 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 3, 300, "canal", "26 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 4, 400, "intretinere", "27 January 2021")

        raport = Rapoarte()
        suma_canal = raport.suma_totala_dupa_tip(lista_apartamente, "canal")
        suma_intretinere = raport.suma_totala_dupa_tip(lista_apartamente, "intretinere")

        assert suma_canal == 400  # 100 + 300
        assert suma_intretinere == 600  # 200 + 400

    def test_suma_in_functie_de_numar(self):
        #   test pentru raportul sumei totale pentru un anumit apartament in functie de numarul apartamentului
        lista_apartamente = []
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 1, 100, "canal", "24 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 2, 200, "intretinere", "25 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 3, 300, "canal", "26 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 4, 400, "intretinere", "27 January 2021")

        raport = Rapoarte()
        suma_apartament_1 = raport.suma_in_functie_de_numar(lista_apartamente, 1)
        suma_apartament_3 = raport.suma_in_functie_de_numar(lista_apartamente, 3)

        assert suma_apartament_1 == 100
        assert suma_apartament_3 == 300

    def test_date_sortate(self):
        # test pentru raportul datelor sortate dupa un anumit tip de cheltuiala
        lista_apartamente = []
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 1, 100, "canal", "24 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 2, 200, "intretinere", "25 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 3, 300, "canal", "26 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 4, 400, "intretinere", "27 January 2021")

        raport = Rapoarte()
        sorted_list = raport.date_sortate(lista_apartamente, "canal")

        assert all(ap['tip_cheltuiala'] == "canal" for ap in sorted_list)
        numar_apartamente = [ap['numar_apartament'] for ap in sorted_list]
        assert numar_apartamente == sorted(numar_apartamente), ":(((((((((("


class TestFiltrareDateApartament:
    # test pentru filtrarea unui apartament de un anumit tip
    @staticmethod
    def filtrare_date():
        lista_apartamente = []
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 1, 100, "canal", "24 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 2, 200, "intretinere", "25 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 3, 300, "canal", "26 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 4, 400, "intretinere", "27 January 2021")
        filtrator = Filtrare()
        filtered_apartments = filtrator.filtrare_tip(lista_apartamente, "intretinere")
        assert all(ap['tip_cheltuiala'] == "intretinere" for ap in filtered_apartments)
        assert {ap['numar_apartament'] for ap in filtered_apartments} == {2, 4}

    # test pentru filtrarea unui apartament mai mare ca o suma data
    def test_filtrare_suma(self):
        lista_apartamente = []
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 1, 100, "canal", "24 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 2, 200, "intretinere", "25 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 3, 300, "canal", "26 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 4, 400, "intretinere", "27 January 2021")
        filtrator = Filtrare()
        filtered_apartments = filtrator.filtrare_suma(lista_apartamente, 250)
        assert all(ap['suma'] < 250 for ap in filtered_apartments)
        assert set(ap['numar_apartament'] for ap in filtered_apartments) == {1, 2}


class TestUndo:
    # test pentru undo
    def test_undo(self):
        undo_manager = Undo()
        lista_apartamente = []
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 1, 100, "canal", "24 January 2021")
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 2, 200, "intretinere", "25 January 2021")
        undo_manager.registers(lista_apartamente)
        Adaugare.adaugare_date_despre_apartamente(lista_apartamente, 3, 300, "canal", "26 January 2021")

        assert len(lista_apartamente) == 3
        lista_apartamente = undo_manager.pop_undo()

        assert len(lista_apartamente) == 2
        assert all(apartament.get_numar_apartament() in {1, 2} for apartament in lista_apartamente)

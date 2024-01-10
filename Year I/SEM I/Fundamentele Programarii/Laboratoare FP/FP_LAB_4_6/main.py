from module import user_interface
from module.second_module import test
if __name__ == '__main__':
    test.TestAdaugareDateDespreApartamente().test_adugare_date_despre_apartamente()
    test.TestStergereDateDespreApartamente().test_stergere_date_despre_apartamente()
    test.TestTiparDateDespreApartamente().test_tipar_date_tip()
    test.TestTiparDateDespreApartamente().test_tipar_mare_ca_o_suma()
    test.TestTiparDateDespreApartamente().test_tipar_in_functie_de_zi_suma()
    test.TestRaportDateApartament().test_suma_in_functie_de_numar()
    test.TestRaportDateApartament().test_suma_totala_dupa_tip()
    test.TestRaportDateApartament().test_date_sortate()
    test.TestFiltrareDateApartament().filtrare_date()
    test.TestFiltrareDateApartament().test_filtrare_suma()
    test.TestUndo().test_undo()
    user_interface.Meniu.Meniu()

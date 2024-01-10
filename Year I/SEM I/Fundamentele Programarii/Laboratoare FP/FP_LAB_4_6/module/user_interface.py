from module.third_module import undo
from module.second_module.citire import Input_comanda
import datetime
from module.second_module.models import ListaApartamente
from module.third_module import processing
from module.third_module import command


# setare datetime valid de forma zi luna(fullname) an
def convert_datetime(string_datetime):
    string_datetime = string_datetime.strip()
    date = datetime.datetime.strptime(string_datetime, "%d %B %Y")
    return date


# vizualizare date din manager list
def printing(manager):
    for apartament in manager.lista_apartamente_vizualizare():
        if len(manager.lista_apartamente_vizualizare()) == 0:
            print({})
        print(apartament.to_dict())


# meniu cu optinui
def meniu():
    print('''
                            Aplicația permite:
                                1. Adăugare:
                                     a. adaugă cheltuială pentru un apartament -> comanda: adaugare(numar_apartament, suma, tip, data)
                                     b. modifică cheltuială -> comanda: modifica(numar_apartament, suma, tip, data)
                                2. Ștergere:
                                     a. Șterge toate cheltuielile de la un apartament -> comanda: stergere_apartament(numar_apartament)
                                     b. Șterge cheltuielile de la apartamente consecutive -> comanda: stergere_apartament_ab(numar_apartament_a, numar_apartament_b)
                                     (Ex. se dau două numere de apartament 2 și 5 și se șterg toate cheltuielile de la apartamentele 1,2,3,4 și 5)
                                     c. Șterge cheltuielile de un anumit tip de la toate apartamentele -> comanda: stergere_apartament_tip(tip)
                                3. Căutări:
                                        a. Tipărește toate cheltuielile mai mari decât o sumă dată -> comanda: tipar_sum(suma)
                                        b. Tipărește toate cheltuielile de un anumit tip -> comanda: tipar_tip(tip)
                                        c. Tipărește toate cheltuielile mai mari decât o sumă dată de la un apartament -> comanda: tipar_zi_suma(zi, suma)
                                4. Rapoarte:
                                        a. Tipărește suma totală pentru un anumit tip de cheltuială -> comanda: raport_suma_totala(tip)
                                        b. Tipărește suma totală pentru un anumit apartament -> comanda: raport_suma_totala_numar(numar_apartament)
                                        c. Tipărește toate cheltuielile sortate după tip -> comanda: raport_sortare_tip(tip)
                                5. Filtru:
                                        a. Filtrează cheltuielile mai mari decât o sumă dată -> comanda: filtrare_suma(suma)
                                        b. Filtrează cheltuielile de un anumit tip -> comanda: filtrare_tip(tip)
                                6. Undo: -> comanda: undo
                                7. Vizualizare apartamente existente in bloc: -> comanda: vizualizare
                                8. Iesire din aplicatie
                    ''')


class Meniu:
    @staticmethod
    def Meniu():
        initial_lista_apartamente = []
        manager = ListaApartamente(initial_lista_apartamente)
        manager_undo = undo.Undo()
        while True:
            try:
                meniu()
                try:
                    comanda = Input_comanda()
                    cmdz = processing.comanda_split(comanda)

                    for com in cmdz:
                        try:
                            processing_comanda = processing.processing(com)
                            param0 = processing_comanda[0]
                            if param0 == "adaugare":
                                manager_undo.registers(manager.lista_apartamente)
                                command.Command.adaugare_cheltuiala(manager.lista_apartamente, *processing_comanda[1:])
                            elif param0 == "modifica":
                                manager_undo.registers(manager.lista_apartamente)
                                command.Command.modificare_cheltuiala(manager.lista_apartamente, *processing_comanda[1:])
                            elif param0 == "stergere_apartament":
                                manager_undo.registers(manager.lista_apartamente)
                                command.Command.stergere_ap(manager.lista_apartamente, *processing_comanda[1:])
                            elif param0 == "stergere_apartament_ab":
                                manager_undo.registers(manager.lista_apartamente)
                                command.Command.stergere_ap_ab(manager.lista_apartamente, *processing_comanda[1:])
                            elif param0 == "stergere_apartament_tip":
                                manager_undo.registers(manager.lista_apartamente)
                                command.Command.stergere_ap_tip(manager.lista_apartamente, *processing_comanda[1:])
                            elif param0 == "tipar_sum":
                                lista = command.Command.tipar_suma(manager.lista_apartamente, *processing_comanda[1:])
                                print(lista)
                            elif param0 == "tipar_tip":
                                lista = command.Command.tipar_tip(manager.lista_apartamente, *processing_comanda[1:])
                                print(lista)
                            elif param0 == "tipar_zi_suma":
                                try:
                                    lista = command.Command.tipar_zi_suma(manager.lista_apartamente, *processing_comanda[1:])
                                    print(lista)
                                except (ValueError, TypeError) as e:
                                    print(f"Eroarea: {e}")
                            elif param0 == "raport_suma_totala":
                                try:
                                    sumatotala = command.Command.raport_suma_totala(manager.lista_apartamente,
                                                                                    *processing_comanda[1:])
                                    print(sumatotala)
                                except (ValueError, TypeError) as e:
                                    print(f"Eroarea: {e}")
                            elif param0 == "raport_suma_totala_numar":
                                try:
                                    suma_totala_dupa_ap = command.Command.raport_suma_totala_numar(manager.lista_apartamente,
                                                                                                   *processing_comanda[1:])
                                    print(suma_totala_dupa_ap)
                                except (ValueError, TypeError) as e:
                                    print(f"Eroarea: {e}")
                            elif param0 == "raport_sortare_tip":
                                try:
                                    lista = command.Command.raport_sortare_tip(manager.lista_apartamente, *processing_comanda[1:])
                                    print(lista)
                                except (ValueError, TypeError) as e:
                                    print(f"Eroarea: {e}")
                            elif param0 == "filtrare_tip":
                                try:
                                    lista = command.Command.filtrare_tip(manager.lista_apartamente, *processing_comanda[1:])
                                    print(lista)
                                except (ValueError, TypeError) as e:
                                    print(f"Eroarea: {e}")
                            elif param0 == "filtrare_suma":
                                try:
                                    lista = command.Command.filtrare_suma(manager.lista_apartamente, *processing_comanda[1:])
                                    print(lista)
                                except (ValueError, TypeError) as e:
                                    print(f"Eroarea: {e}")
                            elif param0 == "undo":
                                try:
                                    manager.lista_apartamente = manager_undo.pop_undo()
                                except (ValueError, TypeError) as e:
                                    print(f"Eroarea: {e}")
                            elif param0 == "vizualizare":
                                try:
                                    printing(manager)
                                except (ValueError, TypeError) as e:
                                    print(f"Eroarea: {e}")
                            elif param0 == "Nu s-a putut face comanda":
                                continue
                            else:
                                print("Comanda nu exista")
                        except ValueError:
                            print("Nu s-a putut executa!!!")
                except ValueError as e:
                    print(f"Eroarea: {e}")
            except ValueError as e:
                print(f"Eroarea: {e}")

"""
Scrieti o aplicatie care are interfata utilizator tip consolă cu un meniu:
    1 Citirea unei liste de numere intregi
    2,3 Gasirea secventelor de lungime maxima care respectă o proprietatea dată. Fiecare student primeste 2 proprietati din lista
    de mai jos.
    4 Iesire din aplicatie.
    Documentatia să contină:
        Scenarii de rulare pentru cele două cerinte primite (vezi curs 1 – scenarii de rulare)
        Cazuri de testare pentru cele doua cerinte în format tabelar (vezi curs 1 – cazuri de testare)
        Se cauta secventa de lungime maximă cu proprietatea:
            2. Contine cel mult trei valori distincte
            6. sunt toate distincte intre ele
"""
from sys import exit


def IntroducereOptiuneMeniu():
    option = int(input("Optiunea dorita este: "))
    return option


def IesireOptiuneMeniu():
    return exit('Ai iesit din aplicatia de tip consola!!!')


def CitireaListeiIntregi():
    lista_numere = []
    n = int(input("Cate elemente doriti sa adaugati: "))

    for i in range(n):
        x = int(input(f'Elementul cu numarul de ordine {i + 1}: '))
        lista_numere.append(x)

    return lista_numere


def secventadistincte(num: list) -> list:
    if not num:
        return []
    subsecventa_maxima = []
    subsecventa_curenta = []
    for element in num:
        if element not in subsecventa_curenta:
            subsecventa_curenta.append(element)
            if len(subsecventa_curenta) > len(subsecventa_maxima):
                subsecventa_maxima = subsecventa_curenta[:]
        else:
            pozitie = subsecventa_curenta.index(element)
            subsecventa_curenta = subsecventa_curenta[pozitie + 1:]
            subsecventa_curenta.append(element)
    return subsecventa_maxima


def TestSecventaDistincte():
    assert secventadistincte([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert secventadistincte([1, 2, 2, 3, 1, 5]) == [2, 3, 1, 5]
    assert secventadistincte([1, 1, 1, 1]) == [1]
    assert secventadistincte([]) == []


def TreiSecventaDistincte(num: list) -> list:
    if num is []:
        return []
    subsecventa_maxima = []
    subsecventa_curenta = []
    for element in num:
        subsecventa_curenta.append(element)
        while len(set(subsecventa_curenta)) > 3:
            subsecventa_curenta.pop(0)
        if len(subsecventa_maxima) < len(subsecventa_curenta):
            subsecventa_maxima[:] = subsecventa_curenta
    return subsecventa_maxima


def TestTreiSecventaDistincte():
    assert TreiSecventaDistincte([1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 4, 4, 4]) == [2, 2, 2, 3, 3, 3, 2, 2, 4, 4, 4]
    assert TreiSecventaDistincte([4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4]
    assert TreiSecventaDistincte([]) == []
    assert TreiSecventaDistincte([1, 1, 1, 1, 2, 2, 4, 5]) == [1, 1, 1, 1, 2, 2, 4]
    assert TreiSecventaDistincte([1, 2, 2, 2, 3, 4, 4]) == [2, 2, 2, 3, 4, 4]


def SumaMaxima(num: list) -> list:
    if not num:
        return []
    index_start = 0
    index_final = 0
    auxiliar = 0
    maxim = maxim_total = 0
    for element in range(0, len(num)):
        if num[element] > maxim + num[element]:
            maxim = num[element]
            auxiliar = element
        else:
            maxim = maxim + num[element]
        if maxim_total < maxim:
            maxim_total = maxim
            index_start = auxiliar
            index_final = element
    return num[index_start:index_final + 1]


def TestSumaMaxima():
    assert SumaMaxima([]) == []
    assert SumaMaxima([4]) == [4]
    assert SumaMaxima([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [4, -1, 2, 1]
    assert SumaMaxima([-2, 1, 2, -1, -2, 2, -2]) == [1, 2]


def Meniu():
    numere = []
    while True:
        print("""
            1. Citirea unei liste de numere intregi.
            2. Gasirea secventelor de lungime maxima care respectă o proprietatea dată: contine cel mult trei valori 
            distincte.
            3. Gasirea secventelor de lungime maxima care respectă o proprietatea dată: sunt toate distincte intre ele.
            4. Gasirea secventelor de lungime maxima care respectă o proprietatea dată:are suma maxima.
            5. Iesire din aplicatie.
        """)
        option = IntroducereOptiuneMeniu()
        if option == 1:
            numere = CitireaListeiIntregi()
        elif option == 2:
            print(TreiSecventaDistincte(numere))
        elif option == 3:
            print(secventadistincte(numere))
        elif option == 4:
            print(SumaMaxima(numere))
        elif option == 5:
            IesireOptiuneMeniu()
        else:
            print('Introduceti o optiune valida pentru meniu!!! O optiune valida contine numerele 1,2,3 sau 4. '
                  f'{option} nu face parte din numerele de optiuni!')


if __name__ == '__main__':
    TestSecventaDistincte()
    TestTreiSecventaDistincte()
    TestSumaMaxima()
    Meniu()

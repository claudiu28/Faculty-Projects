# bkt iterativ + recursiv
# Cerinta:Se dă o listă de numere întregi a1,...an, determinați toate sub-secvențele (ordinea
# elementelor este menținută) strict crescătoare.


def read_list():
    lst = []
    n = int(input("Dati numarul de elemente: "))
    while n != 0:
        lst.append(int(input("Dati elementul: ")))
        n = n - 1
    return lst


def solutie(lst, lg):
    return len(lst) <= lg


def consistent(lst, x):

    for i in range(1, len(x)):
        if lst[x[i-1]] >= lst[x[i]]:
            return False
    return True


def solutie_gasita(lst, x):

    for i in x:
        print(lst[i], end=' ')
    print()


def bkt_iterativ(lst, lg):
    x = [-1]
    while len(x) > 0:
        ales = False
        while not ales and x[-1] < lg - 1:
            x[-1] = x[-1] + 1
            ales = consistent(lst, x)
        if ales:
            if solutie(x, lg):
                solutie_gasita(lst, x)
            x.append(-1)
        else:
            x = x[:-1]


def bkt_recursiv(lst, x, lg):
    if x:
        if consistent(lst, x):
            solutie_gasita(lst, x)
    if solutie(x, lg):
        if x:
            start = x[-1] + 1
        else:
            start = 0
        for i in range(start, lg):
            x.append(i)
            bkt_recursiv(lst, x, lg)
            x.pop()


lista = read_list()
lungime = len(lista)
#bkt_iterativ(lista, lungime)
bkt_recursiv(lista, [], lungime)

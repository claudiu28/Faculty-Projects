
def insertion_sort(lista):
    for i in range(len(lista)):
        index = i - 1
        element = lista[i]
        while element < lista[index] and index >= 0:
            lista[index + 1] = lista[index]
            index = index - 1
        lista[index + 1] = element

    return lista


def selection_sort(lista):
    for i in range(0, len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mij = len(lista) // 2

    st = merge_sort(lista[:mij])
    dr = merge_sort(lista[mij:])

    i = j = 0
    lista_noua = []
    while i < len(st) and j < len(dr):
        if st[i] < dr[j]:
            lista_noua.append(st[i])
            i = i + 1
        else:
            lista_noua.append(dr[j])
    while i < len(st):
        lista_noua.append(st[i])
        i = i + 1
    while j < len(dr):
        lista_noua.append(dr[j])
        j = j + 1
    return lista_noua


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista.pop()
    st = quick_sort([x for x in lista if x < pivot])
    dr = quick_sort([x for x in lista if x > pivot])
    return st + [pivot] + dr


def det_pivot(lista, stanga, dreapta):
    pivot = lista[stanga]
    i = stanga
    j = dreapta

    while i != j:
        while i < j and lista[j] >= pivot:
            j = j - 1
        lista[j] = lista[i]
        while i < j and lista[i] <= pivot:
            i = i + 1
        lista[i] = lista[j]

    lista[i] = pivot

    return i


def quick_sort_inplace(lista, stanga, dreapta):
    position = det_pivot(lista, stanga, dreapta)
    if position - 1 > stanga:
        return quick_sort_inplace(lista, position - 1, dreapta)
    if position + 1 < dreapta:
        return quick_sort_inplace(lista, stanga, position + 1)


def bs_iterativ(lista, element):
    if len(lista) == 0:
        return -1

    stanga = 0
    dreapta = len(lista) - 1

    while stanga <= dreapta:
        mijloc = (stanga + dreapta) // 2
        if lista[mijloc] == element:
            return mijloc
        elif lista[mijloc] > element:
            dreapta = mijloc - 1
        elif lista[mijloc] < element:
            stanga = mijloc + 1


def bs_recursiv(lista, element, stanga, dreapta):
    if len(lista) == 0 or stanga > dreapta:
        return -1

    mijloc = (stanga + dreapta) // 2

    if lista[mijloc] == element:
        return mijloc
    elif lista[mijloc] < element:
        return bs_recursiv(lista, element, mijloc + 1, dreapta)
    else:
        return bs_recursiv(lista, element, stanga, mijloc - 1)


def divide_et_impera(lista):
    if len(lista) == 1:
        if lista[0] % 2 == 0:
            return []
        return [lista[0]]
    mij = len(lista) // 2
    st = divide_et_impera(lista[:mij])
    dr = divide_et_impera(lista[mij:])
    return st + dr




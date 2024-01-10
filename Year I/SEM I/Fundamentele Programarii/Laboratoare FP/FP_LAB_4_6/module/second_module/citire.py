def Input_comanda():
    # introducere comanda de la tastatura, impreuna cu parametrii necesari
    try:
        comanda = input("Comanda pentru ce doriti sa faceti:")
        # daca comanda este vida, se arunca o exceptie
        if comanda.strip() == "":
            raise ValueError("Comanda nu poate fi vida")
        return comanda
    except ValueError as ve:
        print(ve)


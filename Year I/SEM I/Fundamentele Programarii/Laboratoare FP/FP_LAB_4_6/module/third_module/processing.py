def comanda_split(comanda_initiala):
    return comanda_initiala.split("; ")


def modify_comanda(comanda):
    if comanda == "" or ">" in comanda or "<" in comanda or "=" in comanda:
        raise ValueError("Comanda nu poate fi vida sau contine caractere invalide.")
    elif '(' in comanda and ')' in comanda:
        nume_comanda = comanda.split('(')[0]
        argumente_string = comanda[comanda.find('(') + 1:comanda.rfind(')')]
        argumente = argumente_string.split(',')
        processed_args = []
        for arg in argumente:
            arg = arg.strip()
            try:
                if '.' in arg:
                    processed_args.append(float(arg))
                else:
                    processed_args.append(int(arg))
            except ValueError:
                processed_args.append(arg)
        return [nume_comanda] + processed_args
    else:
        return [comanda]


def processing(comanda):
    parameters = modify_comanda(comanda)
    cmd = parameters[0]
    commands = {
        'adaugare': lambda p: [cmd] + p[1:],
        'modifica': lambda p: [cmd] + p[1:],
        'stergere_apartament': lambda p: [cmd] + p[1:],
        'stergere_apartament_ab': lambda p: [cmd] + p[1:],
        'stergere_apartament_tip': lambda p: [cmd] + p[1:],
        'tipar_sum': lambda p: [cmd] + p[1:],
        'tipar_tip': lambda p: [cmd] + p[1:],
        'tipar_zi_suma': lambda p: [cmd] + p[1:],
        'raport_suma_totala': lambda p: [cmd] + p[1:],
        'raport_suma_totala_numar': lambda p: [cmd] + p[1:],
        'raport_sortare_tip': lambda p: [cmd] + p[1:],
        'filtrare_tip': lambda p: [cmd] + p[1:],
        'filtrare_suma': lambda p: [cmd] + p[1:],
        'undo': lambda p: [cmd] + p[1:],
        'vizualizare': lambda p: [cmd] + p[1:],
    }
    if cmd in commands:
        return commands[cmd](parameters)
    else:
        return "Nu s-a putut face comanda"

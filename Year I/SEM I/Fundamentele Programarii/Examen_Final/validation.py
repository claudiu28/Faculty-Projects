class Validation:
    @staticmethod
    def validare_titlu(titlu):
        "validare date pt titlu"
        "returneaza true sau eraore"
        errors = []
        if titlu == "":
            errors.append("Titlu vid!!!")
        if not errors:
            return True
        return errors

    @staticmethod
    def validare_artist(artist):
        "validare date pt artist"
        "returneaza true sau eraore"
        errors = []
        if artist == "":
            errors.append("Artistul e vid!!!")
        if not errors:
            return True
        return errors

    @staticmethod
    def validare_durata(durata):
        "validare date pt durata"
        "returneaza true sau eraore"
        errors = []
        if int(durata) >= 0:
            return True
        else:
            errors.append("Durata nu poate fi negativa!")
        if not errors:
            return True
        return errors

    @staticmethod
    def validare_gen(gen):
        " validare date pt gen"
        "returneaza true sau eraore"
        errors = []
        if gen == "Comedie" or gen == "Altele" or gen == "Balet" or gen == "Concert":
            return True
        else:
            errors.append("Genul nu este corepunzator!")
        if not errors:
            return True
        return errors


def test_validare():
    valid = Validation()
    assert valid.validare_gen("Rock") == ['Genul nu este corepunzator!']
    assert valid.validare_gen("Comedie") == True
    assert valid.validare_artist("") == ["Artistul e vid!!!"]
    assert valid.validare_titlu("") == ["Titlu vid!!!"]
    assert valid.validare_durata(1000) == True
    assert valid.validare_durata(-2000) == ["Durata nu poate fi negativa!"]


test_validare()

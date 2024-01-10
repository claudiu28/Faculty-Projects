class Validation:

    @staticmethod
    def verificare_tip(tip):
        # validare in functie de tipul imobilului
        if tip != "vanzare" and tip != "inchiriere":
            raise ValueError("Tipul nu este valid!")
        return tip

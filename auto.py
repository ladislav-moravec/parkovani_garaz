class Auto:

    spz = None
    barva = None

    # Konstruktor
    def __init__(self, spz, barva):
        self.spz = spz
        self.barva = barva

    # Vrátí SPZ auta
    def vrat_spz(self):

        return self.spz

    # Zaparkuje auto do garáže
    def zaparkuj(self, garaz):

        garaz.vloz(self)

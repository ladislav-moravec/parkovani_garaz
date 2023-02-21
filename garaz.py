class Garaz:
    # Třída reprezentuje garáž

    auto = None

    # Vloží auto do garáže
    def vloz(self, auto):

        self.auto = auto

    # Vrátí textovou reprezentaci garáže
    def __str__(self):

        return "V garáži je auto {0}".format(self.auto.vrat_spz())

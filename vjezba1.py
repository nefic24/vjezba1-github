# Ovo je template za klasu
class Vozilo:
    def __init__(self, marka):
        self.marka = marka

    def info(self):
        print(f"Marka: {self.marka}")

class Auto(Vozilo):
    def __init__(self, marka, model):
        super().__init__(marka)
        self.model = model

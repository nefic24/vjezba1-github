# Ovo je template za klasu

"""
Initialize the class with atribute1 and atribute2.

args:
atribute1 (type)
atribute2 (type)
"""

class Vozilo:
    def __init__(self, marka):
        self.marka = marka

    def info(self):
        print(f"Marka: {self.marka}")

class Auto(Vozilo):
    def __init__(self, marka, model):
        super().__init__(marka)
        self.model = model

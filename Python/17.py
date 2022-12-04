class Zwierze():
    def glos(self):
        return "Ja mowie!"

class Malpa(Zwierze):
    def glos(self):
        return "costamcostam"

class Kon(Zwierze):
    def glos(self):
        return "hiha"

class Pies(Malpa, Kon):
    pass

class Kot(Kon, Malpa):
    pass

# Pokazanie sortowania z dziedziczenia
#print(Pies.mro())

pi = Pies()
ko = Kot()

print(ko.glos())
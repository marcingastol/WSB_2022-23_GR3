class Czlowiek():
    def __init__(self, name):
        self.name = name

class Lekarz(Czlowiek):
    def __init__(self, name):
        self.name = "Lekarz: ", name

class Prawnik(Czlowiek):
    def __init__(self, name):
        self.name = "Prawnik: ", name

cz = Czlowiek("Michal")
le = Lekarz("Anna")
pr = Prawnik("Magdalena")

print(cz.name)
print(le.name)
print(pr.name)
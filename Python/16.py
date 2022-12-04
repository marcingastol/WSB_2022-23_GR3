class Czlowiek():
    def __init__(self, name):
        self.name = name

class EmailCzlowiek(Czlowiek):
    def __init__(self, name, email):
        self.name = name
        #super().__init__(name)
        self.email = email

cz = EmailCzlowiek("Imie Nazwisko", "imie@nazwisko.com")
print(cz.name)
print(cz.email)
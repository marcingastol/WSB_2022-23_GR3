class CatParent():
    def voice(self):
        print("Jestem rodzicem!")

class CatKid(CatParent):
    pass

# sprawdzenie potomnosci dziedzieczenia klasy
#print(issubclass(CatKid, CatParent))

parent = CatParent()
kid = CatKid()

print(kid.voice())
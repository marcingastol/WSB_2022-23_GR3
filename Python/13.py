class CatParent():
    def voice(self):
        print("Jestem rodzicem!")

class CatKid(CatParent):
    def voice(self):
        print("Jestem dzieckiem")

# sprawdzenie potomnosci dziedzieczenia klasy
#print(issubclass(CatKid, CatParent))

parent = CatParent()
kid = CatKid()

parent.voice()
kid.voice()
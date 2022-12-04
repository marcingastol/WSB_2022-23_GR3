class CatParent():
    def voice(self):
        print("Jestem rodzicem!")

class CatKid(CatParent):
    def voice(self):
        print("Jestem dzieckiem")
    
    def walk(self):
        print("Moge chodzic")


parent = CatParent()
kid = CatKid()

kid.walk()
parent.walk()
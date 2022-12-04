class Cat():
    pass

a_cat = Cat()
another_cat = Cat()

a_cat.age = 5
a_cat.name = "Kicia"
a_cat.sibling = another_cat

another_cat.age = 9
another_cat.name = "Kotek"
another_cat.sibling = a_cat

print(a_cat.sibling.name)
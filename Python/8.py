def print_more(required1, required2, *args):
    print("Parameter 1:", required1)
    print("Parameter 2:", required2)
    print("Everything else:", *args)

print_more(22,43,56456,"hehe","bleble")
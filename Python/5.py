def kolory(kolor):
    if kolor == "czerwony":
        return "W tym kolorze mam jablka"
    elif kolor == "zielony":
        return "W tym kolorze mam papryke"
    elif kolor == "zolty":
        return "W tym kolorze mam banany"
    else:
        return "Nie mam nic w podanym kolorze"

print(kolory("zielony"))
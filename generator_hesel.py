import random
while True:
    obtiznost = input("""Vyberte, jak obtížné heslo chcete vygenerovat
                        1. Slabé
                        2. Střední
                        3. Silné
                        4. Neprůstřelné """)
    slabe = ("abcdefghijklmnoprqstuvwxyz")  #
    stredni = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")#
    silne = ("0123456789")
    neprustrelne = (",.-!?:_/*-+")
    heslo = "" 
    if obtiznost == "1":
        for _ in range(7):
            slabeheslo = random.choice(slabe)
            heslo += slabeheslo
        print(f"Vaše heslo je: {heslo}")
    elif obtiznost == "2":
        znaky = list(slabe + stredni)
        random.shuffle(znaky)
        heslo = "".join(random.choice(znaky) for _ in range(7))
        print(f"Vaše heslo je: {heslo}")
    elif obtiznost == "3":
        znaky = list(slabe + stredni + silne)
        random.shuffle(znaky)
        heslo = "".join(random.choice(znaky) for _ in range(10))
        print(f"Vaše heslo je: {heslo}")
    elif obtiznost == "4":
        znaky = list(slabe + stredni + silne + neprustrelne)
        random.shuffle(znaky)
        heslo = "".join(random.choice(znaky) for _ in range(12))
        print(f"Vaše heslo je: {heslo}")
    else:
          ("Zadali jste špatné číslo obtížnosti hesla")

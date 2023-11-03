import random
while True:
    obtiznost = input("""Vyberte, jak obtížné heslo chcete vygenerovat
                        1. Slabé
                        2. Střední
                        3. Silné
                        4. Neprůstřelné """)
    slabe = ("abcdefghijklmnoprqstuvwxyz")
    stredni = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    silne = ("0123456789")
    heslo = ""
    neprustrelne = (",.-!?:_/*-+") 
    if obtiznost == "1":
            for _ in range(7):
                slabeheslo = random.choice(slabe)
                heslo += slabeheslo
            print(f"Vaše heslo je: {heslo}")
    if obtiznost == "2":
            for _ in range(3):
                 slabeheslo = random.choice(slabe)
                 heslo += slabeheslo
            for _ in range(3):
                  stredniheslo = random.choice(stredni)
                  heslo += stredniheslo
            print(f"Vaše heslo je{heslo}")
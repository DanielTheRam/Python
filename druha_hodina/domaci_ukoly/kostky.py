import random
kostka = (1,2,3,4,5,6)
konec_hry = True
while konec_hry:
    input("Napište 'hod' pro začátek hry: ")
    pocitac = random.choice(kostka)
    hrac = random.choice(kostka)

    print("Hráč hodil:", hrac)
    print("Počítač hodil:", pocitac)
    if hrac > pocitac:
        print("Vyhrals!")
        konec_hry = False
    elif hrac < pocitac:
        print("Prohrals!")
        konec_hry = True
    elif hrac == pocitac:
        print("Nerozhodně, hrajte znovu")
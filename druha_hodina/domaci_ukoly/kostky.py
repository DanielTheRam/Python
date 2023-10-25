import random
kostka = (1,2,3,4,5,6)
while True:
    input("Napište 'hod'  začátek hry: ")       # hod - aby hod opravdu něco dělal (zapl/vypl hru)
    pocitac = random.choice(kostka)
    hrac = random.choice(kostka)
    print("Hráč hodil:", hrac)
    print("Počítač hodil:", pocitac)        # jeden fstring
    if hrac > pocitac:
        print("Vyhrals!")
        quit()                  #forcuje vypnutí skriptu (jen u while cyklu)
    elif hrac < pocitac:
        print("Prohrals!")
    else:
        print("Remíza")         
seznam = (1,2,3,4,5,6,7,8) 
while True:
    print(""" Jakou akci chcete provést?
          1. Přidat číslo
          2. Spočítat počet čísel""")
    akce = input("Vyberte 1. nebo 2. možnost ")
    if akce == "1":
        cislo = input("Jaké číslo chcete přidat? ")
        if cislo.isdigit():    
            seznam += tuple(cislo)
            print(seznam)
        else:
            print("Pište pouze čísla")
    elif akce == "2":
        pocet_cisel = len(seznam)
        print(f"Počet čísel v seznamu je: {pocet_cisel}")
    else: 
        print("Špatně zadané číslo operace")
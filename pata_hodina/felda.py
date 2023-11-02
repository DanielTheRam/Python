seznam = ["Karel","Robert","Tomáš","Alice","Jarda"] 
while True:
    akce = input("Jakou akci chcete provést? (pridat/odebrat/zobrazit_seznam)")
    if akce == "pridat":
        name = input("Napište své jméno ")
        seznam.append(name)
        print(seznam)
    elif akce == "odebrat":
        remove = input(f"Koho chcete ze seznamu odebrat? {seznam} ")
        if remove in seznam:
            remove = seznam.remove(remove)
            print(seznam)
        elif remove not in seznam:
            print("Jméno není na seznamu")
    elif akce == "zobrazit_seznam":
        print(seznam)
    else:
        print("Špatně zadaný výraz")
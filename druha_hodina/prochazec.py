#dostanu od uzivatele vetu. Pokud ve vete je "a" - konec hry, pokud ne - hra pokracuje
konec = False
while not konec:
    veta = input("Napište náhodnou větu: ")
    for i in veta:
        if i == "a":
            print("Konec hry")
            konec = True
    if konec == False:                  #hlídat si řádky podmínek, aby to necyklilo v if nad tím
        print("Napište novou větu")

konec = False                           #ideální stav
while not konec:
    veta = input("Napište náhodnou větu: ")
    if "a" in veta:
        print("Konec hry")
        konec = True
    else:                  
        print("Napište novou větu")
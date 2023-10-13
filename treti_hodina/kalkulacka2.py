try:
    prvni_cislo = (input("Zadejte první číslo "))    
    druhe_cislo = (input("Zadejte druhé číslo "))
    operace = input("Vyberte operaci(+,-,*,/) ")

    if operace == "+":
        print(prvni_cislo + druhe_cislo)
    elif operace == "-":
        print(prvni_cislo - druhe_cislo)
    elif operace == "*":
        print(prvni_cislo * druhe_cislo)
    elif operace == "/":
        print(prvni_cislo / druhe_cislo)
    else:
       print("Chybně zadaná operace")
except ValueError:    
    print("ValueError") #pouze pro ValueError 
except:
    print("Nechápu")  # pokud dojde k jakéhokoliv jinému erroru - vypíše tuto hlášku | uživatel nepozná, kde vlastně nastala chyba

    #úkoly: - na začátku zajistím, aby nemuselo docházet k try/except -> použiji ale metodu (tj blbost.) -> našprtat se metody
    
    
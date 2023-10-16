try:
    prvni_cislo = float(input("Zadejte první číslo "))  
    operace = input("Vyberte operaci(+,-,*,/) ")  
    druhe_cislo = float(input("Zadejte druhé číslo "))
    
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
    print("Neznámá hodnota") #pouze pro ValueError 
except:
    print("Nechápu")  # pokud dojde k jakéhokoliv jinému erroru - vypíše tuto hlášku | uživatel nepozná, kde vlastně nastala chyba
                      # nevím, jak tuto chybu vyvolat - nejspíš ani nejde, protože to tam je ošetřeno elsem a prvním exceptem
    #úkoly: - na začátku zajistím, aby nemuselo docházet k try/except -> použiji ale metodu (tj blbost.) -> našprtat se metody
    

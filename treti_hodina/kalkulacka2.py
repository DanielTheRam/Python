prvni_cislo = input("Zadejte první číslo ")
operace = input("Vyberte operaci(+,-,*,/) ")  
druhe_cislo = input("Zadejte druhé číslo ")
if prvni_cislo.isnumeric() and druhe_cislo.isnumeric():
    prvni_cislo = int(prvni_cislo)
    druhe_cislo = int(druhe_cislo)
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
else:
    print("Nevhodný input")
    

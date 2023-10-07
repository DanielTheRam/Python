#kalkukacka

prvni = int(input("prvni cislo: "))         #vezme vstup uzivatele, urci datovy typ na int. a ulozi hodnotu do promenne prvni 
operace = input("vyber operaci (+,-,*,/)")
druhe = int(input("druhe cislo: "))         #vezme vstup uzivatele, urci datovy typ na int. a ulozi hodnotu do promenne druhe

if operace == "+":                          #vezme hodnotu promenne a pokud je hodnota +
    vysledek = (prvni + druhe)
    print(vysledek)                    #secte prvni a druhe promenne a vysledek vytiskne
elif operace == "-":  
    vysledek = (prvni - druhe)                      #vezme hodnotu promenne a pokud je hodnota -
    print(vysledek)                    
elif operace == "*":
    vysledek = (prvni * druhe)
    print (vysledek)
elif operace == "/":
    vysledek =(prvni / druhe)
    print(vysledek)
else:
    print("spatne zadano")   
druha_operace = input("vyber operaci (+,-,*,/)")  
treti = int(input("treti cislo" ))

if druha_operace == "+":
    print(vysledek + treti)
elif druha_operace == "-":
    print(vysledek - treti)
elif druha_operace == "*":
    print(vysledek * treti)
elif druha_operace == "/":
    print(vysledek / treti)
else:
    print("spatne zadano")


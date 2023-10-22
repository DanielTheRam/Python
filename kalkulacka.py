prvni = int(input("prvni cislo: "))         
operace = input("vyber operaci (+,-,*,/)")
druhe = int(input("druhe cislo: "))         
if operace == "+":                          
    vysledek = (prvni + druhe)
    print(vysledek)                         
elif operace == "-":  
    vysledek = (prvni - druhe)                      
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


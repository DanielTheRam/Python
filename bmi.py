#bmi kalkulacka
vaha = int(input("zadej svoji hmotnost(v kg)"))
vyska = float(input("zadej svoji vysku (v m)"))
vyska_na_druhou = (vyska * vyska) 
bmi = float(vaha / vyska_na_druhou)

if bmi < 18.5:
    print(bmi) 
    print("Mate podvahu, zacnete vice jist")
elif bmi <= 24.9:
    print(bmi)
    print("Vase vaha je v norme")
elif bmi <= 29.9:
    print(bmi)
    print("Mate nadvahu, zacnete se vice hybat")
elif bmi >= 30:
    print(bmi)
    print("Vyhledejte sveho obvodniho lekare")

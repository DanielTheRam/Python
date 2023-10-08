#bmi kalkulacka
vaha = float(input("zadej svoji hmotnost(v kg)"))
vyska = float(input("zadej svoji vysku (v m)"))
vyska_na_druhou = (vyska * vyska) 
bmi = vaha / vyska_na_druhou               #pokud chceme BMI s desetinným místem, napíšeme float místo int

if bmi < 18.5:
    print("Vase BMI je ",bmi,"\n"
    "Mate podvahu, zacnete vice jist\n"
    "Spocitejte si doporuceny denni kaluricky prijem\n"
    "Jezte pravidelne a alespon 5x denne\n"
    "Neopominejte dostatecny a kvalitni spanek")
elif bmi <= 24.9:
    print("Vase BMI je ",bmi,"\n"
    "Vase vaha je v norme\n"
    "Dodrzujte pravidelny pohyb, stravovaci navyky\n"
    "Nezapominejte na zdravy spankovy rezim")
elif bmi <= 29.9:
    print("Vase BMI je ",bmi,"\n"
    "Mate nadvahu, zacnete se vice hybat\n"
    "Omezte vysokokaloricka jidla\n"
    "Vyhybejte se piti slazenych napoju\n"
    "Nastavte si zdravy spankovy rezim")
elif bmi >= 30:
    print("Vase BMI je ",bmi,"\n"
    "Vyhledejte sveho obvodniho lekare\n"
    "Vynechte vysokokaloricka jidla a slazene napoje\n"
    "Zaradte pohyb do vaseho denniho rezimu\n"
    "Pravidelne spete alespon 8 hodin\n"
    "Nepijte alkohol a nekurte")
# f string - dohledat
# více řádkový string
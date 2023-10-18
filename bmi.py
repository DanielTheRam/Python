#bmi kalkulacka
vaha = float(input("zadej svoji hmotnost(v kg)"))
vyska = float(input("zadej svoji vysku (v m)"))
vyska_na_druhou = (vyska * vyska) 
bmi = vaha / vyska_na_druhou               #pokud chceme BMI s desetinným místem, napíšeme float místo int
podvaha =   f"""Vaše BMI je {bmi}.
               Mate podvahu, zacnete vice jist
               Spocitejte si doporuceny denni kaluricky prijem
               Jezte pravidelne a alespon 5x denne
               Neopominejte dostatecny a kvalitni spanek"""
norma =     f"""Vaše BMI je {bmi}.
               Vase vaha je v norme
               Dodrzujte pravidelny pohyb, stravovaci navyky
               Nezapominejte na zdravy spankovy rezim"""
nadvaha =   f"""Vaše BMI je {bmi}.
               Mate nadvahu, zacnete se vice hybat
               Omezte vysokokaloricka jidla
               Vyhybejte se piti slazenych napoju
               Nastavte si zdravy spankovy rezim"""                 
obezita =   f"""Vaše BMI je {bmi}.
               Vyhledejte sveho obvodniho lekare
               Vynechte vysokokaloricka jidla a slazene napoje
               Zaradte pohyb do vaseho denniho rezimu
               Pravidelne spete alespon 8 hodin
               Nepijte alkohol a nekurte"""
if bmi < 18.5:
    print(podvaha)
elif bmi <= 24.9:
    print(norma)
elif bmi <= 29.9:
    print(nadvaha)
elif bmi >= 30:
    print(obezita)


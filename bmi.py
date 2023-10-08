#bmi kalkulacka
vaha = float(input("zadej svoji hmotnost(v kg)"))
vyska = float(input("zadej svoji vysku (v m)"))
vyska_na_druhou = (vyska * vyska) 
bmi = vaha / vyska_na_druhou               #pokud chceme BMI s desetinným místem, napíšeme float místo int
hlaska = f"Vase BMI je {bmi}\n"
podvaha =    """Mate podvahu, zacnete vice jist
                Spocitejte si doporuceny denni kaluricky prijem
                Jezte pravidelne a alespon 5x denne
                Neopominejte dostatecny a kvalitni spanek"""
norma=       """Vase vaha je v norme
                Dodrzujte pravidelny pohyb, stravovaci navyky
                Nezapominejte na zdravy spankovy rezim"""
nadvaha=     """Mate nadvahu, zacnete se vice hybat
                Omezte vysokokaloricka jidla
                Vyhybejte se piti slazenych napoju
                Nastavte si zdravy spankovy rezim"""
obezita=     """Vyhledejte sveho obvodniho lekare
                Vynechte vysokokaloricka jidla a slazene napoje
                Zaradte pohyb do vaseho denniho rezimu
                Pravidelne spete alespon 8 hodin
                Nepijte alkohol a nekurte"""
if bmi < 18.5:
    print(hlaska, podvaha)
elif bmi <= 24.9:
    print(hlaska, podvaha)
elif bmi <= 29.9:
    print(hlaska, nadvaha)
elif bmi >= 30:
    print(hlaska, obezita)
    
# f string - dohledat
# více řádkový string
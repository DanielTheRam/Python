kosik = {"rohlík": 5, "banán": 3, "máslo": 1, "sýr": 2, "šunka": 2}
while True:   
    stav = input("Chcete nakupovat? (ano/ne): ")
    if stav == "ano":
         polozka = input("Kterou položku chceš přikoupit? (rohlík, banán, máslo, sýr, šunka): ")
         mnozstvi = int(input("Kolik toho chceš přikoupit? "))
         kosik[polozka] = kosik[polozka] + mnozstvi 
         print(f"Stav vašeho košíku je: {kosik}")
    elif stav == "ne":
         print(f"Nákup je ukončen, v košíků máte {kosik}")
         quit()

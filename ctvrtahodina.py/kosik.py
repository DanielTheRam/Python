# vytovřím slovník, kde budu mít jako klíč položku v nákupním seznamu a jeho hodnota bude kolikrát to mám koupit +
# pojede nekonečný cyklus, dokud neukončím nákup. 
# Uživatel bude v průběhu moct přidávat nebo ubírat množství jednotlivých položek
#ctrl + k + c - zakomentuju 
#ctrl + k + u - odkomentuje

kosik = {"rohlík": 5, "banán": 3, "máslo": 1, "sýr": 2, "šunka": 2}
for i in kosik:
    print(f"položka: {i}, množství: {kosik[i]}")
print(kosik)
print (f"rohlík: {kosik['rohlík']}")
print(f"počet sýrů a šunky: {kosik['sýr'] + kosik['šunka']}")
print(f"všechny hodnoty košíku: {kosik.values()}")
# while true:   
#     stav = input("chcete nakupovat? (ano/ne): ")
#     if stav == "ano":
#         polozka = input("kterou položku chceš přikoupit? (rohlík/banán, máslo, sýr, šunka): ")
#         mnozstvi = int(input("kolik toho chceš přikoupit? "))
#         kosik[polozka] = kosik[polozka] + mnozstvi 
#     elif stav == "ne":
#         print(f"nákup je ukončen, v košíků máte {kosik}")
#         quit()

procento_snezeneho_kolace = int(input("napis v procentech, kolik kolace jsi snedl: "))
if procento_snezeneho_kolace <0:
    print("Zadej kladné číslo")
elif procento_snezeneho_kolace <= 20:
    print("OK")
elif procento_snezeneho_kolace <= 40:
    print("OK, ale už brzdi")
elif procento_snezeneho_kolace <=60:
    print("Už stačilo")
elif procento_snezeneho_kolace <=80:
    print("Přestaň už jíst")
elif procento_snezeneho_kolace <=99:
    print("Nech drobeček ptáčkům")
elif procento_snezeneho_kolace ==100:
    print("Snědl jsi celý koláč, nenažranče")
else: 
    print("Nechápu")
#uzivatel zada % kolace, ktery sni a ja vypisu jak moc je to pro nej nezdrave
#5 druhu odpovedi na zakladce procent, kolik toho sni:      0-20 OK
                                                        #   20-*40 OK ale brzdi
                                                        #   40-60 uz stacilo
                                                        #   60-80 prestan uz jist
                                                        #   81-99 uz dost
                                                        #   100 snedl jsi cely kolac



procento_snezeneho_kolace = int(input("napis v procentech, kolik kolace jsi snedl: "))
if procento_snezeneho_kolace <0:
    print("zadej kladne cislo")
elif procento_snezeneho_kolace <= 20:
    print("OK")
elif procento_snezeneho_kolace <= 40:
    print("OK ale brzdi")
elif procento_snezeneho_kolace <=60:
    print("Uz stacilo")
elif procento_snezeneho_kolace <=80:
    print("Prestan uz jist")
elif procento_snezeneho_kolace <=99:
    print("Uz dost")
elif procento_snezeneho_kolace ==100:
    print("snedl jsi cely kolac")
else: 
    print("nechapu")
czeng = {"pes" : "dog", "kočka" : "cat", "auto" : "car", "slunce" : "sun", "dům" : "house"}
engit = {"dog" : "cane", "cat" : "gatto", "car" : "auto", "sun" : "sole", "house" : "casa"}
itcz = {"cane": "pes", "gatto" : "kočka", "auto" : "auto", "sole" : "slunce", "casa" : "dům"}
jazyk = input("Vyberte jazyk, ze kterého chcete překládat - 'CZ','ENG','IT' ")
slovo = input("Jaké slovo chcete přeložit? ")
if jazyk == "CZ":
    if slovo in czeng:
        preklad_aj = czeng[slovo]
        preklad_it = engit[preklad_aj]
        print(f"Anglický překlad je {preklad_aj} a italský je {preklad_it}")
    else:
        print("Slovo se nenachází ve slovníku")
elif jazyk == "ENG":
    if slovo in engit:
        preklad_it = engit[slovo]
        preklad_cz = itcz[preklad_it]
        print(f"Český překlad je {preklad_cz} a italský je {preklad_it}")
    else:
        print("Slovo se nenachází ve slovníku")
elif jazyk == "IT":
    if slovo in itcz:
        preklad_cz = itcz[slovo]
        preklad_aj = czeng[preklad_cz] 
        print(f"Český překlad je {preklad_cz} a anglický je {preklad_aj}")
    else:
        print("Slovo se nenachází ve slovníku") 
else:
    print("Vyberte jeden ze zmíněných jazyků")



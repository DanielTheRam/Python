veta = input("Napište libovolně dlouhý text: ")
pocet_znaku = 0
for a in veta: 
    if a == "a":
        pocet_znaku += 1
    elif a == "á":
        pocet_znaku += 1
vysledek = f"Počet 'a' ve vaší větě je {pocet_znaku}"
print(vysledek)         #velká písmena - ignorovat velikost písmen
# for je procházecí cyklus - projde všechny prvky
# while - nekonečný cyklus - cyklus, dokud se nesplní podmínka

slovo = "nahodne vytvoreny vyraz"
for i in slovo: 
    print(i)                    # i jsou jednotlivé prvky věci - tj. písmena ze slova

while len(slovo) > 5:           # pojede do nekonecna| len je délka (programátoři číslují od 0 -> 0=1) 
    print(slovo)
    slovo = slovo[1:]
